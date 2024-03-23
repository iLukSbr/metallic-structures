# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:14:54 2020

@author: lucas
"""

Lb = 1848

#Perfil U 305 x 30.7
rmin = 2.03

K = 0.65

IE = K*Lb/rmin

if(IE <= 200):
    print('Ok')
else:
    print('Não')