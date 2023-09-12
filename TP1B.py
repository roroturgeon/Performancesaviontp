# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:17:35 2023

@author: Vincent
"""

import numpy as np
import math
from TP1A import atmosphere

def parametres_de_vol(Hp,T_C,delISA,W,**kwargs):
    Sref=520        # [pi^2]
    MACref=8.286    # [pi]
    gamma=1.4       # Rapport des chaleurs specifiques de l'air [-]
    R = 96          # Constante des gaz [ft/K]
    fts_to_kts =0.5924838   # 1 pi/s = 0.5924838 kts
    
    # CONSTANTES IMPORTEES, À trier et commenter !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    CtoK=273.15
    labda=0.0019812 #(Celsius/pi**2)
    rho_0=0.002377 #(slug/pi**3)
    T_tropo_C=-56.5
    T_tropo_K=-56.5+CtoK
    p_0=2116.22 #(lb/pi^2)
    T_0_C=15    
    T_0_K=CtoK+T_0_C
    a0_kts = 661.48 # Vitesse son niveau mer ISA [kts]
    K=1             # Facteur de récupération de sonde
    # FIN ##########################
    
    if kwargs.get('S'):
        S=kwargs.get('S')
    else:
        S=Sref
        
    if kwargs.get('l'):
        l=kwargs.get('l')
    else:
        l=MACref     
    
    # Recuperation des donnees atmospheriques
    theta,delta,sigma,T_C,T_K,delISA,p,rho=atmosphere(Hp, T_C, delISA)
    
    # Calcul de la vitesse du son
    a_fts = np.sqrt(gamma*R*T_K)
    a_kts = fts_to_kts*a_fts
    

    # Calcul et conversion des vitesses et pression d'impact selon le cas
    
    if kwargs.get('Vc'):
        Vc_kts=kwargs.get('Vc')
        qc = p_0*((1+((gamma-1)/2)*(Vc_kts/a0_kts)**2)**(gamma/(gamma-1)) - 1)#[lb/pi^2]
        M = np.sqrt( (2/(gamma-1)) * ((1+qc/(p))**((gamma-1)/gamma)-1))
        
        V_kts = M*a_kts
        V_fts = M*a_fts
        
        V_e_kts = V_kts*np.sqrt(sigma)
        V_e_fts = V_fts*np.sqrt(sigma)
    
    else :        
        if kwargs.get('M'):
            M = kwargs.get('M')
            
            V_kts = M*a_kts
            V_fts = M*a_fts
            
            V_e_kts = V_kts*np.sqrt(sigma)
            V_e_fts = V_fts*np.sqrt(sigma)
            
            
        elif kwargs.get('V'):
            V_kts = kwargs.get('V')
            V_fts = V_kts/fts_to_kts
            
            M = V_kts/a_kts
            
            V_e_kts = V_kts*np.sqrt(sigma)
            V_e_fts = V_fts*np.sqrt(sigma)
            
        
        elif kwargs.get('Ve'):
            Ve_kts = kwargs.get('Ve')
            Ve_fts = Ve_kts/fts_to_kts
            
            V_kts = V_e_kts/np.sqrt(sigma)
            V_fts = V_e_fts/np.sqrt(sigma)
            
            M = V_kts/a_kts
        
            
        qc = p*((1+((gamma-1)/2)*M**2)**(gamma/(gamma-1))-1)
        V_c_kts = a0_kts*np.sqrt(5*((qc/p_0+1)**0.2857-1))
        V_c_fts = V_c_kts/fts_to_kts
        
    # Calcul pression dynamique
    q = .5*rho*V_fts**2     # [lb/pi^2]
    
    # Calcul pression totale
    pt = qc+p               # [lb/pi^2]
    
    # Calcul température totale
    Tt_K = T_K*(1+0.2*K*M**2)
    Tt_C = Tt_K-CtoK
    
    # Calcul viscosité dynamique
    mu = (0.3125*1e-7*T_K**1.5)/(T_K+120) # [lb-sec/pi^2]
    
    # Calcul nb Reynolds
    RN = rho*V_fts*l/mu #[-]
    
    # Coefficient de portance
    CL = W/(q*S)        # [-]
    
    
    
        
    
