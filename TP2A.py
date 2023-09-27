# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 16:47:37 2023

@author: Vincent M & Rosalie T
"""
import numpy as np
import math 
from TP1A import atmosphere
from TP1B import parametres_de_vol

def forces(Hp,T_C,delISA,W,CG, dVolets, pRoues, rMoteur, **kwargs):
    
    
    # Liste des paramètres utilisés du fichier avion de référence
    Sref=520                # [pi^2] Surface ailaire par défaut
    

    
    # Definition globale CLmax selon config
    if dVolets==0 and pRoues=="up":
        CLmax=1.65
    elif dVolets==0 and pRoues=="down":
        CLmax=1.60
    elif dVolets==20 and pRoues=="up":
        CLmax=1.85
    elif dVolets==20 and pRoues=="down":
        CLmax=1.80
    elif dVolets==45 and pRoues=="down":
        CLmax=2.10
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
    
    # 
    if kwargs.get('VVsr'):
        VVsr=kwargs.get("VVsr")
        CL=CLmax/(VVsr**2)    
        q=W*nz/(CL*S)
        theta,delta,sigma,T_C,T_K,delISA,p,rho = atmosphere(Hp, T_C, delISA)
        V = np.sqrt(q/0.5/rho)
        a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, V=V, **kwargs)
        
    else:
        print("CACA")
    
    
    # kwargs a ajouter : Autre option de vitesse, Nz ou Angle roulis.
    #                    Inclut egalement S et L
    
    
    
    
    return S
