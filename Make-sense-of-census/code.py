# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data  = np.genfromtxt(path , delimiter = ",",skip_header = 1) 
print("\n Data :\n\n",data)
print("\n Type of data \n\n",type(data))
print("=="*25)

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
census = np.concatenate((data,new_record))
print(census)


# --------------
#Code starts here
age = census[:,0]
print(age)
print("=="*25)

# max age
max_age  = age.max()
print(max_age)
print("=="*25)

#min age
min_age = age.min()
print(min_age)
print("=="*25)

# age mean
age_mean = age.mean()
print(age_mean)
print("=="*25)

# Standerd deviation
age_std = age.std()
print(age_std)
print("=="*25)


# --------------
#Code starts here
race_0 = census[census[:,2]==0]
race_1 = census[census[:,2]==1]
race_2 = census[census[:,2]==2]
race_3 = census[census[:,2]==3]
race_4 = census[census[:,2]==4]

# Creating the length of arraus
len_0 = len(race_0)     
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

# Displaying the lengths...
print('len_0 is ', len_0)
print('='*50)
print('len_1 is ', len_1)
print('='*50)
print('len_2 is ', len_2)
print('='*50)
print('len_3 is ', len_3)
print('='*50)
print('len_4 is ', len_4)
print('='*50)

# Finding the race with the minimum no of citizens...
if (len_0 < len_1 and len_0 < len_2 and len_0 < len_3 and len_0 < len_4):
    minority_race = 0
elif (len_1 < len_0 and len_1 < len_2 and len_1 < len_3 and len_1 < len_4):
    minority_race = 1
elif (len_2 < len_0 and len_2 < len_1 and len_2 < len_3 and len_2 < len_4):
    minority_race = 2
elif (len_3 < len_0 and len_3 < len_1 and len_3 < len_2 and len_3 < len_4):
    minority_race = 3
else:
    minority_race = 4

# Display the minority race
print(minority_race)


# --------------
#Code starts here
#Subsetting the array based on the age 
senior_citizens=census[census[:,0]>60]

#Calculating the sum of all the values of array
working_hours_sum=senior_citizens.sum(axis=0)[6]

#Finding the length of the array
senior_citizens_len=len(senior_citizens)

#Finding the average working hours
avg_working_hours=working_hours_sum/senior_citizens_len

#Printing the average working hours
print((avg_working_hours))

#Code ends here


# --------------
#Code starts here
high = census[census[:,1]>10]
low = census[census[:,1]<=10]

# Calculating avg_pay_high and avg_pay_low
avg_pay_high = high[:,7].mean()
print(avg_pay_high)
print("="*50)

avg_pay_low = low[:,7].mean()
print("="*50)
print(avg_pay_low)

# Comparing both
if (avg_pay_high>avg_pay_low):
    print("The truth is better education leads to the pay")
else:
    print("It is false")


