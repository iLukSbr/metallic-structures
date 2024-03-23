# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:40:18 2020

@author: Mariana
"""
#

import numpy as np

"""
coeficientes de ponderação
"""

gamma_a1 = 1.1

"""
propriedades do metal
"""

E = 20000. #kN/cm²
fy = 25. #kN/cm²

"""
propriedades do perfil
"""

d = 65. #cm
hw = 62.5 #cm - pefil soldado não desconta a altura da solda
tw = 0.8 #cm
kv = 5.0 #Não há especificação de enrijecedores, então considera que não há nenhum

"""
verificação das esbeltezas
"""

lambda_e = hw/tw
lambda_p = 1.1*np.sqrt(kv*E/fy)
lambda_r = 1.37*np.sqrt(kv*E/fy)

"""
resistencia do perfil ao cisalhamento
"""

Aw = d*tw
Vpl = Aw*0.6*fy

"""
resistência máxima ao cisalhamento no regime semicompacto
"""

Vrd = lambda_p/lambda_e*Vpl/gamma_a1

"""
Determinação de kv e a para tornar o perfil compacto ao cisalhamento
"""

kv = fy/E*(lambda_e/1.1)**2

"""
Determinação da distância entre enrijecedores de alma de cisalhamento
"""

a = np.sqrt(5*hw**2)/(kv-5.0)

"""
verificação do valor de a
"""

lede = a/hw
ldde = (260*tw/hw)**2
if lede > ldde:
    print('kv - 5,0')
else:
    print('O valor de a está verificado')

