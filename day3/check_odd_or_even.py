def even(n):
    return n % 2 == 0   #Don't need the if/else inside the function because the expression n % 2 == 0 already returns True or False directly.
    
number = int(input("Insert a number:"))

if even(number):
    print("The number is EVEN")
else:
    print("The number is ODD")