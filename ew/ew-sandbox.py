## Import
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
#import latex 
import ew_fx as fx

#

sanyter_df = pd.read_csv('ew_data/sanyter.csv', sep='|')

#print(sanyter_df)

k = 0.5
#

ew_sw = pd.read_csv('ew_in/0001_sw_input.csv', sep='|')
ew_sw['id'] = ew_sw['id'].astype(str)

#print(ew_sw)

#


ew_sw = pd.merge(left=ew_sw, right=sanyter_df, how='outer', on='san')
ew_sw = ew_sw.sort_values(by='id')

print(ew_sw)


##

id_du = ew_sw[['du']]

trans = ew_sw[['du']].transpose()

trans.columns = ew_sw['id']

print(trans)

##

#trans.loc['11'] = 

#df[i] = df[kid(i).value.sum()] + df[bro(i).value.sum()]
trans['3'] = trans[['30', '31']].values.sum()

trans['22'] = trans[['220', '221']].values.sum()
trans['211'] = trans[['2110', '2111']].values.sum()
trans['21'] = trans['211'].values.sum() + trans['22'].values.sum()
trans['2'] = trans['21'].values.sum() + trans['3'].values.sum()
trans['11'] = trans[['110', '111']].values.sum()
trans['1'] = trans['11'].values.sum() + trans['2'].values.sum()
trans['0'] = trans['1'].values.sum()

print(trans.transpose())

##

#df[i] = df['san']['du'] > i.sum()

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





