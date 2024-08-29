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
