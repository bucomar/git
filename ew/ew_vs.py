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
# 
#######################################
#  
# Flächenversickerung 
#  
#######################################

## Grunddaten

# örtliche Regenspendedaten
LOCAL_RS = pd.read_csv('local_rs.csv', index_col='Regendauer') 

rs_005 = LOCAL_RS['HN_005A']

#print(rs_005)
#print()


#print(r_Dn)
#print()

##

A_u = 858.23       # m2
r_Dn = rs_005[30]     # l/(s*ha)

Q_zu_Form = 'Q_zu = A_u * r_Dn * 1e-7' 
Q_zu = fx.vs_q_zu(A_u, r_Dn)

pdf_Q_zu = 'A_u = ', A_u, ' m^2', 'r_Dn = ', r_Dn, ' l/(s*ha)'

#print(Q_zu_Form)
#print('Q_zu = ', fx.normal_form(Q_zu), ' m^3/s')
##


A_s = 50    # m2
k_f = 0.00001   # m/s

Q_s_Form = 'A_s * k_f / 2'
Q_s = fx.vs_q_s(A_s, k_f)

# print('A_s = ', A_s, ' m^2')
# print('k_f = ', k_f)
# print(   )
# print(Q_s_Form)
# print('Q_s = ', fx.normal_form(Q_s), ' l/m^3')
# 
# print(   )
# print(fx.normal_form(Q_zu), ' l/m^3 < ', fx.normal_form(Q_s), 'l/m^3')
# 
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
