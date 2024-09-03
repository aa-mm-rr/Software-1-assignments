numbers = []
number = input("Enter a number or enter to quit: ")
while number != "":
    numbers.append(number)
    number = input("Enter a number or enter to quit: ")
numbers.sort(reverse=True)
print(numbers[:5])
