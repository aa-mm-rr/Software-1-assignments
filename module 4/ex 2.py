#2
while True:
    inches = float(input('Enter the number of inches: '))
    if inches<0:
        print('program stopped')
        break
    cm = inches * 2.54
    print(f'{inches} is equal to {cm} centimeters')