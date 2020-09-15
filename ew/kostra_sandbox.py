import pandas as pd
import zipfile as zip

# my_zipfile = zip.ZipFile('ew/StatRR_KOSTRA-DWD-2010R_D0005.csv.zip')
my_zipfile = zip.ZipFile('https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D0005.csv.zip')
my_zipfile.extractall()
# https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D0005.csv.zip




LOCAL_RS = pd.read_csv('ew/kostra_21031.csv', sep=',', index_col=('Regendauer'))
print(LOCAL_RS)
# LOCAL_RS.to_excel('kostra_21031.xls')


# def mm_to_lsha(df):

a_row = LOCAL_RS.loc[[5]]
print(a_row)

a_row = a_row.apply(lambda i: i*100*100/60/5)
print(a_row)

I_RC = 21031

# tab1 = pd.DataFrame([
# [1, 2, 3],
# [4, 5, 6,],
# [7, 8, 9]
# ], index=('t', 'a', 'b'))
# print(tab)
#
# tab1 = pd.DataFrame([[1, 2, 3]])
# print(tab1)
# print()
# tab2 = pd.DataFrame([[4, 5, 6]])
# print(tab2)
# print()
# tab1 = pd.concat([tab1, tab2])
# print(tab1)

# index = [tab.index]
# print(index)
# tab.index(['t', 'a', 'b'])

# print(tab)

df = pd.DataFrame()

df1 = pd.read_csv('temp/StatRR_KOSTRA-DWD-2010R_D0005.csv', sep=';', index_col='INDEX_RC')
df2 = pd.read_csv('temp/StatRR_KOSTRA-DWD-2010R_D0010.csv', sep=';', index_col='INDEX_RC')
df3 = pd.read_csv('temp/StatRR_KOSTRA-DWD-2010R_D0015.csv', sep=';', index_col='INDEX_RC')
# print(table.loc[table['INDEX_RC'] == 21031])
# print(df.index)
# print(df.iloc[5:10, :])
# print(df.tail())
# df.info()
row1 = df1.loc[[I_RC]]
print(row1)
print()
df = pd.concat([df, row1])
print(df)
print()

row2 = df2.loc[[I_RC]]
print(row2)
print()
df = pd.concat([df, row2])
print(df)
print()


row3 = df3.loc[[I_RC]]
print(row1)
df = pd.concat([df, row3])
print()
print(df)
print()
