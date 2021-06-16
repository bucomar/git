# 
# _______        __  _______  __
# | ____\ \      / / |  ___\ \/ /
# |  _|  \ \ /\ / /  | |_   \  / 
# | |___  \ V  V /   |  _|  /  \ 
# |_____|  \_/\_/    |_|   /_/\_\
# 
# 

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################




import math as mt
import pandas as pd

import requests, zipfile, io






######################################################
# KOSTRA
# KOSTRA
# KOSTRA
######################################################


def kos_csv_name(nro):
	""" csv name generator """
	csv_nm = str(
	'StatRR_KOSTRA-DWD-2010R_D'+str(nro)+'.csv')
	return csv_nm

def kos_df_name(nro):
	""" df name generator """
	df_nm = str('df'+str(nro)+'.csv')
	return df_nm

def kos_get_csv_df(pos, URL, REGEN_DAUER):
	""" get csv-s to df """
	print(pos)
	r = requests.get(URL[pos])
	z = zipfile.ZipFile(io.BytesIO(r.content))
	csv = z.open(kos_csv_name(REGEN_DAUER[pos]))
	df = pd.read_csv(csv, sep = ';', index_col=('INDEX_RC'))
	return df

def kos_df_row_exp(from_df, rc_i, to_df, pos, REGEN_DAUER):
	""" ##	row export to INDEX_RC """
	# to_df = pd.concat([to_df, from_df.loc[from_df['INDEX_RC'] == int(rc_index)]])
	a_row = from_df.loc[[rc_i]]
	a_row = a_row.apply(lambda i: round(i*100*100/60/int(REGEN_DAUER[pos]), 2))
	# print(a_row)
	# print()
	to_df = pd.concat([to_df, a_row])
	# print(to_df)
	# print()
	return to_df

######################################################
# import
# einlesen
# beolvasás
######################################################


def float_col(df):
    ''' df colnames to float '''
    x = df.columns
    y = []
    for i in x:
        y.append(float(i))
    df.columns = y

def sw_imput():
    pass

def rw_input():
    pass

######################################################
# edit 
# bearbeiten
# szerkesztés
######################################################


def lastindex(df):
    ''' Last index of a DataFrame. '''
    lastindex = list(df.index)[-1]
    return str(lastindex)


def get_loc(df, col_ind, val):
    ''' Return location from value. '''
    loc = df[col_ind][df[col_ind] == val].index.tolist()
    return loc


def bro(i):
    ''' Init a "brother" index -  11 => 111 '''
    return str(i)+str(1)


def son(i):
    ''' Init a "son" index -  11 => 12 '''
    return str(int(i)+1)

"""
def add_bro(i, df = df):
    ''' Add a "brother" row to df '''

    nan_val = []

    for a in range(len(df.columns)):
        nan_val.append(np.nan) 
    
    df.loc[ew.bro(i)] = nan_val
    df.sort_index()
    return df
"""



######################################################
# computing 
# berechnung
# számítás
######################################################

######################################################
# SW | Schmutzwasswe #################################
######################################################

def q_ww(k, du):
    ''' SW |
    Q_ww [l/s] = k * SQRT(DU)
    '''
    qww = k*m.sqrt(du)
    return qww


def q_tot(q_ww, q_c, q_p):
    ''' SW |
    Q_tot [l/s] = Q_ww + Q_C + Q_P
    '''
    q_tot = q_ww + q_c + q_p
    return p_tot

######################################################
# RW | Regenwasser ###################################
######################################################

def c_e(q_r, a_u):
    ''' RW | 
    C_e Endabflussbeiwert = Q_r / A_U
    '''
    c_e = q_r / a_u
    return c_e

def a_u(a_e, c_m):
    '''  RW | 
    A_U [m2] Angeschlossene undurchlässige Fläche = A_E * C_m
    '''
    a_u = a_e * c_m
    return a_u

def q_r():
    ''' RW | 
    Q_r [l/s] = r_DT * C_m * A_U * 1 / 10000
    '''
    a_u = a_e * c_m
    return a_u


######################################################
# VS | Versickerung ##################################
######################################################

def vs_q_zu (A_u, r_Dn):
    ''' VS |
    Q_zu    [m3/s] = A_u * r_Dn * 1e-7
    '''
    #A_u = 858.23       # m2
    #r_Dn = 40.14     # l/(s*ha)

    Q_zu = A_u * r_Dn * 1e-7    # m3/s 

    return Q_zu


def vs_q_s (A_s, k_f):
    ''' VS |
    Q_s     [m3/s] = A_s * k_f / 2
    '''

    #A_s = 50    # m2
    #k_f = 0.00001   # m/s

    Q_s = A_s * k_f / 2 # m3/s
    return Q_s

def vs_v_erf (Q_zu, Q_s, Q_dr, D_vs_5, f_z=1.15):
    ''' VS |
    V_erf    [m3] = (Q_zu - Q_s - Q_dr) * D_vs_5 * 60 * f_z
    '''

    #D_vs_5 = 120 # min
    #f_z = 1.15

    V_erf = (Q_zu - Q_s - Q_dr) * D_vs_5 * 60 * f_z
    return V_erf

def vs_v_vs (A_s, z=0.30):
    ''' VS |
    V_vs [m3] = A_s * z
    '''

    #z = 0.30 # m

    V_vs = A_s * z
    return V_vs

"""
def mulde(A_u, r_Dn, A_s, k_f, D_vs_5, f_z=1.15, z=0.30):
    ''' VS |
    Q_zu    [m3/s] = A_u * r_Dn * 1e-7
    Q_s     [m3/s] = A_s * k_f / 2
    V_VS    [m3] = (Q_zu - Q_s) * D_vs_5 * 60 * f_z
    V_mulde [m3] = A_s * z

    return: V_mulde, V_VS
    '''
    
    q_zu(A_u, r_Dn)
    q_s(A_s, k_f)
    v_vs(D_vs_5, f_z)
    v_mulde(A_s, z)

    return V_mulde, V_VS    
"""




######################################################
# export 
# Auswertung
# kiírás
######################################################





def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)
  
# display superscipt
# print(get_super('GeeksforGeeks')) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ


def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)
  
# display subscript
# print('H{}SO{}'.format(get_sub('2'),get_sub('4'))) #H₂SO₄


def normal_form(num):
    ''' Print a number in normal form ve: 1.23e-5 '''
    return ('{:.2e}'.format(num))


def latex_export(key, value):
    import csv
    import os

    dict_var = {}

    file_path = os.path.join(os.getcwd(), "ew_data/ew.dat")

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
            f.write(f"{key}|{dict_var[key]}\n")


def to_data(df, k, v):
    d = pd.DataFrame(data=[v], index=[k])
    df = pd.concat([df, d])
    return df



######################################################
# 
# 
# 
######################################################


######################################################
# 
# 
# 
######################################################


