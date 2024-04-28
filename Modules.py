#Calci.py
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a//b


from Calci import *  #to import all methods of calci Calci-->user defined module
print(add (2,8))
print(subtract(12,2))
print(multiply(2,5))
print(divide(20,2))

Output
10
10
10
10

from Calci import add
print(add(5,8))
from Calci import subtract
print(subtract(5,8))
from Calci import multiply
print(multiply(5,8))
from Calci import divide
print(divide(5,8))

Output
13
-3
40
0

import Calci
print(Calci.add (2,8))
print(Calci.subtract(12,2))
print(Calci.multiply(2,5))
print(Calci.divide(20,2))

Output
10
10
10
10

