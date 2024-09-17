def gasoline():
    quantity = int(input('write a gasoline quantity or enter a negative value to exit: '))
    while quantity >= 0:
        litres = quantity*3,785
        print(litres)
        quantity = int(input('write a gasoline quantity or enter a negative value to exit: '))

gasoline()