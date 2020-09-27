# COVID 19 grafikon Pythonnal meg Jupyter Notebook-kal

Szükséges csomagok importálása.


```python
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import output_file, show
from bokeh.models import HoverTool
from bokeh.io import output_notebook
```
Országok és lakosságuk.

```python
countryes = ['Hungary', 'Germany']
pop = [1000, 8300]

print(countryes)
print(pop)
```

    ['Hungary', 'Germany']
    [1000, 8300]


Adatforrások
https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases


```python
url_c = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_confirmed_global.csv&filename=time_series_covid19_confirmed_global.csv'
url_d = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_deaths_global.csv&filename=time_series_covid19_deaths_global.csv'
url_r = 'https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_covid19_recovered_global.csv&filename=time_series_covid19_recovered_global.csv'
```

Felesleges oszlopok eltávolítása.


```python
def prep(url):
    # Index=Countries, Columns=Datum, Values=Values
    df = pd.read_csv(url)
    df.set_index('Country/Region', inplace=True)
    df.drop(columns=['Province/State', 'Lat', 'Long'], inplace=True)
    return df


conf = prep(url_c)
death = prep(url_d)
rec = prep(url_r)

print(conf.head())
print(death.head())
print(rec.head())
```

                    1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  \
    Country/Region                                                                  
    Afghanistan           0        0        0        0        0        0        0   
    Albania               0        0        0        0        0        0        0   
    Algeria               0        0        0        0        0        0        0   
    Andorra               0        0        0        0        0        0        0   
    Angola                0        0        0        0        0        0        0   
    
                    1/29/20  1/30/20  1/31/20  ...  9/17/20  9/18/20  9/19/20  \
    Country/Region                             ...                              
    Afghanistan           0        0        0  ...    38872    38883    38919   
    Albania               0        0        0  ...    11948    12073    12226   
    Algeria               0        0        0  ...    49194    49413    49623   
    Andorra               0        0        0  ...     1483     1564     1564   
    Angola                0        0        0  ...     3789     3848     3901   
    
                    9/20/20  9/21/20  9/22/20  9/23/20  9/24/20  9/25/20  9/26/20  
    Country/Region                                                                 
    Afghanistan       39044    39074    39096    39145    39170    39186    39192  
    Albania           12385    12535    12666    12787    12921    13045    13153  
    Algeria           49826    50023    50214    50400    50579    50754    50914  
    Andorra            1564     1681     1681     1753     1753     1836     1836  
    Angola             3991     4117     4236     4363     4475     4590     4672  
    
    [5 rows x 249 columns]
                    1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  \
    Country/Region                                                                  
    Afghanistan           0        0        0        0        0        0        0   
    Albania               0        0        0        0        0        0        0   
    Algeria               0        0        0        0        0        0        0   
    Andorra               0        0        0        0        0        0        0   
    Angola                0        0        0        0        0        0        0   
    
                    1/29/20  1/30/20  1/31/20  ...  9/17/20  9/18/20  9/19/20  \
    Country/Region                             ...                              
    Afghanistan           0        0        0  ...     1436     1437     1437   
    Albania               0        0        0  ...      347      353      358   
    Algeria               0        0        0  ...     1654     1659     1665   
    Andorra               0        0        0  ...       53       53       53   
    Angola                0        0        0  ...      144      147      147   
    
                    9/20/20  9/21/20  9/22/20  9/23/20  9/24/20  9/25/20  9/26/20  
    Country/Region                                                                 
    Afghanistan        1441     1444     1445     1446     1451     1451     1453  
    Albania             362      364      367      370      370      373      375  
    Algeria            1672     1679     1689     1698     1703     1707     1711  
    Andorra              53       53       53       53       53       53       53  
    Angola              152      154      155      159      162      167      171  
    
    [5 rows x 249 columns]
                    1/22/20  1/23/20  1/24/20  1/25/20  1/26/20  1/27/20  1/28/20  \
    Country/Region                                                                  
    Afghanistan           0        0        0        0        0        0        0   
    Albania               0        0        0        0        0        0        0   
    Algeria               0        0        0        0        0        0        0   
    Andorra               0        0        0        0        0        0        0   
    Angola                0        0        0        0        0        0        0   
    
                    1/29/20  1/30/20  1/31/20  ...  9/17/20  9/18/20  9/19/20  \
    Country/Region                             ...                              
    Afghanistan           0        0        0  ...    32505    32576    32576   
    Albania               0        0        0  ...     6788     6831     6888   
    Algeria               0        0        0  ...    34675    34818    34923   
    Andorra               0        0        0  ...     1054     1164     1164   
    Angola                0        0        0  ...     1405     1443     1445   
    
                    9/20/20  9/21/20  9/22/20  9/23/20  9/24/20  9/25/20  9/26/20  
    Country/Region                                                                 
    Afghanistan       32576    32576    32576    32610    32619    32619    32635  
    Albania            6940     6995     7042     7139     7239     7309     7397  
    Algeria           35047    35180    35307    35428    35544    35654    35756  
    Andorra            1164     1199     1199     1203     1203     1263     1263  
    Angola             1445     1449     1462     1473     1503     1554     1639  
    
    [5 rows x 249 columns]


Kiválogatjuk az országokra vonatkozó sorokat.
Itt most Magyarország és Németország adatait gyüjtögetem ki.


```python
hu_c = conf.loc[countryes[0]]
hu_d = death.loc[countryes[0]]
hu_r = rec.loc[countryes[0]]

de_c = conf.loc[countryes[1]]
de_d = death.loc[countryes[1]]
de_r = rec.loc[countryes[1]]

print(hu_c)
print(hu_d)
print(hu_r)
print(de_c)
print(de_d)
print(de_r)
```

    1/22/20        0
    1/23/20        0
    1/24/20        0
    1/25/20        0
    1/26/20        0
               ...  
    9/22/20    19499
    9/23/20    20450
    9/24/20    21200
    9/25/20    22127
    9/26/20    23077
    Name: Hungary, Length: 249, dtype: int64
    1/22/20      0
    1/23/20      0
    1/24/20      0
    1/25/20      0
    1/26/20      0
              ... 
    9/22/20    694
    9/23/20    702
    9/24/20    709
    9/25/20    718
    9/26/20    730
    Name: Hungary, Length: 249, dtype: int64
    1/22/20       0
    1/23/20       0
    1/24/20       0
    1/25/20       0
    1/26/20       0
               ... 
    9/22/20    4559
    9/23/20    4644
    9/24/20    4818
    9/25/20    4945
    9/26/20    5099
    Name: Hungary, Length: 249, dtype: int64
    1/22/20         0
    1/23/20         0
    1/24/20         0
    1/25/20         0
    1/26/20         0
                ...  
    9/22/20    277412
    9/23/20    279025
    9/24/20    281346
    9/25/20    283712
    9/26/20    285026
    Name: Germany, Length: 249, dtype: int64
    1/22/20       0
    1/23/20       0
    1/24/20       0
    1/25/20       0
    1/26/20       0
               ... 
    9/22/20    9405
    9/23/20    9423
    9/24/20    9436
    9/25/20    9451
    9/26/20    9459
    Name: Germany, Length: 249, dtype: int64
    1/22/20         0
    1/23/20         0
    1/24/20         0
    1/25/20         0
    1/26/20         0
                ...  
    9/22/20    244693
    9/23/20    245706
    9/24/20    247766
    9/25/20    249164
    9/26/20    250104
    Name: Germany, Length: 249, dtype: int64


Időskálát is készítünk.
Itt ez úgytörténik, hogy az egyik DataFrame dátum fejlécét dátumokká alakítom.


```python
t = pd.to_datetime(hu_c.index)

print(t)
```

    DatetimeIndex(['2020-01-22', '2020-01-23', '2020-01-24', '2020-01-25',
                   '2020-01-26', '2020-01-27', '2020-01-28', '2020-01-29',
                   '2020-01-30', '2020-01-31',
                   ...
                   '2020-09-17', '2020-09-18', '2020-09-19', '2020-09-20',
                   '2020-09-21', '2020-09-22', '2020-09-23', '2020-09-24',
                   '2020-09-25', '2020-09-26'],
                  dtype='datetime64[ns]', length=249, freq=None)


Kiszedem az értékeket teljes lakosságra és 10000 főre vetítve is.


```python
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

print(v_hu_c)
print(v_hu_d)
print(v_hu_r)
print('stb...')
print()
print()
```

    [    0     0     0     0     0     0     0     0     0     0     0     0
         0     0     0     0     0     0     0     0     0     0     0     0
         0     0     0     0     0     0     0     0     0     0     0     0
         0     0     0     0     0     0     2     2     2     4     7     9
         9    13    13    19    30    32    39    50    58    73    85   103
       131   167   187   226   261   300   343   408   447   492   525   585
       623   678   733   744   817   895   980  1190  1310  1410  1458  1512
      1579  1652  1763  1834  1916  1984  2098  2168  2284  2443  2443  2500
      2583  2649  2727  2775  2863  2942  2998  3035  3065  3111  3150  3178
      3213  3263  3284  3313  3341  3380  3417  3473  3509  3535  3556  3598
      3641  3678  3713  3741  3756  3771  3793  3816  3841  3867  3876  3892
      3921  3931  3954  3970  3990  4008  4014  4017  4027  4039  4053  4064
      4069  4076  4077  4078  4079  4081  4086  4094  4102  4107  4114  4123
      4127  4138  4142  4145  4155  4157  4166  4172  4174  4183  4189  4205
      4210  4220  4223  4229  4234  4247  4258  4263  4279  4293  4315  4333
      4339  4347  4366  4380  4398  4424  4435  4448  4456  4465  4484  4505
      4526  4535  4544  4553  4564  4597  4621  4653  4696  4731  4746  4768
      4813  4853  4877  4916  4946  4970  5002  5046  5098  5133  5155  5191
      5215  5288  5379  5511  5669  5961  6139  6257  6622  6923  7382  7892
      8387  8963  9304  9715 10191 10909 11825 12309 13153 13879 14460 15170
     16111 16920 17990 18866 19499 20450 21200 22127 23077]
    [  0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
       0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
       0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1
       1   1   1   1   3   4   6   7   9  10  10  10  11  13  15  16  20  21
      26  32  34  38  47  58  66  77  85  99 109 122 134 142 156 172 189 199
     213 225 239 262 262 272 280 291 300 312 323 335 340 351 363 373 383 392
     405 413 421 425 430 436 442 448 451 462 467 470 473 476 482 486 491 499
     505 509 517 524 526 527 532 534 539 542 545 546 548 550 551 553 555 559
     562 563 565 567 568 568 570 570 572 573 576 577 578 578 581 585 585 586
     587 588 589 589 589 589 589 591 593 595 595 595 595 595 595 595 596 596
     596 596 596 596 596 596 596 596 596 596 596 596 597 597 597 598 599 600
     602 602 602 605 605 605 607 607 607 608 608 609 609 609 611 611 613 613
     614 614 614 614 614 614 615 616 619 620 621 624 624 625 626 628 630 631
     633 637 642 646 654 663 669 675 683 686 694 702 709 718 730]
    [   0    0    0    0    0    0    0    0    0    0    0    0    0    0
        0    0    0    0    0    0    0    0    0    0    0    0    0    0
        0    0    0    0    0    0    0    0    0    0    0    0    0    0
        0    0    0    0    0    0    0    0    0    0    1    1    1    2
        2    2    2    7   16   16   21   21   28   34   34   34   34   37
       40   42   43   58   66   67   71   94   96  112  115  118  120  122
      192  199  207  231  250  267  287  295  390  458  458  485  498  516
      536  581  609  625  629  630  709  759  801  865  904  933  958 1007
     1102 1169 1287 1371 1396 1400 1412 1454 1509 1587 1655 1690 1711 1836
     1856 1996 2024 2142 2147 2156 2160 2190 2205 2245 2279 2279 2284 2324
     2355 2391 2447 2476 2482 2485 2516 2547 2564 2581 2585 2589 2590 2600
     2618 2640 2663 2681 2685 2685 2692 2714 2721 2752 2784 2811 2860 2874
     2885 2887 2941 2974 3036 3073 3106 3126 3156 3220 3222 3223 3232 3257
     3283 3300 3312 3324 3329 3329 3331 3339 3346 3353 3364 3389 3413 3415
     3431 3463 3464 3491 3499 3525 3527 3529 3561 3590 3606 3623 3630 3631
     3665 3678 3681 3692 3695 3695 3716 3734 3757 3759 3759 3759 3761 3821
     3903 3930 3944 3952 3958 3961 3972 3984 3990 4014 4058 4069 4117 4130
     4153 4227 4240 4382 4391 4401 4559 4644 4818 4945 5099]
    stb...
    
    


A grafikont itt a notebookban szeretnénk megjeleníteni.


```python
output_notebook()
```



<div class="bk-root">
    <a href="https://bokeh.org" target="_blank" class="bk-logo bk-logo-small bk-logo-notebook"></a>
    <span id="1001">Loading BokehJS ...</span>
</div>




Meghatározom, hogy az értékeket is mutassa a grafikonon.


```python
hover = HoverTool(tooltips='@y', mode='vline')
```

Meghatározom a megjelenítendő koordinátarendszert.


```python
p = figure(title='COVID 19', x_axis_label='Dátum', x_axis_type='datetime', y_axis_label='Esetek száma / 10 000 Fő', tools=[hover, 'crosshair'])
```

Meghatározom a grafikonokat.


```python
p.line(t, v_hu_c_pop, legend_label='Magyar betegek', color='red')
p.line(t, v_hu_r_pop, legend_label='Magyar gyógyultak', line_dash='dashed', color='blue')
p.line(t, v_hu_d_pop, legend_label='Magyar halottak', line_dash='dotted', color='black')

p.line(t, v_de_c_pop, legend_label='Német betegek', color='purple')
p.line(t, v_de_r_pop, legend_label='Német gyógyultak', line_dash='dashed', color='green')
p.line(t, v_de_d_pop, legend_label='Német halottak', line_dash='dotted', color='orangered')

```




<div style="display: table;"><div style="display: table-row;"><div style="display: table-cell;"><b title="bokeh.models.renderers.GlyphRenderer">GlyphRenderer</b>(</div><div style="display: table-cell;">id&nbsp;=&nbsp;'1175', <span id="1208" style="cursor: pointer;">&hellip;)</span></div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">data_source&nbsp;=&nbsp;ColumnDataSource(id='1172', ...),</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">glyph&nbsp;=&nbsp;Line(id='1173', ...),</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">hover_glyph&nbsp;=&nbsp;None,</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">js_event_callbacks&nbsp;=&nbsp;{},</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">js_property_callbacks&nbsp;=&nbsp;{},</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">level&nbsp;=&nbsp;'glyph',</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">muted&nbsp;=&nbsp;False,</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">muted_glyph&nbsp;=&nbsp;None,</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">name&nbsp;=&nbsp;None,</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">nonselection_glyph&nbsp;=&nbsp;Line(id='1174', ...),</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">selection_glyph&nbsp;=&nbsp;None,</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">subscribed_events&nbsp;=&nbsp;[],</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">tags&nbsp;=&nbsp;[],</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">view&nbsp;=&nbsp;CDSView(id='1176', ...),</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">visible&nbsp;=&nbsp;True,</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">x_range_name&nbsp;=&nbsp;'default',</div></div><div class="1207" style="display: none;"><div style="display: table-cell;"></div><div style="display: table-cell;">y_range_name&nbsp;=&nbsp;'default')</div></div></div>
<script>
(function() {
  var expanded = false;
  var ellipsis = document.getElementById("1208");
  ellipsis.addEventListener("click", function() {
    var rows = document.getElementsByClassName("1207");
    for (var i = 0; i < rows.length; i++) {
      var el = rows[i];
      el.style.display = expanded ? "none" : "table-row";
    }
    ellipsis.innerHTML = expanded ? "&hellip;)" : "&lsaquo;&lsaquo;&lsaquo;";
    expanded = !expanded;
  });
})();
</script>




A magyarázat fent lesz balra.


```python
p.legend.location='top_left'
```

Ha lementenénk, akkor így tennénk.


```python
#output_file('./COVID_19/templates/COVID_19.html')
```

És a grafikon...


```python
show(p)
```








<div class="bk-root" id="da7bf788-75ce-4575-a681-8c7b67f15a0f" data-root-id="1003"></div>






