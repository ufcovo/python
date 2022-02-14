def digits(n):
    # if n is 0, returning a list with only 0 as element
    if n == 0:
        return [0]
    # otherwise using modulo operator, finding last digit
    last_digit = n % 10
    # removing last digit from n
    n = n // 10
    # if n is now 0, returning a list containing last_digit only
    if n == 0:
        return [last_digit]
    # otherwise calling digits on new n, combining the resultant list with a list containing
    # last_digit and returning combined list
    else:
        return digits(n) + [last_digit]
number = int (input("Enter a number: "))
degits(number)