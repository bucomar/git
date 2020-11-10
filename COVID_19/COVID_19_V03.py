
'''
       _              _            _                 
__   _(_)_ __ ___    | |_ ___  ___| |_   _ __  _   _ 
\ \ / / | '_ ` _ \   | __/ _ \/ __| __| | '_ \| | | |
 \ V /| | | | | | |  | ||  __/\__ \ |_ _| |_) | |_| |
  \_/ |_|_| |_| |_|___\__\___||___/\__(_) .__/ \__, |
                 |_____|                |_|    |___/ 

'''
## Import librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#from bokeh.plotting import figure
#from bokeh.io import output_file, show
#from bokeh.models import HoverTool

## Konstant
countryes = ['Hungary', 'Germany', 'Austria']
pop = [1000, 8300, 880]
# pop = [1, 1, 1]

## Links
url_c = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'

url_d = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'

url_r = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'

## Functions
def prep(url):
    """Index=Countries, Columns=Datum, Values=Values."""
    df = pd.read_csv(url)
    df.set_index('Country/Region', inplace=True)
    df.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    return df

## Prep Data
conf = prep(url_c)
death = prep(url_d)
rec = prep(url_r)

## Print DF
# print(conf.head())

# print(death.head())

# print(rec.head())

## Filter Data

hu_c = conf.loc[countryes[0]]
hu_d = death.loc[countryes[0]]
hu_r = rec.loc[countryes[0]]

de_c = conf.loc[countryes[1]]
de_d = death.loc[countryes[1]]
de_r = rec.loc[countryes[1]]

at_c = conf.loc[countryes[2]]
at_d = death.loc[countryes[2]]
at_r = rec.loc[countryes[2]]

t = pd.to_datetime(hu_c.index)

## Extract Data for axes

# v_hu_c = hu_c.values
# v_hu_d = hu_d.values
# v_hu_r = hu_r.values
# 
# v_de_c = de_c.values
# v_de_d = de_d.values
# v_de_r = de_r.values

v_hu_c_pop = hu_c.values/pop[0]
v_hu_d_pop = hu_d.values/pop[0]
v_hu_r_pop = hu_r.values/pop[0]

v_de_c_pop = de_c.values/pop[1]
v_de_d_pop = de_d.values/pop[1]
v_de_r_pop = de_r.values/pop[1]

v_at_c_pop = at_c.values/pop[2]
v_at_d_pop = at_d.values/pop[2]
v_at_r_pop = at_r.values/pop[2]

## Plot

p1, = plt.plot(t, v_hu_c_pop, '-', label='Magyar betegek')
p2, = plt.plot(t, v_hu_r_pop, '--', label='Magyar gyógyultak')
p3, = plt.plot(t, v_hu_d_pop, ':', label='Magyar halottak')

p4, = plt.plot(t, v_de_c_pop, '-', label='Német betegek')
p5, = plt.plot(t, v_de_r_pop, '--', label='Német gyógyultak')
p6, = plt.plot(t, v_de_d_pop, ':', label='Német halottak')

p7, = plt.plot(t, v_at_c_pop, '-', label='Osztrák betegek')
p8, = plt.plot(t, v_at_r_pop, '--', label='Osztrák gyógyultak')
p9, = plt.plot(t, v_at_d_pop, ':', label='Osztrák halottak')

# plt.yscale('log')

plt.title('A koronavírus Magyarországon, Ausztriában és Németországban')

plt.legend(loc='upper left')

plt.xlabel('Dátum')
plt.ylabel('Esetek száma 100 ezer főre vetítve')

plt.grid(True)

plt.show()

