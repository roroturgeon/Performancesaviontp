# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:10:28 2023
JOYEUX HALLOWEEN

AER8375 - Performances avion

Script principal d'exécution du TP3B

@author: Rosalie Turgeon & Vincent Moreau
         ( 2072092 )       ( 2075782 )
"""


import numpy as np
from TP3B import croisiere

# ###CAS 1
# Hp=15000
# T_C=0
# delISA=True
# Vvent=0
# W=40000
# Vmd="Vmd"

# Vc, Vg, M, SAR, SR, Wf=croisiere(Hp, T_C, delISA, Vvent, W, Vmd=Vmd)


# ### CAS 2

# Hp=31000
# T_C=10
# delISA=True
# Vvent=20
# W=45000
# M=.74

# Vc, Vg, M, SAR, SR, Wf=croisiere(Hp, T_C, delISA, Vvent, W, M=M)


### CAS 3

Hp=35000
T_C=10
delISA=True
Vvent=-50
W=40000
LRC="LRC"

Vc, Vg, M, SAR, SR, Wf=croisiere(Hp, T_C, delISA, Vvent, W, LRC=LRC)