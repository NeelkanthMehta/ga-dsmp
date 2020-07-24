### Project Overview

 For this project, we will be exploring the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

__Problem Statement__: What is the probability that the borrower paid back their loan in full?

__dataset overview__

!!![container width="100%" align="center"]
![data_description](undefined/account/b16/6a1f0c95-2915-474c-917f-dc711cc8d89b/b-629/18685306-88d9-4f67-a4e3-913c822cabc8/file.png)
!!![container-end]



### Learnings from the project

 We have explored the following concepts:

1. Independency check
2. Bayes theorem
3. Visualizing discrete variable
4. Visualizing continuous variable


### Approach taken to solve the problem

 1. Event A and Event B are independent if the probability of their occurance aren't affected by occurance or non-occurance of another. To solve first problem;  one needs to compute the individual probability of both the events and their joint probabilities P(A intersection B). If their joint probability equals the product of their individual probabilities, then the events are independent. We tested whether the event that applicants' FICO score > 700 and whether purpose of debt is debt consolidation are independent.
2. !!![container width="100%" align="center"]
![bayes_theorem](undefined/account/b16/6a1f0c95-2915-474c-917f-dc711cc8d89b/b-523/ca105c34-a9df-449a-8bc6-e2c5d49c8461/file.png)
!!![container-end]
3. plotted frequency of values loan purposes and histogram of loan installment amounts







### Challenges faced

 I coded as per directions; however, dtype of FICO score was not float, as a result its probability computation was errorneous in the beginning. Rectified the issue once identified.


### Additional pointers

 Thank you.


