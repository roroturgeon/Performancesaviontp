# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:11:12 2023

@author: Vincent M & Rosalie T
"""
import numpy as np
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces
from TP2B import montee
from TP4A import decollage_aterrissage

def longpiste(V1Vr, W, Hp, T_C, delISA):
    fact=V1Vr
    CLG_20_NS=0.8290
    CLG_20_S=0.2090
    CDG_20_NS_AEO=0.0750
    delCD_OEI=0.0030+0.0020
    CDG_20_NS_OEI=CDG_20_NS_AEO+delCD_OEI
    CDG_20_S_AEO=0.1171
    Muroll=0.020
    Mubrk=0.4 #Piste sèche
    V1mcg=95.0 #noeuds
    kts_to_fts=1.6878
    V1mcg_KTAS=parametres_de_vol(Hp, T_C, delISA, W,Vc=V1mcg)[3]
    Vr=decollage_aterrissage(Hp, W, T_C, delISA)[2]
    V1=V1Vr*Vr
    if V1<V1mcg_KTAS*kts_to_fts:
        print("Erreur V1 inférieur à V1mcg")
    V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO=decollage_aterrissage(Hp, W, T_C, delISA)
    
    #AEO
    
    #Vo à Vr
    V0=0
    Vrms_VoVr=(np.sqrt(2)/2)*np.sqrt(V0**2+Vr**2)
    #Vr à Vo
    Vrms_VrVo=Vrms_VoVr
    #Vr à Vlof
    
    #Vlof à V35
    
    #OEI
    
    if V1Vr!=1:
        b=2
        
        
    
    
    
    
    return
