# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 08:14:54 2020

@author: lucas
"""

Lb = 708

#Perfil L 76 x 7
rmin = 1.5

K = 1

IE = K*Lb/rmin

if(IE <= 200):
    print('Ok')
else:
    print('Não')