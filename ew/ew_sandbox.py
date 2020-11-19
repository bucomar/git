## Import
import ewfx as ew
import pandas as pd


## Functions ####################################


sw_input = open('ew_prj/0001_sw_input', 'r') 

sorlista = []
count = 0

for line in sw_input:
    if line.strip() == '':
        print('Hopp, egy üres sor!!!')
    else:
        sorlista.append(line.strip())


sorlista

#    print("Line{}: {}".format(count, line.strip())) 

##


# x = get_loc(df, 'DU', 0)
# print(x)
# print(type(x))

## 1 sor dekódolása #############################


lista = []
szam_sor = '123456789abcdefghijklmnopqrstuvwxyz'
fall_sor = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sor = sorlista[2]
sor

##

szam = ''
sanyters = []

for i in sor:
    if i == '/':
        print('csatlakozás')
        #break
    elif i == 'C':
        sanyters.append('WC')
    elif i == 'T':
        sanyters.append('WT')
    elif i == 'D':
        sanyters.append('DU')
    elif i == 'M':
        sanyters.append('WM')
    else:
        szam += i
    
szam

##

sanyters

##
szamsor[15]

##
sor1 = '1Actdm'
##
lista.append(sor1[0])
lista
##
sor[1]
lista
##
sor[2]
lista
##




## DF ###########################################

df = pd.DataFrame([0], columns=['DU'], index=['1'])
print(df)
print()

print(lastindex(df))
print()

print(type(lastindex(df)))

#################################################


df_i = pd.DataFrame([12], columns=['DU'], i:ndex=[lastindex(df)+1])
print(df_i)
print()

df = pd.concat([df, df_i])


print(df)
print()


print(lastindex(df))
print()

print(type(lastindex(df)))

#################################################


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

#################################################






