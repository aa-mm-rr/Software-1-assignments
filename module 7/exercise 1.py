season = 'spring','summer','autumn','winter'
number = int(input('Enter a number of a month: '))
if 1<=number<=3 :
    print(season[3])
elif 4<=number<=6 :
    print(season[0])
elif 7<=number<=9 :
    print(season[1])
else :
    (10<=number<=12) 
    print(season[2])