#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:23:28 2018

@author: felipe
"""

import numpy as np
import matplotlib.pyplot as plt

#return true if x,y inside of range of interest 
def inside(x,y):
    if x**2 + y**2 < 1:
        return True
    return False

def f(x):
    return np.sqrt(1 - x**2)

n_samples = 100000
start_x, start_y = 0, 0
end_x, end_y = 1, 1

x_inside = []
y_inside = []

x = np.random.uniform( start_x, end_x, n_samples);
y = np.random.uniform( start_y, end_y, n_samples);

for i in range(n_samples):
    if inside(x[i],y[i]):
        x_inside.append(x[i])
        y_inside.append(y[i])

plt.figure(1)
plt.plot(x,y,'o', color='blue',markersize=3)
plt.plot(x_inside,y_inside,'o', color='red',markersize=3)

plt.plot(np.sort(x),f(np.sort(x)), color='black', linewidth=2.0)
plt.xlabel('x')
plt.ylabel('y')


A = (float(len(x_inside)))/(float(n_samples)) #points_inside/total_points
print(A*4.0)
plt.title("$\pi$ value = "+str(A*4.0)+" with "+str(n_samples)+" samples")
plt.savefig('img.png')
plt.show()
