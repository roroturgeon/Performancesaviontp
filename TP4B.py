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
    deltASD=2 #secondes
    RAD=0
    dVolets=20
    pRoues="up"
    nz=1
    CG=0.09
    nb_brk=4
    V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO=decollage_aterrissage(Hp, W, T_C, delISA)
    V1mcg_fts=V1mcg*kts_to_fts
    V1=V1VR*VR
    if V1<V1mcg_fts:
        print("Attention V1 est inférieur à V1mcg")
        V1=V1mcg_fts
        VR=V1/V1VR
    
    
    #AEO
    rMoteur = "AEO"
    pVol = "MTO"
    
    #Vo à Vr
    V0=0
    Vrms_VoVR=(np.sqrt(2)/2)*np.sqrt(V0**2+VR**2)
    Vrms_VoVR_kts=Vrms_VoVR/kts_to_fts
    Mrms_VoVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoVR_kts)[2]
    qrms_VoVR=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoVR_kts)[10]
    T_VoVR=forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, nz=nz,V=Vrms_VoVR_kts)[15]
    a_VoVR=(g/W)*((T_VoVR-CDG_20_NS_AEO*qrms_VoVR*S-Muroll*(W-CLG_20_NS*qrms_VoVR*S)))
    delt_VoVR=(VR-V0)/a_VoVR
    deldisVoVR=delt_VoVR*(V0+(VR-V0)/2)

    pVol = "IDLE"
    #Vr à Vo
    Vrms_VRVo=Vrms_VoVR
    Vrms_VRVo_kts=Vrms_VoVR_kts
    Mrms_VRVo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRVo_kts)[2]
    qrms_VRVo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRVo_kts)[10]
    T_VRVo=forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, nz=nz,V=Vrms_VRVo_kts)[15]
    a_VRVo=(g/W)*((T_VRVo-CDG_20_S_AEO*qrms_VRVo*S-Mubrk*(W-CLG_20_S*qrms_VRVo*S)))
    delt_VRVo=(V0-VR)/a_VRVo
    deldisVRVo=delt_VRVo*(VR+(V0-VR)/2)
    ASDmargin1=deltASD*V1
    #Vr à Vlof
    
    #Vlof à V35
    
    #OEI
    #Vr à Vlof
    
    #Vlof à V2
    
    if V1VR!=1:
        #AEO
        rMoteur = "AEO"
        pVol = "MTO"
        #Vo à V1

        Vrms_VoV1=(np.sqrt(2)/2)*np.sqrt(V0**2+V1**2)
        Vrms_VoV1_kts=Vrms_VoV1/kts_to_fts
        Mrms_VoV1=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoV1_kts)[2]
        qrms_VoV1=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VoV1_kts)[10]
        T_VoV1=forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, nz=nz,V=Vrms_VoV1_kts)[15]
        a_VoV1=(g/W)*((T_VoV1-CDG_20_NS_AEO*qrms_VoV1*S-Muroll*(W-CLG_20_NS*qrms_VoV1*S)))
        delt_VoV1=(V1-V0)/a_VoV1
        deldisVoV1=delt_VoV1*(V0+(V1-V0)/2)
        
        pVol = "IDLE"
        #V1 à Vo
        Vrms_V1Vo=Vrms_VoV1
        Vrms_V1Vo_kts=Vrms_VoV1_kts
        Mrms_V1Vo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_V1Vo_kts)[2]
        qrms_V1Vo=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_V1Vo_kts)[10]
        T_V1Vo=forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, nz=nz,V=Vrms_V1Vo_kts)[15]
        a_V1Vo=(g/W)*((T_V1Vo-CDG_20_S_AEO*qrms_V1Vo*S-Mubrk*(W-CLG_20_S*qrms_V1Vo*S)))
        delt_V1Vo=(V0-V1)/a_V1Vo
        deldisV1Vo=delt_V1Vo*(V1+(V0-V1)/2)
        ASDmargin2=deltASD*V1
        
        
        #OEI
        rMoteur = "OEI"
        pVol = "MTO"
        #V1 à VR
        Vrms_VRV1=(np.sqrt(2)/2)*np.sqrt(V1**2+VR**2)
        Vrms_VRV1_kts=Vrms_VRV1/kts_to_fts
        Mrms_VRV1=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRV1_kts)[2]
        qrms_VRV1=parametres_de_vol(Hp, T_C, delISA, W, V=Vrms_VRV1_kts)[10]
        T_VRV1=forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, nz=nz,V=Vrms_VRV1_kts)[15]
        a_VRV1=(g/W)*((T_VRV1-CDG_20_NS_OEI*qrms_VRV1*S-Muroll*(W-CLG_20_NS*qrms_VRV1*S)))
        delt_VRV1=(VR-V1)/a_VRV1
        deldisVRV1=delt_VRV1*(V1+(VR-V1)/2)
        

        TODOEI_1=deldisVoV1+deldisVRV1+disvlovrOEI+disvlov35OEI
        TODOEI_2=deldisVoVR+disvlovrOEI+disvlov35OEI
        TODOEI=max(TODOEI_1,TODOEI_2)
        
        ASD1=deldisVoV1+ASDmargin2+deldisV1Vo
        print(ASD1)
        ASD2=deldisVoVR+ASDmargin1+deldisVRVo
        print(ASD2)
        ASD=max(ASD1,ASD2)
        
    else:
        TODOEI=deldisVoVR+disvlovrOEI+disvlov35OEI
        ASD=deldisVoVR+ASDmargin1+deldisVRVo
        
        
    FTOD=1.15*(deldisVoVR+disvlovrAEO+dtvlov35AEO)
    LMIN=max(FTOD,ASD,TODOEI)
    
    # Évaluer la portance à VRMS pour FB a VRMS
    if ASD1>=ASD2 : 
        q_brk = qrms_VoV1
    else: 
        q_brk = qrms_VRVo
    q_brk = 22.11596
    print(q_brk)
    L_brk=CLG_20_S*S*q_brk
    FB = Mubrk*(W-L_brk)
    ds=max(deldisV1Vo,deldisVRVo)
    ds = 1597.46751479
    print(ds)
    
    #enlever div et 1 million
    DBRKE = FB*ds/1e6
    
    
    return FTOD,TODOEI,ASD,LMIN, DBRKE
