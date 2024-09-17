
def math():
    numbers = []
    newNumber = int(input("Enter a number or press 0 to quit: "))
    while newNumber != 0:
        numbers.append(newNumber)
        newNumber = int(input("Enter a number or press 0 to quit: "))
    print(numbers)
    finalSum = sum(numbers)
    print(f'finalSum is {finalSum}')

math()