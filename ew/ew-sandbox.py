## Import
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
#import sympy as sp
#import latex

##
Q_s = 1.4
Q_s_tex = f'Q_s: {Q_s} m^3/s'
print(Q_s_tex)
with open('sandbox.tex','r') as myfile:
    text = myfile.read()
    text_new = text.replace('Q_s', str(Q_s_tex))
    
    with open('sandbox_new.tex', 'w') as output:
        output.write(text_new)

'''
'''







