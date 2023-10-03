# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:20:42 2023

@author: Rosalie
"""

import numpy as np
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces

def montee(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, Vconst, **kwargs):
    
    labda=0.0019812 #(Celsius/pi**2)
    T_0_C=15    #Temperature au niveau de la mer
    CtoK=273.15 
    g=32.18503937007874     #Accélération gravitationnelle (pi/s**2)
    
    
    CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA, nzSw, phiSw, nzBuffet,phi, M= forces(Hp,T_C, delISA, W, CG, dVolets,pRoues, rMoteur, pVol, **kwargs)
    
    if kwargs.get('M'):
        a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL=parametres_de_vol(Hp, T_C, delISA, W,**kwargs)
    else:
       a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL=parametres_de_vol(Hp, T_C, delISA, W,M=M,**kwargs)
    
    
    phi_rad=np.deg2rad(phi)
    T_STD_C=T_0_C-labda*Hp
    T_STD_K=T_STD_C+CtoK
    
    ####Facteur d'accélération
    if delISA==True:
        Treel_K=T_STD_C+T_C+CtoK
    else:
        Treel_K=T_C +CtoK
    
    phi_AF = (1/(0.7*M**2))*((1+.2*M**2)**3.5-1)/((1+.2*M**2)**2.5)
    if Vconst== "CAS":     
            if Hp<=36089:
                AF=0.7*M**2*(phi_AF-0.190263*(T_STD_K/Treel_K))
            else:
                AF=0.7*M**2*phi_AF
            
    elif Vconst== "MACH":
            if Hp<=36089:
                AF=-0.133184*M**2*(T_STD_K/Treel_K)
            else:
                AF=0
        
                
    ### Taux de montée géométrique et de pression
    RoCg_s=(V_fts*(T-D)/W)/(1+AF)  
    RoCg_min=RoCg_s*60
    RoCp_min=RoCg_min*(T_STD_K/Treel_K)        
        
    ### Gradient
    grad=RoCg_s/V_fts
    
    ###Accélération selon l'axe de la trajectoire de vol
    a=((RoCg_s-((V_fts*(T-D))/W))/(-V_fts/g))/g
    
    
    
    
    
    
    return grad, RoCg_min, RoCp_min, AF,a

