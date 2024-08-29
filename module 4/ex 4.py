import random
randomNumber = random.randint(1, 10)
number = 0
while True :
    userNumber = int(input("Enter a number from 1 to 9: "))
    if randomNumber == userNumber:
        print("Correct!")
        break
    elif randomNumber > userNumber:
        print("Too low!")
    elif randomNumber < userNumber:
        print("Too high!")