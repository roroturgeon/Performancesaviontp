# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:54:00 2023

@author: Rosalie
"""

import numpy as np
from TP4A import decollage_aterrissage

# W=45000
# Hp=0
# T_C=20
# delISA=True

# V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO=decollage_aterrissage(Hp, W, T_C, delISA)

# W=30000
# Hp=2000
# T_C=0
# delISA=True

# V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO=decollage_aterrissage(Hp, W, T_C, delISA)

W=51000
Hp=10000
T_C=35
delISA=True

V1_min,V1_max,VR,V2_TAS,VLOFOEI,VLOFAEO,V35AEO, dtvlovrOEI,dtvlov35OEI,dtvlovrAEO,dtvlov35AEO,disvlovrOEI,disvlov35OEI,disvlovrAEO,disvlov35AEO=decollage_aterrissage(Hp, W, T_C, delISA)