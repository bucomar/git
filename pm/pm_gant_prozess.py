##	A	folyamat


# rezsioradij = input('Rezsioradij:')

def menu():
	while True:

		print('df_feladatok')

		print(
		'+ : hozzaad\n'
		'l : lista\n'
		'- : torol\n'
		'x : kilep\n'
		)
		mi_legyen = input('mi legyen?\n')
		if mi_legyen == '+':
			print('uj_feladat()')

		#elif mi_legyen == 'l':
			#print(feladatok, '\n')

		elif mi_legyen == '-':
			print('torol_feladat()\n')

		elif mi_legyen == 'x':
			print('main_menu()\n')
			break
		
		else:
			print('Nem ertem! Valassz a listabol!\n')

menu()