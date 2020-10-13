# adatvesztes ellen

import ewfx as ew
import math as mt
import numpy as np
import pandas as pd

## Épülethasználat fajtája
## Gebäudenutzungsart

k = pd.read_csv('ew/ew_csv/k.csv', sep='/', index_col=[0])
k

k.k.hotel


sanyter = pd.read_csv('ew/ew_csv/sanyter.csv', sep='/', index_col=[0])

sanyter
type(sanyter)
sanyter.DN.wc
sanyter.du.de
sanyter.loc['wc', 'DN']
# s
# type(s)




## fg, dn, gf, qmax, v
## h/D, mm, cm/m, l/s, m/s

qmax_sl_set = np.array([
[0,5, 70, 1.0, 1.3, 0.6],
[0,5, 70, 1.5, 1.5, 0.7],
[0,5, 70, 2.0, 1.8, 0.8],
[0,5, 100, 1.0, 2.5, 0.7],
[0,5, 100, 1.5, 3.1, 0.8],
[0,5, 100, 2.0, 3.5, 1.0],
[0,5, 125, 1.0, 4.1, 0.8],
[0,5, 125, 1.5, 5.0, 1.0],
[0,5, 125, 2.0, 5.7, 1.1],
[0,5, 150, 1.0, 7.7, 0.9],
[0,5, 150, 1.5, 9.4, 0.1],
[0,5, 150, 2.0, 10.9, 0.3]
])
print(qmax_sl_set)
print()

## Strangok
## Falleitungen

### DN, Qmax
### mm, l/s

fl_set = np.array([
[70, 1.5],
[100, 4.0],
[125, 5.8],
[150, 9.5]
])
print(fl_set)
print()

#############################

du = sanyter.du.wc
du
k = k.k.wohnehaus
k

QWW = ew.qww(k, du)
print('qww = ')
print(QWW)
