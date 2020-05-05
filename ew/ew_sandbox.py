import pandas as pd
import numpy as np

df1 = pd.DataFrame([(1, 1, 1), (4, 5, 6), (7, 8, 9)])
df2 = pd.DataFrame([(2, 2, 2), (4, 5, 6), (7, 8, 9)])
df3 = pd.DataFrame([(3, 3, 3), (4, 5, 6), (7, 8, 9)])

sr = pd.Series([df1, df2, df3])

print(sr)

ar1 = np.array([(1, 1, 1), (4, 5, 6), (7, 8, 9)])
ar2 = np.array([(2, 2, 2), (4, 5, 6), (7, 8, 9)])
ar3 = np.array([(3, 3, 3), (4, 5, 6), (7, 8, 9)])

ar = np.array([ar1, ar2, ar3])

print(ar)
print(ar[2, :, :])


#for i in abc:
#	for j in szam:
#		x = str(i+j)
	
