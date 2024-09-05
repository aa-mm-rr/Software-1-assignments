import random
points = int(input("How many points do you want? "))
inCircle = 0
counter = 0

while counter < points:
    xOfPoints = float(random.uniform( -1, 1))
    yOfPoints = float(random.uniform( -1, 1))
    if xOfPoints**2 + yOfPoints**2 < 1:
        inCircle += 1
    counter += 1

pi = 4 * inCircle / points
print(pi)