# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:47:37 2023

@author: Vincent M & Rosalie T
"""
import numpy as np
from TP1A import atmosphere
from TP1B import parametres_de_vol

def forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, pVol, **kwargs):
    
    
    # Liste des paramètres utilisés du fichier avion de référence
    Sref=520                # [pi^2] Surface ailaire par défaut
    fts_to_kts =0.5924838   # 1 pi/s = 0.5924838 kts
    DCDLG = 0.0200          # Augmentation de drag pour roues baissées
    MACref=8.286            # [pi] Corde par défaut
    Lt    =  40.56          # Bras de levier de la queue [pieds]

    # Corde aérodynamique moyenne
    
    if kwargs.get('l'):
        l=kwargs.get('l')
    else:
        l=MACref
        
    # Definition globale CLmax selon config
    if dVolets==0 and pRoues=="up":
        CLmax=1.65
        K = .0364
        Cdp = 0.0206 
    elif dVolets==0 and pRoues=="down":
        CLmax=1.60
        K = .0364
        Cdp = 0.0206 + DCDLG
    elif dVolets==20 and pRoues=="up":
        CLmax=1.85
        K = .0334
        Cdp = 0.0465
    elif dVolets==20 and pRoues=="down":
        CLmax=1.80
        K = .0334
        Cdp = 0.0465 + DCDLG
    elif dVolets==45 and pRoues=="down":
        CLmax=2.10
        K = .0301
        Cdp = 0.1386 + DCDLG
    else : 
        print("ERREUR CLmax(dVolets/pRoues)")
    
    # Definition globale nz
    if kwargs.get("nz"):
        nz=kwargs.get("nz")
    elif kwargs.get("phi"):
        phi=kwargs.get("phi")
        nz=1/np.cos(np.deg2rad(phi))
    else : 
        print("ERREUR specifier nz ou phi correctement")
    
    # Definition surface référence
    if kwargs.get('S'):
        S=kwargs.get('S')
    else:
        S=Sref
    
    # Calcul de la vitesse vraie et parametres de vol selon le cas
    if kwargs.get('VVsr'):
        VVsr=kwargs.get("VVsr")
        CL_2=CLmax/(VVsr**2)    
        q=W*nz/(CL_2*S)
        print(q)
        theta,delta,sigma,T_C,T_K,delISA,p,rho = atmosphere(Hp, T_C, delISA)
        V_fts = np.sqrt(q/0.5/rho)# Vitesse et fts car calculee avec q 
        V = V_fts*fts_to_kts 
        a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, V=V, **kwargs)
        print(q)
        CL=CL_2
    else:
        a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, **kwargs)
        CL=nz*CL
        print(CL)
    
    # Calcul des sorties (forces et coefficients)
    L = nz*W
    
    #Pousse en lb
    T=0
    MTOFN = ((8775 - 0.1915*Hp) - (8505-0.195*Hp)*M)
    if delISA>15:
        MTOFN=MTOFN*(1-0.01*(delISA-15))   
    MCLFN = (5690 - 0.0968*Hp) - (1813-0.0333*Hp)*M
    if delISA>10:
        MCLFN = MCLFN*(1-0.01*(delISA-10))
        
    MCRFN = MCLFN*.98
    MCTFN = MTOFN*.9
    IDLEFN = 600 - 1000*M
    
    
    
    if rMoteur == "AEO":
        nbMot = 2
        if pVol == "MTO" or pVol == "GA":
            T = nbMot*MTOFN
        elif pVol == "MCL":
            T=nbMot*MCLFN            
        elif pVol == "MCR":
            T = nbMot*MCRFN
        elif pVol == "IDLE":
            T = nbMot*IDLEFN
        elif isinstance(pVol, (int,float)):
            T = pVol
        else : 
            print("ERREUR type pVol")
            
        DCDWM = 0.0 
        DWM = DCDWM*q*S
        
        DCDCNTL = 0
        DCNTL = DCDCNTL*q*S
            
    elif rMoteur == "OEI":
        if pVol == "MTO" or "GA":
            T = MTOFN
        elif pVol == "MCT":
            T = MCTFN
        elif pVol == "IDLE":
            T = IDLEFN
        # Trainee de ventilateur
        DCDWM = 0.0030 
        DWM = DCDWM*q*S
        
        # Trainee de controle a cause de moteur mort
        kasyma = 0.1 
        CT=T/(q*S)
        DCDCNTL = kasyma*CT*CT
        DCNTL = DCDCNTL*q*S
        
        

    else : 
        print("ERREUR Regime moteur incorrect")
        
    if dVolets == 0:
        if M <= .6:
            dCDComp = 0
        elif M<= .78 : 
            dCDComp = (0.0508 - 0.1748*M + 0.1504*M**2)*CL**2
        elif M <= .85 : 
            dCDComp = (-99.3434 + 380.888*M - 486.8*M**2 + 207.408*M**3)*CL**2
    else:
        dCDComp = 0
    

    
    dCDTRN = K*CL*CL*(nz*nz-1)
    
    CD = Cdp+K*CL*CL+dCDComp + DCDCNTL + DCDWM + dCDTRN
    D = CD*q*S

    CDi = K*CL*CL
    Di = CDi*q*S
    Dp = Cdp*q*S
    DComp = dCDComp*q*S
    
    # Calcul AOA
    if dVolets==0 and pRoues=="up":
        AOA_9 = (CL-0.05)/0.1
        CLstall_9 = .05+.1*14.7
    elif dVolets==0 and pRoues=="down":
        AOA_9 = (CL-0.00)/0.1
        CLstall_9 = .1*14.7
    elif dVolets==20 and pRoues=="up":
        AOA_9 = (CL-0.25)/0.1
        CLstall_9 = .25+.1*14.6
    elif dVolets==20 and pRoues=="down":
        AOA_9 = (CL-0.20)/0.1
        CLstall_9 = .2+.1*14.6
    elif dVolets==45 and pRoues=="down":
        AOA_9 = (CL-0.5)/0.1
        CLstall_9 = .5+.1*14.4
    
    CLstall = CLstall_9/(1+l/Lt*(0.09-CG))
    # Conditions stall warning
    nzSw = CLstall*q*S/W
    phiSw = np.rad2deg(np.arccos(1/nzSw))
    
    # Calcul buffet
    if dVolets == 0:
        MACH = np.linspace(.275,.9,26)
        CL_buffet_arr = np.array([1.3424,  1.3199,  1.2974,  1.2667,  1.2310,  1.1930,  1.1551,  1.1191  ,
              1.0863,  1.0577,  1.0337,  1.0142,  0.9989,  0.9868,  0.9764,  0.9659,  
              0.9530,  0.9349,  0.9085,  0.8698,  0.8149,  0.7391,  0.6373,  0.5039,  
              0.3330,  0.118])
        CL_buffet_9_MAC = np.interp(M, MACH, CL_buffet_arr)
        CL_buffet= CL_buffet_9_MAC / (1+(l/Lt)*(.09-CG))
        nzBuffet = CL_buffet/CL
    else :
        nzBuffet=0
    
        
    
    return CL, L, CD, D, L/D, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA_9, nzSw, phiSw, nzBuffet
