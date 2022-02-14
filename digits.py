# Mert Bulut 17243510036
# conversion of number to list of integers 
# using list comprehension 
  
# initializing number  
num = input("Enter a number: ")
  
# printing number  
print ("The original number is " + str(num)) 
  
# using list comprehension 
# to convert number to list of integers 
res = [int(x) for x in str(num)] 
  
# printing result  
print ("The list from number is " + str(res)) 