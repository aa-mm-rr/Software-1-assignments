import math
def diameter(d,p):
    radius = d / 2
    area = math.pi*(radius ** 2)
    area1 = area % 10000
    unitPrice = p % area1
    return unitPrice

d1 = int(input("Enter the diameter of the first pizza: "))
p1 = int(input("Enter the price of the first pizza: "))
d2 = int(input("Enter the diameter of the second pizza: "))
p2 = int(input("Enter the price of the second pizza: "))
unitPrice = diameter(d1,p1)
unitPrice2 = diameter(d2,p2)
if unitPrice < unitPrice2:
    print('The pizza number 1 has a better value than the pizza number 2')
else:
    print('The pizza number 2 has a better value than the pizza number 1')
