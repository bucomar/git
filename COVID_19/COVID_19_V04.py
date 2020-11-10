
'''
 _           _        _     
| |__   ___ | | _____| |__  
| '_ \ / _ \| |/ / _ \ '_ \ 
| |_) | (_) |   <  __/ | | |
|_.__/ \___/|_|\_\___|_| |_|

'''
# Import librarys

import numpy as np

import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool


# Konstant
countryes = ['Hungary', 'Germany', 'Austria']
pop = [1000, 8370, 880]

# Links
url_c = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'

url_d = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'

url_r = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'

## Prep Data ######################################################
def prep(url):
    """Index=Countries, Columns=Datum, Values=Values."""
    df = pd.read_csv(url)
    df.set_index('Country/Region', inplace=True)
    df.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    return df


conf = prep(url_c)
death = prep(url_d)
rec = prep(url_r)


## Cases ######################################################

def filter_country(data_source, list_countrys):
    ''' Input: dataset + countrey index
    Output: df with the countreys/row.'''
    df_countrys = ()
    return df_countrys

df = conf.loc[countryes[:]]

t = pd.to_datetime(df.columns)

## Cases / 100 000 ######################################################

'''
hu_c_pop = hu_c.values/pop[0]
hu_d_pop = hu_d.values/pop[0]
hu_r_pop = hu_r.values/pop[0]

de_c_pop = de_c.values/pop[1]
de_d_pop = de_d.values/pop[1]
de_r_pop = de_r.values/pop[1]

at_c_pop = at_c.values/pop[2]
at_d_pop = at_d.values/pop[2]
at_r_pop = at_r.values/pop[2]

print(type(v_hu_c_pop))
print(v_hu_c_pop.shape)
'''


# ## Cases 7 day ######################################################
 
'''
v_hu_c_pop_7 = v_hu_c_pop[-7: -1]
v_hu_d_pop_7 = v_hu_d_pop[-7: -1]
v_hu_r_pop_7 = v_hu_r_pop[-7: -1]

v_de_c_pop_7 = v_de_c_pop[-7: -1]
v_de_d_pop_7 = v_de_d_pop[-7: -1]
v_de_r_pop_7 = v_de_r_pop[-7: -1]

v_at_c_pop_7 = v_at_c_pop[-7: -1]
v_at_d_pop_7 = v_at_d_pop[-7: -1]
at_r_pop_7 = v_at_r_pop[-7: -1]

'''


## 7 day sum ######################################################

# v_hu_7 = []
# v_hu_c_pop_list = list(v_hu_c_pop)

def last_x_sum(f_rom, x):
    ''' Summe of the last 7'''
    to = []
    for i in range(len(f_rom)-x):
        dx = f_rom[i+x] - f_rom[i]
        to.append(dx)
    to_np = np.array(to)
    return to_np

'''
v_hu_7 = last_x_sum(hu_c, 7)
v_de_7 = last_x_sum(de_c, 7)
v_at_7 = last_x_sum(at_c, 7)

v_hu_pop_7 = last_x_sum(v_hu_c_pop, 7)
v_de_pop_7 = last_x_sum(v_de_c_pop, 7)
v_at_pop_7 = last_x_sum(v_at_c_pop, 7)

t_7 = t[7: ]

print(t_7.shape)
# print(v_hu_7[-10: -1])



# print(conf.head())
# print(hu_c.tail(7))

# print(t[-7: ])
print('\nDátum')
print(t_7[-7: ])

print('\nEsetek')
print(de_c[-7: ])

#print('\nEsetek / 100 000 fő')
#print(v_de_c_pop[-7: ])

print('\nÚj esetek 7 nap alatt')
print(v_de_7[-7: ])

#print('\nÚj esetek / 100 000 7 nap alatt')
#print(v_de_pop_7[-7: ])
'''

## Bokeh  ######################################################

hover = HoverTool(tooltips='@y', mode='vline')

p = figure(title='COVID 19', x_axis_label='Dátum', x_axis_type='datetime', y_axis_label='Esetek száma / 10 000 Fő', tools=[hover, 'crosshair'])

# p.background_fill_color='lightgreen'

p.line(t, conf.loc[countryes[0]], legend_label='Magyar betegek')
# p.line(t, v_hu_r_pop, legend_label='Magyar gyógyultak', line_dash='dashed', color='blue')
# p.line(t, v_hu_d_pop, legend_label='Magyar halottak', line_dash='dotted', color='black')
#
p.line(t, conf.loc[countryes[1]], legend_label='Német betegek')
#p.line(t, v_de_r_pop, legend_label='Német gyógyultak', line_dash='dashed', color='green')
#p.line(t, v_de_d_pop, legend_label='Német halottak', line_dash='dotted', color='orangered')

p.line(t, conf.loc[countryes[2], legend_label='Osztrák betegek')

p.legend.location = 'top_left'

show(p)



