
######################################################
# _______        ________        __                  #
# | ____\ \      / / ___\ \      / /                 #
# |  _|  \ \ /\ / /\___ \\ \ /\ / /                  #
# | |___  \ V  V /  ___) |\ V  V /                   #
# |_____|  \_/\_/  |____/  \_/\_/                    #
#                                                    #
######################################################
# EWSW
# Entwässerung - Schmutzwasser
# Maitz Balázs
# 2020.
######################################################
# in_tab:     Konstans táblázatok /   csv
# in_sys:    hálózat számokkal   /   csv
# df:        itt van minden rendszeradat
# out_tab:   Számítások          /   ???
# out_cad:   CAD terv            /   ifc
# out_graf:  systemschnitt       /   plot grapf
######################################################

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################

import ewfx
import math as mt
import numpy as np
import pandas as pd


######################################################
# import datasets
# Dateiensets imortieren
# adatkészletek importálása
######################################################


#######################################
# variables list 
# Liste der technische Paramters
# műszaki paraméterek listája
#######################################


#######################################
# use of the building
# Gebäudenutzungsart
# épülethasználat fajtája
#######################################

k_df = pd.read_csv('ew_csv/k.csv', sep='|', index_col=0)
print(k_df)


#######################################
# ??? sanyiter
# Sanytärobjekten
# szaniterek importálása W|T|D|M|K|G
#######################################

sanyter_df = pd.read_csv('ew_csv/sanyter.csv', sep='|', index_col=0)
print(sanyter_df)
print(type(sanyter_df))

#sanyter.DN.wc
#sanyter.du.de
#sanyter.loc['wc', 'DN']
# s
# type(s)


#######################################
# ???
# Q_max vertikal
# csőkapacitás függőlegesen |
#######################################

q_max_ver_df = pd.read_csv('ew_csv/Q_max_ver.csv', sep='|', index_col=0)
print(q_max_ver_df)
print(type(q_max_ver_df))


#######################################
# ???
# Q_max horisontal
# Csőkapacitás vízszintesen - 
#######################################

q_max_hor_50_df = pd.read_csv('ew_csv/Q_max_hor_50.csv', sep='|', index_col=0)
ewfx.float_col(q_max_hor_50_df)

q_max_hor_70_df = pd.read_csv('ew_csv/Q_max_hor_70.csv', sep='|', index_col=0)
ewfx.float_col(q_max_hor_70_df)

print(q_max_hor_50_df)
print(q_max_hor_70_df)

######################################################
# projectvalues
# Projektdaten
# projektadatok
######################################################


#######################################
# import imput_sanyter 
# import imput_sanyter
# imput_saniter beolvasása
#######################################


#######################################
# import sw_network
# import sw_netz
# szennyvízhálózat beolvasása
#######################################



#######################################
# import rw_network
# import rw_netz
# esővízhálózat beolvasása
#######################################









######################################################
# groundvalues
# Grunddaten
# Alapadatok
######################################################


#######################################
# k = ? 
#  
#  
#######################################

k = k_df.iloc[0]
print(k)




######################################################
# init df 
#  
#  
######################################################

#######################################
#  
#  
#  
#######################################


#######################################
#  
#  
#  
#######################################

#######################################
#  
#  
#  
#######################################


######################################################
# fill df 
#  
#  
######################################################

#######################################
#  
#  
#  
#######################################

#######################################
#  
#  
#  
#######################################

#######################################
#  
#  
#  
#######################################


######################################################
# export data
# 
# 
######################################################

#######################################
# tab
# Berechnungen
# számítások
#######################################

#######################################
# CAD
# Zeichnungen
# Tervek
#######################################

#######################################
# graph
# Systemschnitt
# függőleges csőterv
#######################################






######################################################
#  _____ _   _ _____   _____ _   _ ____              # 
# |_   _| | | | ____| | ____| \ | |  _ \             #
#   | | | |_| |  _|   |  _| |  \| | | | |            #
#   | | |  _  | |___  | |___| |\  | |_| |            #
#   |_| |_| |_|_____| |_____|_| \_|____/             #
#                                                    #
######################################################

