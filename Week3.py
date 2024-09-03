names = []

name = input("Enter the first name or quit by pressing Enter: ")
while name!="":
    names.append(name)
    name = input("Enter the next name or quit by pressing Enter: ")

names.append('Lj')
print(names)
names.remove('Lj')
print(names)
names.insert(2, 'BB')
print(names)
other=['QW','ER']
names.insert(other)
print(names)
