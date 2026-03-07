#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
import numpy as np
import scipy
import matplotlib.pyplot as plt

# Setting the calling envorinemnt

A = float(input("A value:"))
x0 = float(input("x0 value:"))
sigma = float(input("sigma value:"))
z0 = float(input("z0 value:"))
a = float(input("lower bound:"))
b = float(input("upper bound:"))

x = np.linspace(-10,10,200)

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

area_, error = scipy.integrate.quad(lambda x: A*np.exp(-(x-x0)**2/(2*sigma**2))+z0, a, b)

plt.scatter(x, gauss(x, A, x0, sigma, z0), label = f'Area = {area_}', marker= '*' )
plt.fill_between(x, gauss(x, A, x0, sigma, z0), where=(x >= a) & (x <= b), color = 'green', alpha = 0.4)
plt.legend(loc='upper right')
plt.show


# In[ ]:




