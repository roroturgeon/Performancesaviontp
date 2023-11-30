# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:19:03 2023

AER8375 - Performances avion

Script principal d'exécution du TP4C

@author: Rosalie Turgeon & Vincent Moreau
         ( 2072092 )       ( 2075782 )
"""

import numpy as np
import matplotlib.pyplot as plt
from TP4B import longpiste

# CAS 3
V1VR = 1    # V1/VR
# W =  30000      # Poids (lbs) (VALEUR INITIALE SEULEMENT1)
Hp = 0          # ft
delISA = True   # Déviation isa
T_C = 20        # °C
CG = 0.09
l_piste_tot=5700        # [pi]
RAD = 200               # [pi]
l_piste_dispo = l_piste_tot - RAD


nbitermax=50
# Plage de poids et de ratio V1VR pour maximiser le poids

W_max = 53000
W_min = 31500
W_lo = W_min
W_hi = W_max
V1VR_max = 1
V1VR_min = 0.6
V1VR_arr=np.linspace(V1VR_min,V1VR_max, 100)

nbiter=0

while nbiter<nbitermax:
    nbiter+=1
    W=(W_lo+W_hi)*.5
    LMIN_arr = np.zeros_like(V1VR_arr)
    for i in range(len(V1VR_arr)):
        LMIN_arr[i]=longpiste(V1VR_arr[i], W, Hp, T_C, delISA, CG)[3]
    succes = np.any(LMIN_arr[:]<l_piste_dispo)
    
    if succes:
        W_lo=W
    else:
        W_hi=W
    
# V1VR_min_trouve = False
# V1VR_max_trouve = False
# for i in range(len(LMIN_arr)):
#     if LMIN_arr[i]<l_piste_dispo and V1VR_min_trouve == False:
#         V1VR_min = V1VR_arr[i]
#         V1VR_min_trouve = True
#     if LMIN_arr[i]>l_piste_dispo and V1VR_max_trouve == False:
#         V1VR_max = V1VR_arr[i]
#         V1VR_max_trouve = True

plt.figure(dpi=500)
plt.plot(V1VR_arr,LMIN_arr)
plt.xlabel("V1VR [-]")
plt.ylabel("LMIN [pi]")
plt.plot([V1VR_min, V1VR_max], [l_piste_dispo,l_piste_dispo] ,'--')

print("Poids = ",W)
# print("V1VR (min) = ",V1VR_min)
# print("V1VR (max) = ",V1VR_max)

    
    
    
    
    
    
    
    
    
    