import numpy as np
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces
from TP2B import montee

def montee_descente(Hpi,Hpf,T_C,delISA,Vvent,VKCAS,MACH, Wi, dVolets, pRoues, rMoteur, pVol, **kwargs):
    
    ROC_min=100 # Taux de montée minimum (ft/min)
    labda=0.0019812 #(Celsius/pi**2)
    T_0_C=15    #Temperature au niveau de la mer
    CtoK=273.15 
    g=32.18503937007874     #Accélération gravitationnelle (pi/s**2)
    ViC_kts=250          #Vitesse calibrée initiale sous 10 000 ft (kts)
    fts_to_kts = 0.5924838      # 1 pi/s = 0.5924838 kts
    ViC_fts=ViC_kts*fts_to_kts     #Vitesse calibrée initiale sous 10 000 ft (fts)
    increment=1000          #Incrément utilisé pour l'intérgration
    CG=0.09             # CG pour ne pas impacter les données
    Tneg = 1200         # Poussee pour calcul de SFC si poussee neg
    
    s1 = 10000
    s2 = 30000
 
    if Hpf>Hpi:
        signe=1
    else:
        signe=-1
    
    increment*=signe # 1 si monte, -1 si descend
    palier_10k=False
    palier_30k=False
 
    # Altitudes pour plage d'integration (initiales)
    Hp1=Hpi
    Hp2=Hp1+increment*signe
    
    # Initialisation des compteurs d'intégration
    Wmoy=Wi
    t1=0
    d1=0
    
    # Initialisation des compteurs et epsilon pour while
    eps=1
    nbiter=0
    
    """
    Fonction d'incrémentation de l'altitude entre les plages d'intégration
    """
    def incrementation(Hp1,Hp2,signe,increment):
        Hp1=Hp2
        if (Hp2+increment > Hpf and signe == 1) or (Hp2+increment<Hpf and signe==-1):
            Hp2 = Hpf    
        else : 
            Hp2=Hp1+increment
        
        return Hp1,Hp2
    
    
    while (Hp1<Hpf and signe == 1) or (Hp1> Hpf and signe==-1):
        print(nbiter)
        print("Hp1 = ",Hp1, ", Hp2 = ", Hp2)
        nbiter += 1
        
        # Verifier si on doit rapetisser l'increment pour faire la portion 
        # avant le palier (prépalier)
        if signe==1 and Hp1<s1 and Hp2>s1 : 
            Hp2=s1
        elif signe==1 and Hp1<s2 and Hp2>s2 : 
            Hp2=s2
        elif signe==-1 and Hp1>s1 and Hp2<s1:
            Hp2=s1
        elif signe==-1 and Hp1>s2 and Hp2<s2:
            Hp2=s2
        
        # Verifier si on est rendu à calculer l'acceleration à un palier
        if Hp1 == s1 and nbiter>1: 
            palier_10k = True
        elif Hp1 == s2 and nbiter>1:
            palier_30k = True

            
        # Calcul de palier le cas echeant
        if palier_10k:
            print("Calculer l'acceleration du palier 10k")
            
            Hp1+=eps*signe
            palier_10k = False
        elif palier_30k:
            print("Calculer l'acceleration du palier 30k")
            
            Hp1+=eps*signe
            palier_30k = False
        else: 
        # Definition des vitesses
            if Hp1<=s1 and not palier_10k:
                Vconst= "CAS"
                vitesse_kwarg = {"Vc":ViC_kts}
            elif Hp1<=s2 and Hp1>s1 and not palier_30k:
                Vconst= "CAS"
                vitesse_kwarg = {"Vc":VKCAS}
            elif Hp1>s2 and not palier_10k and not palier_30k:
                Vconst= "MACH"
                vitesse_kwarg = {"M":MACH}
            
            Hpmoy=(Hp1+Hp2)/2
            deltaHp=Hp2-Hp1
            TISA_K=(T_0_C-labda*Hpmoy)+CtoK
            T_K=TISA_K+T_C
            deltaH=deltaHp*(T_K/TISA_K)
            
            a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL=parametres_de_vol(Hpmoy, T_C, delISA, Wmoy,  **kwargs, **vitesse_kwarg)
            CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA_9, nzSw, phiSw, nzBuffet, phi, M=forces(Hpmoy, T_C, delISA, Wmoy, CG, dVolets, pRoues, rMoteur, pVol, **kwargs, **vitesse_kwarg)
            grad, RoCg_min, RoCp_min, AF,a=montee(Hpmoy, T_C, delISA, Wmoy, CG, dVolets, pRoues, rMoteur, pVol, Vconst, **kwargs, **vitesse_kwarg)
               
            RoCg_min*=signe
            RoCg_s=RoCg_min/60
            dt=deltaH/RoCg_s
            t2=t1+dt
            deltadis=V_fts*dt
            d2=d1+deltadis
            SFC = 0.58 + (0.035 * Hpmoy/ 10000)
            if T>=0:
                Wfmoy=SFC*T
            else:
                Wfmoy=SFC*Tneg
                
            
                
            Hp1,Hp2 = incrementation(Hp1,Hp2,signe,increment)
            
   
    
    
    return
    


        
        
        
        
        

