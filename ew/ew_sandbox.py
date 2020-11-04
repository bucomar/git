## Import
# import ewfx as ew
import pandas as pd


## Functions

def lastindex(df):
    ''' Last index of a DataFrame. '''
    lastindex = list(df.index)[-1]
    return str(lastindex)

def get_loc(df, col_ind, val):
    ''' Return location from value. '''
    loc = df[col_ind][df[col_ind] == val].index.tolist()
    return loc

def bro(df, index):
    none

def son(df, index):
    none

# x = get_loc(df, 'DU', 0)
# print(x)
# print(type(x))


## DF

df = pd.DataFrame([0], columns=['DU'], index=['1'])
print(df)
print()

print(lastindex(df))
print()

print(type(lastindex(df)))

##


df_i = pd.DataFrame([12], columns=['DU'], i:ndex=[lastindex(df)+1])
print(df_i)
print()

df = pd.concat([df, df_i])


print(df)
print()


print(lastindex(df))
print()

print(type(lastindex(df)))

##


df_i = pd.DataFrame([9], columns=['DU'], index=[int(str(lastindex(df))+'1')])
print(df_i)
print()

df = pd.concat([df, df_i])


print(df)
print()


print(lastindex(df))
print()

print(type(lastindex(df)))
# df_b = 


