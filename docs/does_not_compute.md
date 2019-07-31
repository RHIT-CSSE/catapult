# Does Not Compute

A very informal introduction to incomputability

Catapult 2019

# Are there things that cannot be computed?

* I'm not talking philosophical things "can an Artificial Intelligence
  feel love?"​
* Or fuzzy things like "can a computer detect a great essay?"​
* But rather, are there true formal mathematical properties that can't
  be calculated by a computer?​
* An example of a formal mathematical property is "is X prime?"​
  - But we can calculate if a number is prime

# A Calculation

    def ends_with_d(input):​
        if input[-1] == 'd':
            return True
        else:
            return False

Practice:

a.  ends\_with\_d('abcd')
b.  ends\_with\_d('dog')

# A Second Calculation

    def not_ends_with_d(input):
        if ends_with_d(input):
            return False
        else:
            return True

Practice:

a. not\_ends\_with\_d('abcd')
b. not\_ends\_with\_d(ends\_with\_d)
b. not\_ends\_with\_d(not\_ends\_with\_d)
        
# Calculation with a loop

    def next_multiple_of_10(input):
        loop:
            if input[-1] = '0':
                return input
            input = input + 1
            goto loop

Practice:

a. next\_multiple\_of\_10(100)
a. next\_multiple\_of\_10(8)

# Another calculation with a loop

    def is_even(input):
        loop:
            if input == 2:
                return True
            if input == 1
                return False
            input = input - 2
            goto loop

a. is\_even(4)
b. is\_even(5)
c. is\_even(98)
d. is\_even(-1)

# Running forever is bad

We should really write a program that detects if a given program runs
forever on a given input.

    def check_halts(input_program, input_data):
        # really awesome programming goes here
        # note that this checker program never runs forever
        
a. check\_halts(ends\_with\_d, 'hello')
b. check\_halts(is_even, 98)
c. check\_halts(is\_even, -1)
d. check\_halts(check\_halts, ????)

# A bad example

    def bad\_program(input_program):
        if not check_halts(input_program, input_program):
            return True
        else:
            loop:
                # does nothing so loops forever
                goto loop

a. bad\_program(ends\_with\_d)
b. bad\_program(check\_halts)
c. bad\_program(bad\_program)

# Let's break the last one down

## assume bad\_program(bad\_program) runs forever

Then check\_halts(bad\_program, bad\_program) returns false

Then tracing the code of bad\_program we see that it returns true and halts

Contradiction!

## assume bad\_program(bad\_program) runs halts

Then check\_halts(bad\_program, bad\_program) returns true

Then tracing the code of bad\_program we see that it runs forever

Contradiction!

# What does this mean?

The idea that a program that can check if another program will run
forever is self-contradictory.

This is halting problem and it's the first incomputable function.
            
# Some intuition

Does this run forever?

    def femat():
        loop:
            if a^n + b^n == c^n:
                return True
            # adjust a b c and n to visit all 
            # number combinations, n > 2 a b c > 0
            goto loop

# Are other things incomputable?

Consider

    def can_return_true(input_program):
        # returns true if the input program can
        # ever return true, for any input

# Anything that lets you build impossible things...
...is itself impossible.

    def weird(some_program, some_input):
        some_program(some_input)
        # ignore the result
        return True
        
    def check_halts(some_program, some_input)
        if can_return_true(weird(some_program, some_input)):
            return True
        else:
            return False

# What to take away?

+ I wanted to show that there were certain formal mathematical
  properties that cannot be computed
+ Whether a program terminates is a formal property that can't be
  computed
+ There is something about computing systems that are fundamentally
  unpredictable
+ A approximately similar argument to this is used to prove Godel's
  incompleteness theorem that it doesn't tend to possible to build
  formal systems free of paradox
+ Theoretical computer science is weird (but hopefully cool)
