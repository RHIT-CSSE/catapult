from EmployeeClass import Employee

# We're going to use the class defined in the other file, above

emp3 = Employee("Derek", 6000)
emp4 = Employee("Anthony", 7000)

emp3.displayEmployee()
emp4.displayEmployee()

print ("Total Employee %d" % Employee.empCount)

# Notice that Python ran the code from the other class first, the one we imported, above.

# That includes other stuff besides just getting the class definition from there!

