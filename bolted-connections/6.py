# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
print(' ')

#================================================================
#Carga solicitante
Fg = 101 #kN permanente
Fq = 0 #kN variável
gamma_g = 1.3 #CARGA DE PESO PRÓPRIO DE ESTRUTURA PRÉ-MOLDADA
gamma_q = 0 #CARGA DE 
Fsd_calc = gamma_g*Fg + gamma_q*Fq

if Fsd_calc < 45:
    Fsd = 45 #kN
else:
    Fsd = Fsd_calc

#================================================================
#Tipos de dimensionamento (s = sim ; n = não)
acharN = 'n'
espacamento = 'n'
cisalhamento = 's'
contato = 's'

#================================================================
#Propriedades e dimensões dos parafusos
#Resistência última
fub = 41.5 #kN/cm² parafuso tipo ASTM A307
gamma_a2 = 1.35
#Diâmetro do parafuso
db = 2.2 #cm
#Área da seção transversal do parafuso
Ab = np.pi*db**2/4 #cm²

#================================================================
#Parâmetro para dimensionamento ao cisalhamento dos parafusos
#~~~~~~~~~~~
#Coeficiente
#Parafusos tipo AR: ASTM A325, ISO-4016 Classe 8.8, ASTM A490 e ISO-4016 Classe 10.9
#Parafusos comuns: ASTM A307 e ISO 898-1 Classe 4.6
#Parafuso AR com corte na rosca ou parafuso comum: Cpc=0,4
#Parafuso AR com corte no fuste: Cpc=0,5
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Cpc = 0.4 #COMUM

#================================================================
#Dimensões dos furos
#Diâmetro
df = db + 0.15 #cm
dfe = df + 0.2 #cm

#================================================================
#Propriedades e dimensões das chapas
fu = 42.7 #kN/cm² aço tipo A500

#Medidas verticais
c = 2.9 #cm
g = 7.65 #cm
b = 0 #cm

#Medidas horizontais
a = 2.9 #cm
s = 8.03 #cm

#Espessuras
t1 = 1.72 #cm
t2 = 0.4 #cm

#N° da chapa, vide tabela da aula de ligações parafusadas
tipo_chapa = 9

#N° de furos (parafusos)
if tipo_chapa == 1:
    n_parafusos = 9
elif tipo_chapa == 2 or tipo_chapa == 3 or tipo_chapa == 8:
    n_parafusos = 5
elif tipo_chapa == 4:
    n_parafusos = 4
elif tipo_chapa == 5 or tipo_chapa == 7:
    n_parafusos = 7
elif tipo_chapa == 6 or tipo_chapa == 10:
    n_parafusos = 6
elif tipo_chapa == 9:
    n_parafusos = 8

#N° de chapas por tipo 
if tipo_chapa == 1 or tipo_chapa == 3 or tipo_chapa == 7 or tipo_chapa == 10:
    n_chapas1 = 1
    n_chapas2 = 1
elif tipo_chapa == 2 or tipo_chapa == 8:
    n_chapas1 = 2
    n_chapas2 = 1
elif tipo_chapa == 4 or tipo_chapa == 9:
    n_chapas1 = 1
    n_chapas2 = 2
elif tipo_chapa == 5:
    n_chapas1 = 2
    n_chapas2 = 3
elif tipo_chapa == 6:
    n_chapas1 = 2
    n_chapas2 = 2

#N° de planos de corte entre chapas
if tipo_chapa == 1 or tipo_chapa == 3 or tipo_chapa == 7 or tipo_chapa == 10:
    n_planoscorte = 1
elif tipo_chapa == 2 or tipo_chapa == 4 or tipo_chapa == 8 or tipo_chapa == 9:
    n_planoscorte = 2
elif tipo_chapa == 5:
    n_planoscorte = 4
elif tipo_chapa == 6:
    n_planoscorte = 3

#Comprimento do fuste dentro das chapas (espessura total das chapas combinadas)
lpega = n_chapas1*t1 + n_chapas2*t2 #cm

#Distância entre início da borda do primeiro e o término da do último furo
if tipo_chapa == 1 or tipo_chapa == 2 or tipo_chapa == 7:
    lc = 4*s + dfe #cm
elif tipo_chapa==3 or tipo_chapa==5 or tipo_chapa==6 or tipo_chapa==8 or tipo_chapa==9:
    lc = 2*s + dfe
elif tipo_chapa == 4 or tipo_chapa == 10:
    lc = s + dfe

if lc > 127:
    Fsd = 1.25*Fsd_calc

#================================================================
#Parâmetros para dimensionamento por contato nas chapas
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Limitações da pressão de contato
#Limitado para forças de serviço: Cpl=1,2 e Cfp=2,4
#Não limitado para forças de serviço: Cpl=1,5 e Cfp = 3
#Furos muito alongados na direção perpendicular à força: Cpl=1 e Cfp=2
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if contato == 's':
    Cpl = 1.5 #NÃO LIMITADO PARA SERVIÇO
    Cfp = 3
    #Comprimentos de fissuração para uma chapa
    if tipo_chapa == 1:
        lf = 2*(4*s+a-1.5*dfe) + 2*(2*s+s+a-1.5*dfe) + (2*s+a-0.5*dfe)
    elif tipo_chapa == 2:
        lf = (2*s+s+a-1.5*dfe) + (2*s+2*s+a-2.5*dfe)
    elif tipo_chapa == 3:
        lf = 2*(2*s+a-1.5*dfe) + (s+a-0.5*dfe)
    elif tipo_chapa == 4:
        lf = 2*(s+a-1.5*dfe)
    elif tipo_chapa == 5:
        lf = 2*(s+s+a-2.5*dfe) + (s+a-0.5*dfe)
    elif tipo_chapa == 6:
        lf = 2*(s+s+a-2.5*dfe)
    elif tipo_chapa == 7:
        lf = 2*(2*s+a-0.5*dfe) + (s+s+s+s+a-4.5*dfe)
    elif tipo_chapa == 8:
        lf = 2*(s+a-0.5*dfe) + (s+s+a-2.5*dfe)
    elif tipo_chapa == 9:
        lf = 2*(s+s+a-2.5*dfe) + (2*s+a-1.5*dfe)
    elif tipo_chapa == 10:
        lf = 3*(s+a-1.5*dfe)

#================================================================
#Verificação dos espaçamentos mínimos e máximos dos furos
if espacamento == 's':
#Exposto à corrosão atmosférica? [s = sim ; n = não]
    corrosao = 'n'
#Distância mínima entre borda da chapa e do furo, tabelada, para diâmetro do parafuso até abaixo daquele db
    beta = 0
    db_tabela = db*(1 + beta) #cm
#~~~~~~~~~~~~~~~~~~~~~~~
#Tipo de corte dos furos
#Borda cortada com serra ou tesoura = impreciso
#Borda laminada ou cortada a maçarico = preciso
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    tipo_corte = 'impreciso'

#Tabela das distâncias mínimas
    if tipo_corte == 'impreciso':
        if db_tabela <= 1.6:
            dmin = 2.9 #cm
        elif db_tabela <= 2:
            dmin = 3.5 #cm
        elif db_tabela <= 2.2:
            dmin = 3.8 #cm
        elif db_tabela <= 2.4:
            dmin = 4.2 #cm
        elif db_tabela <= 2.7:
            dmin = 5 #cm
        elif db_tabela <= 3:
            dmin = 5.3 #cm
        elif db_tabela <= 3.6:
            dmin = 6.4 #cm
        elif db_tabela > 3.6:
            dmin = 1.75*db_tabela #cm
    elif tipo_corte == 'preciso':
        if db_tabela <= 1.6:
            dmin = 2.2 #cm
        elif db_tabela <= 2:
            dmin = 2.7 #cm
        elif db_tabela <= 2.2:
            dmin = 2.9 #cm
        elif db_tabela <= 2.4:
            dmin = 3.1 #cm
        elif db_tabela <= 2.7:
            dmin = 3.8 #cm
        elif db_tabela <= 3:
            dmin = 3.9 #cm
        elif db_tabela <= 3.6:
            dmin = 4.6 #cm
        elif db_tabela > 3.6:
            dmin = 1.25*db_tabela #cm

#Espaçamento entre bordas internas dos furos
    if tipo_chapa == 1:
        menoresp = min(2*s,2*g,np.sqrt(s**2 + g**2)) - dfe
    elif tipo_chapa == 2:
        menoresp = min(2*s,np.sqrt(s**2 + g**2)) - dfe
    elif tipo_chapa == 3:
        menoresp = min(2*s,2*g,np.sqrt(s**2 + g**2)) - dfe
    elif tipo_chapa >= 4 and tipo_chapa <= 10:
        menoresp = min(s,g) - dfe

    print('Espaçamento entre bordas internas dos furos')
    if menoresp >= db:
        print('lf_interno=',menoresp,'>= db=',db,', espaçamento entre furos atende ao mínimo.')
    else:
        print('lf_interno=',menoresp,'< db=',db,', espaçamento entre furos NÃO atende ao mínimo.')
    print(' ')

#Espaçamento entre borda da chapa e borda externa do furo
#Menor distância entre borda do furo e borda da chapa
    dext = min(a,c) #cm

    print('Espaçamento entre borda da chapa e borda externa do furo')
    #Chapa tipo 1:
    print('Chapa tipo 1:')
    if dext <= min(12*t1,15) and dext >= dmin:
        if 12*t1 <= 15:
            print('dmin=',dmin,'<= dexterna1=',dext,'<= 12*t1=',12*t1,', espaçamento entre borda da chapa e borda do furo atende ao mínimo e máximo')
        else:
            print('dmin=',dmin,'<= dexterna1=',dext,'<= 15, espaçamento entre borda da chapa e borda do furo atende ao mínimo e máximo')
    elif 15 <= 12*t1 and dext >= dmin:
        print('dexterna1=',dext,'> 1,5, espaçamento entre borda da chapa e borda do furo NÃO atende ao máximo')
    elif 12*t1 < 15 and dext >= dmin:
        print('dexterna1=',dext,'> 12*t1=',12*t1,', espaçamento entre borda da chapa e borda do furo NÃO atende ao máximo')
    else:
        print('dexterna1=',dext,'< dmin=',dmin,', NÃO atende ao mínimo')
    print(' ')

#Parâmetros de espaçamento máximo entre eixos
    print('Parâmetros de espaçamento máximo entre eixos')
#Espessura mínima
    tmin = min(t1,t2)
    if t1 < t2:
        print('tmin = t1=',t1)
    else:
        print('tmin = t2=',t2)
    print(' ')
#Exposição à corrosão atmosférica
    if corrosao == 's':
        dmax = min(14*tmin,18)
        if 14*tmin < 18:
            print('dmax = 14*tmin=',14*tmin)
        else:
            print('dmax = 18')
    else:
        if 14*tmin < 1.8:
            print('dmax = 24*tmin=',24*tmin)
        else:
            print('dmax = 30')
        dmax = min(24*tmin,30)
    print(' ')

#Menor espaçamento entre eixos dos furos
    menordeixo = menoresp + dfe

#Maior espaçamento entre eixos dos furos
    if tipo_chapa == 1:
        maiordeixo = max(4*s,4*g)
    elif tipo_chapa == 2:
        maiordeixo = np.sqrt((3*s)**2 + g**2)
    elif tipo_chapa == 3:
        maiordeixo = max(2*s,2*g,np.sqrt(s**2 + g**2))
    elif tipo_chapa == 4 or tipo_chapa == 8:
        maiordeixo = np.sqrt(s**2 + g **2)
    elif tipo_chapa == 5 or tipo_chapa == 10:
        maiordeixo = np.sqrt(s**2 + (2*g)**2)
    elif tipo_chapa == 6 or tipo_chapa == 7:
        maiordeixo = np.sqrt((2*s)**2 + g**2)
    elif tipo_chapa == 9:
        maiordeixo = np.sqrt((2*s)**2 + (2*g)**2)

#Verificação do espaçamento entre eixos dos furos
    print('Espaçamento entre eixos dos furos')
    if menordeixo >= 3*db and menordeixo <= dmax:
        print('menordeixo=',menordeixo,'>= 3*db=',3*db,', entre eixos dos furos atende ao mínimo')
    elif menordeixo < 3*db:
        print('menordeixo=',menordeixo,'< 3*db=',3*db,', entre eixos dos furos NÃO atende ao mínimo.')
    if maiordeixo <= dmax:
        print('maiordeixo=',maiordeixo,'<= dmax=',dmax,', entre eixos dos furos atende ao máximo')
    elif maiordeixo > dmax:
        print('maiordeixo=',maiordeixo,'> dmáximo=',dmax,', entre eixos dos furos NÃO atende ao máximo.')
    print(' ')

#================================================================
#Força resistente ao cisalhamento nos parafusos
if cisalhamento == 's':
    print('Força resistente de cisalhamento dos parafusos:')
    Fvrd_calc = Cpc*Ab*fub*n_parafusos*n_planoscorte/gamma_a2
    if lpega > 5*db:
        print('lpega=',lpega,'> 5*db=',5*db)
        Fvrd = (1 - 0.01*(lpega - 5*db)/0.15)*Fvrd_calc
    else:
        Fvrd = Fvrd_calc
    if Fvrd >= Fsd and acharN == 'n':
        print('Fvrd=',Fvrd,'>= Fsd=',Fsd,'resiste ao cisalhamento!')
    elif acharN == 'n':
        print('Fvrd=',Fvrd,'< Fsd=',Fsd,'NÃO resiste ao cisalhamento!')
print(' ')

#================================================================
#Força resistente ao contato nas chapas
if contato == 's':
    print('Força resistente ao contato das chapas:')
    if min(n_chapas1*t1,n_chapas2*t2) == n_chapas1*t1:
        print('Espessura limitada pela chapa tipo 1,',n_chapas1,'*espessura',t1,':')
        Fcrd_lf = (Cpl*fu/gamma_a2)*t1*lf*n_chapas1
        Fcrd_db = (Cfp*fu/gamma_a2)*t1*db*n_parafusos*n_chapas1
        Fcrd = min(Fcrd_lf , Fcrd_db)
    elif min(n_chapas1*t1,n_chapas2*t2) == n_chapas2*t2:
        print('Espessura limitada pela chapa tipo 2,',n_chapas2,'*espessura',t2,':')
        Fcrd_lf = (Cpl*fu/gamma_a2)*t2*lf*n_chapas2
        Fcrd_db = (Cfp*fu/gamma_a2)*t2*db*n_parafusos*n_chapas2
        Fcrd = min(Fcrd_lf , Fcrd_db)
    if Fcrd >= Fsd and acharN == 'n':
        print('Fcrd=',Fcrd,'>= Fsd=',Fsd,'resiste ao contato!')
    elif acharN == 'n':
        print('Fcrd=',Fcrd,'< Fsd=',Fsd,'NÃO resiste ao contato!')
    print(' ')

#================================================================
#Verificação da menor resistência
#Chapa tipo 1
Frd = min(Fvrd,Fcrd)
print('Resistência da ligação parafusada:')
print('Frd=',Frd)
if min(Fvrd,Fcrd) == Fvrd:
    print('Limitada pelo cisalhamento dos parafusos.')
elif min(Fvrd,Fcrd) == Fcrd:
    print('Limitada pelo contato das chapas.')
print(' ')

#================================================================
#Maior força característica possível de se aplicar
if acharN == 's':
    gammaN = max(gamma_g,gamma_q)
    if lc > 127:
        print('Caso especial de ligação comprida, lc=',lc,'> 127')
        Fk = Frd/(1.25*gammaN)
    else:
        Fk = Frd/gammaN
    print('Suportaria até a força característica máxima Nk=',Fk)
    print(' ')