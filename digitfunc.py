# code to convert integer number into list of digits in number
def digits(val): 
    print ("The given number is " + str(val)) 
    res = [int(x) for x in str(val)] 
  
   # printing result  
    print ("The list from number is " + str(res)) 

value = int (input("Enter a number: "))
digits(value)