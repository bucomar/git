## Import
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
#import latex 
import ew_fx as fx

k = 0.5
sw = {}

# sw: key = id, val = objekt

def name(id):
    return f'_{id}'


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
    id = str(int(key)+1)
    neu_obj = leitungen(id)
    sys[id] = neu_obj

def add_bro(sys, key):
    id = str(key)+'1'
    neu_obj = leitungen(id)
    sys[id] = neu_obj


##

sw['0'] = leitungen(0)

print(sw)
print(sw['0'].id)
print(vars(sw['0']))

## Add Son

sw['1'] = leitungen('1')

print(sw)
print(sw['1'].id)
print(vars(sw['1']))

##

id = str(1+1)
neu_obj = leitungen(id)
sw[id] = neu_obj


print(sw.keys())
print(sw[id].id)
print(vars(sw[id]))

##

add_son(sw, '2')

print(sw.keys())


##

add_bro(sw, '1')
print(sw.keys())

print(sorted(sw.keys()))





##






