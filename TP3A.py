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
    CG=0.09             #CG pour ne pas impacter les données
 
    if Hpf>Hpi:
        signe=1
    else:
        signe=-1
    
    increment*=signe

 
    
    Hp1=Hpi
    Hp2=Hp1+increment
    Wmoy=Wi
    t1=0
    d1=0
    while Hp2<Hpf:
        Hpmoy=(Hp1+Hp2)/2
        deltaHp=Hp2-Hp1
        TISA_K=(T_0_C-labda*Hpmoy)+CtoK
        T_K=TISA_K+T_C
        deltaH=deltaHp*(T_K/TISA_K)
        if Hp1<10000:
            Vc=ViC_kts
            Vconst= "CAS"
            a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL=parametres_de_vol(Hpmoy, T_C, delISA, Wmoy, Vc=Vc, **kwargs)
            CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA_9, nzSw, phiSw, nzBuffet, phi, M=forces(Hpmoy, T_C, delISA, Wmoy, CG, dVolets, pRoues, rMoteur, pVol,Vc=Vc, **kwargs)
            grad, RoCg_min, RoCp_min, AF,a=montee(Hpmoy, T_C, delISA, Wmoy, CG, dVolets, pRoues, rMoteur, pVol, Vconst,Vc=Vc, **kwargs)
            RoCg_min*=signe
            RoCg_s=RoCg_min/60
            dt=deltaH/RoCg_s
            t2=t1+dt
            deltadis=V_fts*dt
            d2=d1+deltadis
            SFC = 0.58 + (0.035 * Hpmoy/ 10000)
            Wfmoy=SFC*T
            
        elif Hp1<30000:
            Vc=VKCAS
            Vconst= "CAS"
        else:
            M=MACH
            Vconst= "MACH"
            
            
        Hp1=Hp2
        Hp2=Hp1+increment
            
    
    
    
    
    return


