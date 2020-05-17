import pandas as pd
import numpy as np


arr = np.arange(20).reshape(4, 5)
df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D', 'E'])
#print(df.columns)
#print(df.index)
#print(type(df.index))
print(df, '\n')

#df.index = ['p', 'q', 'r', 's']

#df.rename_axis('szam')
#df.rename_axis('betu', axis=1)

#newindex = [5, 6, 7, 8]
#newindex = ['p', 'q', 'r', 's']
#df.set_index(newindex)

print(df, '\n')

print('**************************')

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


