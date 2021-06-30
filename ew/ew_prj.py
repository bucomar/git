# 
#  _______        __  ____  ____     _ 
# | ____\ \      / / |  _ \|  _ \   | |
# |  _|  \ \ /\ / /  | |_) | |_) |  | |
# | |___  \ V  V /   |  __/|  _ < |_| |
# |_____|  \_/\_/    |_|   |_| \_\___/ 
# 
# 

######################################################
# import modules
# Modulen imortieren
# modulok importálása
######################################################
#import ev_in_kostra as kos
import pandas as pd
import ew_fx as fx

######################################################
#                                                    #
# Projektdaten                                       #
#                                                    #
######################################################


# Bauvorhaben
#ew_data = pd.DataFrame(index=['bauvorhaben'], data=['Ein Bauvorhaben'])
#print(ew_data)
#fx.to_data(ew_data, 'bauvorhaben', 'Ein Bauvorhaben')
#print(ew_data)
bauvorhaben = 'Ein Bauvorhaben'


# Anschrift
#ew_data = fx.to_data(ew_data, 'bauvorhaben_anschrift', 'Musterstrase 3, 12345 Musterdorf')

bauvorhaben_anschrift = 'Musterstrase 3, 12345 Musterdorf'


#print(ew_data)

# Bauherr
#ew_data = fx.to_data(ew_data, 'bauherr', 'Herr Bauherr')

bauherr = 'Herr Bauherr'


#d = pd.DataFrame(data=['bauherr'], index=['Herr Bauherr'])
#ew_data = pd.concat([ew_data, d])



#print(ew_data)

# Anschrift des Bauherrs
#ew_data = fx.to_data(ew_data, 'bauherr_anschrift', 'Bauherrstrasse 666, 98765 Bauherdorf')

bauherr_anschrift = 'Bauherrstrasse 666, 98765 Bauherdorf'

#print(ew_data)

# GEO Koordinaten 
geo_x = 9.2
geo_y = 53.2


URL_COORD = 'https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/KOSTRA-DWD-2010R_geog_Bezug.xlsx'

SHEET = 'Raster_geog_Bezug'

df = pd.read_excel(URL_COORD, sheet_name = SHEET)

#df.info()

i_rc_row = df[ (df['X1_NW_GEO'] <= geo_x) & (df['X4_NE_GEO'] >= geo_x) & (df['Y1_NW_GEO'] >= geo_y) & (df['Y2_SW_GEO'] <= geo_y)]

I_RC = i_rc_row.iloc[0, 0]
#print(I_RC)

'''

'''
