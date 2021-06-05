## Import
import ewfx as ew
import pandas as pd
import numpy as np
import math as mt
from decimal import *

##
##
A_u = 858.23       # m2
r_Dn = 40.14     # l/(s*ha)

Q_zu = A_u * r_Dn * 1e-7 

print(ew.normal_form(Q_zu))
##

A_s = 50    # m2
k_f = 0.00001   # m/s

Q_s = A_s * k_f / 2

ew.normal_form(Q_s)
##

'''
Q_zu	m3/s	Zulässiger Schmutzwasserabfluss	10^-7 * 
r_Dn	l/sxha	Regenspende	NaN
A_E	m2	Einzugsgebietsfläche [m2]
A_u	m2	Rechenwert undurchlässige Fläche [m2]
f_A	NaN	Abminderungsfaktor nach DWA-A 117 [−]
f_Z	NaN	Zuschlagfaktor nach DWA-A 117 [−]
Ihy	m/m	Hydraulisches Gefälle [m/m]
IR	m	Rigolenlänge [m]
k_f	m/s	Durchlässigkeitsbeitwert   der   gesättigtenZone [m/s]
n	1/a	Häufigkeit [1/a]
q_s	m3/(s·ha)	spezifische Versickerungsrate [m3/(s·ha)]
Q_zu	m3/s	Zufluss zur Versickerungsanlage [m3/s]
r_Dn	l/(sxha)	Regenspende   der   DauerDund   derHäufigkeitn[l/(s·ha)]
sRR	NaN	Speicherkoeffizent der (Rohr-)Rigole [−]
vs	m/s	Filtergeschwindigkeit der gesätigten Zone[m/s]
z	a	Jährlichkeit  oder  Wiederkehrzeit,  auchTn[a]
Ψ	NaN	mmittlerer Abflussbeiwert [−]
'''

##
'''
list = [0, 1, 2, 3]

# print(len(list))

nan_val = []

for a in range(len(list)):
    nan_val.append(np.nan) 

print(nan_val)
'''


##



## Functions ####################################

'''
sw_input = open('ew_prj/0001_sw_input', 'r') 

sorlista = []
count = 0

for line in sw_input:
    if line.strip() == '':
        print('Hopp, egy üres sor!!!')
    else:
        sorlista.append(line.strip())


sorlista

#    print("Line{}: {}".format(count, line.strip())) 

##


# x = get_loc(df, 'DU', 0)
# print(x)
# print(type(x))

## 1 sor dekódolása #############################


lista = []
szam_sor = '123456789abcdefghijklmnopqrstuvwxyz'
fall_sor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sor = sorlista[2]
sor

##

szam = ''
sanyters = []

for i in sor:
    if i == '/':
        print('csatlakozás')
        #break
    elif i == 'C':
        sanyters.append('WC')
    elif i == 'T':
        sanyters.append('WT')
    elif i == 'D':
        sanyters.append('DU')
    elif i == 'M':
        sanyters.append('WM')
    else:
        szam += i
    
szam

##

sanyters

##
szamsor[15]

##
sor1 = '1Actdm'
##
lista.append(sor1[0])
lista
##
sor[1]
lista
##
sor[2]
lista
##


'''

## DF ###########################################

head = ['DU', 'Qw', 'DN', 'J', 'n/n']
#nan_val = [np.nan, np.nan, np.nan, np.nan, np.nan]

#df = pd.DataFrame([0], columns=['DU'], index=['1'])
df = pd.DataFrame([], columns=head)
print(df)
print()

'''
df.loc[0] = [1, 2, 3, 4, 5]
df.loc[1] = [1, 2, 3, 4, 5]
df.loc[3] = [1, 2, 3, 4, 5]
df.loc[11] = [1, 2, 3, 4, 5]
df.loc[21] = [1, 2, 3, 4, 5]
df.loc[2] = [1, 2, 3, 4, 5]

df.loc['0'] = [1, 2, 3, 4, 5]
df.loc['1'] = [1, 2, 3, 4, 5]
df.loc['3'] = [1, 2, 3, 4, 5]
df.loc['11'] = [1, 2, 3, 4, 5]
df.loc['21'] = [1, 2, 3, 4, 5]
df.loc['2'] = [1, 2, 3, 4, 5]

'''
nan_val = []
for a in range(len(head)):
    nan_val.append(np.nan) 


print(nan_val)

df.loc['0'] = [1, 2, 3, 4, 5]

df.loc[ew.son(0)] = [1, 2, 3, 4, 5]
df.loc[ew.bro(0)] = nan_val 
df.loc[ew.son(ew.lastindex(df))] = nan_val
df.loc[ew.bro(ew.lastindex(df))] = nan_val
df.loc[ew.son(ew.lastindex(df))] = nan_val
df.loc[ew.bro(ew.lastindex(df))] = nan_val

print(df)

add_bro('01')

#df.loc[ew.son(ew.lastindex(df))] = pd.DataFrame(columns=head)


##
'''
print(ew.lastindex(df))
print()

print(type(ew.lastindex(df)))
'''

#################################################


df_i = pd.DataFrame([12], columns=['DU'], i:ndex=[lastindex(df)+1])
print(df_i)
print()

df = pd.concat([df, df_i])


print(df)
print()


print(lastindex(df))
print()

print(type(lastindex(df)))

#################################################


df_i = pd.DataFrame([9], columns=['DU'], index=[int(str(lastindex(df))+'1')])
print(df_i)
print()

df = pd.concat([df, df_i])


print(df)
print()


print(lastindex(df))
print()

print(type(lastindex(df)))
# df_b = 

#################################################






