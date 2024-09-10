names = set()
while True:
    newName = input("Enter a name or press enter to quit : ")
    if newName == "":
        break
    elif newName in names:
        print("Name already in use")
        continue
    else :
        names.add(newName)
for newName in names:
    print(newName)

