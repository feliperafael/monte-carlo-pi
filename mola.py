#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 18:59:57 2018

@author: felipe
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


def sigma(d,D,P,alpha):
    return ((16*P*D)/(np.pi*d*d*d))*(1 + d/(4*D))*np.sin(alpha)

def tal(d,D,P,alpha):
    return ((8*P*D)/(np.pi*d*d*d))*(1 + d/(2*D))*np.cos(alpha)

def delta(d,D,P,alpha,n,E,G):
    return ((8*P*D*D*D*n)/(d*d*d*d*np.cos(alpha)))*(2*(1 + ((d*d)/(4*D*D)))*((np.sin(alpha*np.sin(alpha)))/E) + (1+ (d*d)/(2*D*D))*((np.cos(alpha)*np.cos(alpha))/E*G))

n_samples = 1000
P = 12 #forca em kNewton
d = np.random.uniform( 19, 21, n_samples);
D = np.random.uniform( 77, 83, n_samples);
alpha = np.random.uniform( 13, 17, n_samples);
E = np.random.uniform( 197, 203, n_samples);
G = np.random.uniform( 77, 83, n_samples);

sigma_v = []
tal_v = []
delta_v = []

for i in range(n_samples):
    sigma_v.append(sigma(d[i],D[i],P,alpha[i]))
    tal_v.append(tal(d[i],D[i],P,alpha[i]))
    delta_v.append(delta(d[i],D[i],P,alpha[i],10,E[i],G[i]))
    
plt.hist(sigma_v, bins=30)
plt.ylabel('amostras')
plt.xlabel('sigma')
plt.title('Mean: '+str(np.mean(sigma_v))+' STD:'+str(np.std(sigma_v)))
plt.savefig('sigma.png')
plt.show()

plt.hist(tal_v, bins=30)
plt.ylabel('amostras')
plt.xlabel('tal')
plt.title('Mean: '+str(np.mean(tal_v))+' STD:'+str(np.std(tal_v)))
plt.savefig('tal.png')
plt.show()

plt.hist(tal_v, bins=30)
plt.ylabel('amostras')
plt.xlabel('delta')
plt.title('Mean: '+str(np.mean(delta_v))+' STD:'+str(np.std(delta_v)))
plt.savefig('delta.png')
plt.show()

print("Media Sigma: "+str(np.mean(sigma_v)))
print("Desvio Padrao Sigma: "+str(np.std(sigma_v)))
print()
print("Media tal: "+str(np.mean(tal_v)))
print("Desvio Padrao tal: "+str(np.std(tal_v)))
