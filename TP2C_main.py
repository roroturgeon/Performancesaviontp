# -*- coding: utf-8 -*-
"""
AER8375 - Performances avion

Script principal d'exécution du TP2C

@author: Rosalie Turgeon & Vincent Moreau
         ( 2072092 )       ( 2075782 )
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces
from TP2B import montee

import warnings
warnings.filterwarnings("ignore")

"""
Question 5
"""
print("\n\n===================")
print("=   Question 5    =")
print("===================")



Hp = 5000
T_C = 38
delISA = False
W = 35000
dVolets = 20
pRoues = "up"
rMoteur = "OEI"
pVol = "MTO"
Vconst = "CAS"
CG=.25
nz=1
VVsr=1.15

# Génération du graphique illustrant la relation entre le gradient et le poids
W_min = 10000    # Valeurs de poids initiale
W_max = 75000     # Valeurs de poids finale
W_arr = np.linspace(W_min, W_max, 100)
grad_arr = np.zeros_like(W_arr)

for i in range(len(W_arr)):
    grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W_arr[i], CG, dVolets, pRoues, rMoteur, pVol, Vconst, VVsr=VVsr,nz=nz)
    grad_arr[i] = grad
plt.figure(dpi=500) 
plt.title("Gradient de monté selon le poids")
plt.plot(W_arr, grad_arr)
plt.xlabel("Poids [lbs]")
plt.ylabel("Gradient [-]")
#grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, VVsr=VVsr,nz=nz)

W_min = 10000     # Valeurs de vitesse initiale maximales et minimales pour itérer
W_max = 100000     # Valeurs de vitesse initiale maximales et minimales pour itérer

erreur = 1      # Écart de départ pour initialiser
eps=0.0001      # Tolélance d'écart entre calcul de deux valeurs de gradient pour critère d'arrêt
grad_target=0.03
nbiter=0
while erreur>eps:
    nbiter+=1
    W=(W_min+W_max)/2
    grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, VVsr=VVsr,nz=nz)
    erreur = abs(grad-grad_target)
    if grad-grad_target>0:
        W_min=W
    else: 
        W_max=W
        
    
print("Poids trouvé : ",W," [lbs]")
print("Gradient trouvé : ",grad," [-]")
print("Erreur : ",erreur)
print("Nombre d'itérations : ",nbiter)





"""
Question 6
"""
print("\n\n===================")
print("=   Question 6    =")
print("===================")



Hp = 12000
T_C = 10
delISA = True
W = 35000
dVolets = 0
pRoues = "up"
rMoteur = "OEI"
pVol = "MCT"
Vconst = "CAS"
CG=.25
nz=1

# Génération du graphique illustrant la relation entre le gradient et le nombre de Mach
M_min = 0.1     # Valeurs de vitesse initiale maximales et minimales pour itérer
M_max = .85     # Valeurs de vitesse initiale maximales et minimales pour itérer
M_arr = np.linspace(M_min, M_max, 100)
grad_arr = np.zeros_like(M_arr)

for i in range(len(M_arr)):
    grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, M=M_arr[i],nz=nz)
    grad_arr[i] = grad
plt.figure(dpi=500)    
plt.plot(M_arr, grad_arr)
plt.title("Gradient de monté selon le nb de Mach")
plt.xlabel("M [-]")
plt.ylabel("Gradient [-]")

# Initialisation de la méthode de maximisation
step_size = 0.0001
eps = 0.0001
learn_rate = 0.01
iter_max = 10000
pente = 1           # Initialisation pente pour while
M_eval_position = 0.1       

while abs(pente)>eps and iter_max>0:
    grad = montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, M=M_eval_position,nz=nz)[0]
    grad_eps = montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, M=M_eval_position+eps,nz=nz)[0]
    pente=(grad_eps-grad)/eps
    M_eval_position += learn_rate*pente
    iter_max-=1
print("Nombre de Mach = ",M_eval_position," [-]")
print("Grad = ",grad," [-]")
print("Critère d'arrêt : ",eps)
print("Nombre d'itérations : ",10000-iter_max)



"""
Question 7
"""
print("\n\n===================")
print("=   Question 7    =")
print("===================")



Hp = 30000
T_C = 25
delISA = True
W = 47000
dVolets = 0
pRoues = "up"
rMoteur = "AEO"
pVol = "MCR"
Vconst = "MACH"
CG=.25
nz=1
M_min = 0.1     # Valeurs de vitesse initiale maximales et minimales pour itérer
M_max = 1.5     # Valeurs de vitesse initiale maximales et minimales pour itérer

erreur = 1      # Écart de départ pour initialiser
eps=0.0001      # Tolélance d'écart entre calcul de deux valeurs de ROC pour critère d'arrêt
nbiter=0
while erreur>eps:
    nbiter+=1
    M=(M_min+M_max)/2
    grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, M=M,nz=nz)
    erreur = abs(grad)
    if grad>0:
        M_min=M
    else: 
        M_max=M
    # print("\ngrad=",grad)
    # print("M=",M)

print("Nombre de Mach : ",M, " [-]\nGradient : ",grad," [-]\nErreur  : ",erreur,"\nNombre d'itérations : ",nbiter)
    


