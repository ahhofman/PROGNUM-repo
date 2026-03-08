#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import numpy as np
from numpy import sin, cos, exp, pi
import scipy

while True:
   try:
       fun = input("Enter a function f(x)=")
       a = eval(input("Lower bound:"))
       b = eval(input("Upper bound:"))
       n = int(input("Number of data points:"))
       x = np.random.uniform(a, b, n)
       y = eval(fun, {"x": x, "sin": sin, "cos": cos, "exp": exp, "pi": pi, "np": np})
       int_ = ((b-a)/n)*np.sum(y)     
       print(f"The intergral of {fun} from {a} to {b} using Monte Carlo integration is {int_}.")
       break
   except TypeError:
      print("Wrong object type for this value")
   except NameError:
       print("This variable was not defined")
   except ValueError:
       print("The value is wrong")
   except ZeroDivisionError:
       print("Can't divide by zero")
   except SyntaxError:
       print("The syntax is wrong")

