# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 07:09:55 2020

@author: lucas
"""
pi = 3.14159265359

#Aço MR250
E = 20000 #kN/cm²
G = 7700 #kN/cm²
fy = 25

#Perfil HEA300
d = 29
bf = 30
tw = 0.85
tf = 1.4
r = 2.7
hw = d - 2*r - 2*tf
Ag = 112

#Alma
lambdae_alma = hw/tw
lambdaelim_alma = 1.49*(E/fy)**0.5

if(lambdae_alma < lambdaelim_alma):
    print('Alma ok')
else:
    print('Alma não')
   
#Mesa
lambdae_mesa = bf/(2*tf)
lambdaelim_mesa = 0.56*(E/fy)**0.5

if(lambdae_mesa < lambdaelim_mesa):
    print('Mesa ok')
else:
    print('Mesa não')