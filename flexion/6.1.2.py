# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço ASTM A36
fy = 25 #kN/cm²
fu = 40 #kN/cm²
E = 20000 #kN/cm²
Msd = 7000 #kN.cm

gamma_a1 = 1.1
gamma_a2 = 1.35

#Perfil I254x37,7
#Contido lateralmente: sem FLT
Ag = 48.1 #cm²
h =25.4 #cm
hw = 22.9 #cm
Zx = 465 #cm³
Wx = 405 #cm³
tw = 0.787 #cm
tf = 1.25 #cm
bf = 11.84 #cm
db = 1.9 #cm
df = db + 0.15
defetivo = df + 0.2
Afg = bf*tf
Afe = Afg - 2*defetivo*tf

if fy/fu<=0.8:
    Yt = 1
else:
    Yt = 1.1

if fu*Afe >= Yt*fy*Afg:
    print('Furos verifica')
    
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

else:
    Mrd = Afe*Wx*fu/(Afg*gamma_a2)

print("Mrd =", round(Mrd/100,3) ,"kN.m")