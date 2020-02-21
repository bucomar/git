#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math as mt

## Épülethasználat fajtája
## Gebäudenutzungsart

k_set = np.array([
['Wohnehaus, Pension, Büro', 0.5],
['krankenhaus, Scjule, Restaurant, Hotel ', 0.7],
['öffendliche Toilet und Dusche', 1.0],
['special bz. Labor', 1.2]
])
print(k_set)
print()

# Szaniterek
# Sanytäranlagen

# Sanyter, DU, DN¶
# -, l/s, mm

san_set = np.array([
['wc', 2.0, 100],
['wt', 0.5, 50],
['de', 0.8, 70],
['wm', 0.8, 50],
['ks', 0.8, 50],
['gs', 0.8, 50]
])
print(san_set)
print()

## fg, dn, gf, qmax, v
## h/D, mm, cm/m, l/s, m/s

qmax_sl_set = np.array([
[0,5, 70, 1.0, 1.3, 0.6],
[0,5, 70, 1.5, 1.5, 0.7],
[0,5, 70, 2.0, 1.8, 0.8],
[0,5, 100, 1.0, 2.5, 0.7],
[0,5, 100, 1.5, 3.1, 0.8],
[0,5, 100, 2.0, 3.5, 1.0],
[0,5, 125, 1.0, 4.1, 0.8],
[0,5, 125, 1.5, 5.0, 1.0],
[0,5, 125, 2.0, 5.7, 1.1],
[0,5, 150, 1.0, 7.7, 0.9],
[0,5, 150, 1.5, 9.4, 0.1],
[0,5, 150, 2.0, 10.9, 0.3]
])
print(qmax_sl_set)
print()

## Strangok
## Falleitungen

### DN, Qmax
### mm, l/s

fl_set = np.array([
[70, 1.5],
[100, 4.0],
[125, 5.8],
[150, 9.5]
])
print(fl_set)
print()

#############################


def f_mm():
    # Main Menü    
    mm = input('Main menu \n'
              '1 - New Project \n'
              '2 - Load Project \n' 
              '0 - Exit Project \n \n')
    
    
    # prj == Projekt, Projektdatei    
    if mm == '1':
        prj = np.array([[1, 2,], [3, 4]])
        f_k()
        print('Project created. \n')
        print(prj, ' \n \n')
        f_pm()
    
    # read from csv
    elif mm == '2':
        print('Project loaded. \n \n')
        f_pm()
            
    elif mm == '0':
        print("Tschüß! \n \n")
        quit()
    
    else:
        print('Siehe instructionen!!! \n \n')
        f_mm()

def f_pm():
    # Projekt Menü
    pm = input('Project Menu \n'
             '1 - Add Falleitung \n'
             '2 - Add Sanitär \n'
             '9 - Save Project \n'
             '0 - Exit to Main Menu  \n \n')      
    
    if pm == '0':
        s = input('Sawe Project? \n'
        				'y - Sawe \n'
        				'n - Do not sawe \n \n')
        if s == 'y':
        	print('Project saved. \n \n')
        elif s == 'n':
        	print('Project dos not saved. \n \n')
        else:
        	print('Siehe instructionen!!! \n \n')
        	f_mm() 
        
        print('Return to Main Menu. \n \n')
        f_mm()
        
    elif pm == '1':
        print('Falleitung added. \n \n')
        f_pm()

    elif pm == '2':
        print('Sanytär added. \n \n')
        f_pm()

    elif pm == '9':
        #np.savetxt('prj.csv', arr2D, delimiter='\t', fmt='%d')
        print('Project saved. \n \n')
        f_pm()

def f_k():
    # k bestimmen
	#    k = input('Abflusskennzahl: \n'
	#             '1 - '+k_set[0,0]+': '+k_set[0,1]+' \n')


    k = input('Abflusskennzahl: \n'
             '1 - '+k_set[0,1]+': '+k_set[0,0]+' \n'+
             '2 - '+k_set[1,1]+': '+k_set[1,0]+' \n'+
             '3 - '+k_set[2,1]+': '+k_set[2,0]+' \n'+
             '4 - '+k_set[3,1]+': '+k_set[3,0]+' \n')

    print('k = ' + k)


# 
# #Save 2D numpy array to csv file
# #np.savetxt('2darray.csv', arr2D, delimiter=',', fmt='%d')

#def f_swf():
    #SW Falleitung
    #san =
    
## Szennyvíz elvezető berendezések
## Schmutzwassermenge

def f_qww(k, du):
    qww = float(k)*mt.sqrt(float(du))
    return qww 

#Start
f_mm()

