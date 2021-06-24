#######################################################
#  _______        __  _______  __  ____  ____  _____  # 
# | ____\ \      / / | ____\ \/ / |  _ \|  _ \|  ___| #
# |  _|  \ \ /\ / /  |  _|  \  /  | |_) | | | | |_    #
# | |___  \ V  V /   | |___ /  \  |  __/| |_| |  _|   #
# |_____|  \_/\_/    |_____/_/\_\ |_|   |____/|_|     #
#                                                     #
#######################################################

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################

import ew_prj as prj

import ew_sw as sw
import ew_rw as rw
import ew_vs as vs



with open('ew_ex/ew_vorlage.tex','r') as myfile:
    text = myfile.read()
    text = text.replace('as-tex', vs.A_s_Form)
    text = text.replace('z-tex', vs.z_Form)
    text = text.replace('kf-tex', vs.k_f_Form)
    text = text.replace('qs-tex', vs.Q_s_Form)
    text = text.replace('verf-tex', vs.V_erf_Form)
    
    with open('ew_ex/ew.tex', 'w') as output:
        output.write(text)


'''

as-tex
z-tex
kf-tex
qs-tex
verf-tex



'''



