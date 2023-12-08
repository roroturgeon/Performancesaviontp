# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:17:35 2023

@author: Vincent M & Rosalie T
"""
import numpy as np
from TP1A import atmosphere

def parametres_de_vol(Hp,T_C,delISA,W,**kwargs):
    """
    Parameters
    ----------
    Hp : TYPE
        DESCRIPTION.
    T_C : TYPE
        DESCRIPTION.
    delISA : TYPE
        DESCRIPTION.
    W : TYPE
        DESCRIPTION.
    **kwargs : TYPE
        DESCRIPTION.

    Returns
    -------
    a_kts : TYPE
        DESCRIPTION.
    a_fts : TYPE
        DESCRIPTION.
    M : TYPE
        DESCRIPTION.
    V_kts : TYPE
        DESCRIPTION.
    V_fts : TYPE
        DESCRIPTION.
    Ve_kts : TYPE
        DESCRIPTION.
    Ve_fts : TYPE
        DESCRIPTION.
    Vc_kts : TYPE
        DESCRIPTION.
    Vc_fts : TYPE
        DESCRIPTION.
    pt : TYPE
        DESCRIPTION.
    q : TYPE
        DESCRIPTION.
    qc : TYPE
        DESCRIPTION.
    Tt_C : TYPE
        DESCRIPTION.
    Tt_K : TYPE
        DESCRIPTION.
    mu : TYPE
        DESCRIPTION.
    RN : TYPE
        DESCRIPTION.
    CL : TYPE
        DESCRIPTION.

    """
    
    Sref=520                # [pi^2] Surface ailaire par défaut
    MACref=8.286            # [pi] Corde par défaut
    gamma=1.4               # Rapport des chaleurs specifiques de l'air [-]
    R = 287.052874          # Constante des gaz [J/Kg-K]
    fts_to_kts =0.5924838   # 1 pi/s = 0.5924838 kts
    m_to_ft = 3.28084       # Conversion mètre à pieds
    CtoK=273.15             # Conversion Celsius à Kelvin
    p_0=2116.22             #(lb/pi^2) Pression au niveau de la mer
    a0_kts = 661.48         # Vitesse son niveau mer ISA [kts]
    K=1                     # Facteur de récupération de sonde
    nz=1                    # poids = nz*masse (en virage)
    
    # Chois des dimensions de référence pour S et l
    
    if kwargs.get('S'):
        S=kwargs.get('S')
    else:
        S=Sref
 #   print("S="+str(S))
    if kwargs.get('l'):
        l=kwargs.get('l')
    else:
        l=MACref     
    
    # Recuperation des donnees atmospheriques
    theta,delta,sigma,T_C,T_K,delISA,p,rho=atmosphere(Hp, T_C, delISA)
    
    # Calcul de la vitesse du son

    a_ms = np.sqrt(gamma*R*T_K)
    a_fts = a_ms*m_to_ft
    a_kts = fts_to_kts*a_fts
    

    # Calcul et conversion des vitesses et pression d'impact selon le cas
    
    if kwargs.get('Vc'):
        Vc_kts=kwargs.get('Vc')
        Vc_fts = Vc_kts/fts_to_kts
        qc = p_0*((1+((gamma-1)/2)*(Vc_kts/a0_kts)**2)**(gamma/(gamma-1)) - 1)#[lb/pi^2]
        M = np.sqrt( (2/(gamma-1)) * ((1+qc/(p))**((gamma-1)/gamma)-1))
        
        V_kts = M*a_kts
        V_fts = M*a_fts
        
        Ve_kts = V_kts*np.sqrt(sigma)
        Ve_fts = V_fts*np.sqrt(sigma)
    
    else :        
        if kwargs.get('M'):
            M = kwargs.get('M')
            
            V_kts = M*a_kts
            V_fts = M*a_fts
            
            Ve_kts = V_kts*np.sqrt(sigma)
            Ve_fts = V_fts*np.sqrt(sigma)
            
            
        elif kwargs.get('V'):
            V_kts = kwargs.get('V')
            V_fts = V_kts/fts_to_kts
            
            M = V_kts/a_kts
            
            Ve_kts = V_kts*np.sqrt(sigma)
            Ve_fts = V_fts*np.sqrt(sigma)
            
        
        elif kwargs.get('Ve'):
            Ve_kts = kwargs.get('Ve')
            Ve_fts = Ve_kts/fts_to_kts
            
            V_kts = Ve_kts/np.sqrt(sigma)
            V_fts = Ve_fts/np.sqrt(sigma)
            
            M = V_kts/a_kts
        
    # Calcul de pression d'impact et de la vitesse calibrée lorsque 
    #la vitesse calibrée n'est pas donnée en entrée.        
        qc = p*((1+((gamma-1)/2)*M**2)**(gamma/(gamma-1))-1)
        Vc_kts = a0_kts*np.sqrt(5*((qc/p_0+1)**0.2857-1))
        Vc_fts = Vc_kts/fts_to_kts
        
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
    CL = W*nz/(q*S)        # [-]
    
    
    return a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL