# adatvesztes ellen

import numpy as np
#import matplotlib.pyplot as plt

'''
['nev', 'mennyiseg', 'egyseg', 'norma', 'egysegar']
['str', float, 'str', float, float,]


tableten is megyen :{
'''

feladatok = np.array([
['nev', 'mennyiseg', 'egyseg', 'norma', 'egysegar'],
['feladat1', 2, 'db', 0.8, 567]
])
#dtype = [('nev', 'U25'), ('mennyiseg', 'f32'), ('egyseg', 'U25'), ('norma', 'f32'), ('egysegar', 'f32')]

# rezsioradij = input('Rezsioradij:')

while True:

	print(feladatok[1])

	#plt.plot(feladatok)
	#plt.show()


	print(
	'+ : hozzaad\n'
	'l : lista\n'
	'- : torol\n'
	'x : kilep'
	)
	mi_legyen = input('mi legyen?\n')
	if mi_legyen == '+':
		feladat_nev = input('A feladat neve: ')
		feladat_mennyiseg = input('mennyiseg: ')
		feladat_egyseg = input('egyseg: ')
		feladat_norma = input('norma: ')
		feladat_egysegar = input('egysegar: ')

		feladat_uj = np.array([[feladat_nev, feladat_mennyiseg, feladat_egyseg, feladat_norma, feladat_egysegar]])

		print(feladat_uj)
		print(type(feladat_uj))

		feladatok = np.append(feladatok, feladat_uj, axis=0)

		print(feladatok, '\n')

	elif mi_legyen == 'l':
		print(feladatok, '\n')

	elif mi_legyen == '-':
		print('Melyik tevekenyseget toroli?')
		print(feladatok, '\n')

	elif mi_legyen == 'x':
		break

print(feladatok)
