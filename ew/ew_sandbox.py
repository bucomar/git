import pandas as pd
import numpy as np


arr = np.arange(20).reshape(4, 5)
df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D', 'E'])
#print(df.columns)
#print(df.index)
#print(type(df.index))
print(df, '\n')
#print(df.a)
#print(df[0:3])
#print(df.loc[:, ['A', 'B']])
df_uj = df.loc[[0], :]
print(df_uj, '\n')

#df_ujabb = df.loc[[1], :]
#print(df_ujabb, '\n')

#df_uj = pd.concat([df_uj, df.loc[[1], :]])

for i in range(1, len(df.index), 1):
	df_uj = pd.concat([df_uj, df.loc[[i], :]])
	print(i, '\n', df_uj, '\n')

print(df_uj, '\n')
print('', '\n')


###############

##	NiderschlagSpendenDaten von KOSTRA
import numpy as np
import pandas as pd
from wget import download as dl
from zipfile import ZipFile as zip
import subprocess as cmd
import glob

##	make index_rc

coord_b = 53.5928618
coord_l = 9.4709494

col = 21
row = 31

index_rc = str(col) + '0' + str(row)
print ('col: ', col, '\n', 'row: ', row, '\n', 'index_rc: ', index_rc)


##	url list
url_nro = ['0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320']
print('url_nro pype is :', type(url_nro))

url = []

for i in range(len(url_nro)):
	url.append('https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D'+url_nro[i]+'.csv.zip')

##	csv name generator
def csv_name(nro):
	csv = str('StatRR_KOSTRA-DWD-2010R_D'+nro+'.csv')
	return csv

##	df name generator
def df_name(nro):
	df = str('df'+nro+'.csv')
	return df


	
			
##	url + nro generator

#def nr_gen(pos):
#	link = url[pos]
#	nro = url_nro[pos]
#	return link, nro

#print(nr_gen(0))

##	download zips extract csv-s, del zips
def get_csv_df(pos):
    # download, unzip, delet_zip
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



##	row export to
			#INDEX_RC 

def df_row_exp(from_df, rc_index, to_df):
	to_df = pd.concat([to_df, from_df.loc[from_df['INDEX_RC'] == int(rc_index)]])
	return to_df


##	make local_RS

df = get_csv_df(0)
local_RS = pd.DataFrame(data = None, columns = df.columns)
local_RS = df_row_exp(df, index_rc, local_RS)

for i in range(1, len(url_nro)):
	df = get_csv_df(i)
	local_RS = df_row_exp(df, index_rc, local_RS)


# !!!local_RS.reindex(url_nro)

print(local_RS) 
'''
##	df names
df_names = []

for i in url_nro:
	df_names.append(str('df_'+i)) 

# print(df_names)



##	make dfs
for i in range(len(url_nro)):
		df = get_df(url_nro[i]) 
		print(df)
	
print(df_0090)
'''

##	dont delete!!!	##
'''
for i in url_nro:
	#get_df(url_nro[i])
	exec(f'df_{i} = get_df(i)')
	#exec(f'print(df_{i})')
'''
##	dont delete!!!	##


