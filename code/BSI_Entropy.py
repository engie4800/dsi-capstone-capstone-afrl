import numpy as np
import copy as cp

def BSIE(x, limits=None, k=None):
    x = np.sort(x)          # sort the values before starting
    if limits:
        # If limits are provided as bounds of the state space, 
        #       we must add them to the data before defining 
        #       bins, making sure that the histogram p does not
        #       include the added boundaries in frequency counts
        #  If you want to include a single limit, use 
        #       float('nan') for the other one, e.g., 
        #       BSIE(x,[0,float('nan')]).
        if not np.isnan(limits[0]):
            if x[0] < limits[0]:
                print('ERROR: data outside limits')
                return
            else:
                y = np.concatenate(([limits[0]], x))
        else:
            y = cp.deepcopy(x)  # if bound is nan skip

        if not np.isnan(limits[1]):
            if x[-1] > limits[1]:
                print('ERROR: data outside limits')
                return
            else:
                y = np.concatenate((y, [limits[1]]))
    else:
        # If no limits are boundaries make sure that the 
        #       min and max of the data are used as boundary
        y=cp.deepcopy(x)    

    if k:
        # Defaults to using k=N-1 so that the quantiles can be 
        #       estimated quickly using differences, but allows
        #       the option of course graining the measure with k 
        t = np.linspace(0, 1, k + 1)
        # using y instead of x includes the limits if provided
        #       for geometric distribution
        s = np.quantile(y, t)
        l = s[1:] - s[:-1]
        q = l / np.sum(l)
    else:
        # Use the extreme values as bounds (with default k)
        #       Use difference to estimate quantiles for k=N
        q = (y[1:] - y[:-1]) / (np.max(y) - np.min(y))
        # Let k = N-1 so that p end up being the same length as q 
        k = len(y) - 1              

    t = np.linspace(y[0], y[-1], k + 1)     # create bins using y
    # but only count the actual data x (not the limits in y)
    h,bins = np.histogram(x, t)         
    p = h / np.sum(h)
    
    #print(f'this is p:{p}')
    #print(f'this is q:{q}')
    # Divergence: Boltzmann-Shannon Interaction Divergence
    m = (p + q) / 2
    ix = np.argwhere(p)
    p = p[ix]
    m_ = m[ix]  # use dummy variable so that m remains for q
    D = np.dot(p.T, np.log(p / m_))
    ix = np.argwhere(q)
    q = q[ix]
    m = m[ix]
    # Since we use np.log, must normalize by dividing by log(2)
    D = 1 - 0.5 * (D + np.dot(q.T, np.log(q / m))) / np.log(2)
    return D