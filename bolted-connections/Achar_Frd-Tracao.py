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
Fq = 0 #kN variável
gamma_g = 0 #CARGA DE 
gamma_q = 0 #CARGA DE 
Fsd_calc = gamma_g*Fg + gamma_q*Fq
if Fsd_calc < 45:
    Fsd = 45 #kN
else:
    Fsd = Fsd_calc

#================================================================
#Propriedades e dimensões dos parafusos
#Resistência última
fub =  #kN/cm² parafuso tipo 
gamma_a2 = 1.35
#Diâmetro do parafuso
db =  #cm
#Área da seção transversal do parafuso
Ab = np.pi*db**2/4 #cm²
#N° de parafusos
n_parafusos = 

#================================================================
#Dimensões dos furos
#Diâmetro
df = db + 0.15 #cm
dfe = df + 0.2 #cm

#================================================================
#Força resistente à tração nos parafusos
print('Força resistente à tração dos parafusos:')
Ftrd = 0.75*Ab*fub*n_parafusos/gamma_a2
if Ftrd >= Fsd:
    print('Ftrd=',Ftrd,'>= Fsd=',Fsd,'resiste ao contato!')
else:
    print('Ftrd=',Ftrd,'< Fsd=',Fsd,'NÃO resiste ao contato!')
print(' ')