# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:06:35 2023

@author: Vincent
"""

import numpy as np
from test1 import test_kwarg

a=5
vt=4
ve=2
type_vitesse_arr=np.array([{'vt':4}, {'ve':6}])
valeur_vitesse=2

test_kwarg(a, **type_vitesse_arr[1])