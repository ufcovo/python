x = int (input("Enter first number: "))
y = int (input("Enter second number: "))
z = input("Choose an operator (+,-,/,*): ")

if z == '+' :
    sum = x + y
    print("Sum = ", sum)
    
elif z == '-' :
    fraction = x - y
    print("Fraction =  ", fraction)
elif z == '/' :
    div = x / y
    print("Division =  ", div)
else :
    mult = x * y
    print("Multiply = ", mult)