"""@author: Vincent M & Rosalie T"""
import numpy as np
import math 

###delISA true ou false, si true T est un delta ISA si false T est la température. 
###La valeur d'altitude donnée doit être en pieds.
CtoK=273.15
labda=0.0019812 #(Celsius/pi**2)
rho_0=0.002377 #(slug/pi**3)
T_tropo_C=-56.5
T_tropo_K=-56.5+CtoK
p_0=2116.22 #(lb/pi^2)
T_0_C=15    
T_0_K=CtoK+T_0_C

def atmosphere(Hp,T_C,delISA):
    
    if delISA==True:

        if Hp<=36089:
            delISA=T_C
            delta=(1-6.87535*10**(-6)*Hp)**(5.2559)
            p=delta*p_0
            T_ISA=T_0_C-labda*Hp
            T_C=T_ISA+delISA
            T_K=T_C+CtoK
            theta=T_K/T_0_K
            sigma=delta/theta
            rho=sigma*rho_0
            
        elif Hp>38089 and Hp<=65617:
            delISA=T_C
            T_C=T_tropo_C+delISA 
            T_K=T_tropo_K+delISA 
            theta=T_K/T_0_K
            delta=0.22336*math.e**(-((Hp-36089)/20806))
            p=delta*p_0
            sigma=delta/theta
            rho=sigma*rho_0
            
            
    else:
        T_K=T_C+CtoK
        if Hp<=36089:
            T_ISA=T_0_C-labda*Hp
            delISA=T_C-T_ISA
            theta=T_K/T_0_K
            delta=(1-6.87535*10**(-6)*Hp)**(5.2559)
            p=delta*p_0
            sigma=delta/theta
            rho=sigma*rho_0
            
        elif Hp>38089 and Hp<=65617:
            T_ISA=T_0_C-labda*Hp
            delISA=T_C-T_ISA
            theta=T_K/T_0_K
            delta=0.22336*math.e**(-((Hp-36089)/20806))
            p=delta*p_0
            sigma=delta/theta
            rho=sigma*rho_0
            
            
    
    return theta,delta,sigma,T_C,T_K,delISA,p,rho

# TEST APPEL FONCTION




