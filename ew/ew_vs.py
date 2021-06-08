# 
#  _______        __ __     ______  
# | ____\ \      / / \ \   / / ___| 
# |  _|  \ \ /\ / /   \ \ / /\___ \ 
# | |___  \ V  V /     \ V /  ___) |
# |_____|  \_/\_/       \_/  |____/ 
# 
# 

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################

import ew_fx as fx
# import ew_in_kostra as kostra
#  
# import math as mt
# import numpy as np
import pandas as pd
#import simpy as sp

import matplotlib.pyplot as plt

#######################################
#  
# Flächenversickerung 
#  
#######################################

## Grunddaten

# örtliche Regenspendedaten
LOCAL_RS = pd.read_csv('local_rs.csv', index_col='Regendauer') 

rs_005 = LOCAL_RS[['HN_005A']]
rs_100 = LOCAL_RS[['HN_100A']]

'''
print(rs_005)
print(rs_005.loc[5, 'HN_005A'])
print(LOCAL_RS)
print(rs_100)
print()

print(r_Dn)
print()

'''
## Zufluss

A_u = 858.23       # m2
A_u_Form = 'A_u = ' + str(A_u) + ' m^2'


r_Dn = rs_005.loc[5, 'HN_005A']     # l/(s*ha)
r_Dn_Form = 'r_Dn = ' + str(r_Dn) + ' l/(s*ha)'

Q_zu = fx.vs_q_zu(A_u, r_Dn)
Q_zu_Form = 'Q_zu = A_u * r_Dn * 1e-7 = ' + str(fx.normal_form(Q_zu)) + ' m^3/s' 

rs_005['Q_zu'] = fx.vs_q_zu(A_u, rs_005['HN_005A'])





'''

print(rs_005)
print(A_u_Form)
A_u_Form
r_Dn_Form
Q_zu_Form
'''

## Versickerung

A_s = 500    # m2
A_s_Form = 'A_s = ' + str(A_s) + ' m^2'

k_f = 0.00001   # m/s
k_f_Form = 'k_f = ' + str(k_f) + ' m/s'

Q_s = fx.vs_q_s(A_s, k_f)
Q_s_Form = 'Q_S = A_s * k_f / 2 = ' + str(fx.normal_form(Q_s)) + ' m^3/s'

rs_005['Q_s'] = Q_s


print(rs_005)


'''
A_s_Form
k_f_Form
Q_s_Form
'''

## Konklusion

concl_fl_vs_form = str(fx.normal_form(Q_zu)) + ' l/m^3 < ' + str(fx.normal_form(Q_s)) + ' l/m^3'

## Graph

rs_005.loc[:, 'Q_zu':'Q_s'].plot()
# plt.show()
plt.savefig('ew_ex/ew_vs_flvs.png', format = 'png')

'''
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
'''

 
#######################################
#  
#  Mulde
#  
#######################################

#######################################
#  
#  Rigole
#  
#######################################
