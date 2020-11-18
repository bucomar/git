## Import
import ewfx as ew
import pandas as pd


## Functions


sw_input = open('ew_prj/0001_sw_input', 'r') 
count = 0

while True: 
    count += 1
    line = sw_input.readline() 
    if not line: 
        break
    print("Line{}: {}".format(count, line.strip())) 

sw_input.close() 

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







