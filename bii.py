# method for b. ii)
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


a = input("sayi1: ")
b = input("sayi2: ")
multiply(a,b)
print(a,b)