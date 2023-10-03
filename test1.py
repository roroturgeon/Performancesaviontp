# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:05:52 2023

@author: Vincent
"""

def test_kwarg(a, **kwargs):
    
    
    print("a="+str(a))
    if kwargs.get('vt'):
        vt=kwargs.get('vt')
        print("vt="+str(vt))
    else:
        ve=kwargs.get('ve')
        print("ve="+str(ve))