def main():
    numbersList = []
    number = int(input("Enter a number or press 0 to exit: "))
    while number != 0 :
        numbersList.append(number)
        number = int(input("Enter a number or press 0 to exit: "))

    oddNumbers = []
    for number in numbersList:
        if number % 2 ==0:
            oddNumbers.append(number)
    print(oddNumbers)


main()