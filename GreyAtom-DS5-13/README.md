### Project Overview

 For this project we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back

The data that we have is from 2007-2010.

**Problem Statement**
Using Decision Tree model, classify whether or not the borrower paid back their loan in full.

**About the Dataset**
The snapshot of the data you will be working on:

**Feature**: **Description**
01. customer.id: ID of the customer
02. credit.policy: If the customer meets the credit underwriting criteria of LendingClub.com or not
03. purpose: The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other").
04. int.rate: The interest rate of the loan
05. installment: The monthly installments owed by the borrower if the loan is funded
06. log.annual.inc: The natural log of the self-reported annual income of the borrower
07. dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income)
08. fico: The FICO credit score of the borrower
09. days.with.cr.line: The number of days the borrower has had a credit line.
10. revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
11. revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
12. pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
13. inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months
14. delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years
15. paid.back.loan: Whether the user has paid back loan


### Learnings from the project

 After completing this project, you will have a better understanding of how to build a decision tree model. In this project, you will apply the following concepts.

1. Train-test split
2. Correlation between the features
3. Decision Tree Modeling
4. Evaluation Metrics
5. Graphviz plotting


### Approach taken to solve the problem

 We performed following approach:
1. Loading, cleaning and splitting the dataset into train and test set.
2. Exploratory Data Analysis, w.r.t. distribution of the target, numerical features, frequency distribution of categorical variables, 
3. Encoding the categories
4. Conducted hyperparameter tuning Decision Tree Classifier through grid search cross validation, fitted the model on the train dataset
5. Evaluate its performance on test set
6. Visualized the tree


### Challenges faced

 Standardized syntax of Scikit-Learn library makes it easy and straightforward to implement; plus it has excellent documentation, just in case.


### Additional pointers

 None


