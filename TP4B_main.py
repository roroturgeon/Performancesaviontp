# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 13:11:37 2023

@author: Vincent M & Rosalie T
"""

import numpy as np
from TP4B import longpiste

# # CAS 1
# V1VR = 0.90    # V1/VR
# W =  45000      # Poids (lbs)
# Hp = 0          # ft
# delISA = True   # Déviation isa
# T_C = 20        # °C

# CAS 2
V1VR = 0.80    # V1/VR
W =  30000      # Poids (lbs)
Hp = 2000          # ft
delISA = True   # Déviation isa
T_C = 0        # °C

# # CAS 3
# V1VR = 1.0    # V1/VR
# W =  51000      # Poids (lbs)
# Hp = 10000          # ft
# delISA = True   # Déviation isa
# T_C = 35        # °C




FTOD,TODOEI,ASD,LMIN, DBRKE=longpiste(V1VR, W, Hp, T_C, delISA)