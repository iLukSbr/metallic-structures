# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço MR250
fy = 25 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Perfil T
hw = 30.48 #cm
tw = 2.54 #cm
tf = 2.2225 #cm
bf = 25.4 #cm
Zx =  #cm³

comprimida = input('Qual comprimida? [mesa/alma] ')
if comprimida == 'mesa':
    T1 = 1.19
    T2 = 0.5
    T3 = 0;69
elif comprimida == 'alma':
    T1 = 2.43
    T2 = 1.72
    T3 = 0.71

Mpl = Zx*fy

#FLM
lambda_flm = (bf/2)/tf
lambdap_flm = 0.38*(E/fy)**0.5
lambdar_flm = (E/fy)**0.5
if lambda_flm<=lambdap_flm:
    print('Compacta em FLM')
    Mrd = Mpl/gamma_a1
elif lambda_flm>lambdap_flm and lambda_flm<=lambdar_flm:
    print('Semicompacta em FLM')
    Mrd = (T1-T2*lambda_flm*(fy/E)**0.5)*fy*Wc/gamma_a1
else:
    print('Esbelta em FLM')
    Mrd = T3*E*Wc/(gamma_a1*lambda_flm**2)

print("Mrd =", round(Mrd/100,3) ,"kN.m")