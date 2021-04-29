# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
# code starts here
bank =  pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)
print('='*50)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

# code ends here


# --------------
# code starts here

# load the dataset and drop the loan_ID
banks = bank.drop(columns = 'Loan_ID')

# Check all the missing values are filled.
print(banks.isnull().sum())

# apply mode
bank_mode = banks.mode().iloc[0]

# Fill the missing values with
banks.fillna(bank_mode,inplace = True)

# Checking again all the missing values filled
print(banks.isnull().sum())

#code ends here


# --------------
# Code starts here

# Generating the pivot table
avg_loan_amount = pd.pivot_table(banks, index = ['Gender','Married','Self_Employed'],values = ['LoanAmount'], aggfunc = 'mean')

# code ends here



# --------------
# code starts here

# Creating variable loan_approved_se
loan_approved_se = banks.loc[(banks["Self_Employed"]== 'Yes') & (banks["Loan_Status"]=='Y'),["Loan_Status"]].count()
print(loan_approved_se)

# Creating the loan approved for non self employed
loan_approved_nse = banks.loc[(banks["Self_Employed"]== 'No') & (banks["Loan_Status"]=='Y'),["Loan_Status"]].count()
print(loan_approved_nse)

# percentage of loan approved for self employed
percentage_se = (loan_approved_se * 100 / 614) 
percentage_se = percentage_se[0]
print(percentage_se)

# Percentage of loan approved  for non self employed
percentage_nse = (loan_approved_nse * 100 / 614)
percentage_nse = percentage_nse[0]
print(percentage_nse)

# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x / 12)
print(loan_term)
print("="*100)

big_loan_term1 = [x for x in loan_term if x >= 25]

print("="*50)

def counting(big_loan):
    count = 0
    for x in big_loan:
        count = count + 1
    return count

big_loan_term = counting(big_loan_term1)
print(big_loan_term)
# code ends here


# --------------
# code starts here
loan_groupby = banks.groupby('Loan_Status')


loan_groupby = loan_groupby['ApplicantIncome', 'Credit_History']
mean_values = loan_groupby.mean()
print(mean_values)

# code ends here


