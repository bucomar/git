## Import
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
import sympy as sp
#import latex

##

a, b, c = sp.symbols('a b c')

a = 3
b = 4
c = sp.sqrt(a**2+b**2)

form = sp.solve([c], [sp.sqrt(a**2 + b**2)])

sp.print_latex(a)
sp.print_latex(b)
sp.print_latex(c)
form_tex = sp.print_latex(form)


with open('sandbox.tex','r') as myfile:
    text = myfile.read()
    text_new = text.replace('Q_s', str(form_tex))
    
    with open('sandbox_new.tex', 'w') as output:
        output.write(text_new)








'''
Q_s = 1.4
Q_s_tex = f'Q_s: {Q_s} m^3/s'
print(Q_s_tex)
with open('sandbox.tex','r') as myfile:
    text = myfile.read()
    text_new = text.replace('Q_s', str(Q_s_tex))
    
    with open('sandbox_new.tex', 'w') as output:
        output.write(text_new)

'''







