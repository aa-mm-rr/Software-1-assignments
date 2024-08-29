#1
length = float(input("Enter the length of the zander in centimeters: "))
sizeLimit = 42

if length >= sizeLimit:
    print("The zander meets the size limit. You can keep the fish")
else:
    difference = sizeLimit - length
    print(f"The zander does not meet the size limit. Please release the fish back into the lake")
    print(f"The fish is {difference:.2f} centimeters below the size limit")
#2
cabinClass = input("Which cabin class do you want? ")
if cabinClass == "A":
    print('A: above the car deck, equipped with a window.')
elif cabinClass == "B":
    print('B: windowless cabin above the car deck')
elif cabinClass == "C":
    print('B: windowless cabin below the car deck')
elif cabinClass == "lux":
    print('Lux: upper-deck cabin with')
else :
    print("Invalid cabin class")

#3
gender = input('Enter your gender: ')
hemo = int(input('Enter your hemoglobin (g/l): '))
if gender == "female" and hemo <117 :
    print("Your hemoglobin is low")
elif gender == 'female' and 117<hemo<155 :
    print("Your hemoglobin is normal")
elif gender == 'female' and hemo>155:
    print("Your hemoglobin is high")
elif gender == 'male'and hemo<134:
    print("Your hemoglobin is low")
elif gender == 'male' and 134<hemo<167:
    print("Your hemoglobin is normal")
else:
    gender = 'male' and hemo>167
    print("Your hemoglobin is high")
