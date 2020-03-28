import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# url = 'https://data.humdata.org/hxlproxy/data/download/time_series-ncov-Confirmed.csv?dest=data_edit&filter01=explode&explode-header-att01=date&explode-value-att01=value&filter02=rename&rename-oldtag02=%23affected%2Bdate&rename-newtag02=%23date&rename-header02=Date&filter03=rename&rename-oldtag03=%23affected%2Bvalue&rename-newtag03=%23affected%2Binfected%2Bvalue%2Bnum&rename-header03=Value&filter04=clean&clean-date-tags04=%23date&filter05=sort&sort-tags05=%23date&sort-reverse05=on&filter06=sort&sort-tags06=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_19-covid-Confirmed.csv'

url_c = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'

# url_d = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'

# url_r = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'


#url = '/home/buco/github/git/COVID_19/time_series-ncov-Confirmed.csv'

# url = 'COVID_19/time_series-ncov-Confirmed.csv'

conf = pd.read_csv(url_c)
# death = pd.read_csv(url_d)
# rec = pd.read_csv(url_r)

df_conf = pd.DataFrame(conf)
# df_death = pd.DataFrame(death)
# df_rec = pd.DataFrame(rec)


# print(df_conf)
# print(df_conf.head(9))

# print 'head(): \n', df_cvd.head(9), '\n'
# print 'sample(): \n', df_cvd.sample(9), '\n'
# print 'tail(): \n', df_cvd.tail(9), '\n'


# df_conf_hude = pd.DataFrame(df_conf.loc[df_conf['Country/Region'] == 'Hungary'])

df_conf_hude = pd.DataFrame(df_conf.loc[df_conf['Country/Region'] == 'Hungary'])
# df.loc[(df["B"] > 50) & (df["C"] == 900), "A"]
print(df_conf_hude)

# print(df_conf_hude.index)
# print(df_conf_hude.columns[4:])
t = pd.to_datetime(df_conf_hude.columns[4:])
v = df_conf_hude.values[0, 4:]
# v = df_conf_hude.index[4:]


print(t)
print(v)


plt.plot(t, v)
plt.suptitle('Koronavirus terjedese Magyarorszagon')
plt.xlabel('Datum')
plt.ylabel('Regisztralt esetek szama')
plt.show()



# print 'len: \n', len(df_cvd), '\n'
# print 'describe(): \n', df_cvd.describe(), '\n'
# print 'sum(): \n', df_cvd.sum(), '\n'
# print 'count(): \n', df_cvd.count(), '\n'
# print 'median(): \n', df_cvd.median(), '\n'
# print 'quantile(): \n', df_cvd.quantile(), '\n'
# print 'min(): \n', df_cvd.min(), '\n'
# print 'max(): \n', df_cvd.max(), '\n'
# print 'mean(): \n', df_cvd.mean(), '\n'
