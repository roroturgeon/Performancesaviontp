# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:00:27 2023

@author: Rosalie
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from TP1B import parametres_de_vol


###Question 4:
    
Vc=270 #noeuds
Hp=3000 #pi
delISA=True
W=40000 #lbs

###Calcul des deux vitesses
a=-55
b=55
V_kts=0
while abs(V_kts-Vc)>=0.0001:
    m=(a+b)/2
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, m, delISA,W, Vc=Vc)    
    if V_kts<Vc:
        a=m
    else:
        b=m

print('Question 4:')
print("TAS = %.4g noeuds" % (V_kts))
print("CAS = %.7g noeuds" % (Vc_kts))
print("delISA = %.6g C" % (m))


###Question 5:
Vc=275
T_C=0 #C ou K dépendemment de delISA
    
###Tendance de la variation de Mach en fonction de l'altitude de pression
Mref=0.76
alt=np.linspace(31000, 34000,200)
Ma=np.zeros(len(alt))
for i in range(len(alt)):
        a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(alt[i], T_C, delISA,W, Vc=Vc)
        Ma[i]=M
        
plt.plot(alt,Ma,'-',label='Mach vs Altitude de pression')
plt.xlabel("Altitude de pression (pi)", fontsize=11)
plt.ylabel("Mach", fontsize=11)
plt.legend(loc='best')
plt.grid(True)
plt.savefig('Machvsalt.png', dpi = 300, bbox_inches='tight')
plt.show()


###Calcul de l'altitude de pression pour un M=0.76 avec la méthode de la bissection

a=0
b=40000
M=0
while abs(M-Mref)>=0.0001:
    m=(a+b)/2
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(m, T_C, delISA,W, Vc=Vc)    
    if M<Mref:
        a=m
    else:
        b=m
print('Question 5:')
print("Altitude de pression = %.9g pieds" % (m))  

Hp=31992.1875  #pi


###Vérification que la température n'a pas d'influence grâce à un graphique

T_Ce=np.linspace(0,200,100)
Me=np.zeros(len(T_Ce))
for j in range(len(T_Ce)):
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(m, T_Ce[j], delISA,W, Vc=Vc)    
    Me[j]=M
    
plt.plot(T_Ce,Me,'-',label='Mach vs delta ISA')
plt.xlabel("delta ISA (K)", fontsize=11)
plt.ylabel("Mach", fontsize=11)
plt.legend(loc='best')
plt.grid(True)
plt.savefig('Machvsdelisa.png', dpi = 300, bbox_inches='tight')
plt.show() 
    
###Question 6:

Vc=275 #noeuds
Hp=15000  #pi
T_C=0 #C car delISA est False, donc une température est donnée. Le delISA est un bouléen qui permet au code
###de savoir de quel type d'entrée il s'agit
delISA=False
W=40000 #lbs 


###Vérification de l'allure de la variation de température totale

Vce=np.linspace(100,275,200)
Tt_Ce=np.zeros(len(Vce))
for k in range(len(Vce)):
        a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA,W, Vc=Vce[k])
        Tt_Ce[k]=Tt_C
        
plt.plot(Vce,Tt_Ce,'-',label='Température totale (C) vs CAS')
plt.xlabel("CAS", fontsize=11)
plt.ylabel("Température totale (C)", fontsize=11)
plt.legend(loc='best')
plt.grid(True)
plt.savefig('TtvsVc.png', dpi = 300, bbox_inches='tight')
plt.show()


###Calcul de la vitesse calibrée

Tref=10
a=100
b=275  
Tt_C=0
while abs(Tt_C-Tref)>=0.0001:
    m=(a+b)/2       
    a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA,W, Vc=m)     
    if Tt_C<Tref:
        a=m
    else:
        b=m 
    
print('Question 6:')    
print("CAS = %.7g noeuds" % (m))









