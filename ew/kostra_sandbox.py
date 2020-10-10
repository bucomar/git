import pandas as pd
import numpy as np

URL = 'https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/KOSTRA-DWD-2010R_geog_Bezug.xlsx'

SHEET = 'Raster_geog_Bezug'

############################################
### KOSTRA Koordinaten hier schreiben!!! ###
############################################
# COL = 68 ###################################
# ROW = 20 ###################################
############################################

############################################

# I_RC = int(str(COL) + '0' + str(ROW))
# print ('col: ', COL, '\n', 'row: ', ROW, '\n', 'index_rc: ', I_RC)

df = pd.read_excel(URL, sheet_name = SHEET)
df.head()
df.info()

df.describe()

s = df[df['index_rc'] == I_RC ]
type(s)
m = s[['X1_NW_GEO', 'Y1_NW_GEO', 'X2_SW_GEO', 'Y2_SW_GEO', 'X3_SE_GEO', 'Y3_SE_GEO', 'X4_NE_GEO', 'Y4_NE_GEO']]
type(m)
print(m)

m.iloc[0, 2] - m.iloc[0, 0]
m.iloc[0, 4] - m.iloc[0, 2]
m.iloc[0, 4] - m.iloc[0, 6]

m.iloc[0, 3] - m.iloc[0, 1]
m.iloc[0, 5] - m.iloc[0, 3]
m.iloc[0, 7] - m.iloc[0, 5]


# 14,3567786060	55,1337218550	
# 
# 14,2947722416	55,1738965021	
# 14,2870671472	55,0979657677	
# 14,4186673513	55,0935149681	
# 14,4266078543	55,1694382340


#   |
#   |
#   | 1    -    4
#   | |  (x,y)  |
#   | 2    -    3
#   0--------------->

# x = 9.578804
# y = 53.507799

x = 9.691219
y = 53.540720

9.675579
53.464662

# x = 9.675579
# y = 53.464662

# df.loc[df['X1_NW_GEO'] == x]
df[ (df['X1_NW_GEO'] <= x) & (df['X4_NE_GEO'] >= x) & (df['Y1_NW_GEO'] >= y) & (df['Y2_SW_GEO'] <= y)]

22032	
9,6185751978	53,5316517398

9,5546203191	53,5695458085
9,5553906632	53,4933326134
9,6824200252	53,4937232944
9,6818697696	53,5699371363
