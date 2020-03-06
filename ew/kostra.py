# NiderschlagSpendenDaten von KOSTRA
import numpy as np
import pandas as pd

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

d0005.describe()
d0005.head()
d0005.tail(5)
# cxycxycxy
