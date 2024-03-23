# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Aço A500
fy = 31.7 #kN/cm²
fu = 42.7 #kN/cm²
E = 20000 #kN/cm²

gamma_a1 = 1.1
gamma_a2 = 1.35

#Perfil H102x20,5
#Não contido lateralmente: com FLT
Ag = 26.1 #cm²
d = 10.1 #cm
hw = 9.24 #cm
Zx = 100.1 #cm³
Wx = 88.4 #cm³
tw = 0.795 #cm
tf = 0.92 #cm
bf = 10.1 #cm
db = 2.54 #cm
df = db + 0.15
defetivo = df + 0.2
Afg = bf*tf
Afe = Afg - 2*defetivo*tf

if fy/fu<=0.8:
    Yt = 1
else:
    Yt = 1.1

print('fu*Afe', fu*Afe)
print('Yt*fy*Afg', Yt*fy*Afg)
if fu*Afe >= Yt*fy*Afg:
    print('Furos não influenciam')
    
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
    print('Furos influenciam')
    Mrd = Afe*Wx*fu/(Afg*gamma_a2)

print("Mrd =", round(Mrd/100,3) ,"kN.m")