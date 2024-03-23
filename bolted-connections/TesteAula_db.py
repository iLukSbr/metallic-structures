# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
print(' ')

#================================================================
#Carga solicitante
Fg = 0 #kN permanente
Fq = 617 #kN variável
gamma_g = 0 #CARGA DE 
gamma_q = 1.5 #CARGA DE USO
Fsd_calc = gamma_g*Fg + gamma_q*Fq

if Fsd_calc < 45:
    Fsd = 45 #kN
else:
    Fsd = Fsd_calc

#================================================================
#Tipos de dimensionamento (s = sim ; n = não)
espacamento = 'n'
cisalhamento = 's'
contato = 's'

#================================================================
#Propriedades e dimensões dos parafusos
#Resistência última
fub = 40 #kN/cm² parafuso tipo ISO 898-1 Classe 4.6
gamma_a2 = 1.35

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
#Propriedades e dimensões das chapas
fu = 52 #kN/cm² aço tipo AR415

#Medidas verticais
c = 4.6 #cm
g = 18.01 #cm
b = 0 #cm

#Medidas horizontais
a = 4.6 #cm
s = 12.64 #cm

#Espessuras
t1 = 1.87 #cm
t2 = 2 #cm

#N° da chapa, vide tabela da aula de ligações parafusadas
tipo_chapa = 6

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

#================================================================
#Diâmetro devido à força resistente ao contato nas chapas
if contato == 's':
    print('Diâmetros devidos à força resistente ao contato das chapas:')
    if min(n_chapas1*t1,n_chapas2*t2) == n_chapas1*t1:
        print('Limitado pela espessura da chapa 1')
        lf_lf = Fsd*gamma_a2/(Cfp*fu*t1*n_chapas1)
        db_db = Fsd*gamma_a2/(Cfp*fu*t1*n_parafusos*n_chapas1)
    elif min(n_chapas1*t1,n_chapas2*t2) == n_chapas2*t2:
        print('Limitado pela espessura da chapa 2')
        lf_lf = Fsd*gamma_a2/(Cfp*fu*t2*n_chapas2)
        db_db = Fsd*gamma_a2/(Cfp*fu*t2*n_parafusos*n_chapas2)
    print('db_db=',db_db)
#Diâmetro do furo efetivo a partir dos comprimentos de fissuração para uma chapa
    if tipo_chapa == 1:
        dfe_lf = ((2*(4*s+a) + 2*(2*s+s+a) + (2*s+a)) - lf_lf)/6.5
    elif tipo_chapa == 2:
        dfe_lf = (((2*s+s+a) + (2*s+2*s+a)) - lf_lf)/4
    elif tipo_chapa == 3:
        dfe_lf = ((2*(2*s+a) + (s+a)) - lf_lf)/3.5
    elif tipo_chapa == 4:
        dfe_lf = ((2*(s+a)) - lf_lf)/3
    elif tipo_chapa == 5:
        dfe_lf = ((2*(s+s+a) + (s+a)) - lf_lf)/5.5
    elif tipo_chapa == 6:
        dfe_lf = ((2*(s+s+a)) - lf_lf)/5
    elif tipo_chapa == 7:
        dfe_lf = ((2*(2*s+a) + (s+s+s+s+a)) - lf_lf)/5.5
    elif tipo_chapa == 8:
        dfe_lf = ((2*(s+a) + (s+s+a)) - lf_lf)/3.5
    elif tipo_chapa == 9:
        dfe_lf = ((2*(s+s+a) + (2*s+a)) - lf_lf)/6.5
    elif tipo_chapa == 10:
        dfe_lf = ((3*(s+a)) - lf_lf)/4.5
#Diâmetro do parafuso a partir da equação que usa lf
    db_lf = dfe_lf - 0.2 - 0.15
    print('db_lf=',db_lf)
#Prova real de Fcrd usando db encontrado pela equação que usa lf
    if min(n_chapas1*t1,n_chapas2*t2) == n_chapas1*t1:
        Fcrd_db1 = (Cfp*fu/gamma_a2)*t1*db_lf*n_parafusos*n_chapas1
        Fcrd1 = min(Fsd , Fcrd_db1)
    elif min(n_chapas1*t1,n_chapas2*t2) == n_chapas2*t2:
        Fcrd_db1 = (Cfp*fu/gamma_a2)*t2*db_lf*n_parafusos*n_chapas2
        Fcrd1 = min(Fsd , Fcrd_db1)
#Diâmetro do furo efetivo pela equação que usa db
    dfe_db = db_db + 0.2 + 0.15
#Comprimentos de fissuração para uma chapa
    if tipo_chapa == 1:
        lf_db = 2*(4*s+a-1.5*dfe_db) + 2*(2*s+s+a-1.5*dfe_db) + (2*s+a-0.5*dfe_db)
    elif tipo_chapa == 2:
        lf_db = (2*s+s+a-1.5*dfe_db) + (2*s+2*s+a-2.5*dfe_db)
    elif tipo_chapa == 3:
        lf_db = 2*(2*s+a-1.5*dfe_db) + (s+a-0.5*dfe_db)
    elif tipo_chapa == 4:
        lf_db = 2*(s+a-1.5*dfe_db)
    elif tipo_chapa == 5:
        lf_db = 2*(s+s+a-2.5*dfe_db) + (s+a-0.5*dfe_db)
    elif tipo_chapa == 6:
        lf_db = 2*(s+s+a-2.5*dfe_db)
    elif tipo_chapa == 7:
        lf_db = 2*(2*s+a-0.5*dfe_db) + (s+s+s+s+a-4.5*dfe_db)
    elif tipo_chapa == 8:
        lf_db = 2*(s+a-0.5*dfe_db) + (s+s+a-2.5*dfe_db)
    elif tipo_chapa == 9:
        lf_db = 2*(s+s+a-2.5*dfe_db) + (2*s+a-1.5*dfe_db)
    elif tipo_chapa == 10:
        lf_db = 3*(s+a-1.5*dfe_db)
#Prova real de Fcrd usando lf encontrado pela equação que usa db
    if min(n_chapas1*t1,n_chapas2*t2) == n_chapas1*t1:
        Fcrd_lf2 = (Cpl*fu/gamma_a2)*t1*lf_db*n_chapas1
        Fcrd2 = min(Fcrd_lf2 , Fsd)
    elif min(n_chapas1*t1,n_chapas2*t2) == n_chapas2*t2:
        Fcrd_lf2 = (Cpl*fu/gamma_a2)*t2*lf_db*n_chapas2
        Fcrd2 = min(Fcrd_lf2 , Fsd)
    print('Fcrd com db_lf=',Fcrd1)
    print('Fcrd com db_db=',Fcrd2)
    if Fcrd1 >= Fsd and Fcrd1 == Fcrd2:
        print('Como os Fcrd são iguais e respeitam Fsd, uso o menor db possível')
        db_c = min(db_lf,db_db)
    elif Fcrd1 >= Fsd and Fcrd1 < Fcrd2:
        print('Fcrd com db_lf <= Fcrd com db_db e respeita Fsd')
        db_c = db_lf
    elif Fcrd2 >= Fsd and Fcrd2 < Fcrd1:
        print('Fcrd com db_db <= Fcrd com db_lf e respeita Fsd')
        db_c = db_db
    elif Fcrd1 < Fsd and Fcrd2 < Fsd:
        print('Fcrd com db_db e Fcrd com db_lf não respeitam Fsd, recalculando')
#Diâmetros a partir da igualdade entre Fcrd_lf e Fcrd_db para uma chapa
        if tipo_chapa == 1:
            db_c = (2*(4*s+a) + 2*(2*s+s+a) + (2*s+a) - 6.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 6.5)
        elif tipo_chapa == 2:
            db_c = ((2*s+s+a) + (2*s+2*s+a) - 4*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 4)
        elif tipo_chapa == 3:
            db_c = (2*(2*s+a) + (s+a) - 3.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 3.5)
        elif tipo_chapa == 4:
            db_c = (2*(s+a) - 3*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 3)
        elif tipo_chapa == 5:
            db_c = (2*(s+s+a) + (s+a) - 5.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 5.5)
        elif tipo_chapa == 6:
            db_c = (2*(s+s+a) - 5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 5)
        elif tipo_chapa == 7:
            db_c = (2*(2*s+a) + (s+s+s+s+a) - 5.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 5.5)
        elif tipo_chapa == 8:
            db_c = (2*(s+a) + (s+s+a) - 3.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 3.5)
        elif tipo_chapa == 9:
            db_c = (2*(s+s+a) + (2*s+a) - 6.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 6.5)
        elif tipo_chapa == 10:
            db_c = (3*(s+a) - 4.5*(0.2 + 0.15))/(Cfp*n_parafusos/Cpl + 4.5)
    print('db do contato=',db_c)
    print(' ')

#================================================================
#Diâmetro devido à força resistente ao cisalhamento nos parafusos
if cisalhamento == 's':
    print('Diâmetro devido à força resistente ao cisalhamento nos parafusos:')
    db_v = 2*np.sqrt(Fsd*gamma_a2/(Cpc*np.pi*fub*n_parafusos*n_planoscorte))
    print('db do cisalhamento=',db_v)
    print(' ')

#================================================================
#Diâmetro mínimo para atender a todas as resistências
if contato == 's' and cisalhamento == 's':
    db = max(db_c,db_v)
    print
elif contato == 's' and cisalhamento == 'n':
    db = db_c
elif contato == 'n' and cisalhamento == 's':
    db = db_v
print('Maior db encontrado=',db)
print(' ')

#================================================================
#Diâmetro devido a caso especial de resistência = ao cisalhamento nos parafusos
if lpega > 5*db and cisalhamento == 's':
    print('lpega=',lpega,'> 5*db=',5*db,'caso especial de ligação espessa:')
    db_v = 0
    while True:
        db_v = db_v + 0.0001
        buff = 0.05*db_v**3 + (0.15 - 0.01*lpega)*db_v**2 - 0.6*Fsd*gamma_a2/(n_parafusos*n_planoscorte*fub*np.pi*Cpc)
        if not ((buff >= 0.0001 and buff <= 10000) or (buff <= -0.0001 and buff >= -10000)):
            break
    print('Novo db do cisalhamento=',db_v)
    if contato == 's' and cisalhamento == 's':
        db = max(db_c,db_v)
    elif contato == 'n' and cisalhamento == 's':
        db = db_v
    print('Novo maior db encontrado=',db)
    print(' ')

#Tabela dos diâmetros comerciais
if db <= 1.6:
    db_tabela = 1.6 #cm
elif db <= 2:
    db_tabela = 2 #cm
elif db <= 2.2:
    db_tabela = 2.2 #cm
elif db <= 2.4:
    db_tabela = 2.4 #cm
elif db <= 2.7:
    db_tabela = 2.7 #cm
elif db <= 3:
    db_tabela = 3 #cm
elif db <= 3.6:
    db_tabela = 3.6 #cm
elif db > 3.6:
    db_tabela = round(db,1) #cm
print('Diâmetro dos parafusos encontrado: db=',db_tabela)
dfe = db_tabela + 0.2 + 0.15
print(' ')
print('Diâmetro dos furos efetivo encontrado: dfe=',dfe)
print(' ')

#================================================================
#Verificação dos espaçamentos mínimos e máximos dos furos
if espacamento == 's':

#Distância mínima entre borda da chapa e do furo, tabelada, para diâmetro do parafuso até abaixo daquele db
    beta = 0
    db_tabela = db_tabela*(1 + beta) #cm

#Exposto à corrosão atmosférica? [s = sim ; n = não]
    corrosao = 'n'

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

#Verificação da distância entre início da borda do primeiro e o término da do último furo
if tipo_chapa == 1 or tipo_chapa == 2 or tipo_chapa == 7:
    lc = 4*s + dfe #cm
elif tipo_chapa==3 or tipo_chapa==5 or tipo_chapa==6 or tipo_chapa==8 or tipo_chapa==9:
    lc = 2*s + dfe
elif tipo_chapa == 4 or tipo_chapa == 10:
    lc = s + dfe

if lc > 127:
    Fsd = 1.25*Fsd_calc
    print('Caso especial de ligação comprida, lc=',lc,'>127, recalcular com 1,25*Fsd')