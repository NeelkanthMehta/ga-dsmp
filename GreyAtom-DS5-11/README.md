### Project Overview

 In this project, we will predict the Insurance claim using logistic regression. 

This dataset contains information on the insurance claim. each observation is different policyholder with various features like the age of the person, the gender of the policyholder, body mass index, providing an understanding of the body, number of children of the policyholder, smoking state of the policyholder and individual medical costs billed by health insurance.

**About the Dataset**:

The snapshot of the data, you will be working on 

**Feature**	**Description**
1. age: age of policyholder
2. sex: male(1)/ female(0)
3. bmi: body mass index (kg / m^2m 2)
4. children: number of children/ dependents of policyholder
5. smoker: smoking state nonsmoker(0)/ smoker(1)
6. region: residential area northeast(0)/ northwest(1)/ southeast(2)/ southwest(3)
7. charges: medical cost
8. insuranceclaim: yes(1)/ no(0)


### Learnings from the project

 After completing this project, you will have a better understanding of how to build a logistic regression model. In this project, you will apply the following concepts.

1. Train-test split
2. Correlation between the features
3. Logistic Regression
4. Auc score
5. Roc AUC plot


### Approach taken to solve the problem

 - First, we loaded the dataset from the path and split into train and test set. 
- Next, we explored the dataset w.r.t. outliers, multicolinearity etc. 
- Once the data is brought in the desired format, we fit the Logistic Regression model to the train set and evaluated against the test set.

The model obtained an accuracy score of ~82%


### Challenges faced

 The standardized syntax of the Scikit Learn library makes it simple and straightforward exercise.


### Additional pointers

 Not.


