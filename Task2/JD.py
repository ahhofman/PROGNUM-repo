#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

D = float(input("What is the day?"))
M = float(input("What is the month?"))
Y = float(input("What is the year?"))

JD = 367*Y -7*(Y+(M+9)//12)//4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print(f"The Julian Date corresponding to the date you input is {JD}")

