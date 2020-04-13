import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

conf = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
death = pd.DataFrame([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'j']])
rec = pd.DataFrame([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]])

print(conf)
print
print(death)
print
print(rec)
print


''' multiindexed columns

2020.04.10, 2020.04.11, 2020.04.12,
c, d, r,    c, d, r,    c, d, r,
1, 2, 3,    4, 5, 6,    7, 8, 9,
'''
df = pd.DataFrame([])




print(df)



'''
def prep(link):

    df = pd.read_csv(link)
    csv.set_index('Country/Region')
    print(df, 'Type csv: ', type(df))
    print(csv)

    ind = np.array(df)
    ind = ind[0:, 1]

    df = pd.DataFrame(csv)

    df.set_index('Country/Region', inplace=True)

    df.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)


x = prep(url)

print(x,  'Type: ', type(x))

conf = prep(url_c)
death = prep(url_d)
rec = prep(url_r)

print('conf type: ', type(conf))

conf_hu = conf.loc[countryes]
print(conf_hu)

'''

'''

a = [[1, 2, 3],
    ['p', 'q', 'r'],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]]
print(a, type(a))

a_np = np.array(a)
print(a_np, type(a_np))

a_np_ford = np.array(np.reshape(a_np[0], (3, 1)))
a_np_ford = np.hstack( (a_np_ford, (np.reshape(a_np[1], (3, 1)))) )
a_np_ford = np.hstack( (a_np_ford, (np.reshape(a_np[2], (3, 1)))) )
a_np_ford = np.hstack( (a_np_ford, (np.reshape(a_np[3], (3, 1)))) )
a_np_ford = np.hstack( (a_np_ford, (np.reshape(a_np[4], (3, 1)))) )

# e = [[1], [2], [3]]
# f = [['x'], ['y'], ['z']]
# a_np_ford = np.hstack( ( [[1], [2], [3]], [['x'], ['y'], ['z']] ) )

print(a_np_ford, type(a_np))
print(a_np_ford[:, 2:], type(a_np))


ind=a_np_ford[:, 1]
col=a_np_ford[0, 2:]
print(ind)
print(col)

a_pd = pd.DataFrame(a_np_ford[:, 2:], index=ind, columns=col)
print a_pd, type(a_pd)


# df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['x0', 'x1'], index=['y0', 'y1', 'y2'])
# df=df/pop[0]
# print(df)
'''
