# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:08:57 2023

@author: Vincent
"""

import numpy as np
import math 
from TP2A import forces

Hp=30000
T_C=15
delISA=True
W=40000
dVolets=0
pRoues="up"
rMoteur="MCR AEO"
CG=.25

S=forces(Hp, T_C, delISA, W, CG, dVolets, pRoues, rMoteur, S=410, VVsr=1.23, nz=2)