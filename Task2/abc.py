#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

a = float(input("What's the value of a?"))
b = float(input("What's the value of b?"))
c = float(input("What's the value of c?"))

d = b**2-4*a*c

if d > 0:
    x1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    x2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    print(f"The roots of f(x) are {x1} and {x2}.")
elif d==0:
    x3 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    print(f"The root of f(x) is {x3}.")
else:
    print("There are no real solutions")

