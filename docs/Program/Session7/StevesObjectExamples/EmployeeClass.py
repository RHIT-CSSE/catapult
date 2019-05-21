# First we define the class:

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
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
print ("Total Employee %d" % Employee.empCount)

emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
print ("Employee 1 age is ",emp1.age)
del emp1.age  # Delete 'age' attribute.
