# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

#Propriedades do aço do PERFIL
fy = 25 #kN/cm² aço tipo ASTM A36
fu = 40 #kN/cm²

#Carga cortante
Fg = 0 #kN permanente
Fq = 0 #kN variável
gamma_g = 0 #CARGA DE 
gamma_q = 0 #CARGA DE 
Fsd_calc = gamma_g*Fg + gamma_q*Fq
if Fsd_calc < 4.5:
    Fsd = 4.5 #kN
else:
    Fsd = Fsd_calc

#Tipos de solicitação (s = sim ; n = não)
cortante = 's'
tracao = 'n'
contato = 's'
rasgamento = 's'
alavanca = 'n'

#Parafusos
#Resistência última
fub = 41.5 #kN/cm² parafuso tipo ASTM A307
gamma_a2 = 1.35
#Diâmetro do parafuso
db = 1.27 #cm
#Área da seção transversal do parafuso
Ab = np.pi*db**2/4 #cm²
#N° de parafusos
n_parafusos = 2
#N° de planos de corte
n_planoscorte = 1

#Furos
df = db + 0.15 #cm
dfe = df + 0.2 #cm

#Chapas, MODIFICAR DE ACORDO COM DESENHO
t1 = 0.63 #cm
t2 = 0.6 #cm
#Comprimento do fuste dentro das chapas
lpega = t1 + t2 #cm
#Distância entre bordas do primeiro e último furos
lc = 3 + dfe #cm
#N° de chapas tipo 1
n_chapas1 = 1
#N° de chapas tipo 2
n_chapas2 = 2

#Parâmetros para dimensionamento por contato na chapa
#Limitações para FORÇAS DE SERVIÇO
Cpl = 1.2
Cfp = 2.4
#Comprimentos de fissuração
#Distância reta da borda do furo à borda da chapa
lf_borda = 2.5 - dfe/2 #cm VER DESENHO
#Distância reta da borda de um furo à borda de outro furo
lf_interno = 3 - dfe #cm VER DESENHO

#Parâmetro para dimensionamento ao cisalhamento dos parafusos
#Coeficiente de parafuso COMUM
Cpc = 0.4 #COMUM

#Para rasgamento:
#Coeficiente de tensão de rasgamento CONSTANTE
Cts = 1

#Área líquida sujeita à tração (medida transversal à carga)
Ant1 = (3.59 - dfe/2)*t1*n_chapas1 #cm² VER DESENHO
Ant2 = 0 #cm² VER DESENHO

#Área bruta sujeita ao cisalhamento (medida paralela à carga)
Agv1 = (3 + 2.5)*t1*n_chapas1 #cm² VER DESENHO
Agv2 = 0 #cm² VER DESENHO

#Área líquida sujeita ao cisalhamento (medida paralela à carga)
Anv1 = Agv1 - 1.5*dfe*t1*n_chapas1 #cm² VER DESENHO
Anv2 = 0 #cm² VER DESENHO

#Força resistente de cisalhamento
if cortante == 's':
    print('Força resistente de cisalhamento dos parafusos:')
    Fvrd1 = Cpc*Ab*fub/gamma_a2
    Fvrd_calc = n_parafusos*n_planoscorte*Fvrd1
    if lpega > 5*db:
        print('lpega=',lpega,'> 5*db=',5*db)
        Fvrd = (1-0.01*(lpega - 5*db)/0.15)*Fvrd_calc
    else:
        Fvrd = Fvrd_calc
    if lc > 127:
        Fsd = 1.25*Fsd_calc
    if Fvrd >= Fsd:
        print('Fvrd=',Fvrd,'>= Fsd=',Fsd,'resiste ao cisalhamento!')
    else:
        print('Fvrd=',Fvrd,'< Fsd=',Fsd,'NÃO resiste ao cisalhamento!')
    print(' ')

if contato == 's':
    print('Força resistente ao contato das chapas:')
#Força resistente de contato, CHAPA 1 interna
    print('Chapa tipo 1, interna:')
    Fcrda = (Cpl*fu/gamma_a2)*t1*(n_parafusos/2)*lf
    Fcrdb = (Cfp*fu/gamma_a2)*t1*n_parafusos*db
    Fcrd1 = n_chapas1*min(Fcrda , Fcrdb)
    if Fcrd1 >= Fsd:
        print('Fcrd=',Fcrd1,'>= Fsd=',Fsd,'resiste ao contato!')
    else:
        print('Fcrd=',Fcrd1,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    print(' ')

#Força resistente de contato, CHAPA 2 externa
    # print('Chapa tipo 2, externa:')
    # Fcrdc = (Cpl*fu/gamma_a2)*t2*(n_parafusos/2)*(lf_borda + lf_interno)
    # Fcrdd = (Cfp*fu/gamma_a2)*t2*n_parafusos*db
    # Fcrd2 = n_chapas2*min(Fcrdc , Fcrdd)
    # if Fcrd2 >= Fsd:
    #     print('Fcrd=',Fcrd2,'>= Fsd=',Fsd,'resiste ao contato!')
    # else:
    #     print('Fcrd=',Fcrd2,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    # print(' ')

#Força resistente ao rasgamento
if rasgamento == 's':
    print('Força resistente ao rasgamento das chapas:')
    print('Chapa tipo 1, interna:')
    Frrd1_1 = (0.6*fu*Anv1 + Cts*fu*Ant1)/gamma_a2
    Frrd2_1 = (0.6*fy*Agv1 + Cts*fu*Ant1)/gamma_a2
    Frrd_1 = min(Frrd1_1,Frrd2_1)
    if Frrd_1 >= Fsd:
        print('Frrd=',Frrd_1,'>= Fsd=',Fsd,'resiste ao contato!')
    else:
        print('Frrd=',Frrd_1,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    print(' ')
    # print('Chapa tipo 2, externa:')
    # Frrd1_2 = (0.6*fu*Anv2 + Cts*fu*Ant2)/gamma_a2
    # Frrd2_2 = (0.6*fy*Agv2 + Cts*fu*Ant2)/gamma_a2
    # Frrd_2 = min(Frrd1_2,Frrd2_2)
    # if Frrd_2 >= Fsd:
    #     print('Frrd=',Frrd_2,'>= Fsd=',Fsd,'resiste ao contato!')
    # else:
    #     print('Frrd=',Frrd_2,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    # print(' ')

#Tração
# if tracao == 's':
#     Ftrd = 0.75*Ab*fub/gamma_a2
#     if Ftrd >= Fsd:
#         print('Ftrd=',Ftrd,'>= Fsd=',Fsd,'resiste ao contato!')
#     else:
#         print('Ftrd=',Ftrd,'< Fsd=',Fsd,'NÃO resiste ao contato!')
#     print(' ')

#Alavanca
# if alavanca == 's':
#     b = 0
#     a = 0
#     Ae = 0
#     Ag = 0
#     delta = Ae/Ag
#     Fsd = Fsd_calc*(1 + alfa*delta*b/((1+alfa*delta)*a)

Frd = n_chapas2*min(Fvrd,Fcrd1,Frrd_1)
print('Frd=',Frd)
if min(Fvrd,Fcrd1,Frrd_1) == Fvrd:
    print('Resistência limitada pelo cisalhamento dos parafusos.')
elif min(Fvrd,Fcrd1,Frrd_1) == Fcrd1:
    print('Resistência limitada pelo contato das chapas.')
elif min(Fvrd,Fcrd1,Frrd_1) == Frrd_1:
    print('Resistência limitada pelo rasgamento das chapas.')