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

ew_sw = {}


class leitungen:
    def __init__(self, id='id?', sys='sw?', typ='SW??', du=np.nan, q_ww=np.nan):
        self.id = id
        self.sys = sys
        self.typ = typ
        self.du = du
        self.q_ww = q_ww
        #sw.append(id: objekt)
        #print(sw keys)


def add_son(sys, key):
    id = fx.son(key)
    neu_obj = leitungen(id)
    sys[id] = neu_obj

def add_bro(sys, key):
    id = fx.bro(key)
    neu_obj = leitungen(id)
    sys[id] = neu_obj


#ew_sw_head = ['Typ', 'DU', 'DU_SUM', 'Q_ww', 'Q_P', 'Q_C', 'Q_tot', 'Q_zul']


#ew_sw = pd.DataFrame(columns=ew_sw_head)

#sw_in_link = 'ew_in/0001_sw_input.csv'
#sw_in_file = open(sw_in_link, 'r')

ew_sw_df = pd.read_csv(sw_in_link, sep='|')
print(ew_sw_df)

##


## print rows

for row in ew_sw_df.index:
    print(ew_sw_df.iloc[row,:])



## add data df => dict


for row in ew_sw_df.index:
    #print(ew_sw_df.iloc[row,:])
    ew_sw[ew_sw_df.iloc[row,0]] = leitungen(ew_sw_df.iloc[row,0], 'sw', typ=ew_sw_df.iloc[row,1])

## print keys

print(ew_sw.keys())

## print object vars

for key in ew_sw.keys():
    #print(vars(ew_sw[key]))
    print(f'{ew_sw[key].sys}-{ew_sw[key].id}')







#############################################

#print(ew_sw_df.iloc[0,0])
#print(ew_sw_df.iloc[0,1])
#print(ew_sw_df.iloc[0,2])

#print('\n')

##

print(ew_sw_df.iloc[3,:])
print('\n')

##

print(ew_sw_df.iloc[0:10,:])
print('\n')

##

print(ew_sw_df.iloc[5,:])
print('\n')

##

print(ew_sw_df.iloc[0,:])

print('\n')

##

ew_sw[str(ew_sw_df.iloc[0,0])] = leitungen(ew_sw_df.iloc[0,0], 'sw', typ=ew_sw_df.iloc[0,1])


print('\n')

##

ew_sw[str(ew_sw_df.iloc[1,0])] = leitungen(ew_sw_df.iloc[1,0], 'sw', typ=ew_sw_df.iloc[1,1])

print('\n')


##



print(ew_sw)
print(ew_sw.keys)

##

print(ew_sw)
print(ew_sw['0'].id)
print(vars(ew_sw['0']))

##

print(ew_sw)
print(ew_sw['1'].id)
print(vars(ew_sw['1']))

##

print(ew_sw_df)


##

print(ew_sw_df.iloc[1,:])



