from random import randint # For gettin a random number
import math #For the math function we used in 13 line
    
print("\t^^** Playing Dart Game **^^\t") # This show the game is starting
print("*^" * 25)
print("-----------------------------------------")

def create_number_of_point (hit_points):  #In this function we create the random numbers.
    x2 = randint (-20, 20) #This is for the x2 value
    y2 = randint (-20, 20) #This is for the y2 value
    return (x2, y2) # We return what we got the numbers

#This map function show that create 10 randomly numbers and stores the list_for_tupple and send to create_number_of_points
list_for_tupple = list (map (create_number_of_point, range (10)))

def calculate_distance (x2, y2): #In this function we calculate the distance
    return math.sqrt ( pow(x2, 2) + pow(y2, 2)) #This is how to calculate distance.
    #return math.sqrt ( (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) #Also we can use that but x1 and x2 is centre points which means 
                                                                        #their values are 0,0. So there is no needed x1 and x2 values.

def calculate_scores (hit_points): #In this function we calculate scores.
    print ("fd")
    #x1 = 0
    #y1 = 0
    #18 and 19 lines are for 26 line
    x2, y2 = hit_points   #These are the hit points which are randomly numbers 
    print ("Hit points are: ", (x2, y2)) #These x2 and y2 numbers are the hit points which are randomly created.
    print ("Center points are: ", (0, 0)) #This is center points which is 0,0
    distance = calculate_distance (x2, y2) #This is for assign on distance what we got calculate_distance before
    #distance = calculate_distance (x1, x2, y1, y2) #This is for assign on distance what we got calculate_distance before
    print ("The distance is: ", distance) #This is distance.

    if 0 <= distance <= 19: #This is if distance between 0 and 19 the result is true and hit the board.
        print ("Result: True")
        print ("Hit the board!")
    
        if 0 <= distance <= 3: #This is for 10 points creteria
            print ("Score: ", 10)
        elif distance <= 4 and distance <= 7: #This is for 5 points creteria
             print ("Score: ", 5)
        elif distance <= 8 and distance <= 11: #This is for 3 points creteria
            print ("Score: ", 3)
        elif distance <= 12 and distance <= 15: #This is for 2 points creteria
            print ("Score: ", 2)
        elif distance <= 16 and distance <= 19: #This is for 1 points creteria
            print ("Score: ", 1)
        elif distance > 19: #This is for 0 points creteria
            print ("Score: ", 0)
            
    else: #If the distance is not between 0 and 19 then result false and outside of the dart board
        print ("Result: False")
        print ("Outside of the dart board!")
        
    print("-----------------------------------------")

#This map function show that the numbers where take list_for_tupple and stores calculate_numbers and send to calculate_numbers.
calculate_numbers = list (map (calculate_scores, list_for_tupple))