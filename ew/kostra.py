# NiderschlagSpendenDaten von KOSTRA
import numpy as np
import pandas as pd
import zipfile as zp

url_nro = ('0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320')

url = []

for i in range(len(url_nro)):
    url.append('https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D'+url_nro[i]+'.csv.zip')






'''
coord_b = 53.5928618
coord_l = 9.4709494

col = 21
row = 31

index_rc = str(col) + '0' + str(row)
print ('index_rc: ', index_rc)

d0005 = pd.DataFrame(pd.read_csv('ew/strsp/StatRR_D0005.csv'))
d0010 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0010.csv"))
d0015 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0015.csv"))
d0020 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0020.csv"))
d0030 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0030.csv"))
d0045 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0045.csv"))
d0060 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0060.csv"))
d0090 = pd.DataFrame(pd.read_csv("ew/strsp/StatRR_D0090.csv"))

print(d0005.describe())
print(d0005.head(9))
print(d0005.tail(9))
# cxycxycxy

'''
