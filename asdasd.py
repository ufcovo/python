from random import randint # For gettin a random number
import math #For the math function we used in 10 line

def create_number_of_point ():  #In this function we create the random numbers.
    x2 = randint (-20, 20) #This is for the x2 value
    y2 = randint (-20, 20) #This is for the y2 value
    return (x2, y2) # We return what we got the numbers

def calculate_distance (x1, x2, y1, y2):
    return math.sqrt ( (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) #This is how to calculate distance
    #return math.sqrt ( pow(x2, 2) + pow(y2, 2)) #Also we can use this because x1 and x2 are the centre points which are the 0 for this question.

def calculate_scors (x1, x2, y1, y2):
    print ("Hit points are: ", (x2, y2))
    print ("Center points are: ", (0, 0))
    distance = calculate_distance (x1, x2, y1, y2)
    print ("The distance is: ", distance)

def calculate_the_score ():
    if 0 <= distance <= 19:
        print ("Result: True")
        print ("Hit the board!")
    
        if 0 <= distance <= 3:
            print ("Score: ", 10)
        elif distance <= 4 and distance <= 7:
             print ("Score: ", 5)
        elif distance <= 8 and distance <= 11:
            print ("Score: ", 3)
        elif distance <= 12 and distance <= 15:
            print ("Score: ", 2)
        elif distance <= 16 and distance <= 19:
            print ("Score: ", 1)
        elif distance > 19:
            print ("Score: ", 0)
            
    else:
        print ("Result: False")
        print ("Outside of the dart board!")
        
    print("--------------------------------------")
    
print("\t^^**Playing Dart Game **^^\t")
print("*^"*25)

print("-"*40)
l = []

for i in range(10):
    l.append(generatePoint())
    
for i in l:
    x2,y2 = i
    calculate(0,x2,0,y2)