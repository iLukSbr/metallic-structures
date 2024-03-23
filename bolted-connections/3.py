# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
print(' ')

#================================================================
#Carga cortante
Fg = 0 #kN permanente
Fq = 763.2 #kN variável
gamma_g = 0 #CARGA DE 
gamma_q = 1.2 #CARGA DE AÇÃO TRUNCADA
Fsd_calc = gamma_g*Fg + gamma_q*Fq
if Fsd_calc < 45:
    Fsd = 45 #kN
else:
    Fsd = Fsd_calc

#================================================================
#Propriedades e dimensões dos parafusos
#Resistência última
fub = 103.5 #kN/cm² parafuso tipo ASTM A490
gamma_a2 = 1.35
#Diâmetro do parafuso
db = 3.6 #cm
#Área da seção transversal do parafuso
Ab = np.pi*db**2/4 #cm²

#================================================================
#Dimensões dos furos
#Diâmetro
df = db + 0.15 #cm
dfe = df + 0.2 #cm

#================================================================
#Força resistente à tração nos parafusos
print('Quantidade mínima de parafusos necessária para resistir à tração:')
n_parafusos = Fsd*gamma_a2/(0.75*Ab*fub)
n_parafusos_arred = np.ceil(n_parafusos)
print('São necessários',n_parafusos_arred,'parafusos para resistir ao Fsd=',Fsd)