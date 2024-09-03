correctName ='python'
correctPassword = 'rules'
i = 1
while i <= 5:
    name = input('Enter your username: ')
    password = input('Enter your password: ')
    if name == correctName and password == correctPassword:
        print('welcome')
        break
    print('try again')
    i += 1
else:
    print('access denied')
