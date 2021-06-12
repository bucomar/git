# 
#  _______        __  ___ _   _   _  _____  ____ _____ ____      _    
# | ____\ \      / / |_ _| \ | | | |/ / _ \/ ___|_   _|  _ \    / \   
# |  _|  \ \ /\ / /   | ||  \| | | ' / | | \___ \ | | | |_) |  / _ \  
# | |___  \ V  V /    | || |\  | | . \ |_| |___) || | |  _ <  / ___ \ 
# |_____|  \_/\_/    |___|_| \_| |_|\_\___/|____/ |_| |_| \_\/_/   \_\
#                                                                     
# 

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################

import ew_prj as prj
import ew_fx as fx

import requests, zipfile, io

import math as mt
import numpy as np
import pandas as pd


#######################################
# Kostra Daten einlesen.
#  
#  
#######################################

print('Kostra Daten einlesen.')

URL_COORD = 'https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/KOSTRA-DWD-2010R_geog_Bezug.xlsx'

SHEET = 'Raster_geog_Bezug'

df = pd.read_excel(URL_COORD, sheet_name = SHEET)

#df.info()

i_rc_row = df[ (df['X1_NW_GEO'] <= prj.geo_x) & (df['X4_NE_GEO'] >= prj.geo_x) & (df['Y1_NW_GEO'] >= prj.geo_y) & (df['Y2_SW_GEO'] <= prj.geo_y)]

I_RC = i_rc_row.iloc[0, 0]

print('Index_RC: ', I_RC)
print('Benötigte Daten samelln.')

##	url list
REGEN_DAUER = [
'0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320'
]

'''
REGEN_DAUER = [
'0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320'
]
'''


REGEN_DAUER_Index = [
'5', '10', '15', '20', '30', '45', '60', '90', '120', '180', '240', '360', '540', '720', '1080', '1440', '2880', '4320'
]


WIEDERKEHR_ZEIT = [
'1', '2', '3', '5', '10', '20', '30', '50', '100'
]

URL = []

for i in range(len(REGEN_DAUER)):
	URL.append(
	f'https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D{REGEN_DAUER[i]}.csv.zip'
	)

#######################################
# make local_RS
#  
#  
#######################################


LOCAL_RS = pd.DataFrame()

for i in range(0, len(REGEN_DAUER)):
	DF_TEMP = fx.kos_get_csv_df(i, URL, REGEN_DAUER)
	LOCAL_RS = fx.kos_df_row_exp(DF_TEMP, I_RC, LOCAL_RS, i, REGEN_DAUER)

LOCAL_RS.index = REGEN_DAUER_Index
LOCAL_RS.index.name = 'Regendauer'
LOCAL_RS.columns = WIEDERKEHR_ZEIT
LOCAL_RS.columns.name = 'Regenhaufigkeit'

LOCAL_RS.to_csv(f'ew_ex/{I_RC}_local_rs.csv')

print(LOCAL_RS)
print('LOCAL_RS ist fertig!')
