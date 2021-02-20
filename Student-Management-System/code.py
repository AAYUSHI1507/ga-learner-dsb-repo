# --------------
# Code starts here
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

new_class = class_1 + class_2
print(new_class)
print('='*50)

new_class.append('Peter Warden')
print(new_class)
print('='*50)

new_class.remove('Carla Gentry')
print(new_class)
# Code ends here


# --------------
# Code starts here

# creating dictionary for Geoffrey Hinton in each subject to generate his report...
courses = {'Math': 65,'English':70,'History':80,'French':70,'Science':60}
print(courses)
print('='*50)

# displaying marks 
marks = courses.values()
print(marks)

total = sum(marks)
print('total = ',total)
print('='*50)

# Calculating percentage
percentage = (total/500)*100
print('percentage scored by Geoffrey Hinton is',percentage ,'%')
# Code ends here


# --------------
# Code starts here
mathematics = {'Geoffrey Hinton': 78,'Andrew Ng':95,'Sebastian Raschka':65,
'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

# calculate the topper
topper = max(mathematics,key = mathematics.get)
print('topper is ',topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here

first_name = topper.split()[0]
last_name = topper.split()[1]

full_name = last_name +' '+first_name
certificate_name = full_name.upper()
print('-------------',certificate_name,'--------------')
# Code ends here


