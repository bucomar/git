import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

countryes = ['Hungary', 'Germany']
pop = [10, 83]
# pop = [1, 1]

url_c = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'

url_d = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'

url_r = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'

def prep(url):
    # Index=Countries, Columns=Datum, Values=Values
    df = pd.read_csv(url)
    df.set_index('Country/Region', inplace=True)
    df.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    return df


conf = prep(url_c)
death = prep(url_d)
rec = prep(url_r)

hu_c = conf.loc[countryes[0]]
# print(conf_hu)
hu_d = death.loc[countryes[0]]
hu_r = rec.loc[countryes[0]]

de_c = conf.loc[countryes[1]]
# print(conf_hu)
de_d = death.loc[countryes[1]]
de_r = rec.loc[countryes[1]]

# print(df_conf_hude.index)
# print(df_conf_hude.columns[4:])
# t = pd.to_datetime(conf.columns)

t = pd.to_datetime(hu_c.index)

v_hu_c = hu_c.values
v_hu_d = hu_d.values
v_hu_r = hu_r.values

v_de_c = de_c.values
v_de_d = de_d.values
v_de_r = de_r.values

plt.subplot(2, 2, 1)
plt.plot(t, v_hu_c, label='Beteg HU')
plt.plot(t, v_hu_d, label='Halott HU')
plt.plot(t, v_hu_r, label='Gyogyult HU')
plt.legend()

# plt.yscale('log')
plt.yscale('linear')

plt.suptitle('Koronavirus terjedese')
plt.xlabel('Datum')
plt.ylabel('Regisztralt esetek szama')


plt.subplot(2, 2, 2)
plt.plot(t, v_de_c, label='Beteg DE')
plt.plot(t, v_de_r, label='Gyogyult DE')
plt.plot(t, v_de_d, label='Halott DE')
plt.legend()

# plt.yscale('log')
plt.yscale('linear')

plt.suptitle('Koronavirus terjedese')
plt.xlabel('Datum')
plt.ylabel('Regisztralt esetek szama')

v_hu_c_pop = hu_c.values/pop[0]
v_hu_d_pop = hu_d.values/pop[0]
v_hu_r_pop = hu_r.values/pop[0]

v_de_c_pop = de_c.values/pop[1]
v_de_d_pop = de_d.values/pop[1]
v_de_r_pop = de_r.values/pop[1]



plt.subplot(2, 2, 3)
plt.plot(t, v_hu_c_pop, label='Beteg HU')
plt.plot(t, v_hu_d_pop, label='Halott HU')
plt.plot(t, v_hu_r_pop, label='Gyogyult HU')
plt.legend()

# plt.yscale('log')
plt.yscale('linear')

plt.suptitle('Koronavirus terjedese')
plt.xlabel('Datum')
plt.ylabel('Regisztralt esetek szama / Nepesseg / 1.000.000')


plt.subplot(2, 2, 4)
plt.plot(t, v_de_c_pop, label='Beteg DE')
plt.plot(t, v_de_r_pop, label='Gyogyult DE')
plt.plot(t, v_de_d_pop, label='Halott DE')
plt.legend()

# plt.yscale('log')
plt.yscale('linear')

plt.suptitle('Koronavirus terjedese')
plt.xlabel('Datum')
plt.ylabel('Regisztralt esetek szama / Nepesseg / 1.000.000')





# plt.subplot(1, 3, 2,)
# plt.bar(countryes, pop, width=0.3)
# plt.legend()

# countryes = ['Hungary', 'Germany']
# pop = [10, 83]


plt.show()

'''
'''
