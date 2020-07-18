# --------------
import pandas as pd

print(path)
print('')
bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
print('')
numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)



# --------------
# code starts here
import pandas as pd

banks = bank.drop(labels='Loan_ID', axis=1)

print(banks.isnull().sum())
print('')
bank_mode = lambda x: x.fillna(value=x.mode().iloc[0])
print(bank_mode)

banks = banks.apply(bank_mode, axis=0)

print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here
import numpy as np

avg_loan_amount = pd.pivot_table(banks, index=['Gender', 'Married', 'Self_Employed'], values='LoanAmount', aggfunc=np.mean)

print(avg_loan_amount)

# code ends here



# --------------
# code starts here
loan_Status = banks[(banks['Loan_Status'] == 'Y')].shape[0]

loan_approved_se = banks.loc[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y'),:]
percentage_se = (loan_approved_se.shape[0]/ 614) * 100

loan_approved_nse = banks.loc[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y'),:]
percentage_nse = (loan_approved_nse.shape[0]/ 614) * 100
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].div(12)

big_loan_term = loan_term[loan_term >= 25].shape[0]

# code ends here


# --------------
# code starts here
import numpy as np

loan_groupby = banks.groupby('Loan_Status')
mean_values = loan_groupby.agg({'ApplicantIncome': np.mean, 'Credit_History': np.mean})



# code ends here


