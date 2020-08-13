**Problem Statement**
An insurance company wants to know the reason a claim was not made. Doing so would allow insurance company to improve there policy for to the customer. 
This project deals with various feature such as age, occupation etc. that helps to get to the final conclusion.

**About the Dataset**:

The dataset has details of 10302 Insurance claim with the following 25 features.

**Feature**: **Description**
01. ID: Claim ID
02. KIDSDRIV: Number of kids person having
03. AGE: Age of the customer
04. HOMEKIDS: Number of kids in the home
05. YOJ: Year of joining of the customer (employee/unemployed)
06. INCOME: Anual income of the customer
07. PARENT1: parent is alive or not
08. HOME_VAL: Home value of the customer
09. MSTATUS: Marital status
10. GENDER: Male/Female
11. EDUCATION: Degree holds by the customer
12. OCCUPATION: Job title
13. TRAVTIME: Traveling time
14. CAR_USE: purpose of the car (private/commercial)
15. BLUEBOOK: Legal citation system in the United States
16. CAR_TYPE: Type of car(SUV/Pick up)
17. RED_CAR: Colour of the car
18. OLDCLAIM: Old calim of the car
19. CLM_FREQ: Number of times claims taken
20. REVOKED: Claim revoked
21. MVR_PTS: Claim points
22. CLM_AMT: Claim amount
23. CAR_AGE: Age of the car
24. CLAIM_FLAG: Target variable (YES/NO)


**Learning Objective Statement**
The project offers understanding on dealing with imbalanced dataset. The following concepts are applied:
1. Train-test split
2. Standard scaler
3. Logistic Regression
4. SMOTE
5. feature scaling

**How the problem is approached**:

1. Loading and cleaning the data before splitting and pre-processing stage.
2. For preprocessing, label-encoding was done; further various approaches of under-sampling and over-sampling were performed to deal with imbalanced data.
3. Finally a classifier was fit and accuracy is measured.

**Challenges Overcome**
The only challenging part was cleaning the data. Several of the supposedly numerical features were of string type; these had to be converted. 

Besides there were several NaN values - in a imbalanced data, eliminating null values could post challenges, in that the data might not be missing completly at random (MCAR) or missing at random (MAR), we are required to choose an appropriate under/ over-sampling approach.

Rest was straightforward as for any other classification problem.
