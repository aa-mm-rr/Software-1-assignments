airports = {}
while True:
    choice = input('1. Enter new airpot\n2. Find an airport\n3. Choose this to quit')
    if choice =='3':
        print('Program stopped')
        break
    elif choice =='1':
        name = input('Enter airport name')
        code = input('Enter airport ICAO code')
        airports[code] = name
    elif choice =='2':
        code = input('Enter airport ICAO code')
        print('Airport name for', code, 'is', airports[code])
    else :
        print('Invalid input')


