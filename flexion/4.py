# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

pi = 3.14159265359

#Aço AR350
fy = 35 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1
Lbx = 1103.4 #cm

#Não contido lateralmente: com FLT

#Perfil W150x18
liga = 'laminado'
d = 15.3 #cm
hw = 11.9 #cm
Zx = 139.4 #cm³
tw = 0.58 #cm
tf = 0.71 #cm
bf = 10.2 #cm
ry = 2.32 #cm
Iy = 126 #cm4
Wx = 122.8 #cm³
Wmin = 24.7 #cm³
r = (d - 2*tf - hw)/2
c = r + tf

J = (2*bf*tf**3 + (d - 2*c)*tw**3)/3
Cw = (Iy*(d-tf)**2)/4

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
lambda_flt = Lbx/ry
lambdap_flt = 1.76*(E/fy)**0.5
beta1 = 0.7*fy*Wx/(E*J)
lambdar_flt = 1.38*((Iy*J)**0.5)*((1+(1+27*Cw*(beta1**2)/Iy)**0.5)**0.5)/(ry*J*beta1)
if lambda_flt<=lambdap_flt:
    print('Compacta em FLT')
elif lambda_flt>lambdap_flt and lambda_flt<=lambdar_flt:
    print('Semicompacta em FLT')
else:
    print('Esbelta em FLT')
    
Cb = 1.389

Mcr = Cb*(pi**2)*E*Iy*(((Cw/Iy)*(1+0.039*J*(Lbx**2)/Cw))**0.5)/(Lbx**2)
Mr = 0.7*fy*Wx

Mpl = Zx*fy
Mrd1 = Mpl/gamma_a1
Mrd2 = Mcr/gamma_a1
Mrd3 = (Cb/gamma_a1)*(Mpl-(Mpl-Mr)*(lambda_flt-lambdap_flt)/(lambdar_flt-lambdap_flt))

Mrdlim = 1.5*Wmin*fy/gamma_a1

print("Mrd =", round(min(Mrd1,Mrd2,Mrdlim),3) ,"kN.cm")