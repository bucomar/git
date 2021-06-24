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
import ew_prj as prj
# import ew_in_kostra as kostra
#  
# import math as mt
# import numpy as np
import pandas as pd
#import simpy as sp

import matplotlib.pyplot as plt

## Grunddaten

# örtliche Regenspendedaten
LOCAL_RS = pd.read_csv(f'ew_ex/{prj.I_RC}_local_rs.csv', index_col='Regendauer') 
print(LOCAL_RS.loc[:, ('2', '5', '30', '100')])

'''
rs_005 = LOCAL_RS[['5']]
rs_100 = LOCAL_RS[['100']]

print(rs_005)
print(rs_100)
print(rs_005.loc[5, '5'])
print()

print(r_Dn)
print()
'''

## Zufluss

A_u = 858.23       # m2
#A_u_Form = f'A{fx.get_sub("u")} = {A_u} m{fx.get_super("2")}'
A_u_Form = f'A_u = {A_u} m^2'


r_Dn = LOCAL_RS.loc[5, '5']     # l/(s*ha)
r_Dn_Form = f'r_Dn = {r_Dn} l/(s*ha)'

q_dr = 18.20 # l/s
Q_dr = q_dr * 1000
Q_dr_Form = f'Q_dr = q_dr * 1000 = {fx.normal_form(Q_dr)} m^3/s' 

Q_zu = fx.vs_q_zu(A_u, r_Dn)
Q_zu_Form = f'Q_zu = A_u * r_Dn * 1e-7 = {fx.normal_form(Q_zu)} m^3/s' 

'''
print(A_u_Form)
print(r_Dn_Form)
print(Q_dr_Form)
print(Q_zu_Form)
print()


print(rs_005)

'''

#######################################
#  
# Flächen-Versickerung
#  
#######################################

'''
A_s = 500    # m2
A_s_Form = f'A_s = {A_s} m^2'

k_f = 0.00001   # m/s
k_f_Form = f'k_f = {k_f} m/s'

Q_s = fx.vs_q_s(A_s, k_f)
Q_s_Form = f'Q_S = A_s * k_f / 2 = {fx.normal_form(Q_s)} m^3/s'

rs_005['Q_s'] = Q_s

print(rs_005)
A_s_Form
k_f_Form
Q_s_Form
'''


 
#######################################
#  
#  Mulde
#  
#######################################


A_s = 150    # m2
A_s_Form = f'A_s = {A_s} m^2'

z = 0.3    # m
z_Form = f'z = {z} m'

k_f = 0.00001   # m/s
k_f_Form = f'k_f = {k_f} m/s'

Q_s = fx.vs_q_s(A_s, k_f)
Q_s_Form = f'Q_S = A_s * k_f / 2 = {fx.normal_form(Q_s)} m^3/s'


V_erf = fx.vs_v_erf(Q_zu, Q_s, Q_dr, LOCAL_RS.loc[20, '100'], f_z=1.15) # m^3
V_erf_Form = f'V_erf = (Q_zu - Q_s - Q_dr) * D_vs_5 * 60 * f_z = {fx.normal_form(V_erf)} m^3'

#rs_005['V_erf'] = V_mulde



V_vs = fx.vs_v_vs(A_s, z=z) # m^3
V_vs_Form = f'V_vs = A_s * z = {fx.normal_form(V_vs)} m^3'

#rs_005['V_mulde'] = V_mulde







'''

print(A_s_Form)
print(z_Form)
print(k_f_Form)
print(Q_s_Form)
print(V_erf_Form)
print(V_vs_Form)
print()


'''







#######################################
#  
#  Rigole
#  
#######################################
















#######################################
#  
# Konklusion
#  
#######################################

#concl_vs_form = f'{fx.normal_form(Q_zu)} l/m^3 < {fx.normal_form(Q_s)} l/m^3'
concl_vs_form = f'{fx.normal_form(V_erf)} l/m^3 < {fx.normal_form(V_vs)} l/m^3'

#print(concl_vs_form)



#######################################
#  
# Graph
#  
#######################################

'''
rs_005.loc[:, 'Q_zu':'Q_s'].plot()
# plt.show()
plt.savefig('ew_ex/ew_vs_flvs.png', format = 'png')

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
'''
