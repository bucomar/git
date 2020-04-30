# adatvesztes ellen
# from io import BytesIO
# from urllib.request import urlopen
from wget import download as dl
from zipfile import ZipFile as zip

url_nro = ('0005', '0010', '0015', '0020', '0030', '0045', '0060', '0090', '0120', '0180', '0240', '0360', '0540', '0720', '1080', '1440', '2880', '4320')

url = []

for i in range(len(url_nro)):
    url.append('https://opendata.dwd.de/climate_environment/CDC/grids_germany/return_periods/precipitation/KOSTRA/KOSTRA_DWD_2010R/asc/StatRR_KOSTRA-DWD-2010R_D'+url_nro[i]+'.csv.zip')

# def get_csv(url):
    # download, unzip, delet_zip
myzip = dl(url[3], './ew/temp')
with zip(myzip, 'r') as my_zip:
    my_zip.printdir()
    my_zip.extractall()
print()

# mycsv = myzip.exportall()
# print(zip.namelist(myzip))
    # # del_zip
    # zip.close(myzip)
    # print(mycsv)

    # return mycsv





# zipresp = dl(url[0])
# zfile = ZipFile(BytesIO(zipresp.read()))
# zfile.extractall('d'+url_nro[0])
