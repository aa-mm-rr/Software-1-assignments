#4
year = int(input("Enter your year: "))

if (year%100==0 and year % 400==0):
    print ("Your year is a leap year")
elif year % 4 == 0:
    print ("Your year is a leap year")
else :
    print ("Your year is not leap")
