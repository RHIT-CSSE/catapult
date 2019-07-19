# First we define the class:

class Employee:

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# End of class definition

# Now we can use the class, either here, or in other python files in the same directory.
# In the latter case, we would say "import EmployeeClass" to get access to this class.

# Let's try a couple examples here:

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
print ("Employee 1 age is ",emp1.age)

# same kind of thing but usings lists
# lets give everbody a raise!
all_employees = [emp1, emp2]
for e in all_employees:
   e.salary = e.salary + 100
   e.displayEmployee()
