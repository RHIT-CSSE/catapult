# Does Not Compute

A very informal introduction to incomputability

Catapult 2019

# Are there things that cannot be calculated?

* I'm not talking philisophical things "can an Artificial Intelligence
  feel genuine love?"​
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
        loop_forever:
            if input[-1] = '0':
                return input
            input = input + 1

Practice:

a. next\_multiple\_of\_10(100)
a. next\_multiple\_of\_10(8)

# Another calculation with a loop

    def is_even(input):
        loop_forever:
            if input == 2:
                return True
            if input == 1
                return False
            input = input - 2

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
d. check\_halts(always\_halts, ????)

# A bad example

    def bad\_program(input_program):
        if not check_halts(input_program, input_program):
            return True
        else:
            loop_forever:
                # does nothing so loops forever

a. bad\_program(ends\_with\_d)
b. bad\_program(always\_halts)
c. bad\_program(bad\_program)

# What does this mean?

The idea that a program that can check if another program will run
forever is self-contradictory.

This is halting problem and it's the first incomputable function.
            
# Some intuition

