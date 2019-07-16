# Here's what it does.
from math import *
from Session3FirstProgram import divisorsOf, seasonOf

def myNewFunction(x,y):
    returnValue = "Here's x and y "+str(x)+", "+str(y)
    return returnValue

print("Starting my program.")
print(sqrt(7))
print(myNewFunction(3,5))
for x in range(10):
    for y in range(5) :
        print(myNewFunction(x,y))
