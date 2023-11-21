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

def longpiste(V1VR, W, Hp, T_C, delISA):
    fact=V1VR
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
    g=32.174
    S=520
    V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO=decollage_aterrissage(Hp, W, T_C, delISA)
    V1mcg_KTAS=parametres_de_vol(Hp, T_C, delISA, W,Vc=V1mcg)[3]
    V1=V1VR*VR
    if V1<V1mcg_KTAS*kts_to_fts:
        print("Erreur V1 inférieur à V1mcg")
    
    
    #AEO
    
    #Vo à Vr
    V0=0
    Vrms_VoVR=(np.sqrt(2)/2)*np.sqrt(V0**2+VR**2)
    Mrms_VoVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoVR)[2]
    qrms_VoVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoVR)[10]
    T_VoVR = 2*((8775 - 0.1915*Hp) - (8505-0.195*Hp)*Mrms_VoVR)
    a_VoVR=g*((T_VoVR-CDG_20_NS_AEO*qrms_VoVR*S-Muroll*(W-CLG_20_NS*qrms_VoVR*S))/W)
    delt_VoVR=(VR-V0)/a_VoVR
    deldisVoVR=delt_VoVR*(V0+(VR-V0)/2)
    #Vr à Vo
    Vrms_VRVo=Vrms_VoVR
    Mrms_VRVo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRVo)[2]
    qrms_VRVo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRVo)[10]
    T_VRVo = IDRVFN = 2*(-160 -3700*Mrms_VRVo)
    a_VRVo=g*((T_VRVo-CDG_20_S_AEO*qrms_VRVo*S-Mubrk*(W-CLG_20_S*qrms_VRVo*S))/W)
    delt_VRVo=(V0-VR)/a_VRVo
    deldisVRVo=delt_VRVo*(VR+(V0-VR)/2)
    #Vr à Vlof
    
    #Vlof à V35
    
    #OEI
    #Vr à Vlof
    
    #Vlof à V2
    
    if V1VR!=1:
        #AEO
        
        #Vo à V1VR*VR
        V1VRVR=V1VR*VR
        Vrms_VoV1VRVR=(np.sqrt(2)/2)*np.sqrt(V0**2+V1VRVR**2)
        Mrms_VoV1VRVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoV1VRVR)[2]
        qrms_VoV1VRVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoV1VRVR)[10]
        T_VoV1VRVR = 2*((8775 - 0.1915*Hp) - (8505-0.195*Hp)*Mrms_VoV1VRVR)
        a_VoV1VRVR=g*((T_VoV1VRVR-CDG_20_NS_AEO*qrms_VoV1VRVR*S-Muroll*(W-CLG_20_NS*qrms_VoV1VRVR*S))/W)
        delt_VoV1VRVR=(V1VR*VR-V0)/a_VoV1VRVR
        deldisVoV1VRVR=delt_VoV1VRVR*(V0+(V1VR*VR-V0)/2)
        #V1VRVR à Vo
        Vrms_V1VRVRVo=Vrms_VoV1VRVR
        Mrms_V1VRVRVo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_V1VRVRVo)[2]
        qrms_V1VRVRVo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_V1VRVRVo)[10]
        T_V1VRVRVo = IDRVFN = 2*(-160 -3700*Mrms_V1VRVRVo)
        a_V1VRVRVo=g*((T_V1VRVRVo-CDG_20_S_AEO*qrms_V1VRVRVo*S-Mubrk*(W-CLG_20_S*qrms_V1VRVRVo*S))/W)
        delt_V1VRVRVo=(V0-V1VR*VR)/a_V1VRVRVo
        deldisV1VRVRVo=delt_VoV1VRVR*(V1VR*VR+(V0-V1VR*VR)/2)
        
        
        #OEI
        #V1VR*VR à VR
        Vrms_VRV1VRVR=(np.sqrt(2)/2)*np.sqrt(V1VRVR**2+VR**2)
        Mrms_VRV1VRVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRV1VRVR)[2]
        qrms_VRV1VRVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRV1VRVR)[10]
        T_VRV1VRVR = 2*((8775 - 0.1915*Hp) - (8505-0.195*Hp)*Mrms_VRV1VRVR)
        a_VRV1VRVR=g*((T_VRV1VRVR-CDG_20_NS_OEI*qrms_VRV1VRVR*S-Muroll*(W-CLG_20_NS*qrms_VRV1VRVR*S))/W)
        delt_VRV1VRVR=(VR-V1VR*VR)/a_VRV1VRVR
        deldisVRV1VRVR=delt_VRV1VRVR*(V1VR*VR+(VR-V1VR*VR)/2)
    else:
        a=2
        
        
    FTOD=deldisVoVR+disvlovrAEO+dtvlov35AEO
    
    
    
    return
