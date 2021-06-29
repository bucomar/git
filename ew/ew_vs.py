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
A_u_f = '{} = {} \ m^2'.format('A_{u}', A_u)

r_Dn = LOCAL_RS.loc[5, '5']     # l/(s*ha)
r_Dn_f = '{} = {} \ {}'.format('r_{Dn}', r_Dn, '\\frac{l}{s*ha}')

q_dr = 18.20 # l/s
Q_dr = q_dr * 1000
Q_dr_f = '{} = {} = {} \ {}'.format('Q_{dr}', 'q_{dr} * 1000', fx.normal_form(Q_dr), '\\frac{m^3}{s}')

Q_zu = fx.vs_q_zu(A_u, r_Dn)
Q_zu_f = '{} = {} = {} \ {}'.format('Q_{zu}', 'A_{u} * r_{Dn} * 1e-7', fx.normal_form(Q_zu), '\\frac{m^2}{s}')

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


A_s = 150
A_s_f = '{} = {} \ m^2'.format('A_{s}', A_s)

z = 0.3
z_f = '{} = {} \ m'.format('z', z)

k_f = 0.00001
k_f_f = 'k_f = {} \ {}'.format('k_{f}', k_f, '\\frac{m}{s}')

Q_s = fx.vs_q_s(A_s, k_f)
Q_s_f = '{} = {} = {} \ {}'.format('Q_S', 'A_s * k_f / 2', fx.normal_form(Q_s), '\\frac{m^3}{s}')


V_erf = fx.vs_v_erf(Q_zu, Q_s, Q_dr, LOCAL_RS.loc[20, '100'], f_z=1.15)
V_erf_f = '{} = {} = {} \ m^3'.format('V_{erf}', '(Q_{zu} - Q_{s} - Q_{dr}) * D_{vs-5} * 60 * f_{z}', fx.normal_form(V_erf))
#rs_005['V_erf'] = V_mulde



V_vs = fx.vs_v_vs(A_s, z=z)
V_vs_f = '{} = {} = {} \ m^3'.format('V_{vs}', 'A_{s} * z', fx.normal_form(V_vs))

#rs_005['V_mulde'] = V_mulde




'''
print(A_s_f)
print(z_f)
print(k_f_f)
print(Q_s_f)
print(V_erf_f)
print(V_vs_f)




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
concl_vs = '{} \ m^3 < {} \ m^3'.format(fx.normal_form(V_erf), fx.normal_form(V_vs))

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
