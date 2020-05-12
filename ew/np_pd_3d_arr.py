import numpy as np
import  pandas as pd

ar = np.arange(1000).reshape(10, 10, 10)

print(ar)

x = np.where(ar == 245)

print(x)


df_1yx = pd.DataFrame(ar[1,:,:])

print('df_1yx:\n', df_1yx)

df_z2x = pd.DataFrame(ar[:,2,:])

print(' df_z2x:\n', df_z2x)

df_zy3 = pd.DataFrame(ar[:,:,3])

print('df_zy3:\n', df_zy3)

