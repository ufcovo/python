#part a
def dels(x,y):

    #If the length value of x is greater than the length value of y
    #After that return x, by delete first len(y) units
    if(len(x)>len(y)):
        return x[len(y):]
    #If the length value of y is greater than the length value of x
    #After that return y, by delete first len(x) units
    elif(len(y)>len(x)):
        return (y[0:1]+x[:]+y[1:])
    #if the lengths of the two lists are equal
    #return empty list
    else:
        return []
#trying part a
print(dels([3,4,2,5,6,7],[1,3,4]))
print(dels([2,5],[3,4,7,8,9]))
print(dels([2,3,4],[8,7,9]))

# cannot convert int to list directly
# hence convert int to string first
# and string to list

# part b.1

def digits(p):
    p = str(p)  # convert int to string
    r = list(p)  # convert string to list
    return r  # return the list

#part b.2

def multiply(a, b):
    p = a * b  # multiply two numbers
    p = str(p)  # int to string
    r = list(p)  # string to list
    return r  # return the list


print(digits(532))  # calling digit function
print(multiply(532, 1000))  # calling multiply f