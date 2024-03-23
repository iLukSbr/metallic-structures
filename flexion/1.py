# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço AR415
fy = 41.5 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1

#Não contido lateralmente: com FLT

#Perfil W200x15
liga = 'laminado'
d = 20 #cm
hw = 17 #cm
Zx = 147.9 #cm³
tw = 0.43 #cm
tf = 0.52 #cm
bf = 10 #cm
ry = 2.12 #cm

#FLA
lambda_fla = hw/tw
lambdap_fla = 3.76*(E/fy)**0.5
lambdar_fla = 5.7*(E/fy)**0.5
if lambda_fla<=lambdap_fla:
    print('Compacta em FLA')
elif lambda_fla>lambdap_fla and lambda_fla<=lambdar_fla:
    print('Semicompacta em FLA')
else:
    print('Esbelta em FLA')

#FLM
lambda_flm = (bf/2)/tf
lambdap_flm = 0.38*(E/fy)**0.5
if liga == 'laminado':
    Cls = 0.83
if liga == 'soldado':
    kc = 4/((hw/tw)**0.5)
    if kc<0.35 or kc>0.76:
        print('Problema no kc, modificar perfil')
    Cls = 0.95*kc**0.5
lambdar_flm = Cls*(E/(0.7*fy))**0.5
if lambda_flm<=lambdap_flm:
    print('Compacta em FLM')
elif lambda_flm>lambdap_flm and lambda_flm<=lambdar_flm:
    print('Semicompacta em FLM')
else:
    print('Esbelta em FLM')

#FLT
Lbx = 862.1 #m
lambda_flt = Lbx/ry
lambdap_flt = 1.76*(E/fy)**0.5
if lambda_flt<=lambdap_flt:
    print('Compacta em FLT')
# elif lambda_flm>lambdap_flm and lambda_flm<=lambdar_flm:
    # print('Semicompacta em FLM')
# else:
    # print('Esbelta em FLM')


Mpl = Zx*fy
Mrd = Mpl/gamma_a1

print("Mrd =", round(Mrd/100,3) ,"kN.m")