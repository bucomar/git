import pandas as pd

###	Gant diagramm for projektmanagement	###

HEAD = ['Name', 'Begin', 'End', 'Length']

##	def main menu - new, load, save, exit 
def main_menu():
	"""main menu with new, load, save, quit"""
	while True:
		
		print(
		'n : New\n'
		'l : Load\n'
		's : Save\n'
		'q : Quit\n'
		)
		to_do = input('What do You do?\n')
		if to_do == 'n':
			mm_new()

		elif to_do == 'l':
			mm_load()

		elif to_do == 's':
			mm_save()

		elif to_do == 'q':
			quit()
					
		else:
			print('No undestand! Select from the menu!\n')

##	def new 
def mm_new():
	"""make a new process""" 

	##	make en empty df for gant
	global df_processis
	df_processis = pd.DataFrame(columns = HEAD)
	print('\n', df_processis, '\n')
	menu()
	return df_processis

	
##	def load
def mm_load():
	"""Load from file"""
	print('Load\n')
	print('\n', df_processis, '\n')
	menu()
	
##	def sawe
def mm_save():
	"""Sawe to file"""
	print('Save\n')
	print('\n', df_processis, '\n')
	menu()

##	def exit
def mm_quit():
	"""Quit of programm"""
	print('Bay-bay!\n')
	quit()

##	def menu
def menu():
	""" Hier can you edit the processis"""
	while True:

		print(
		'+ : Add a process\n'
		'e : Edit a process\n'
		'- : Delete a process\n'
		'q : kuit to main menu\n'
		)
		to_do = input('What do You do?\n')
		if to_do == '+':
			m_new_proc()

		elif to_do == 'e':
			m_edit_proc()

		elif to_do == '-':
			m_del_proc()

		elif to_do == 'q':
			main_menu()
		
		else:
			print('No undestand! Select from the menu!\n')



def m_new_proc():
	""" New process wit user input"""
	NAME = input('Name of the process: ')
	BEGIN = input('Begin of the process: ')
	END = input('End of the process: ')
	LENGHT = input('Lenght of the process: ')

	df_process = pd.DataFrame([[NAME, BEGIN, END, LENGHT]], columns = HEAD, index = [NAME])
	
	global df_processis
	
	df_processis = pd.concat([df_processis, df_process])
	print('\n', df_processis, '\n')
	return df_processis

##	def szerk_feladat
def m_edit_proc():
	print('Edit process')
	print('\n', df_processis, '\n')
	menu()

##	def szerk_feladat
def m_del_proc():
	print('Delete process')
	print('\n', df_processis, '\n')
	menu()





main_menu()
