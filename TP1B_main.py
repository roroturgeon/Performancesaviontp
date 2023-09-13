# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:22:09 2023

@author: Vincent
"""

import numpy as np
import math
from TP1B import parametres_de_vol
Hp=40000
T_C=-50
delISA=False
W=40000
M=0.74


a_kts, a_fts, M, V_kts, V_fts, Ve_kts, Ve_fts, Vc_kts, Vc_fts, pt, q, qc, Tt_C, Tt_K, mu, RN, CL = parametres_de_vol(Hp, T_C, delISA, W, M=M)
print(RN)
print(CL)

