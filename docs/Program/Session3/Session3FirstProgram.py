# This is an example of a whole program, for you to modify.
# It shows "for loops", "while loops" and "if statements".
# And it gives you an idea of how function calls would be used
# to make an entire program do something you want.

# Python reads the program from top to bottom:
# First there are two functions.  These don't really "do"
# anything until they are called later.

# This function finds the prime divisors of a number.
# Nothing to do here, but it shows a function with a while-loop
# and an if-statement.

def divisorsOf(bigNumber):
    listOfDivisors = [] # An empty list, to start building from
    nextNumber = bigNumber
    nextDivisor = 2
    while (bigNumber > 1):
        if (bigNumber % nextDivisor == 0):
            #print(" "+str(nextDivisor))
            bigNumber = bigNumber // nextDivisor
            listOfDivisors.append(nextDivisor) # add to the list
        else:
            nextDivisor = nextDivisor+1
    return listOfDivisors


# This function finds the season of a date, as in the Session 2 slides.
# The year parameter isn't used!
# This one has a "TODO" at the bottom:

def seasonOf(date): # The date is a "tuple" of month, day, year
    month = date[0] # These commands separate the 3 parts of the tuple
    day = date[1]
    year = date[2]
    season = "error" # in case a date is not assigned to a season
    if (month == 10 or month == 11):
        season = "fall"
    elif (month == 1 or month == 2):
        season = "winter"
    elif (month == 4 or month == 5):
        season = "spring"
    elif (month == 7 or month == 8):
        season = "summer"
    elif (month == 12):
        if (day < 21):
            season = "fall"
        else:
            season = "winter"
    elif (month == 3):
        if (day < 21):
            season = "winter"
        else:
            season = "spring"
    return season
# TODO: You finish this function, for months 6 and 9, above the return!

# Then here's the part of the program which really causes
# something to happen.  Code that includes calling the functions
# defined above:

# Test cases:
print("Divisor tests:")
# The for-loop picks consecutive values from a Python "list":
for myDivisorTest in [2,3,4,5,6,7,8,9,12,13,24,35]:
    print("Prime divisors of "+str(myDivisorTest))
    print (divisorsOf(myDivisorTest))


print("Season tests:")
# This is a list of "tuples" representing dates:
myDateList = [ (1,1,2019), (2,1,2019), (3,1,2019), (3,25,2019),
    (4,1,2019), (5,1,2019), (6,1,2019), (6,25,2019),
    (7,1,2019), (8,1,2019), (9,1,2019), (9,25,2019),
    (10,1,2019), (11,1,2019), (12,1,2019), (12,25,2019) ]

for myDateTest in myDateList:
    print (seasonOf(myDateTest))
