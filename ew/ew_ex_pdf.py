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
    text = text.replace('au-tex', vs.A_u_f)
    text = text.replace('rdn-tex', vs.r_Dn_f)
    text = text.replace('qdr-tex', vs.Q_dr_f)
    text = text.replace('qzu-tex', vs.Q_zu_f)
    text = text.replace('au-tex', vs.A_u_f)
    text = text.replace('as-tex', vs.A_s_f)
    text = text.replace('z-tex', vs.z_f)
    text = text.replace('kf-tex', vs.k_f_f)
    text = text.replace('qs-tex', vs.Q_s_f)
    text = text.replace('verf-tex', vs.V_erf_f)
    text = text.replace('vvs-tex', vs.V_vs_f)
    text = text.replace('concl', vs.concl_vs)
    
    with open('ew_ex/ew.tex', 'w') as output:
        output.write(text)


'''

as-tex
z-tex
kf-tex
qs-tex
verf-tex



'''



