# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:11:01 2023

AER8375 - Performances avion

Script principal d'exécution du TP3A

@author: Rosalie Turgeon & Vincent Moreau
         ( 2072092 )       ( 2075782 )
"""

import numpy as np
from TP3A import montee_descente

"""
Cas 1
"""

Hpi = 1500
Hpf = 41000
delISA = True
T_C = 10
Vvent = 20
VKCAS = 275
MACH=.74
Wi = 52800
dVolets = 0
pRoues = 'up'
rMoteur = "AEO"
pVol = "MCL"
nz = 1

montee_descente(Hpi, Hpf, T_C, delISA, Vvent, VKCAS, MACH, Wi, dVolets, pRoues, rMoteur, pVol, nz=nz)

