# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:53:49 2023

@author: Vincent M & Rosalie T
"""

import numpy as np
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces
from TP2B import montee

def decollage_aterrissage(Hp,W,T_C,delISA):
    dVolets=20
    Vvent=0
    pentepiste=0
    pVol='MTO'
    pRoues="up"
    Vmca=95 #noeuds KCAS=KEAS
    V1mcg = 95.0 #noeuds KCAS=KEAS
    CLMAX_F20_GU = 1.85
    S=520
    CG=0.09
    nz=1
    kts_to_fts=1.6878
    gradmin=0.024
    
    V1mcg_KTAS=parametres_de_vol(Hp, T_C, delISA, W,Vc=V1mcg)[3]
    Vmca_KTAS=parametres_de_vol(Hp, T_C, delISA, W,Vc=Vmca)[3]
    
    #Conditions atmosphériques au sol
    theta,delta,sigma,T_C,T_K,delISA,p,rho=atmosphere(Hp, T_C, delISA)
    
    #Trouvons V2min
    VsrKEAS=np.sqrt((295.37*W)/(CLMAX_F20_GU*520))
    # V2_KEAS=max(1.13*VsrKEAS,1.1*Vmca)
    V2_KEAS=1.13*VsrKEAS
    V2_KTAS=V2_KEAS/np.sqrt(sigma)
    rMoteur='OEI'
    CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA_9, nzSw, phiSw, nzBuffet, phi, M, K=forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Ve=V2_KEAS, nz=nz)
    CDOEI=CD
    rMoteur='AEO'
    CDAEO=forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Ve=V2_KEAS, nz=nz)[2]
    
    
    
    #Calcul des gradients
    grad35AEO=(2*T/W)-(CDAEO/CL)-pentepiste
    grad35OEI=(T/W)-(CDOEI/CL)-pentepiste
    
    if grad35OEI<gradmin:
        print("Erreur le gradient minimum selon le FAR25.121(b) n'est pas respecté")
    

    twdv_arr   = np.array([0.000, 0.010,  0.020,  0.100,  0.120,  0.200,  0.400,  0.60])
    dvrvl_arr  =  np.array([1.80,   2.30,   2.75,   6.50,   7.35,  10.80,  19.80,  30.0])
    dvlo35_arr =  np.array([0.00,   0.00,   1.00,   9.00,  11.00,  16.70,  31.00,  45.0])
    dvlo15_arr =  np.array([0.00,   0.00,   1.00,   8.05,   9.80,  13.00,  21.00,  29.0])
    
    V2_TAS=V2_KTAS*kts_to_fts
    VR=0
    incr=0.001 #pi/s
    V2_TAS-=incr
    
    while VR<V1mcg_KTAS*kts_to_fts or VR<1.05*Vmca_KTAS*kts_to_fts or V2_TAS<1.1*Vmca_KTAS*kts_to_fts:
    
        V2_TAS+=incr
        dvlo35OEI=np.interp(grad35OEI,twdv_arr,dvlo35_arr)
        dvlo35AEO=np.interp(grad35AEO,twdv_arr,dvlo35_arr)
        
        VLOFOEI = V2_TAS-dvlo35OEI
        
        dvrvlOEI = np.interp(grad35OEI,twdv_arr,dvrvl_arr)
        dvrvlAEO = np.interp(grad35AEO,twdv_arr,dvrvl_arr)
        
        VR = VLOFOEI-dvrvlOEI
        

        
        
    VLOFAEO=VR+dvrvlAEO
    
    V35AEO=VLOFAEO+dvlo35AEO
    
    twdt_arr   =  np.array([0.0    ,0.02  ,0.03  ,0.05  ,.065  ,.075  ,0.10  ,0.18   ,0.2   ,0.4   ,0.6])  
    dtvrvl_arr = np.array([2.35,   2.25,  2.19,  2.09,  2.01,  1.96  ,1.83,  1.41  ,1.30,  1.30  ,1.30])
    dtvlo35_arr= np.array([17.00 , 10.00 , 6.60 , 5.50 , 5.10 , 4.90 , 4.50 , 3.80 , 3.80 , 3.80 , 3.80])
    dtvlo15_arr= np.array([12.00  , 7.20  ,4.70  ,4.10  ,3.92  ,3.80,  3.50  ,2.55,  2.55  ,2.55,  2.55])
    
    dtvlovrOEI=np.interp(grad35OEI,twdt_arr,dtvrvl_arr)
    dtvlovrAEO=np.interp(grad35AEO,twdt_arr,dtvrvl_arr)
    
    dtvlov35OEI=np.interp(grad35OEI,twdt_arr,dtvlo35_arr)
    dtvlov35AEO=np.interp(grad35AEO,twdt_arr,dtvlo35_arr)
    
    disvlovrOEI=((VR+VLOFOEI)/2)*dtvlovrOEI
    disvlov35OEI=((V2_TAS+VLOFOEI)/2)*dtvlov35OEI
    disvlovrAEO=((VR+VLOFAEO)/2)*dtvlovrAEO
    disvlov35AEO=((V35AEO+VLOFAEO)/2)*dtvlov35AEO
        
        
    V1_min=V1mcg_KTAS*kts_to_fts
    V1_max=VR
    
    
    
    
    
    
    
    
    
    
    
    
    
    return V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO


