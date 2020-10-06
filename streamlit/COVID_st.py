import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool



st.markdown(
'''
# Hello!
## Ez egy grafikon lesz.
### Türelem...
Hogy ne unatkozz, adig leírom, mi megy a háttérben:

Adatforrások definiálása.    
Az adatok innen származnak: 
https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases
Felesleges oszlopok eltávolítása.  
Kiválogatjuk az országokra vonatkozó sorokat.  
Itt most Magyarország és Németország adatait gyüjtögetem ki.  
Időskálát is készítünk.  
Itt ez úgy történik, hogy az egyik DataFrame dátum fejlécét dátumokká alakítom.  
Kiszedem az értékeket teljes lakosságra és 10000 főre vetítve is.  
Meghatározom, hogy az értékeket is mutassa a grafikonon.  
Meghatározom a megjelenítendő koordinátarendszert.  
Meghatározom a grafikonokat.  
A magyarázat fent lesz balra.  
És a grafikon...  
Köszönöm a figyelmet, és a kitartást!  
'''
)

countryes = ['Hungary', 'Germany']

pops = [1000, 8300]

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

v_hu_c_pop = hu_c.values/pops[0]
v_hu_d_pop = hu_d.values/pops[0]
v_hu_r_pop = hu_r.values/pops[0]

v_de_c_pop = de_c.values/pops[1]
v_de_d_pop = de_d.values/pops[1]
v_de_r_pop = de_r.values/pops[1]

hover = HoverTool(tooltips='@y', mode='vline')

p = figure(title='COVID 19', x_axis_label='Dátum', x_axis_type='datetime', y_axis_label='Esetek száma / 10 000 Fő', tools=[hover, 'crosshair'])

# p.background_fill_color='lightgreen'

# p.line(t, v_hu_c, legend_label='Magyar betegek', color='red')
# p.line(t, v_hu_r, legend_label='Magyar gyógyultak', line_dash='dashed', color='blue')
# p.line(t, v_hu_d, legend_label='Magyar halottak', line_dash='dotted', color='black')
# 
# p.line(t, v_de_c, legend_label='Német betegek', color='purple')
# p.line(t, v_de_r, legend_label='Német gyógyultak', line_dash='dashed', color='green')
# p.line(t, v_de_d, legend_label='Német halottak', line_dash='dotted', color='orangered')


p.line(t, v_hu_c_pop, legend_label='Magyar betegek', color='red')
p.line(t, v_hu_r_pop, legend_label='Magyar gyógyultak', line_dash='dashed', color='blue')
p.line(t, v_hu_d_pop, legend_label='Magyar halottak', line_dash='dotted', color='black')
#
p.line(t, v_de_c_pop, legend_label='Német betegek', color='purple')
p.line(t, v_de_r_pop, legend_label='Német gyógyultak', line_dash='dashed', color='green')
p.line(t, v_de_d_pop, legend_label='Német halottak', line_dash='dotted', color='orangered')

p.legend.location = 'top_left'

st.bokeh_chart(p)
