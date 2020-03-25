import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


url = 'https://data.humdata.org/hxlproxy/data/download/time_series-ncov-Confirmed.csv?dest=data_edit&filter01=explode&explode-header-att01=date&explode-value-att01=value&filter02=rename&rename-oldtag02=%23affected%2Bdate&rename-newtag02=%23date&rename-header02=Date&filter03=rename&rename-oldtag03=%23affected%2Bvalue&rename-newtag03=%23affected%2Binfected%2Bvalue%2Bnum&rename-header03=Value&filter04=clean&clean-date-tags04=%23date&filter05=sort&sort-tags05=%23date&sort-reverse05=on&filter06=sort&sort-tags06=%23country%2Bname%2C%23adm1%2Bname&tagger-match-all=on&tagger-default-tag=%23affected%2Blabel&tagger-01-header=province%2Fstate&tagger-01-tag=%23adm1%2Bname&tagger-02-header=country%2Fregion&tagger-02-tag=%23country%2Bname&tagger-03-header=lat&tagger-03-tag=%23geo%2Blat&tagger-04-header=long&tagger-04-tag=%23geo%2Blon&header-row=1&url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_19-covid-Confirmed.csv'

#url = '/home/buco/github/git/COVID_19/time_series-ncov-Confirmed.csv'
# url = 'COVID_19/time_series-ncov-Confirmed.csv'

cvd = pd.read_csv(url)

df_cvd = pd.DataFrame(cvd)

# print(df_cvd)
# print(df_cvd.head())

# print 'head(): \n', df_cvd.head(9), '\n'
# print 'sample(): \n', df_cvd.sample(9), '\n'
# print 'tail(): \n', df_cvd.tail(9), '\n'

# print(df_cvd.loc[df_cvd['Country/Region'] == 'Hungary'])
df_hu = pd.DataFrame(df_cvd.loc[df_cvd['Country/Region'] == 'Hungary'])
print(df_hu)
# print(type(df_hu['Date'][1]))
# print(df_hu['Date'])
# print(type(df_hu['Value']))

t = df_hu['Date']
v = df_hu['Value']

# df['DOB'] = pd.to_datetime(df['DOB'])

# t = [1, 2, 3]
# v = [4, 5, 6]
# np_t = np.array(t)
# np_v = np.array(v)

# print(v)
# print(t)

t = pd.to_datetime(df_hu['Date'])
v = pd.to_numeric(df_hu['Value'])

plt.plot(t, v)
plt.show()

#pd.df_hu.plot.density(self, bw_method=None, ind=None, **kwargs)

# print 'len: \n', len(df_cvd), '\n'
# print 'describe(): \n', df_cvd.describe(), '\n'
# print 'sum(): \n', df_cvd.sum(), '\n'
# print 'count(): \n', df_cvd.count(), '\n'
# print 'median(): \n', df_cvd.median(), '\n'
# print 'quantile(): \n', df_cvd.quantile(), '\n'
# print 'min(): \n', df_cvd.min(), '\n'
# print 'max(): \n', df_cvd.max(), '\n'
# print 'mean(): \n', df_cvd.mean(), '\n'
