# adatvesztes ellen OK
# NiderschlagSpendenDaten von KOSTRA
import numpy as np
import pandas as pd
from wget import download as dl
from zipfile import ZipFile as zip
import subprocess as cmd
import glob

##	url list
url_nro = ('0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320')
print('url_nro pype is :', type(url_nro))

url = []

for i in range(len(url_nro)):
	url.append('https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D'+url_nro[i]+'.csv.zip')

##	download & extract csv-s, del zips
def get_csv(url):
    # download, unzip, delet_zip
	myzip = dl(url)
	print(myzip)
	with zip(myzip, 'r') as my_zip:
		my_zip.printdir()
		my_zip.extractall('temp')
	cmd.run('pwd', check=True, shell=True)
	cmd.run('rm *.zip', check=True, shell=True)

##	dont delete!!!	##
## for i in range(len(url_nro)):
##	get_csv(url[i])
##	dont delete!!!	##

##	read csv-s
def get_df(csv):
	csv = str('**/*'+csv+'.csv')
	#print(csv)
	csv = glob.glob(csv)
	#print(csv)
	## !!!	index = col index_rc	!!! ##
	df = pd.DataFrame(pd.read_csv(csv[0]))
	#print(df)
	#print(type(df)) 
	return df

for i in url_nro:
	#get_df(url_nro[i])
	exec(f'df_{i} = get_df(i)')
	#exec(f'print(df_{i})')

df_name = 'df_'+url_nro[6]
print(df_name)
print(df_0060)



##	make index_rc

coord_b = 53.5928618
coord_l = 9.4709494

col = 21
row = 31

index_rc = str(col) + '0' + str(row)
print ('index_rc: ', index_rc)

##	make local_RW



'''
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