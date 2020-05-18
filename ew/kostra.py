""" NiderschlagSpendenDaten von KOSTRA """

## import modules

from zipfile import ZipFile as zp
import subprocess as cmd
import glob

import pandas as pd
from wget import download as dl

import numpy as np

##	make index_rc

COORD_B = 53.5928618
COORD_L = 9.4709494

COL = 21
ROW = 31

INDEX_RC = (str(COL) + '0' + str(ROW))
print ('col: ', COL, '\n', 'row: ', ROW, '\n', 'index_rc: ', INDEX_RC)


##	url list
REGEN_DAUER = [
'0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320'
]
#print('REGEN_DAUER type is :', type(REGEN_DAUER))

URL = []

for i in range(len(REGEN_DAUER)):
	URL.append(
	'https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D'
	+REGEN_DAUER[i]
	+'.csv.zip'
	)

def csv_name(nro):
	""" csv name generator """
	csv_nm = str(
	'StatRR_KOSTRA-DWD-2010R_D'+nro+'.csv')
	return csv_nm

def df_name(nro):
	""" df name generator """
	df_nm = str('df'+nro+'.csv')
	return df_nm

def get_csv_df(pos):
	""" download zips extract csv-s, del zips """
	myzip = dl(URL[pos])
	print(myzip)
	with zp(myzip, 'r') as my_zip:
		my_zip.printdir()
		my_zip.extractall('temp')
	cmd.run('pwd', check=True, shell=True)
	cmd.run('rm *.zip', check=True, shell=True)
	mycsv = str('**/*'+REGEN_DAUER[pos]+'.csv')
	mycsv = glob.glob(mycsv)
	print(mycsv)
	## !!!	index = col index_rc	!!! ##
	df_from_csv = pd.DataFrame(pd.read_csv(mycsv[0], sep = ';'))
	# cmd.run('rmdir temp', check=True, shell=True) 
	return df_from_csv

def df_row_exp(from_df, rc_index, to_df):
	""" ##	row export to INDEX_RC """
	to_df = pd.concat([to_df, from_df.loc[from_df['INDEX_RC'] == int(rc_index)]])
	return to_df


##	make local_RS

DF_HEAD = get_csv_df(0)
LOCAL_RS = pd.DataFrame(data = None, columns = DF_HEAD.columns)
LOCAL_RS = df_row_exp(DF_HEAD, INDEX_RC, LOCAL_RS)

for i in range(1, len(REGEN_DAUER)):
	DF_TEMP = get_csv_df(i)
	LOCAL_RS = df_row_exp(DF_TEMP, INDEX_RC, LOCAL_RS)


LOCAL_RS.index = REGEN_DAUER
LOCAL_RS.index.name = 'Regendauer'
LOCAL_RS.columns.name = 'Regenhaufigkeit'

print(LOCAL_RS) 
print(type(LOCAL_RS))

