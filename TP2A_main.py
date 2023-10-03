# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:08:57 2023

@author: Vincent
"""

import numpy as np
from TP2A import forces

Hp_arr=np.array([30000,	5000,	5000,	10000,	10000,	30000,	30000,	5000])
T_C_arr = np.array([15,	 0,	 0,	20,	20,	15,	15,	 0])
delISA_arr= np.array([True, True, True, True, True, True, True, True])
W_arr = np.array([40000,	35000,	35000,	40000,	40000,	40000,	40000, 35000])
CG_arr=np.array([.25,.15,.15,.15,.15,.25,.25,.15])
dVolets_arr = np.array([0,20,20,45,45,0,0,20])
pRoues_arr = np.array(["up","up","up", "down", "down", "up", "up", "up"])
rMoteur_arr=np.array(["AEO", "AEO", "OEI", "AEO", "AEO","AEO", "AEO", "AEO"])
pVol_arr=["MCR", "MTO", "MTO", "GA", "IDLE", "MCT", 4500, "MCL"]
vitesse_arr=np.array([{"M":.74},{"VVsr":1.23},{'VVsr':1.13},{'Vc':140},{'Vc':140},{'M':.74},{'M':.74},{'VVsr':1.23}])
phi_nz_arr=np.array([{"nz":1},{"nz":1},{"nz":1},{'phi':40},{"nz":1},{"nz":1},{"nz":1},{"nz":1}])



for i in range(len(Hp_arr)):
    print("\n\n================================")
    print("=---- CAS "+str(i+1)+" -----=")
    print("================================")  
    print("    Données : ")
    print("Hp = ",Hp_arr[i],", T_C = ",T_C_arr[i], ", delISA = ",delISA_arr[i],", W = ", W_arr[i],", CG = ", CG_arr[i], ", dVolets = ",dVolets_arr[i],", pRoues = ", pRoues_arr[i], ", rMoteur = ",rMoteur_arr[i],", pVol = ", pVol_arr[i], ", phi/nz = ",phi_nz_arr[i], ", vitesse = ",vitesse_arr[i])
    CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA, nzSw, phiSw, nzBuffet = forces(Hp_arr[i],T_C_arr[i], delISA_arr[i], W_arr[i], CG_arr[i], dVolets_arr[i],pRoues_arr[i], rMoteur_arr[i], pVol_arr[i], **phi_nz_arr[i], **vitesse_arr[i])
    print("    Résultats : ")
    print("CD = ", CD)
    print("CL = ",CL)
    print("L/D = ",finesse)
    print("Cdp = ",Cdp)
    print("Cdi = ",CDi)
    print("T = ",T)


# Hp=30000
# T_C=15
# delISA=True
# W=40000
# M=.74
# dVolets=0
# pRoues="up"
# rMoteur="AEO"
# pVol="MCR"
# CG=.25
# nz=1


# CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA, nzSw, phiSw, nzBuffet = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, nz=nz, M=M)
# print(DCDCNTL)
# print(DCNTL)

# print("================================")
# print("=---- CAS 4 -----")


# Hp=30000
# T_C=15
# delISA=True
# W=40000
# dVolets=0
# pRoues="up"
# rMoteur="AEO"
# pVol=4500
# CG=.25



# CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA, nzSw, phiSw, nzBuffet = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, phi=40, Vc=140)

