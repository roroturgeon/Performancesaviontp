# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:08:57 2023

@author: Vincent
"""

import numpy as np
from TP2A import forces

Hp=30000
T_C=15
delISA=True
W=40000
M=.74
dVolets=0
pRoues="up"
rMoteur="AEO"
pVol="MCR"
CG=.25
nz=1


CL, L, CD, D, finesse, Cdp, Dp, CDi, Di, dCDComp, DComp, DCDWM, DWM,DCDCNTL, DCNTL,  T, AOA, nzSw, phiSw, nzBuffet = forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, pVol, nz=nz, M=M)


