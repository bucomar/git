## Import
import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt
#import sympy as sp
#import latex

##

# #sp.init_session()
# x, y, z = sp.symbols('x y z')
# 
# 
# #sp.pprint(Integral(sqrt(2*x), use_unicode=True))
# 
# eq = sp.Eq(x**2 + y**2, z**2 )
# 
# print(sp.latex(eq))

def save_var_latex(key, value):
    import csv
    import os

    dict_var = {}

    file_path = os.path.join(os.getcwd(), "mydata.dat")

    try:
        with open(file_path, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                dict_var[row[0]] = row[1]
    except FileNotFoundError:
        pass

    dict_var[key] = value

    with open(file_path, "w") as f:
        for key in dict_var.keys():
            f.write(f"{key},{dict_var[key]}\n")


save_var_latex('Q_s', 123)
save_var_latex('Q_e', 456)
save_var_latex('V_erf', 798)
save_var_latex('V_RR', 147)



