# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:01:31 2023


AER8375 - Performances avion

Script principal d'exécution du TP3B

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
from TP3B import croisiere


nb_PAX = 20         # [-] Nombre de passagers
PAX_wt = 225        # [lb] Poids unitaire des passagers, incl. baggages
MXFUEL = 15000      # [lb] Quantité d'essence maximale
Vvent = 0           # [kts] Vitesse du vent
T_C = 0             # [K] Déviation ISA
delISA = True       # [boolean] Mode de spécification de la température (déviation)
VKCAS = 275         # [kts] Vitesse calibrée de montée, constante de 10k à transition
M_climb = .78       # [-] Vitesse de montée à Mach constant, de transition à croisière
M_cruise = .78      # [-] Vitesse de croisière à Mach constant
Payload = nb_PAX*PAX_wt

TOF = 250
TAF = 200
APF = 200
reserves = 2000

MZFW = 44000
MTOW = 53000
MLW = 47000
MRW = 53250

OWE = 31500
ZFW = OWE + Payload
if ZFW > MZFW : 
    print("ERREUR ZFW trop grand")
RW = ZFW + MXFUEL
if RW>MRW:
    print("ERREUR RW trop grand")
TOW = RW - TAF
if TOW > MTOW : 
    print("ERREUR TOW trop grand")
ETO = TOW - TOF

LW = ZFW + reserves
if LW > MLW : 
    print("ERREUR LW trop grand")

### NOTE faire grosse boucle while pour la cruise et descente, converger vers le 2000

"""
Calcul de la montée (déterministe)
"""
Hpi = 1500
Hpf = 41000
dVolets = 0
pRoues = "up"
rMoteur = "AEO"
pVol = "MCL"
nz=1

t1, d1, fuel_climb, s2, acc_10k, V_avg_10k, dt_10k, dd_10k, df_10k, W_10k, Hp_low = montee_descente(Hpi, Hpf, T_C, delISA, Vvent, VKCAS, M_climb, ETO, dVolets, pRoues, rMoteur, pVol, nz=nz)

dist_montee = d1
alt_croisiere = Hp_low
print("Distance de montée : ", dist_montee, "[NM]")
print("Altitude de croisière : ", alt_croisiere, "[ft]")

"""
Calcul croisière - descente (Itérations)
"""

# Calcul croisière
# Poids après montée
TOC = ETO-fuel_climb
Vc, Vg, M, SAR, SR, Wf = croisiere(alt_croisiere,T_C,delISA,Vvent,TOC,M=M_cruise)

available_fuel = MXFUEL-fuel_climb-TOF-TAF
print("Gaz brulable : ", available_fuel)
print("Range dispo (cruise + descent) : ",SR*available_fuel)

distances_test = np.linspace(1500,SR*available_fuel,10)
gaz_restant = np.zeros_like(distances_test)

for i in range(len(distances_test)):
    
    fuel_cruise = distances_test[i]/SR
    TOD = TOC-fuel_cruise
    pVol = "IDLE"
    t1, d1, fuel_descent, s2, acc_10k, V_avg_10k, dt_10k, dd_10k, df_10k, W_10k, Hp_low = montee_descente(alt_croisiere, Hpi, T_C, delISA, Vvent, VKCAS, M_climb, TOD, dVolets, pRoues, rMoteur, pVol, nz=nz)
    
    gaz_restant[i] = available_fuel-fuel_cruise-fuel_descent
    
plt.figure(dpi=500)
plt.plot(distances_test, gaz_restant)
plt.xlabel("Distance segment croisière [NM]")
plt.ylabel("Carburant restant à 1500' [lb fuel]")
plt.hlines(2200, 1500, SR*available_fuel)


# Bissection
fuel_target = reserves+APF

dist_min = 1000
dist_max = SR*available_fuel
eps = 0.001
erreur = 1 
while erreur>eps:
    dist_moy = .5*dist_min+.5*dist_max      # Distance pour segment croisière
    

    fuel_cruise = dist_moy/SR
    TOD = TOC-fuel_cruise
    pVol = "IDLE"
    t1, dist_desc, fuel_descent, s2, acc_10k, V_avg_10k, dt_10k, dd_10k, df_10k, W_10k, Hp_low = montee_descente(alt_croisiere, Hpi, T_C, delISA, Vvent, VKCAS, M_climb, TOD, dVolets, pRoues, rMoteur, pVol, nz=nz)
    gaz_restant = available_fuel-fuel_cruise-fuel_descent

    if gaz_restant < fuel_target:
        dist_max = dist_moy
    else:
        dist_min = dist_moy
    erreur = abs(gaz_restant-fuel_target)
    
dist_cruise = dist_moy

print("Distance de croisière : ",dist_cruise ,"[NM]")
print("Distance de descente : ",dist_desc ,"[NM]")
print("Distance totale : ", dist_cruise+dist_desc+dist_montee,"[NM]")
print("Carburant total : ",TAF+TOF+fuel_climb+fuel_cruise+fuel_descent+APF ,"[lb]")
print("Carburant total théorique : ",MXFUEL-reserves,"[lb]")


















