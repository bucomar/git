# 
# _______        __  ______        __
# | ____\ \      / / / ___\ \      / /
# |  _|  \ \ /\ / /  \___ \\ \ /\ / / 
# | |___  \ V  V /    ___) |\ V  V /  
# |_____|  \_/\_/    |____/  \_/\_/   
# 
# 

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################

import ew_fx as fx

import pandas as pd
import numpy as np



######################################################
# import datasets
# Dateiensets importieren
# adatkészletek importálása
######################################################


#######################################
# variables list 
# Liste der technische Paramters
# műszaki paraméterek listája
#######################################

#ew_var = pd.read_csv('ew_data/var.csv', sep='|', index_col=0)

#######################################
# use of the building
# Gebäudenutzungsart
# épülethasználat fajtája
#######################################

k_df = pd.read_csv('ew_data/k.csv', sep='|', index_col=0)
print(k_df)


#######################################
# k = ? 
#  
#  
#######################################

k = k_df.iloc[0]
k = float(k)
print(k)
print(type(k))

#######################################
# ??? sanyiter
# Sanytärobjekten
# szaniterek importálása W|T|D|M|K|G
#######################################

sanyter_df = pd.read_csv('ew_data/sanyter.csv', sep='|')
print(sanyter_df)
print(type(sanyter_df))

#sanyter.DN.wc
#sanyter.du.de
#sanyter.loc['wc', 'dn']
# s
# type(s)


#######################################
# ???
# Q_max vertikal
# csőkapacitás függőlegesen |
#######################################

q_max_ver_df = pd.read_csv('ew_data/Q_max_ver.csv', sep='|', index_col=0)
print(q_max_ver_df)
print(type(q_max_ver_df))


#######################################
# ???
# Q_max horisontal
# Csőkapacitás vízszintesen - 
#######################################

q_max_hor_50_df = pd.read_csv('ew_data/Q_max_hor_50.csv', sep='|', index_col=0)
fx.float_col(q_max_hor_50_df)

q_max_hor_70_df = pd.read_csv('ew_data/Q_max_hor_70.csv', sep='|', index_col=0)
fx.float_col(q_max_hor_70_df)

print(q_max_hor_50_df)
print(q_max_hor_70_df)

#######################################
# import imput_sanyter 
# import imput_sanyter
# imput_saniter beolvasása
#######################################


#######################################
# import sw_network
# import sw_netz
# szennyvízhálózat beolvasása
#######################################


#ew_sw_head = ['Typ', 'DU', 'DU_SUM', 'Q_ww', 'Q_P', 'Q_C', 'Q_tot', 'Q_zul']


#ew_sw = pd.DataFrame(columns=ew_sw_head)
#ew_sw = pd.DataFrame()

ew_sw = pd.read_csv('ew_in/0001_sw_input.csv', sep='|')
print(ew_sw.dtypes)

ew_sw['id'] = ew_sw['id'].astype(str)



print(ew_sw.dtypes)

#ew_sw = fx.add_row(ew_sw, [0, 1, 11, 2, 21, 211, 22, 3])

#print(ew_sw)
##
#print(ew_sw['san'])

##

#ew_sw['du'] = sanyter_df.loc[str(ew_sw['Sany']), 'du']

#ew_sw['du'] = sanyter_df.loc['wc', 'du']

df = pd.merge(left=ew_sw, right=sanyter_df, how='outer', on='san')
df = df.sort_values(by='id')

#ew_sw.loc[0, 'DU'] = 0.25
#ew_sw.loc[1:11, 'DU'] = 0.5
#ew_sw.loc[2:22, 'DU'] = 0.75
#ew_sw.loc[3, 'DU'] = 1.00

#ew_sw['DU_SUM'] = ew_sw['DU'] * 1.15

print(df)

'''
##

#print(ew_sw['DU_SUM'])
#print(type(ew_sw['DU_SUM']))
ew_sw['Q_ww'] = fx.q_ww(k, ew_sw['du']) 
ew_sw['Q_P'] = np.nan
ew_sw['Q_C'] = np.nan

ew_sw['Q_tot'] = fx.q_tot(ew_sw['Q_ww'], ew_sw['Q_C'], ew_sw['Q_P'])

ew_sw['Q_zul'] = np.nan

print(ew_sw)

'''
