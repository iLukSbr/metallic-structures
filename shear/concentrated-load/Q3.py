# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:24:18 2021

@author: lucas
"""

import numpy as np

#Propriedades do aço:
E = 20000 #kN/cm²
fy = 31.7 #kN/cm² TIPO A500
gamma_a1 = 1.1

#Propriedades do perfil:
#PERFIL I 152 x 18,5
d = 15.24 #cm
tw = 0.584 #cm

tf = 0.91 #cm
bf = 8.46 #cm
Wx = 120.6 #cm³
Wy = 17.9 #cm³
K = 1.91 #cm
h = d - 2*K #cm
#Flexão em relação a X (eixo perpendicular à alma)
W = Wx

#Comprimento da viga TIPO 13
L = 117.4 #cm

#Propriedades das cargas
#Carga em cima da alma
#Pra dentro = compressão; Pra fora = tração
tipo_cima = 'tracao'
#Menor distância do apoio
lap_cima = 32.9 #cm
#Região de aplicação
bforca_cima = 4.54 #cm
lforca_cima = 20.22 #cm
#Rotação da mesa
rotac_cima = 'livre'
#Comprimento destravado
Lb_cima = L #cm

#Carga embaixo da alma
#Pra dentro = compressão; Pra fora = tração
tipo_baixo = '-'
#Menor distância do apoio
lap_baixo = 0 #cm
#Região de aplicação
bforca_baixo = 0 #cm
lforca_baixo = 0 #cm
#Rotação da mesa
rotac_baixo = '-'
#Comprimento destravado
Lb_baixo = 0 #cm

#Momento para Flexão Local da Alma
Mr = fy*W #kN.cm
#Adotado
Cr = 16*E

if tipo_cima != 'compressao' and tipo_baixo != 'compressao':
    print('Verificar FLM e ELA.')
    print(' ')
elif (tipo_cima == 'tracao' and tipo_baixo == 'compressao') or (tipo_cima == 'compressao' and tipo_baixo == 'tracao'):
    print('Verificar FLM, ELA, EA e FLA')
    print(' ')
elif tipo_cima == 'compressao' and tipo_baixo == 'compressao':
    print('Verificar ELA, EA, FLA e FAC')
    print(' ')
elif tipo_cima != 'tracao' and tipo_baixo != 'tracao':
    print('Verificar ELA, EA e FLA')
    print(' ')

#Flexão Local da Mesa
print('Flexão Local da Mesa:')
if tipo_cima == 'tracao':
    print('Tração em cima:')
    if bforca_cima < 0.15*bf:
        print('bforça=',bforca_cima,'< 0,15*bf=',0.15*bf,', a verificação não precisa ser feita, resiste à FLM.')
        Frd_FLM_cima = np.nan
    elif lap_cima >= 10*tf:
        print('bforça=',bforca_cima,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_cima,'>= 10*tf=',10*tf)
        Frd_FLM_cima = 6.25*tf**2*fy/gamma_a1
    elif lap_cima < 10*tf:
        print('bforça=',bforca_cima,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_cima,'< 10*tf=',10*tf)
        Frd_FLM_cima = 3.125*tf**2*fy/gamma_a1
    print(' ')
if tipo_baixo == 'tracao':
    print('Tração embaixo:')
    if bforca_baixo < 0.15*bf:
        print('bforça=',bforca_baixo,'< 0,15*bf=',0.15*bf,', a verificação não precisa ser feita, resiste à FLM.')
        print(' ')
        Frd_FLM_baixo = np.nan
    elif lap_baixo >= 10*tf:
        print('bforça=',bforca_baixo,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_baixo,'>= 10*tf=',10*tf)
        Frd_FLM_baixo = 6.25*tf**2*fy/gamma_a1
    elif lap_baixo < 10*tf:
        print('bforça=',bforca_baixo,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_baixo,'< 10*tf=',10*tf)
        Frd_FLM_baixo = 3.125*tf**2*fy/gamma_a1
    print(' ')
elif tipo_cima != 'tracao' and tipo_baixo != 'tracao':
    print('Não há carga de tração, FLM não ocorre.')
    print(' ')
    Frd_FLM_cima = np.nan
    Frd_FLM_baixo = np.nan
else:
    Frd_FLM_baixo = np.nan

#Escoamento Local da Alma
if tipo_cima == 'compressao' or tipo_cima == 'tracao':
    print('Escoamento Local da Alma, em cima:')
    if lap_cima > d:
        print('lap=',lap_cima,'> d=',d)
        Frd_ELA_cima = 1.1*(5*K + lforca_cima)*fy*tw/gamma_a1
    elif lap_cima <= d:
        print('lap=',lap_cima,'<= d=',d)
        Frd_ELA_cima = 1.1*(2.5*K + lforca_cima)*fy*tw/gamma_a1
else:
    Frd_ELA_cima = np.nan
print(' ')
if tipo_baixo == 'compressao' or tipo_baixo == 'tracao':
    print('Escoamento Local da Alma, embaixo:')
    if lap_baixo > d:
        print('lap=',lap_baixo,'> d=',d)
        Frd_ELA_baixo = 1.1*(5*K + lforca_baixo)*fy*tw/gamma_a1
    elif lap_baixo <= d:
        print('lap=',lap_baixo,'<= d=',d)
        Frd_ELA_baixo = 1.1*(2.5*K + lforca_baixo)*fy*tw/gamma_a1
else:
    Frd_ELA_baixo = np.nan
print(' ')

#Enrugamento da Alma
print('Enrugamento da Alma:')
if tipo_cima == 'compressao':
    print('Compressão em cima:')
    if lap_cima >= d/2:
        print('lap=',lap_cima,'>= d/2=',d/2)
        Frd_EA_cima = 0.66*tw**2*(1 + 3*(lforca_cima/d)*np.sqrt((tw/tf)**3))*np.sqrt(E*fy*tf/tw)/gamma_a1
    elif lap_cima < d/2 and lforca_cima/d <= 0.2:
        print('lap=',lap_cima,'< d/2=',d/2,'e lforça/d <=',lforca_cima/d)
        Frd_EA_cima = 0.33*tw**2*(1 + 3*(lforca_cima/d)*np.sqrt((tw/tf)**3))*np.sqrt(E*fy*tf/tw)/gamma_a1
    elif lap_cima < d/2 and lforca_cima/d > 0.2:
        print('lap=',lap_cima,'< d/2=',d/2,'e lforça/d >',lforca_cima/d)
        Frd_EA_cima = 0.33*tw**2*(1 + (4*lforca_cima/d - 0.2)*np.sqrt((tw/tf)**3))*np.sqrt(E*fy*tf/tw)/gamma_a1
else:
    Frd_EA_cima = np.nan
if tipo_baixo == 'compressao':
    print('Compressão embaixo:')
    if lap_baixo >= d/2:
        print('lap=',lap_baixo,'>= d/2=',d/2)
        Frd_EA_baixo = 0.66*tw**2*(1 + 3*(lforca_baixo/d)*np.sqrt((tw/tf)**3))*np.sqrt(E*fy*tf/tw)/gamma_a1
    elif lap_baixo < d/2 and lforca_baixo/d <= 0.2:
        print('lap=',lap_baixo,'< d/2=',d/2,'e lforça/d <=',lforca_baixo/d)
        Frd_EA_baixo = 0.33*tw**2*(1 + 3*(lforca_baixo/d)*np.sqrt((tw/tf)**3))*np.sqrt(E*fy*tf/tw)/gamma_a1
    elif lap_baixo < d/2 and lforca_baixo/d > 0.2:
        print('lap=',lap_baixo,'< d/2=',d/2,'e lforça/d >',lforca_baixo/d)
        Frd_EA_baixo = 0.33*tw**2*(1 + (4*lforca_cima/d - 0.2)*np.sqrt((tw/tf)**3))*np.sqrt(E*fy*tf/tw)/gamma_a1
else:
    Frd_EA_baixo = np.nan
if tipo_cima != 'compressao' and tipo_baixo != 'compressao':
    print('Não há carga de compressão, EA não ocorre.')
    print(' ')

#Flambagem Lateral da Alma com rotação da mesa comprimida IMPEDIDA
print('Flambagem Lateral da Alma com rotação da mesa comprimida IMPEDIDA:')
if tipo_cima == 'compressao' and rotac_cima == 'impedida':
    print("Compressão em cima:")
    if h*bf/(tw*Lb_cima) > 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'> 2.3, a verificação não precisa ser feita, resiste à FLA.')
        Frd_FLA_cima_i = np.nan
    elif h*bf/(tw*Lb_cima) <= 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'<= 2.3, precisa verificar.')
        Frd_FLA_cima_i = Cr*tw**3*tf*(0.94 + 0.37*(h*bf/(tw*Lb_cima))**3)/(gamma_a1*h**2)
else:
    Frd_FLA_cima_i = np.nan
print(' ')
if tipo_baixo == 'compressao' and rotac_baixo == 'impedida':
    print("Compressão embaixo:")
    if h*bf/(tw*Lb_baixo) > 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'> 2.3, a verificação não precisa ser feita, resiste à FLA.')
        Frd_FLA_baixo_i = np.nan
    elif h*bf/(tw*Lb_baixo) <= 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'<= 2.3, precisa verificar.')
        Frd_FLA_baixo_i = Cr*tw**3*tf*(0.94 + 0.37*(h*bf/(tw*Lb_baixo))**3)/(gamma_a1*h**2)
    print(' ')
elif (tipo_cima == 'compressao' and rotac_cima != 'impedida') or tipo_cima != 'compressao':
    print('Não há compressão com rotação IMPEDIDA, FLA impedida não ocorre.')
    Frd_FLA_cima_i = np.nan
    Frd_FLA_baixo_i = np.nan
else:
    Frd_FLA_baixo_i = np.nan
print(' ')

#Flambagem Lateral da Alma com rotação da mesa comprimida NÃO impedida
print('Flambagem Lateral da Alma com rotação da mesa comprimida NÃO impedida:')
if tipo_cima == 'compressao' and rotac_cima == 'livre':
    print("Compressão em cima:")
    if h*bf/(tw*Lb_cima) > 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'> 1.7, a verificação não precisa ser feita, resiste à FLA.')
        Frd_FLA_cima_n = np.nan
    elif h*bf/(tw*Lb_cima) <= 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'<= 1.7, precisa verificar.')
        Frd_FLA_cima_n = Cr*tw**3*tf*0.37*(h*bf/(tw*Lb_cima))**3/(gamma_a1*h**2)
else:
    Frd_FLA_cima_n = np.nan
print(' ')
if tipo_baixo == 'compressao' and rotac_baixo == 'livre':
    print("Compressão embaixo:")
    if h*bf/(tw*Lb_baixo) > 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'> 1.7, a verificação não precisa ser feita, resiste à FLA.')
        rd_FLA_baixo_n = np.nan
    elif h*bf/(tw*Lb_baixo) <= 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'<= 1.7, precisa verificar.')
        Frd_FLA_baixo_n = Cr*tw**3*tf*0.37*(h*bf/(tw*Lb_baixo))**3/(gamma_a1*h**2)
elif (tipo_cima == 'compressao' and rotac_cima != 'livre') or tipo_cima != 'compressao':
    print('Não há compressão com rotação LIVRE, FLA livre não ocorre.')
    Frd_FLA_cima_n = np.nan
    Frd_FLA_baixo_n = np.nan
else:
    Frd_FLA_baixo_n = np.nan
print(' ')

#Flambagem da Alma por Compressão
#Par de forças comprimindo a alma
print('Flambagem da Alma por Compressão:')
if tipo_cima == 'compressao' and tipo_baixo == 'compressao':
    print('Verificação de cima:')
    if lap_cima >= d/2:
        print('lap =',lap_cima,'>= d/2 =',d/2)
        Frd_FAC_cima = 24*tw**3*np.sqrt(E*fy)/(gamma_a1*h)
    elif lap_cima < d/2:
        print('lap =',lap_cima,'< d/2 =',d/2)
        Frd_FAC_cima = 12*tw**3*np.sqrt(E*fy)/(gamma_a1*h)
    print(' ')
    print('Verificação de baixo:')
    if lap_baixo >= d/2:
        print('lap =',lap_baixo,'>= d/2 =',d/2)
        Frd_FAC_baixo = 24*tw**3*np.sqrt(E*fy)/(gamma_a1*h)
    elif lap_baixo < d/2:
        print('lap =',lap_baixo,'< d/2 =',d/2)
        Frd_FAC_baixo = 12*tw**3*np.sqrt(E*fy)/(gamma_a1*h)
    print(' ')
else:
    print('Não há dupla compressão, FAC não ocorre.')
    print(' ')
    Frd_FAC_cima = np.nan
    Frd_FAC_baixo = np.nan

#Majoração
gamma_cima = 1.2 #AÇÃO TRUNCADA
#Carga de cálculo
Frd_cima = np.array([Frd_FLM_cima , Frd_ELA_cima , Frd_EA_cima , Frd_FLA_cima_i , Frd_FLA_cima_n , Frd_FAC_cima])
Frd_cima = Frd_cima[~np.isnan(Frd_cima)]
if len(Frd_cima) != 0:
    Fcima_d = min(Frd_cima) #kN
#Carga característica
    Fcima = Fcima_d/gamma_cima #kN
    print('Fcima máximo =',Fcima,'kN')

#Majoração
gamma_baixo = 0 #PESO DE 
#Carga de cálculo
Frd_baixo = np.array([Frd_FLM_baixo , Frd_ELA_baixo , Frd_EA_baixo , Frd_FLA_baixo_i , Frd_FLA_baixo_n , Frd_FAC_baixo])
Frd_baixo = Frd_baixo[~np.isnan(Frd_baixo)]
if len(Frd_baixo) != 0:
    Fbaixo_d = min(Frd_baixo) #kN
#Carga característica
    Fbaixo = Fbaixo_d/gamma_baixo #kN
    print('Fbaixo máximo =',Fbaixo,'kN')