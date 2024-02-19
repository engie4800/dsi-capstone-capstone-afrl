# Data Science Capstone & Ethics (ENGI E4800)

## Course overview

This course provides a unique opportunity for students in the MS in Data Science program to apply their knowledge of the foundations, theory and methods of data science to address data driven problems in industry, research, government and the non-profit sector. The course activities focus on a semester-long project sponsored by an affiliate company or a Columbia faculty member. The project synthesizes the statistical, computational, engineering and social challenges involved in solving complex real-world problems. The course has a well developed Ethics component supported by Dr. Savannah Thais. 

## Team Structure

Select a team captain (with or without help from mentor/instructor/supervisor)

Record your names here in this format-
1. Team captain Xiao Wen, xw2943




## Instructions

The CourseInfo folder has the templates for your  reports, progress log, meeting minutes with your mentors. These are the deliverables you need to save as .pdf files and upload in this repository. Additionally the folder also contains sample meeting presentations and tips, report grading rubrics, student-mentor email templates and syllabus for your reference.

1. Regularly work on developing your code, provide repository access to your industry mentor/instructor
2. Update your project task status weekly in our progress log and github project board.
3. Record your progress in the reports.
4. Employ a mechanism to select weekly presenter at the mentor meetings 
5. Note down the meeting minutes on a weekly basis

## Main Deliverables

1. Code
2. Reports- Midterm Progress Report, Final Report, Ethics Report
3. Progress Log
4. Meeting Minutes

The code can be placed in a folder named code, and the remaining files can be placed as .pdf files in the root directory.


## Project Outlines
#### Geometric Partition Entropy for identifying Optimal Training Set for Classification Tasks

THE OBJECTIVE:  to be able to identify subsamples of large training data sets so that neural network classifiers perform almost as well as they would if trained on the full original training data.

Although there is a general understanding that more training data leads to better performance, and thus smaller data sets lead to poorer outcomes, this is not entirely true. Data-efficient learning is a large research area and we will not attempt to solve the problem in generality. The goal of this project is to optimize the sub-selection from larger data sets, so that the performance remains as close as possible. It is an assumption of ours that what matters most in the training of neural network classifiers is the density distribution of the data set in the latent feature space, and so our goal is to identify if a subset of the data exhibits the same density distribution as the original. 

Currently, we are using Cifar-10 and a sample CNN to conduct the following steps:

1. Map pictures into feature space (each picture is regarded as a vector) and therefore we have a matrix with the dimension of number of features times number of vectors (number of pictures). 

2. Apply SVD to this matrix:
   i) Will have one matrix vectored in the feature space.
   ii) Will have a matrix of singular values (the middle diagonal matrix). These values are the variances associated with the data in the direction of the singular vectors. The first largest singular value is the variance in the first singular vector direction.
   iii) Will have one matrix vectored in the data space. (picture)

3. Apply SVD to several smaller subsamples of the whole dataset. So, we will have singular value vectors with respect to these subsamples as well as one with respect to the whole dataset. 

4. Figure out whether singular value vectors of these subsamples are pointing in the same direction as the singular value vector of the whole dataset (can use dot product etc.)

5. If they share similar directions as the whole dataset one, then figure out whether they are similar to the whole dataset in geometry/distribution by inputting the singular value vectors of both subsamples and the whole dataset into Geometric Partition Entropy/Boltzmann Shannon interaction Entropy. 

6. If they are, then we can expect similarly good ML model performance as the one associated with the whole dataset even if we use these subsamples to train the model rather than the whole dataset. 



   
