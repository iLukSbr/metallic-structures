# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 16:24:18 2021

@author: lucas
"""

import numpy as np

#Propriedades do aço:
E = 20000 #kN/cm²
fy = 25 #kN/cm² TIPO A-36
gamma_a1 = 1.1

#Propriedades do perfil:
#PERFIL 
d = 50 #cm
tw = 0.63 #cm
tf = 0.95 #cm
h = d - tf #cm
bf = 25 #cm
w = 0.5  #cm
Wx = 0 #cm³
Wy = 0 #cm³
K = tf + w #cm
#Flexão em relação a X (eixo perpendicular à alma)
W = Wx

#Comprimento da viga
L = 500 #cm

#Propriedades das cargas
#Carga em cima da alma
#Pra dentro = compressão; Pra fora = tração
tipo_cima = '-'
#Carga característica
Fcima = 0 #kN
#Menor distância do apoio
lap_cima = 0 #cm
#Majoração
gamma_cima = 0 #CARGA DE 
#Carga de cálculo
Fcima_d = gamma_cima*Fcima #kN
#Região de aplicação
bforca_cima = 0 #cm
lforca_cima = 0 #cm
#Rotação da mesa
rotac_cima = '-'
#Comprimento destravado
Lb_cima = 0 #cm
#Momento solicitante de cálculo
Msd_cima = 0 #kN.cm VIGA TIPO 

#Carga embaixo da alma
#Pra dentro = compressão; Pra fora = tração
tipo_baixo = 'tracao'
#Carga característica
Fbaixo = 0 #kN
#Menor distância do apoio
lap_baixo = 50 #cm
#Majoração
gamma_baixo = 0 #CARGA DE 
#Carga de cálculo
Fbaixo_d = 300 #kN
#Região de aplicação
bforca_baixo = 5 #cm
lforca_baixo = 10 #cm
#Rotação da mesa
rotac_baixo = 'livre'
#Comprimento destravado
Lb_baixo = L #cm
#Momento solicitante de cálculo
Msd_baixo = Fbaixo_d*(L-lap_baixo)*lap_baixo/L #kN.cm VIGA TIPO 6

#Momento para Flexão Local da Alma
Mr = fy*W #kN.cm

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
    elif lap_cima >= 10*tf:
        print('bforça=',bforca_cima,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_cima,'>= 10*tf=',10*tf)
        Frd_FLM_cima = 6.25*tf**2*fy/gamma_a1
    elif lap_cima < 10*tf:
        print('bforça=',bforca_cima,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_cima,'< 10*tf=',10*tf)
        Frd_FLM_cima = 3.125*tf**2*fy/gamma_a1
    if Frd_FLM_cima >= Fcima_d:
        print('Frd_FLM =',Frd_FLM_cima,'>= Fcima_d=',Fcima_d,'ok!')
    elif Frd_FLM_cima < Fcima_d:
        print('Frd_FLM =',Frd_FLM_cima,'< Fcima_d=',Fcima_d,', precisa de enrijecedores locais de alma em ambos os lados nessa região')
    print(' ')
if tipo_baixo == 'tracao':
    print('Tração embaixo:')
    if bforca_baixo < 0.15*bf:
        print('bforça=',bforca_baixo,'< 0,15*bf=',0.15*bf,', a verificação não precisa ser feita, resiste à FLM.')
    elif lap_baixo >= 10*tf:
        print('bforça=',bforca_baixo,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_baixo,'>= 10*tf=',10*tf)
        Frd_FLM_baixo = 6.25*tf**2*fy/gamma_a1
    elif lap_baixo < 10*tf:
        print('bforça=',bforca_baixo,'>= 0,15*bf=',0.15*bf,', precisa verificar FLM.')
        print('lap=',lap_baixo,'< 10*tf=',10*tf)
        Frd_FLM_baixo = 3.125*tf**2*fy/gamma_a1
    if Frd_FLM_baixo >= Fbaixo_d:
        print('Frd_FLM =',Frd_FLM_baixo,'>= Fbaixo_d=',Fbaixo_d,'ok!')
    elif Frd_FLM_baixo < Fbaixo_d:
        print('Frd_FLM =',Frd_FLM_baixo,'< Fbaixo_d=',Fbaixo_d,', precisa de enrijecedores locais de alma em ambos os lados nessa região')
    print(' ')
elif tipo_cima != 'tracao' and tipo_baixo != 'tracao':
    print('Não há carga de tração, FLM não ocorre.')
    print(' ')

#Escoamento Local da Alma
if tipo_cima == 'compressao' or tipo_cima == 'tracao':
    print('Escoamento Local da Alma, em cima:')
    if lap_cima > d:
        print('lap=',lap_cima,'> d=',d)
        Frd_ELA_cima = 1.1*(5*K + lforca_cima)*fy*tw/gamma_a1
    elif lap_cima <= d:
        print('lap=',lap_cima,'<= d=',d)
        Frd_ELA_cima = 1.1*(2.5*K + lforca_cima)*fy*tw/gamma_a1
    if Frd_ELA_cima >= Fcima_d:
        print('Frd_ELA =',Frd_ELA_cima,'>= Fcima_d=',Fcima_d,'ok!')
    elif Frd_ELA_cima < Fcima_d:
        print('Frd_ELA =',Frd_ELA_cima,'< Fcima_d=',Fcima_d,', precisa de enrijecedores locais de alma em ambos os lados nessa região')
    print(' ')
if tipo_baixo == 'compressao' or tipo_baixo == 'tracao':
    print('Escoamento Local da Alma, embaixo:')
    if lap_baixo > d:
        print('lap=',lap_baixo,'> d=',d)
        Frd_ELA_baixo = 1.1*(5*K + lforca_baixo)*fy*tw/gamma_a1
    elif lap_baixo <= d:
        print('lap=',lap_baixo,'<= d=',d)
        Frd_ELA_baixo = 1.1*(2.5*K + lforca_baixo)*fy*tw/gamma_a1
    if Frd_ELA_baixo >= Fbaixo_d:
        print('Frd_ELA =',Frd_ELA_baixo,'>= Fbaixo_d=',Fbaixo_d,'ok!')
    elif Frd_ELA_baixo < Fbaixo_d:
        print('Frd_ELA =',Frd_ELA_baixo,'< Fbaixo_d=',Fbaixo_d,', precisa de enrijecedores locais de alma em ambos os lados nessa região')
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
    if Frd_EA_cima >= Fcima_d:
        print('Frd_EA=',Frd_EA_cima,'>= Fcima_d=',Fcima_d,'ok!')
    elif Frd_EA_cima < Fcima_d:
        print('Frd_EA=',Frd_EA_cima,'< Fcima_d=',Fcima_d,', precisa de enrijecedores locais de alma em um ou ambos os lados nessa região')
    print(' ')
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
    if Frd_EA_baixo >= Fbaixo_d:
        print('Frd_EA=',Frd_EA_baixo,'>= Fbaixo_d=',Fbaixo_d,'ok!')
    elif Frd_EA_baixo < Fbaixo_d:
        print('Frd_EA=',Frd_EA_baixo,'< Fbaixo_d=',Fbaixo_d,', precisa de enrijecedores locais de alma em um ou ambos os lados nessa região')
    print(' ')
elif tipo_cima != 'compressao' and tipo_baixo != 'compressao':
    print('Não há carga de compressão, EA não ocorre.')
    print(' ')

#Flambagem Lateral da Alma com rotação da mesa comprimida IMPEDIDA
print('Flambagem Lateral da Alma com rotação da mesa comprimida IMPEDIDA:')
if tipo_cima == 'compressao' and rotac_cima == 'impedida':
    print("Compressão em cima:")
    if h*bf/(tw*Lb_cima) > 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'> 2.3, a verificação não precisa ser feita, resiste à FLA.')
    elif h*bf/(tw*Lb_cima) <= 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'<= 2.3, precisa verificar.')
        if Msd_cima < Mr:
            print('Msd_cima =',Msd_cima,'< Mr=',Mr)
            Cr = 32*E
        elif Msd_cima >= Mr:
            print('Msd_cima =',Msd_cima,'>= Mr=',Mr)
            Cr = 16*E
        Frd_FLA_cima = Cr*tw**3*tf*(0.94 + 0.37*(h*bf/(tw*Lb_cima))**3)/(gamma_a1*h**2)
        if Frd_FLA_cima >= Fcima_d:
            print('Frd_FLA=',Frd_FLA_cima,'>= Fcima_d=',Fcima_d,'ok!')
        elif Frd_FLA_cima < Fcima_d:
            print('Frd_FLA=',Frd_FLA_cima,'< Fcima_d=',Fcima_d,', precisa de contenção lateral')
    print(' ')
if tipo_baixo == 'compressao' and rotac_baixo == 'impedida':
    print("Compressão embaixo:")
    if h*bf/(tw*Lb_baixo) > 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'> 2.3, a verificação não precisa ser feita, resiste à FLA.')
    elif h*bf/(tw*Lb_baixo) <= 2.3:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'<= 2.3, precisa verificar.')
        if Msd_baixo < Mr:
            print('Msd_cima =',Msd_baixo,'< Mr=',Mr)
            Cr = 32*E
        elif Msd_cima >= Mr:
            print('Msd_baixo =',Msd_baixo,'>= Mr=',Mr)
            Cr = 16*E
        Frd_FLA_baixo = Cr*tw**3*tf*(0.94 + 0.37*(h*bf/(tw*Lb_baixo))**3)/(gamma_a1*h**2)
        if Frd_FLA_baixo >= Fbaixo_d:
            print('Frd_FLA=',Frd_FLA_baixo,'>= Fbaixo_d=',Fbaixo_d,'ok!')
        elif Frd_FLA_baixo < Fbaixo_d:
            print('Frd_FLA=',Frd_FLA_baixo,'< Fbaixo_d=',Fbaixo_d,', precisa de contenção lateral')
    print(' ')
elif (tipo_cima == 'compressao' and rotac_cima != 'impedida') or tipo_cima != 'compressao':
    print('Não há compressão com rotação IMPEDIDA, FLA impedida não ocorre.')
    print(' ')

#Flambagem Lateral da Alma com rotação da mesa comprimida NÃO impedida
print('Flambagem Lateral da Alma com rotação da mesa comprimida NÃO impedida:')
if tipo_cima == 'compressao' and rotac_cima == 'livre':
    print("Compressão em cima:")
    if h*bf/(tw*Lb_cima) > 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'> 1.7, a verificação não precisa ser feita, resiste à FLA.')
    elif h*bf/(tw*Lb_cima) <= 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_cima),'<= 1.7, precisa verificar.')
        if Msd_cima < Mr:
            print('Msd_cima =',Msd_cima,'< Mr=',Mr)
            Cr = 32*E
        elif Msd_cima >= Mr:
            print('Msd_cima =',Msd_cima,'>= Mr=',Mr)
            Cr = 16*E
        Frd_FLA_cima = Cr*tw**3*tf*0.37*(h*bf/(tw*Lb_cima))**3/(gamma_a1*h**2)
        if Frd_FLA_cima >= Fcima_d:
            print('Frd_FLA=',Frd_FLA_cima,'>= Fcima_d=',Fcima_d,'ok!')
        elif Frd_FLA_cima < Fcima_d:
            print('Frd_FLA=',Frd_FLA_cima,'< Fcima_d=',Fcima_d,', precisa de contenção lateral')
    print(' ')
if tipo_baixo == 'compressao' and rotac_baixo == 'livre':
    print("Compressão embaixo:")
    if h*bf/(tw*Lb_baixo) > 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'> 1.7, a verificação não precisa ser feita, resiste à FLA.')
    elif h*bf/(tw*Lb_baixo) <= 1.7:
        print('h*bf/(tw*Lb)=',h*bf/(tw*Lb_baixo),'<= 1.7, precisa verificar.')
        if Msd_baixo < Mr:
            print('Msd_cima =',Msd_baixo,'< Mr=',Mr)
            Cr = 32*E
        elif Msd_cima >= Mr:
            print('Msd_baixo =',Msd_baixo,'>= Mr=',Mr)
            Cr = 16*E
        Frd_FLA_baixo = Cr*tw**3*tf*0.37*(h*bf/(tw*Lb_baixo))**3/(gamma_a1*h**2)
        if Frd_FLA_baixo >= Fbaixo_d:
            print('Frd_FLA=',Frd_FLA_baixo,'>= Fbaixo_d=',Fbaixo_d,'ok!')
        elif Frd_FLA_baixo < Fbaixo_d:
            print('Frd_FLA=',Frd_FLA_baixo,'< Fbaixo_d=',Fbaixo_d,', precisa de contenção lateral')
    print(' ')
elif (tipo_cima == 'compressao' and rotac_cima != 'livre') or tipo_cima != 'compressao':
    print('Não há compressão com rotação LIVRE, FLA livre não ocorre.')
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
    if Frd_FAC_cima >= Fcima_d:
        print('Frd_FAC=',Frd_FAC_cima,'>= Fcima_d=',Fcima_d,'ok!')
    elif Frd_FAC_cima < Fcima_d:
        print('Frd_FAC=',Frd_FAC_cima,'< Fcima_d=',Fcima_d,', precisa de enrijecedor transversal de um ou ambos os lados da alma')
    print(' ')
    print('Verificação de baixo:')
    if lap_baixo >= d/2:
        print('lap =',lap_baixo,'>= d/2 =',d/2)
        Frd_FAC_baixo = 24*tw**3*np.sqrt(E*fy)/(gamma_a1*h)
    elif lap_baixo < d/2:
        print('lap =',lap_baixo,'< d/2 =',d/2)
        Frd_FAC_baixo = 12*tw**3*np.sqrt(E*fy)/(gamma_a1*h)
    if Frd_FAC_baixo >= Fbaixo_d:
        print('Frd_FAC=',Frd_FAC_baixo,'>= Fcima_d=',Fbaixo_d,'ok!')
    elif Frd_FAC_cima < Fbaixo_d:
        print('Frd_FAC=',Frd_FAC_baixo,'< Fcima_d=',Fbaixo_d,', precisa de enrijecedor transversal de um ou ambos os lados da alma')
    print(' ')
else:
    print('Não há dupla compressão, FAC não ocorre.')
    print(' ')