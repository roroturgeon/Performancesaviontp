# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:10:19 2023
JOYEUX HALLOWEEN

AER8375 - Performances avion

Fonctions du TP3B

@author: Rosalie Turgeon & Vincent Moreau
         ( 2072092 )       ( 2075782 )
"""



import numpy as np
import matplotlib.pyplot as plt
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces
from TP2B import montee
from TP3A import montee_descente, Hp_trans


def croisiere(Hp,T_C,delISA,Vvent,W,**kworgs):
    
    incr = 100      # [pi] increment pour valider fin montee    
    Hpi = Hp-incr   # [pi]
    VKCAS = 275     # [kts] Pour verif fin montee
    MACH = .78      # [-] Pour verif fin montee
    dVolets = 0
    pRoues = 'up'
    rMoteur = 'AEO'
    pVol_montee = "MCL"
    pVol_croisiere = "MCR"
    nz = 1          # [-]
    CG = 0.09       # [-]
    Vmo = 330       # [kts] CAS Max
    Mmo = 0.85      # [-]
    Hp_max=41000    # [pi]
    Hp_min=2000     # [pi]
    kts_to_fts=1.6878 # [fts per kts]
    a0 = 661.48     # [kts]
    
    # Constantes fichier avion
    S = 520         # [pi^2]
      
    # Initialisation des retours
    Vc=0
    Vg=0
    M=0
    SAR=0
    SR=0
    Wf = 0 
    
    #Calcul du SFC
    SFC = 0.58 + (0.035 * Hp/ 10000)
    
    # Montee/descente : altitude de transition
    Hp_t = Hp_trans(T_C, delISA, W, VKCAS, MACH)
    if Hp>=Hp_t:
        Vconst = "MACH"
        ROC = montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_montee, Vconst,M=MACH,nz=nz) [2]
    else:
        Vconst = "CAS"
        ROC = montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_montee, Vconst,Vc=VKCAS,nz=nz) [2]
        
    
    
    
    #Condition de croisiere d'altitude respecte
    
    if Hp>Hp_max or Hp<Hp_min:
        print("Erreur l'altitude donnée est hors limite")
    else:
        # Verification taux montée minimum 
        if ROC<300:
            print("ERREUR taux de montee trop faible pour atteindre altitude croisiere\nFIN DE L'EXECUTION")
        else:
            
            # Valeurs CdP et K de Avion selon config connue de volets et de roues
            CdP = .0206
            K = .0364
            
            if kworgs.get("Vmd"):
                CL_Vmd = np.sqrt(CdP/K)
                Vmd_EAS = np.sqrt(295.37*W/(CL_Vmd*S))
                a = parametres_de_vol(Hp, T_C, delISA, W, Ve=Vmd_EAS)
                M_Vmd,V, Vc_Vmd = a[2], a[3], a[7]

                if M_Vmd>Mmo or Vc_Vmd>Vmo:
                    print("ERREUR vitesse trop elevee pour les operations (VMD trop)")
                    print(M_Vmd,">",Mmo)
                    print(Vc_Vmd,">",Vmo)
                Vc=Vc_Vmd
                M=M_Vmd
                b = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_croisiere, M=M, nz=nz)
                D,finesse,T = b[3], b[4], b[15]
                SAR=(V/SFC)*(finesse)*(1/W)
                    
            elif kworgs.get('M'):
                M = kworgs.get('M')
                a =  parametres_de_vol(Hp, T_C, delISA, W, M=M)
                M_M, V, Vc_M = a[2], a[3], a[7]
                if M_M>Mmo or Vc_M>Vmo:
                    print("ERREUR vitesse trop elevee pour les operations (VMD trop)")
                    print(M_M,">",Mmo)
                    print(Vc_M,">",Vmo)
                Vc=Vc_M
                b = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_croisiere, Vc=Vc, nz=nz)
                D,finesse,T = b[3], b[4],b[15]
                SAR=(V/SFC)*(finesse)*(1/W)
                    
            elif kworgs.get("LRC"):
                #Trouvons le SAR maximum
                
                # Initialisation de la méthode de maximisation
                step_size = 0.0001
                eps = 0.0001
                learn_rate = 0.001
                iter_max = 10000
                pente = 1           # Initialisation pente pour while
                M_eval_position = 0.6     
            
                while abs(pente)>eps and iter_max>0:
                    ret = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_croisiere, M=M_eval_position, nz=nz)
                    CL,CD=ret[0],ret[2]
                    optim = np.sqrt(CL)/CD
                    
                    ret_2 = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_croisiere, M=M_eval_position+eps,nz=nz)
                    CL_2,CD_2=ret_2[0],ret_2[2]
                    optim_eps = np.sqrt(CL_2)/CD_2
                    
                    pente=(optim_eps-optim)/eps
                    M_eval_position += learn_rate*pente
                    iter_max-=1
                # print("Nombre de Mach = ",M_eval_position," [-]")
                # print("Optim = ",optim," [-]")
                # print("Critère d'arrêt : ",eps)
                # print("Nombre d'itérations : ",10000-iter_max)

                theta = atmosphere(Hp, T_C, delISA)[0]
                SAR_max = (a0*np.sqrt(theta)/SFC)*(M_eval_position*CL_2/CD_2)*(1/W)
                
                SAR_LRC =  0.99*SAR_max
                # print("SAR LRC = ",SAR_LRC)
                    
                # Methode bissection pour trouver Mach @ SAR_LRC
                M_min = M_eval_position
                M_max = 0.9

                erreur = 1      # Écart de départ pour initialiser
                eps=0.0001      # Tolélance d'écart entre calcul de deux valeurs de ROC pour critère d'arrêt
                nbiter=0
                while erreur>eps:
                    nbiter+=1
                    M_test=(M_min+M_max)/2
                    
                    ret = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_croisiere, M=M_test, nz=nz)
                    CL,CD=ret[0],ret[2]
                    SAR_test = (a0*np.sqrt(theta)/SFC)*(M_test*CL/CD)*(1/W)
                    
                    erreur = abs(SAR_test-SAR_LRC)
                    if SAR_test<SAR_LRC:
                        M_max=M_test
                    else: 
                        M_min=M_test
                
                # print("SAR LRC PAR ITER : ", SAR_test)
                # print("M SAR .99 PAR ITER : ",M_test)
                # print("NB ITER = ",nbiter)
                
                M_LRC = M_test

                ret = parametres_de_vol(Hp, T_C, delISA, W, M=M_LRC)
                
                V, Vc_LRC = ret[3],ret[7]
                
                
                if M_LRC>Mmo or Vc_LRC>Vmo:
                    print("ERREUR vitesse trop elevee pour les operations (VMD trop)")
                    print(M_LRC,">",Mmo)
                    print(Vc_LRC,">",Vmo)
                Vc=Vc_LRC
                M=M_LRC
                SAR=SAR_LRC
                b=forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol_croisiere, M=M_LRC, nz=nz)
                D,T = b[3],b[15]
                          
            else:
                print("ERREUR VITESSE CROISIERE NON SPECIFIEE ")
                
            Vg=V+Vvent
            SR=SAR*(Vg/V)
            Wf=Vg/SR
            
            # Si OK, verification poussée necessaire en croisière
            if D>T :
                print("ERREUR poussee necessaire trop grande, > MCR\nFIN DE L'EXECUTION")
                    
                    
    
    
    

    return Vc, Vg, M, SAR, SR, Wf