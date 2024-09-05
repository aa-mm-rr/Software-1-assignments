numbers=[]
number= int(input("Enter a number or enter 0 to exit: "))
while number != 0:
    numbers.append(number)
    number= int(input("Enter a number or enter 0 to exit: "))
def finalSum(numbers):
    return sum(numbers)
total = finalSum(numbers)
print('the sum of all numbers is', total)

def minNumber(numbers):
    return min(numbers)
minimum = minNumber(numbers)
print('the smallest number is', minimum)
def maxNumber(numbers):
    return max(numbers)
maximum = maxNumber(numbers)
print('the largest number is', maximum)
