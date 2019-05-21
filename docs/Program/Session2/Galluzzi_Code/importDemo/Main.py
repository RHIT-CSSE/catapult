#------------------
# How import works? Either of those works:
#------------------
## import all components from other module
## This is equivalent to just copy and past all the content of GraphicsLib over here
import module1
print(module1.global_variable_in_module1)
module1.global_function_in_module1("Fred")
y = module1.global_class_in_module1()
print(y)


## import as a whole module
from module1 import *
print(global_variable_in_module1)
global_function_in_module1("Fred")
x = global_class_in_module1()
print(x)
