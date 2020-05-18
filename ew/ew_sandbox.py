##	NiderschlagSpendenDaten von KOSTRA
import numpy as np
import pandas as pd
from wget import download as dl
from zipfile import ZipFile as zip
import subprocess as cmd
import glob

##	make index_rc


#coord_b = 53.5928618
#coord_l = 9.4709494

cord_b = input('Breite: ##.####### ')
cord_bl = input('La:nge: ##.####### ')

URL_COO = https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/KOSTRA-DWD-2010R_geog_Bezug.xlsx

col = 21
row = 31

index_rc = str(col) + '0' + str(row)
print ('col: ', col, '\n', 'row: ', row, '\n', 'index_rc: ', index_rc)

##	download zips extract csv-s, del zips
def get_pos():
    # input coordnits, download, unzip, delet_zip
	
	myzip = dl(url[pos])
	print(myzip)
	with zip(myzip, 'r') as my_zip:
		my_zip.printdir()
		my_zip.extractall('temp')
	cmd.run('pwd', check=True, shell=True)
	cmd.run('rm *.zip', check=True, shell=True)
	csv = str('**/*'+url_nro[pos]+'.csv')
	csv = glob.glob(csv)
	print(csv)
	## !!!	index = col index_rc	!!! ##
	df = pd.DataFrame(pd.read_csv(csv[0], sep = ';'))
	#cmd.run('rmdir temp', check=True, shell=True) 
	return df




