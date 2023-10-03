# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:57:50 2023

@author: Vincent Moreau
"""

import numpy as np
import math
from TP1A import atmosphere
from TP1B import parametres_de_vol


""" --------------
--- Question 4 ---
---------------"""
print("Question 4 : ")
Vc=270
Hp=3000
T_C_min=-50
T_C_max=50
W=40000
delISA=True

# Altitude à varier par balayage pour obtenir un match de Mach = 0.76
V_kts_target=Vc

n=100           # nb max iter
e_t=0.00001       # Tolérance d'arrêt pour balayage, valeur absolue d'écart de Mach
    
for i in range(n): 
    
    T_C=(T_C_min+T_C_max)/2
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, Vc=Vc)
    e = np.abs(V_kts-V_kts_target)
    if e<e_t:
        break
    elif V_kts>V_kts_target: 
        T_C_max=T_C
    elif V_kts<V_kts_target:
        T_C_min=T_C
    else : 
        print("ERROR")
        
print("Nombre d'itérations : "+str(i))
print("e =    "+str(e)+" (erreur, M [-])")
print("Vt =    "+str(M)+"  (Vitesse vraie [kt])" )
print("delta ISA = "+str(T_C)+"   (Variation v.s. ISA [°C])")
print("Vc =   "+str(Vc)+"                   (Vitesse calibrée [kt])")


""" --------------
--- Question 5 ---
---------------"""

print("\n \n Question 5 : ")
Vc = 275        # kts
W = 40000       # lbs
delISA = True   # Utilisation de l'écart par rapport à ISA v.s. température réelle
T_C=0           # °C

#Hp=3000

# Altitude à varier par balayage pour obtenir un match de Mach = 0.76
Hp_low=0        # ft (M<0.76)
Hp_high=55000   # ft (M>0.76)
M_t = 0.76      # [-] M target

n=100           # nb max iter
e_t=0.00001       # Tolérance d'arrêt pour balayage, valeur absolue d'écart de Mach
    
for i in range(n): 
    
    Hp=(Hp_low+Hp_high)/2
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, Vc=Vc)
    e = np.abs(M-M_t)
    if e<e_t:
        break
    elif M>M_t : 
        Hp_high=Hp
    elif M<M_t:
        Hp_low=Hp
    else : 
        print("ERROR")
        
print("Nombre d'itérations : "+str(i))
print("e =    "+str(e)+" (erreur, Vt [kt])")
print("M =    "+str(M)+"    (Mach [-])" )
print("Hp =   "+str(Hp)+"    (Altitude pression [pi])") 
print("Tt_C = "+str(Tt_C)+"   (Température totale [°C])")
print("Vc =   "+str(Vc)+"                   (Vitesse calibrée [kt])")
#print("M =    "+str(M)+"    (")

""" --------------
--- Question 6 ---
---------------"""

print("\n\nQuestion 6 : ")

Hp=15000
T_C=0
delISA=False
Tt_C_target = 10
Vc_min=0
Vc_max=500

n=100           # nb max iter
e_t=0.00001       # Tolérance d'arrêt pour balayage, valeur absolue d'écart de Mach


for i in range(n): 
    
    Vc=(Vc_min+Vc_max)/2
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, Vc=Vc)
    e = np.abs(Tt_C-Tt_C_target)
    if e<e_t:
        break
    elif Tt_C>Tt_C_target: 
        Vc_max=Vc
    elif Tt_C<Tt_C_target:
        Vc_min=Vc
    else : 
        print("ERROR")
        
print("Nombre d'itérations : "+str(i))
print("e =    "+str(e)+" (erreur, Tt_C [°C])")
print("Tt_C = "+str(Tt_C)+"     (Température totale [°C])")
print("Vc = "+str(Vc)+"      (Vitesse calibrée [kt])")



