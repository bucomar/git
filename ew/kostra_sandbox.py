import requests, zipfile, io
import pandas as pd

URL='https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D0005.csv.zip'

def get_csv_df(url):
    print('Türelem! Dolgozok')
    r = requests.get(URL)
    type(r)

    z = zipfile.ZipFile(io.BytesIO(r.content))
    type(z)

    csv = z.open('StatRR_KOSTRA-DWD-2010R_D0005.csv')
    type(csv)

    df = pd.read_csv(csv)
    return df

get_csv_df(URL)
