'''random module isused to get the random integers in apriticular range. the math module is used to find 
the euclidean distance'''
from random import  randint
import math
''' returns  the euclidean distance of the two  point (x1,y1) and (x2,y2)'''
def getDistance(x1,x2,y1,y2):
    return math.sqrt((x1-x2)*(x1-x2)+ (y1-y2)*(y1-y2))
'''generates tge random point (x2,y2) and returns that point'''
def generatePoint ():
    '''generates the integer in the range of -20 to 20'''
    x2 = randint(-20,20)
    y2 = randint(-20,20)
    return (x2,y2)
'''calculates the process of the game'''
def calculate(x1,x2,y1,y2):
    '''get the distance'''
    distance = getDistance(x1,x2,y1,y2)
    print("Hit points  is : ", (x2,y2))
    print("Center point is :", (0,0))
    print("The distance is :", distance)
    '''checking the distance if it valid(with in the board then displays the score)
    otherwise else block will executes then out of board message will be displayed.'''
    if 0 <= distance <= 11:
        print("Result: True")
        print("Hit the board!")
        '''if distance is 0 to 3 then if block is executed.
        if the distance is 4  to 7 then second elif block is executed
        other wise the last elif block is executed'''
        if 0 <= distance <= 3:
            print("Socere: ",10)
        elif distance > 3 and distance <= 7:
            print("Score: ",5)
        elif distance >7 and distance <= 11:
            print("Score: ",3)
        elif distance > 11 and distance <= 15:
            print("Score: ", 2)
        elif distance > 15  and distance <= 19:
            print("Score: ", 1)
        elif distance > 19:
            print("Score: ", 0)
    else:
        print("Result: False")
        print("Outside of the dart board'")
    print("-"*40)
'''printing the starting of the game page'''
print("\t^^**Playing Dart Game **^^\t")
print("*^"*20)
print("-"*40)
'''Generates the 10  points and then it will  stores that points into  the list l.'''
l = []
for i in range(10):
    l.append(generatePoint())
'''for each value in the list it will calls the calculate() function and prints the output.'''
for i in l:
    x2,y2 = i
    calculate(0,0,x2,y2)