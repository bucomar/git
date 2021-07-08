## Import
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import latex import ew_fx as fx

##

sanyter_df = pd.read_csv('ew_data/sanyter.csv', sep='|')

print(sanyter_df)

k = 0.5
##

ew_sw = pd.read_csv('ew_in/0001_sw_input.csv', sep='|')
ew_sw['id'] = ew_sw['id'].astype(str)

print(ew_sw)

##


ew_sw = pd.merge(left=ew_sw, right=sanyter_df, how='outer', on='san')
ew_sw = ew_sw.sort_values(by='id')

print(ew_sw)

##

#print(ew_sw['DU_SUM'])
#print(type(ew_sw['DU_SUM']))
ew_sw['Q_ww'] = fx.q_ww(k, ew_sw['du']) 
ew_sw['Q_P'] = 0
ew_sw['Q_C'] = 0

ew_sw['Q_tot'] = fx.q_tot(ew_sw['Q_ww'], ew_sw['Q_C'], ew_sw['Q_P'])

ew_sw['Q_zul'] = 0

print(ew_sw)

##







##








##





