# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 16:22:42 2023

@author: Rosalie
"""

import numpy as np
from TP1A import atmosphere
from TP1B import parametres_de_vol
from TP2A import forces
from TP2B import montee

# Hp=30000
# T_C=15
# delISA=True
# W=40000
# dVolets=0
# pRoues="up"
# rMoteur="AEO"
# pVol="MCL"
# CG=.25
# Vconst="MACH"
# M=0.74
# nz=1

# grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, M=M,nz=nz)
# print(AF)

# Hp=5000
# T_C=0
# delISA=True
# W=35000
# dVolets=20
# pRoues="up"
# rMoteur="AEO"
# pVol="MTO"
# CG=.15
# Vconst="CAS"
# VVsr=1.23
# nz=1

# grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, VVsr=VVsr,nz=nz)
# print(AF)

Hp=5000
T_C=0
delISA=True
W=35000
dVolets=20
pRoues="up"
rMoteur="OEI"
pVol="MTO"
CG=.15
Vconst="CAS"
VVsr=1.13
nz=1

grad, RoCg_min, RoCp_min, AF,a=montee(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, Vconst, VVsr=VVsr,nz=nz)
print(AF)

