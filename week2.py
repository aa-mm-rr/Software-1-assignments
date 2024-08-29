'''
age = int(input("Enter your age: "))
if 15<= age < 18:
    weight = float(input("Enter your weight (kg): "))
if (age>=18 or age>=15 and weight >=55):
    print('The medicine can be used')
else:
    print('The medicine can not be used')


score = float(input("Enter your score: "))
if score>90:
    print ('A1')
elif score > 80:
    print ('A2')
elif score > 70:
    print('B1')
elif score > 60:
    print('B2')
elif score > 50:
    print('C1')
else:
    print('you didnt pass')

numberOfWheels = int(input("Enter number of wheels: "))
if numberOfWheels==2:
    print('You have bicycle')
elif numberOfWheels==3:
    print('You have tricycle')
else :
    numberOfWheels==4
    print('You have car')
'''

age = int(input("Enter your age: "))
if age>65:
    print('You are retired')
elif 18< age <=65 :
    print('You are working')
elif 7< age <= 18 :
    print('You are in school')
else :
    age <7
    print('You are a child')