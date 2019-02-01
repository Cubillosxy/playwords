# -*- coding: utf-8 -*-
#Importamos Librerias 


"""

-add midificar eliminar

"""
try: #Python 2.x
	try:
		from ConfigParser import ConfigParser
	except ImportError:
		from configparser import ConfigParser
	import random
	from Tkinter import Tk
	from Tkinter import Frame
	from Tkinter import StringVar
	from Tkinter import Menu
	from Tkinter import PhotoImage
	from Tkinter import Button
	from Tkinter import Label
	from Tkinter import Entry
	from Tkinter import HORIZONTAL
	from Tkinter import TOP
	from Tkinter import BOTH
	from Tkinter import BOTTOM
	import ttk
	import tkMessageBox
	import sys
	reload(sys)
	sys.setdefaultencoding('utf-8')

except ImportError:
	# Python 3
	from configparser import ConfigParser
	import Random

import re


__version__ = '1.3'


class Dicc:
	def __init__(self):
		# Creamos una instancia de la clase y abrimos el archivo
		self.config = ConfigParser()
		self._filename = 'dicc.cfg'
		self.sections = None
		self.config.read(self._filename)
		sections = self.config.sections() 

		val = len(sections)

		try:
			self.config.getint("INDICE", "cant")
			self.config.set("INDICE", "cant", str(val-1))
			with open(self._filename, "w") as f:
				self.config.write(f)
		except Exception as e:
			print(repr(e))
			self.config.add_section("INDICE")   # add word
			self.config.set("INDICE", "cant", "0")
			with open(self._filename, "w") as f:
				self.config.write(f)

	@staticmethod
	def remove_space(word):
		word = word.replace(' ', '').lower() 
		return word

	def write(self, word, args):

		ind = self.config.getint("INDICE", "cant")
		sections = self.config.sections() 

		word = self.remove_space(word)  # llamamos
	
		# Buscamos para ver si ya existe
		if word in sections:
			items = self.config.items(word)
			pointer = len(items)
			items_spanish = [i[1] for i in items]

			count_modifications = 0
			for i in args:
				if i not in items_spanish:
					pointer_cfg = 'word{}'.format(pointer + count_modifications)
					self.config.set(word, pointer_cfg, i)
					count_modifications += 1

			response = {
				'title': 'Ok edit',
				'message': 'The new meanings were added correctly: {}'.format(count_modifications),
			}

			if not count_modifications:
				response = {
					'title': 'Error',
					'message': 'There was no modification for current word: \n   {}'.format(word),
				}

		else:
			# Modificar Indice
			self.config.set("INDICE", "cant", str(ind + 1))
			self.config.add_section(word)  # adicionamos palabra
			cont = 0

			response = {'title': 'OK', 'message': 'Se agrego correctamente \n   {}'.format(word)}

			for i in args:	 # para cada significado haga
				i = self.remove_space(i)
				self.config.set(word, 'word{}'.format(cont), i)
				cont += 1

		with open(self._filename, "w") as f:
			self.config.write(f)
		return response

	def read(self, num):
		sections = self.config.sections()
		word_in_dicc = sections[num]
		list1 = [word_in_dicc]

		for item in self.config.items(word_in_dicc):
			# read text (word0, 'myword')
			list1.append(item[1])

		return list1

	def numdicc(self):
		ind = self.config.getint("INDICE", "cant")
		self.sections = self.config.sections()
		return len(self.sections) - 1


#  funcion de menu versión
def ver():
	tkMessageBox.showinfo(
		title="Versión {}".format(__version__),
		message="Play Words \nDeveloped by: Edwin Cubillos  -> github.com/Cubillosxy \n Made in Monterrey,Colombia "
	)


#  función de menú instruciones
def instru():
	tkMessageBox.showinfo(
		title="Instrucciones",
		message="-Escribe el significado de la palabra y presiona enter para validar \n -Para agregar nuevas palabras , "
		"ingresa la palabra y sus significados después da clic en guardar \n - "
	)


def reset_all():
	global lis_dif
	global lis_ind_d
	global lis_bien
	global cont_var
	global lis_rep
	lis_dif = []
	lis_ind_d = []
	lis_bien = []
	lis_rep = []
	cont_var = 0

	print("Juego reiniciado")

	tkMessageBox.showinfo(title="Vuelve a iniciar :)", message=" Los valores han sido reseteados  ")


def get_num_not_repeat(max1, list_ok):
	"""
	:param max1:  limit of iterations
	:param list_ok: array for check not repeat
	:return: random num that not exist in array
	"""
	num = random.randint(1, max1)
	size = len(list_ok)
	loop = True
	if size:
		watchdog = 0
		while loop:
			watchdog += 1
			if watchdog == max1:
				loop = False		# para evitar bucle infinito cuando se completen todas las palabras
			else:
				for i in list_ok:
					loop = False
					if int(i) == num:
						loop = True
						num = random.randint(1, max1)
						break  # break for loop

	return num 


def cal_pro(b_n, m_n, limit, rep):
	"""
	:param b_n: palabras correctas
	:param m_n:
	:param limit:
	:param rep: lista de palabras repetidas
	:return:
	"""
	res = 15

	if m_n >= b_n:
		res = 40
	else:
		v1 = b_n - m_n + 1 - rep
		res = v1 * 100 / limit

	res = 125 - res
	if res < 1:
		res = 1
	return res


def pra(dicc, resp, n_actual):
	"""
		dicc: clase con dicc
		resp: user answer
		n_actual: index in dicc
		Funcion para practicar, recive la respuesta, y la palabr actual
	"""
	global eng_play
	global num_a
	global lis_dif
	global lis_ind_d
	global lis_bien
	global cont_var
	global lis_rep
	global esp_res
	num_w = dicc.numdicc()  # must be > 1 for avoid errors
	bol = search_num(resp)
	_result = False
	cont_var = 1 + cont_var

	# calculo de probailidad
	prob = cal_pro(len(lis_bien), len(lis_ind_d), num_w, len(lis_rep))
	print("La probailidad es ", (100-prob), " %")

	if cont_var > 40:
		cont_var = 0
		print("Reset contador")

	if resp and bol:
		resp = dicc.remove_space(resp)  # elimminamos espacio
		resp = split_result(resp)    # si hay comas separamos en vector
		_word = dicc.read(n_actual)
		_result = comp_cade(_word, resp)

		print(_word, " w actul")
		print("numero inte ", cont_var)

		_agg = True
		if _result:

			# guardamos lo que van bien para que no salgan
			lis_bien.append(str(n_actual))
			esp_res.set("")
			if num_w > 1:
				l_lisdi = len(lis_dif)
				if l_lisdi > 0:
					selec = random.randint(1, 100)  # porcentaje de veces que saldra la lista de errores
					if selec > prob:
						print(selec, "no azar")
						ind_noazar = random.randint(0, (l_lisdi-1))
						num_a = int(lis_ind_d[ind_noazar])
						lis_rep.append("1")
					else:
						num_a = get_num_not_repeat(num_w, lis_bien)
						cont_var -= 1
				else:
					num_a = get_num_not_repeat(num_w, lis_bien)
					cont_var -= 1
					
				word = dicc.read(num_a)   # leemos lista en el dicc
				eng_play.set(word[0].upper())
			else:
				eng_play.set("No hay palabras")
		else:
			tkMessageBox.showinfo(
				title="Incorrecto :(",
				message="No coincide con  ningúna palabra \n  **para saltar la palabra deja en blanco la respuesta "
			)
			lis_dif.append(_word[0])
			lis_ind_d.append(str(n_actual))
	elif num_w > 1:
		num_a = random.randint(1, num_w)
		word = dicc.read(num_a)
		eng_play.set(word[0].upper())
	else:
		eng_play.set("No hay palabras")


def comp_cade(_word, resp):
	for i in range(1, len(_word)):
		if isinstance(resp, list):
			if _word[i] in resp:
				return True
		elif resp == _word[i]:
			return True
	return False


def search_num(word):
	#  retorna verdadero si no contiene numeros
	return not bool(re.search(r'\d', word))


def split_result(word):
	return list(set(filter(None, word.split(","))))


def w_write(dicc_class, eng, spa):
	"""
	Escribe en archivo
	"""
	bol = search_num(eng)
	bol2 = search_num(spa)

	if eng and spa and bol and bol2:

		spa = split_result(spa)
		eng = split_result(eng)
		
		for word_eng in eng:
			write_word_result = dicc_class.write(word_eng, spa)
			tkMessageBox.showinfo(**write_word_result)

	else:
		tkMessageBox.showinfo(
			title='Error',
			message='No puedes ingresar valores vacios ni números \n      {}\n     {}'.format(eng, spa)
		)


# captura de teclas
def key(event):

	cap = (repr(event.char))
	if cap == repr('\r'):
		pra(mygame, esp_res.get(), num_a)
	elif cap == repr('0'):
		reset_all()


def main():

	# interfaz
	raiz = Tk()
	raiz.title("LEARN WORDS  V{}".format(__version__))
	width = 240
	higth = 460
	raiz.geometry(str(width)+"x"+str(higth))
	# raiz.configure(background='white')

	h_pc = raiz.winfo_screenheight()
	w_pc = raiz.winfo_screenwidth()
	raiz.geometry("+%d+%d" % ((w_pc/2-width/2), (h_pc/2-higth/2-20)))

	f1 = Frame(raiz)		# contenedores
	f2 = Frame(raiz)

	# variables
	global esp_res
	eng_add = StringVar(value='')
	esp_add = StringVar(value='')
	esp_res = StringVar(value='')
	global eng_play 
	eng_play = StringVar(value='')
	global lis_dif
	global lis_ind_d
	global lis_bien
	global cont_var
	global lis_rep
	lis_dif = []
	lis_ind_d = []
	lis_bien = []
	lis_rep = []
	cont_var = 0

	# llamados a clases
	global mygame
	mygame = Dicc()
	num_w = mygame.numdicc()

	global num_a
	num_a = 0
	if num_w > 1:
		num_a = random.randint(1, num_w)
		word = mygame.read(num_a)
		eng_play.set(word[0].upper())
	else:
		eng_play.set("No hay palabras")

	# MENU BAR

	barraMenu = Menu(raiz)
	
	mnuFile = Menu(barraMenu)
	mnuHelp = Menu(barraMenu)
	mnuFile.add_command(label='Reset', command=reset_all)
	mnuFile.add_command(label='Exit', command=raiz.destroy)

	mnuHelp.add_command(label='Instruciones', command=instru)
	mnuHelp.add_command(label='Versión', command=ver)

	barraMenu.add_cascade(label="File", menu=mnuFile)
	barraMenu.add_cascade(label="Help", menu=mnuHelp)

	raiz.config(menu=barraMenu)

	#Imagenes para botones
	b1 = PhotoImage(file='biblio/add.ppm')
	b2 = PhotoImage(file='biblio/pra.ppm')

	#botones
	bot_add = Button(f1, image=b1, command=lambda: w_write(mygame, eng_add.get(), esp_add.get()))
	bot_practice = Button(f2, image=b2, command=lambda: pra(mygame, esp_res.get(), num_a))

	#

	#labels
	l_en1 = Label(f1, text="ENGLISH :", anchor="n", padx=2)
	txt_en1 = Entry(f1, textvariable=eng_add, width=15)
	l_sp1 = Label(f1, text="ESPAÑOL :", anchor="n", padx=2)
	txt_es1 = Entry(f1, textvariable=esp_add, width=15)

	separ3 = ttk.Separator(f1, orient=HORIZONTAL)
	l_inf1 = Label(f1,text="Separa las palabras por (,)", anchor="n", padx=2)
	separ4 = ttk.Separator(f1, orient=HORIZONTAL)

	#
	l_sp2 = Label(f2, text="Escribe el Significado de: ", anchor="n", padx=2)
	l_eng2 = Label(
		f2,
		textvariable=eng_play,
		foreground="black",
		background="white",
		borderwidth=5,
		anchor="n",
		width=10
	)
	l_inf2 = Label(f2, text="Español", anchor="n", padx=2)
	separ1 = ttk.Separator(f2, orient=HORIZONTAL)
	l_sp3 = Label(f2, text="Separa las palabras por (,): ", anchor="n", padx=2)
	separ2 = ttk.Separator(f2, orient=HORIZONTAL)
	txt_res1 = Entry(f2, textvariable=esp_res, width=15) 

	#  pack
	bot_add.pack(side=TOP)

	l_en1.pack(side=TOP, fill=BOTH, expand=True, padx=1, pady=1)
	txt_en1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
	l_sp1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	txt_es1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	separ3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	l_inf1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	separ4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)

	bot_practice.pack(side=TOP)
	raiz.bind('<KeyPress>', key)  # '<KeyPress>
	l_sp2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	l_eng2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	separ1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	l_sp3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	txt_res1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	separ2.pack(side=BOTTOM, fill=BOTH, expand=True, padx=10, pady=5)

	#  frame- place
	f2.pack(side=TOP)

	separF = ttk.Separator(raiz, orient=HORIZONTAL)
	separF.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
	f1.pack(side=TOP)

	#  COPYRIGHT
	text1 = 'COPYRIGHT (c) EDWIN CUBILLOS 2016 '

	l_copyright = Label(raiz, text=text1, anchor='n', padx=2)
	l_copyright.pack(side=BOTTOM)

	raiz.mainloop()

	if len(lis_dif) > 1:
		list_diff_str = ', '.join(lis_dif)
		tkMessageBox.showinfo(
			title='Bien',
			message='Te recomendamos practicar estas palabras \n {}'.format(list_diff_str)
		)

	lis_fin = []
	for i in lis_bien:
		lis_fin.append(int(i))  # pasar la lista a entera
	lis_fin = sorted(lis_fin)   # ordenar la lista
	print("bien :", lis_fin)


if __name__ == '__main__':
	main()
