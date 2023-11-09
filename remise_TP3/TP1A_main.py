# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:13:23 2023

@author: Vincent M & Rosalie T"""
import numpy as np
import math
from TP1A import atmosphere

hp_liste=np.array([-2000,20000,36089,40000])
T_liste=np.array([35,-40, -60,-50])
dISA_liste=np.array([-20,40,-10,10])

for i in range(len(hp_liste)):
    theta,delta,sigma,T_C,T_K,delISA,p,rho=atmosphere(hp_liste[i], T_liste[i],False)
    print("\n\nhp = %.4g" % (hp_liste[i])+", T = %.4g" % (T_liste[i]))
    print("\ntheta = %.4g" % (theta))
    print("delta = %.4g" % (delta))
    print("sigma = %.4g" % (sigma))
    print("T_C = %.4g" % (T_C))
    print('T_K = %.4g' % (T_K))
    print("delISA = %.4g" % (delISA))
    print("p = %.4g" % (p))
    print("rho = %.4g" % (rho))

for i in range(len(hp_liste)):
    theta,delta,sigma,T_C,T_K,delISA,p,rho=atmosphere(hp_liste[i], dISA_liste[i],True)
    print("\n\nhp = %.4g" % (hp_liste[i])+", T = %.4g" % (T_liste[i]))
    print("\ntheta = %.4g" % (theta))
    print("delta = %.4g" % (delta))
    print("sigma = %.4g" % (sigma))
    print("T_C = %.4g" % (T_C))
    print('T_K = %.4g' % (T_K))
    print("delISA = %.4g" % (delISA))
    print("p = %.4g" % (p))
    print("rho = %.4g" % (rho))
