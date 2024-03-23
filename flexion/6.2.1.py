# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço MR250
fy = 25 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Contidos lateralmente: sem FLT

#Perfil W310x21
h = 29.2 #cm
hw = 27.2 #cm
Zx = 291.9 #cm³
tw = 0.51 #cm
tf = 0.57 #cm
bf = 10.1 #cm

#FLA
lambda_fla = hw/tw
lambdap_fla = 3.76*(E/fy)**0.5
if lambda_fla<=lambdap_fla:
    print('Compacta em FLA')

#FLM
lambda_flm = (bf/2)/tf
lambdap_flm = 0.38*(E/fy)**0.5
if lambda_flm<=lambdap_flm:
    print('Compacta em FLM')

Mpl = Zx*fy
Mrd = Mpl/gamma_a1

print("Mrd =", round(Mrd/100,3) ,"kN.m")