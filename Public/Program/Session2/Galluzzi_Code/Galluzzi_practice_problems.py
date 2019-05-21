'''********************
Description: Takes the x and y coordinates of a
point and prints its distance from (0,0)
Inputs: x and y coordinates of a point as ints
Outputs: None
Side effects: Prints a distance
********************'''
def problem1(x,y):
    print((x**2+y**2)**.5)
print("Testing problem 1")
print("Should be 3.0")
problem1(0,3)

print("Should be 4.0")
problem1(4,0)

print("Should be ~2.8")
problem1(2,2)

'''********************
Description: Takes the side length of a square
and returns its area
Inputs: side length of a square as an int
Outputs: area of the square
Side effects: None
********************'''
def problem2(side):
    return side**2

print("\nTesting problem 2")
print("Should be 9")
problem2(3)

'''********************
Description: Takes a day, month, and year and
prints the season
Inputs: Day, Month, and Year as ints
Outputs: None
Side effects: Prints messages
********************'''
def problem3(day,month,year):
    if month==12 or month<3:
        print("Winter")
    elif month<7:
        print("Spring")
    elif month<10:
        print("Summer")
    else:
        print("Fall")

print("\nTesting problem 3")
print("Should be Winter")
problem3(1,12,2016)

print("Should be Winter")
problem3(1,2,2016)

print("Should be Spring")
problem3(1,4,2016)

print("Should be Summer")
problem3(1,7,2016)

print("Should be Fall")
problem3(1,8,2016)

'''********************
Description: Takes input number and prints
whether it is "Good" or "Bad"
Inputs: an integer
Outputs: None
Side effects: Prints messages
********************'''
def problem4(value):
    if -5<value<5:
        print("Good")
        if -1<value<1:
            print("Zero")
    else:
        print("Bad")

print("\nTesting problem 4")
print("Should be Good")
problem4(4)
print("Should be Good and Zero")
problem4(0)
print("Should be Bad")
problem4(7)

'''********************
Description: Takes input number and prints
a series of numbers between the number and
2*that number
Inputs: an integer
Outputs: None
Side effects: Prints messages
********************'''
def problem5(itself):
    for i in range(itself+1):
        print(itself+i)
print("\nTesting problem 5")
print("Should print 3-6")
problem5(3)

'''********************
Description: Takes input number and prints
a series of numbers starting with that number
and ending with a number divisible by 7
Inputs: an integer
Outputs: None
Side effects: Prints messages
********************'''
def problem6(itself):
    p=itself
    while(p%7!=0):
        print(p)
        p=p+1
print("\nTesting problem 6")
print("Should print nothing")
problem6(7)
print("Should print 4-6")
problem6(4)

'''********************
Description: Finds area of squares with side lengths
between zero and the given end length
Inputs: an integer indicating the end length
Outputs: None
Side effects: Prints messages
********************'''
def problem7(end):
    for i in range(end):
        print(problem2(i))
print("\nTesting problem 7")
print("Should print nothing")
problem7(0)
print("Should print 0,1,4,9")
problem7(4)

'''********************
Description: Finds area of squares with side lengths
between zero and the given end length
Inputs: an integer indicating the end length
Outputs: None
Side effects: Prints messages
********************'''
def problem7(end):
    for i in range(end):
        print(problem2(i))
print("\nTesting problem 7")
print("Should print nothing")
problem7(0)
print("Should print 0,1,4,9")
problem7(4)
