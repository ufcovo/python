from random import  randint
import math

def getDistance(x1,x2,y1,y2):
    return math.sqrt((x1-x2)*(x1-x2)+ (y1-y2)*(y1-y2))

def generatePoint (x):
    x2 = randint(-20,20)
    y2 = randint(-20,20)
    return (x2,y2)

def calculate(x):
    print('fd')
    x1,y1= 0,0
    x2,y2 = x
    
    distance = getDistance(x1,x2,y1,y2)
    print("Hit points  is : ", (x2,y2))
    print("Center point is :", (0,0))
    print("The distance is :", distance)
    
    if 0 <= distance <= 11:
        print("Result: True")
        print("Hit the board!")
        
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
print("\t^^**Playing Dart Game **^^\t")
print("*^"*20)
print("-"*40)

l = list(map(generatePoint,range(10)))

r = list(map(calculate,l))