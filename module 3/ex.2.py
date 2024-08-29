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