import random
dice = int(input("How many dice would you like to roll? "))
sum = 0

for _ in range(dice):
    roll = random.randint(1, 6)
    sum += roll
print(f"The sum is: {sum}")
