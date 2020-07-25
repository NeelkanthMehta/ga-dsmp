### Project Overview

 This mini-project covers inferential statistics.

Problem statement: Bank Of New York wants to expand its branches and for that, it has a certain hypothesis and statements it wants to verify. 

Overview of data:

Feature	Description
customer.id====ID of the customer
credit.policy====If the customer meets the credit underwriting criteria of LendingClub.com or not
purpose=======The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other").
int.rate========The interest rate of the loan
installment=====The monthly installments owed by the borrower if the loan is funded
log.annual.inc===The natural log of the self-reported annual income of the borrower
dti============The debt-to-income ratio of the borrower (amount of debt divided by annual income)
fico===========The FICO credit score of the borrower
days.with.cr.line  The number of days the borrower has had a credit line.
revol.bal=======The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
revol.util=======The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
pub.rec======= The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
inq.last.6mths==The borrower's number of inquiries by creditors in the last 6 months
delinq.2yrs=====The number of times the borrower had been 30+ days past due on a payment in the past 2 years
paid.back.loan==Whether the user has paid back loan


### Learnings from the project

 In this project, we have applied the following concepts:
1. Confidence Interval
2. Central Limit Theorem
3. Hypothesis Testing
4. Chi-Square Test


### Approach taken to solve the problem

 1. for computing confidence interval, we first computed the sample and population means mean and sample standard deviation (n=2000); then computed margin_of_error. From margine of error, it's easy to compute lower and upper bounds of CI.
2. CLT states that mean of randomly drawn samples from a given population tend to converge to true population mean as the number of samples increase. Further, they follow normal distribution, regardless of the population distribution. The fact is depicted graphically (with help of maltplotlib.pyplot figure object). We drew three samples.
3. For hypothesis testing, we went on to test H_a = mean interest rates vary with purpose of loan.
4. Here, we tested the H_a that loan repayment/ default is strongly associated with the purpose of borrowing using Chi2 statistic.


### Challenges faced

 This is faily straight forward exercise.


### Additional pointers

 Not that I can think of


