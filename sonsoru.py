def digits(n):
    if n == 0:
        return [0]
    last_digit = n % 10
    n = n // 10
    if n == 0:
        return [last_digit]
    else:
        return digits(n) + [last_digit]

def multiply(a, b):
    # if a or b is 0, returning list containing 0
    if a == 0 or b == 0:
        return [0]
    # otherwise parsing first number into list
    first = digits(a)
    # parsing second number into list
    second = digits(b)
    # removing first element from second list (which will be 1)
    second = second[1:]
    # returning a new list containing elements of first and second lists combined
    return first + second
val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
print(multiply(val1, val2))
