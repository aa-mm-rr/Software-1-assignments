
import random

def ranNumbers():
    return random.randint(0,6)
def main():
    roll=0
    while roll != 5:
        roll=ranNumbers()
        print(roll)
    print("Thank you for playing!")
main()