number = int(input("Insert a number: "))

try:
    if number % 2 == 0:
        print("The number is EVEN")
    else:
        print("The number is ODD")
except ValueError:
    print("You did not enter an integer")