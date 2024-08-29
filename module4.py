'''
sum = 0
counter = 1
while counter < 10:
    sum = sum + counter
    print(f'the counter,{counter}, and the sum of the counter with sum {sum}')
    counter = counter + 1


i=1
n=int(input('Enter a limit: '))
while i<=n:
    if i % 2 == 0:
        print(f"the even number is {i}")
    else :
        print(f"the odd number is {i}")
    i=i+1


import random
targetNumber = random.randint(1,9)
number = 0
while True:
    userGuess = int(input('Enter a number between 1 and 9: '))
    if userGuess == targetNumber:
        print('You guessed the number')
        break
    else :
        print('try again')
    number =number+1
print(f'it took you {number} times to guess the number')

userInput = ''
while userInput !='exit':
    userInput = input('type something (or exit to quit): ')
    print('You typed:', userInput)

first = 0
while first<5:
    second=1
    while second<5:
        print(f'{first} time {second} is ', first*second)
        second += 1
    first += 1
    print('all done')
'''
