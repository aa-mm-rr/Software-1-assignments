str = '0'
max = 0
min = 100000000000000
while str != '':
    str = input('Enter a number: ')
    if str == '':
        break
    if int(str) > max:
        max = int(str)
    if int(str) < min:
        min = int(str)

print('Minimum:', min, '\nMaximum:', max)