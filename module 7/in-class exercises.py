'''
dict1 = {'m': 11, 'f':34,'h':77}
print(dict1.values())
'''
dict2 = {}
for _ in range(5):
    key = input('Enter a key: ')
    value = int(input('Enter a value: '))
    dict2[key] = value
totalSum = sum(dict2.values())
print('Total sum of all entered values is: ', totalSum)