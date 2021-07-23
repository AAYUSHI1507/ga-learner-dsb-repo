# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Code starts here
data = pd.read_csv(path)
loan_status = data['Loan_Status'].value_counts()
print(loan_status)


plt.figure(figsize=[14,8])
plt.plot(loan_status)
#plt.bar(loan_status)


# --------------
#Code starts here

property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])

property_and_loan = property_and_loan.size().unstack()

property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))

# Label X-axes and Y-axes
plt.xlabel('Property Area')
plt.ylabel('Loan Status')

# Rotate X-axes labels
plt.xticks(rotation=45)

# Display plot
plt.show()


# --------------
#Code starts here
education_and_loan = data.groupby(['Education','Loan_Status'])

education_and_loan = education_and_loan.size().unstack()

education_and_loan.plot(kind='bar', stacked=True, figsize=(15,10))

# Label X-axes and Y-axes
plt.xlabel('Education Status')
plt.ylabel('Loan Status')

# Rotate X-axes labels
plt.xticks(rotation=45)

# Display plot
plt.show()


# --------------
#Code starts here
graduate = data[data['Education'] == 'Graduate']

not_graduate = data[data['Education'] == 'Not Graduate']

graduate['LoanAmount'].plot(kind = 'density', label='Graduate')

not_graduate['LoanAmount'].plot(kind = 'density', label='Not Graduate')





#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3) = plt.subplots(nrows = 3 , ncols = 1, figsize = [15,10])  

ax_1.scatter(data['ApplicantIncome'], data['LoanAmount'])
ax_1.set_title('Applicant Income')

ax_2.scatter(data['CoapplicantIncome'], data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

ax_3.scatter(data['TotalIncome'], data['LoanAmount'])
ax_3.set_title('Total Income')


