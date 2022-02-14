#Mert Bulut 17243510036
#This part for a
def dels (list1, list2):

    # To check if list1 is longer than list2    
    if (len (list1) > len (list2)):
        # removing first len(lst2) number of elements from lst1
        list1 = list1[len(list2):]
        # returning it
        return list1  
   
    # To check if list1 is shorter than list2
    elif (len (list2) > len (list1)):
        """ To take the first element of list2, to add to a list, combining with elements of list1 and then combining with rest of 
            elements in list2, returning combined list. Furthermore, list2[1:] is going to return a list with all elements of list2
            expect the first element. """
        return (list2[0:1] + list1 + list2[1:])
      
    # Otherwise lengths are same so returning empty list
    else:
        return []
#To try part a
print (dels ([3,4,2,5,6,7], [1,3,4]))
print (dels ([2,5], [3,4,7,8,9]))
print (dels ([2,3,4], [8,7,9]))

# We cannot convert integer to list directly. Thus, first converting integer to string and string to list

#This part for b.i
# We cannot convert integer to list directly. Thus, first converting integer to string and string to list
def digits(count):
    count = str (count)         # converting integer to string
    makeList = list (count)     # converting string to list
    return makeList             # returning the list
print (digits (532))            # calling digit function and printing it

""" 
#This is another way for part b.i
# code to convert integer number into list of digits in number
def digits(val): 
    print ("The given number is " + str(val)) 
    res = [int(x) for x in str(val)] 
  
   # printing result  
    print ("The list from number is " + str(res)) 

value = int (input("Enter a number: "))
digits(value)
"""

#This part for b.ii
def multiply (value1, value2):
    multyValue = value1 * value2     # multiply two values
    multyValue = str (multyValue)     # converting integer to string
    makingList = list (multyValue)    # converting string to list
    return makingList                # returning the list
print (multiply (532, 1000))         # calling multiply function and print it