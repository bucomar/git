
import pandas as pd
# import numpy as np
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool

countryes = ['Hungary', 'Germany']
pop = [1000, 8300]
# pop = [1, 1]

url_c = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'

url_d = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'

url_r = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'


def prep(url):
    """Index=Countries, Columns=Datum, Values=Values."""
    df = pd.read_csv(url)
    df.set_index('Country/Region', inplace=True)
    df.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    return df


conf = prep(url_c)
death = prep(url_d)
rec = prep(url_r)

hu_c = conf.loc[countryes[0]]
hu_d = death.loc[countryes[0]]
hu_r = rec.loc[countryes[0]]

de_c = conf.loc[countryes[1]]
de_d = death.loc[countryes[1]]
de_r = rec.loc[countryes[1]]

t = pd.to_datetime(hu_c.index)
# Adatok tengelyekre:

v_hu_c = hu_c.values
v_hu_d = hu_d.values
v_hu_r = hu_r.values

v_de_c = de_c.values
v_de_d = de_d.values
v_de_r = de_r.values

v_hu_c_pop = hu_c.values/pop[0]
v_hu_d_pop = hu_d.values/pop[0]
v_hu_r_pop = hu_r.values/pop[0]

v_de_c_pop = de_c.values/pop[1]
v_de_d_pop = de_d.values/pop[1]
v_de_r_pop = de_r.values/pop[1]

hover = HoverTool(tooltips='@y', mode='vline')

p = figure(title='COVID 19', x_axis_label='Dátum', x_axis_type='datetime', y_axis_label='Esetek száma / 10 000 Fő', tools=[hover, 'crosshair'])

# p.background_fill_color='lightgreen'

# p.line(t, v_hu_c, legend_label='Magyar betegek', color='red')
# p.line(t, v_hu_r, legend_label='Magyar gyógyultak', color='blue')
# p.line(t, v_hu_d, legend_label='Magyar halottak', color='black')
#
# p.line(t, v_de_c, legend_label='Német betegek', color='purple')
# p.line(t, v_de_r, legend_label='Német gyógyultak', color='green')
# p.line(t, v_de_d, legend_label='Német halottak', color='orangered')


p.line(t, v_hu_c_pop, legend_label='Magyar betegek', color='red')
p.line(t, v_hu_r_pop, legend_label='Magyar gyógyultak', line_dash='dashed', color='blue')
p.line(t, v_hu_d_pop, legend_label='Magyar halottak', line_dash='dotted', color='black')
#
p.line(t, v_de_c_pop, legend_label='Német betegek', color='purple')
p.line(t, v_de_r_pop, legend_label='Német gyógyultak', line_dash='dashed', color='green')
p.line(t, v_de_d_pop, legend_label='Német halottak', line_dash='dotted', color='orangered')

p.legend.location = 'top_left'

output_file('./COVID_19/templates/COVID_19.html')

show(p)
