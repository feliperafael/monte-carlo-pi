#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:23:28 2018

@author: Felipe Rafael de Souza
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#return true if x,y inside of range of interest 
def inside(x,y,z):
    if (z <= 8 -x**2 - y**2) and (z >= x**2 + 3*y**2):
        return True
    return False

def f(x):
    return np.sqrt(1 - x**2)

n_samples = 100000
start_x, start_y, start_z = -2, -2, 0
end_x, end_y, end_z = 2, 2, 8

x_inside = []
y_inside = []
z_inside = []

x = np.random.uniform( start_x, end_x, n_samples);
y = np.random.uniform( start_y, end_y, n_samples);
z = np.random.uniform( start_y, end_y, n_samples);

for i in range(n_samples):
    if inside(x[i],y[i],z[i]):
        x_inside.append(x[i])
        y_inside.append(y[i])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.figure(1)
plt.plot(x,y,z,'o', color='blue',markersize=2,alpha=0.01)
plt.plot(x_inside,y_inside,y_inside,'o', color='red',markersize=3,alpha=0.1)

#plt.plot(np.sort(x),f(np.sort(x)), color='black', linewidth=2.0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



A = (float(len(x_inside)))/(float(n_samples)) #points_inside/total_points
print(A)

plt.title("Volume value = "+str(A)+" with "+str(n_samples)+" samples")
plt.savefig('volume_'+str(n_samples)+'.png')
plt.show()
