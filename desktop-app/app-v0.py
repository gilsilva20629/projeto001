import tkinter as tk
import requests
import time
from functools import partial 
# A função partial é uma ferramenta que permite criar uma nova função a partir de uma função existente,
# fixando (ou "prendendo") alguns dos argumentos dessa função.


'''
Convenções de nomenclatura

Classe Widget	Prefixo de nome variável	Exemplo
Label			lbl							lbl_name
Button			btn							btn_submit
Entry			ent							ent_age
Text			txt							txt_notes
Frame			frm							frm_address
'''

current_window = []


def window_manager(janela: str)-> tk.Tk | None :
	
	match janela:

		case "cadastro":
			current_window.append(WindowCad("cadastro"))
			current_window[1].show()
			current_window[0].quit()

		case "shop" | 0 :
			current_window.append(WindowShop("shop"))
			print(current_window)
			current_window[0].quit()
			current_window.pop(0)
			current_window[0].show()
			print(current_window)

		case "stock" | 1 :
			current_window.append(WindowStock("stock"))
			print(current_window)
			current_window[0].quit()
			current_window.pop(0)
			current_window[0].show()
			print(current_window)

		case "car" | 2 :
			current_window.append(WindowCar("car"))
			print(current_window)
			current_window[0].quit()
			current_window.pop(0)
			current_window[0].show()
			print(current_window)

		case "finance" | 3 :
			current_window.append(WindowFinance("finance"))
			print(current_window)
			current_window[0].quit()
			current_window.pop(0)
			current_window[0].show()
			print(current_window)

		case "gear" | 4 :
			current_window.append(WindowGear("gear"))
			print(current_window)
			current_window[0].quit()
			current_window.pop(0)
			current_window[0].show()
			print(current_window)

		case "-":
			Print("Nenhuma janela encontrada.")
		

		#case "login":
		#	current_window.append(WindowLogin("login"))
		#	current_window[1].show()print("Funcao-> identifier_widget: ", end="\n")
		#	current_window[0].quit()
		#	return current_window[0]	

'''
def identifier_widget(self, event)-> str:
	print("Funcao-> identifier_widget: ", end="\n")
	print("identifier", event.widget.winfo_id(), end="\n")
	print(event.widget['text'], end="\n")

	window_mananger(event.widget['text'])
'''

class Window:
	def __init__(self, name:str)-> None:
		self.window = tk.Tk()
		self.window.title(name)
		self.text_log = tk.StringVar()
		self.text_log.set("report log")
		#text_label_frame = ["shop", "stock", "car", "finance", "gear"]
		images = ["images/shop.png", "images/stock.png", "images/car.png", "images/finance.png", "images/gear.png"]
		img_ref_list = []
		btn_ref_list = {}
		window_list = ["shop", "stock", "car", "finance", "gear", "login", "cadastro"]
		


		frame_menu = tk.Frame(master=self.window, background="white", relief=tk.RAISED, borderwidth=1, width=240, height=40)
		frame_middle = tk.Frame(master=self.window, background="white", relief=tk.RAISED, borderwidth=1, width=640, height=450)
		frame_middle_left = tk.Frame(master=frame_middle, background="gray80", relief=tk.RAISED, borderwidth=1, width=160, height=450)
		frame_middle_center = tk.Frame(master=frame_middle, background="gray80", relief=tk.RAISED, borderwidth=1, width=320, height=450)
		frame_middle_right = tk.Frame(master=frame_middle, background="gray80", relief=tk.RAISED, borderwidth=1, width=160, height=450)
		frame_botton = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, width=240, height=80)
		frame_log = tk.LabelFrame(master=self.window, relief=tk.RAISED, borderwidth=1, width=240, height=40, text="Log")
		lbl_log = tk.Label(master=frame_log, textvariable=self.text_log, borderwidth=1)

		frame_menu.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle_left.pack(expand=True, fill="both", side="left", anchor="w", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle_center.pack(expand=True, fill="both", side="left", anchor="center", padx=2, pady=4, ipadx=1, ipady=1)
		frame_middle_right.pack(expand=True, fill="both", side="left", anchor="e", padx=2, pady=4, ipadx=1, ipady=1)
		frame_botton.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		frame_log.pack(expand=True, fill="both", padx=2, pady=4, ipadx=1, ipady=1)
		lbl_log.pack()

		######## Lidando com grid de botoes ##############

		
		for j in range(5):
			frame = tk.Frame(master=frame_menu)
			frame.grid(row=0, column=j, ipadx=2, ipady=2, padx=2, pady=2, sticky="nsew")	#-column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
			
			btn = tk.Button(master=frame, text=window_list[j], compound="top")
			btn['command'] = partial(window_manager, btn['text'])
			#btn = tk.Button(master=frame, text=window_list[j], compound="top", command=lambda : window_manager( btn['text'] ))	
			#btn = tk.Button(master=frame, text=window_list[j], compound="top", command=lambda id=j: window_manager(j))	
			#btn = tk.Button(master=frame, text=window_list[j], compound="top", command=partial(window_manager, btn['text']))	 
			#btn.bind("<Button-1>", identifier_widget) # "<Button-1>" corresponde ao botão esquerdo do mouse

			btn_ref_list.update({window_list[j]: btn})	# Adiciona ao dicionario para manter a referência

			foto = tk.PhotoImage(master=btn, file=images[j], width=35, height=35) 
			btn["image"] = foto
			#gpt confesso que nao entedi as duas linhas abaixo para prevenir garbage collector
			btn.image = foto	# Armazena a referência à imagem
			img_ref_list.append(foto)

			btn.pack(fill="x", padx=2, pady=2, ipadx=2, ipady=2)

			#print(btn_ref_list.keys(), end="\n")
			#print(id(btn), id(btn_ref_list[j]), end="\n")  #teste

		for j in range(5):
			frame_menu.grid_columnconfigure(j, weight=1)  # Ajuste o peso das colunas ao expandir

		######## Fim de grid de botoes ##############

	def start(self):
		self.window.mainloop()

	def show(self):
		self.window.mainloop()

	def quit(self):
		self.window.destroy()

	def exit(self):
		self.window.destroy()

	def teste(self):
		raise NotImplementedError("Este método deve ser implementado pelas filhas/subclasses.")


class WindowLogin:

	def __init__(self, name:str)-> None:
		self.window = tk.Tk()
		self.window.title(name)

		frame_menu = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, width=80, height=40)
		frame_middle = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
		frame_botton = tk.Frame(master=self.window, relief=tk.RAISED, width=80, height=40)
		frame_log =	tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)

		frame_menu.pack(fill="x", padx=4, pady=2)
		frame_middle.pack(padx=4, pady=2)
		frame_botton.pack(fill="x", padx=4, pady=2)
		frame_log.pack(fill="x", padx=4, pady=2)

		for j in range(5):
			frame = tk.Frame(master=frame_menu, relief=tk.RAISED, borderwidth=1)
			frame.grid(row=0, column=j)
			btn = tk.Button(master=frame, text="btn")
			btn.pack(fill="x")		


		self.rep = tk.StringVar()
		self.rep.set("Log")
		lbl_log = tk.Label(master=frame_log, textvariable=self.rep, height=3)
		lbl_user = tk.Label(master=frame_middle, text="user:")
		self.ent_user = tk.Entry(master=frame_middle, width=25)
		lbl_password = tk.Label(master=frame_middle, text="password:")
		self.ent_password = tk.Entry(master=frame_middle, width=25)

		self.ent_user.bind("<Return>", self.evtGetEntry)
		self.ent_password.bind("<Return>", self.evtGetEntry)

		lbl_log.pack()
		lbl_user.pack()
		self.ent_user.pack()
		lbl_password.pack()
		self.ent_password.pack()

		btn_login = tk.Button(master=frame_botton, text="login", command=self.btnGetEntry)
		btn_cad = tk.Button(master=frame_botton, text="cadastro", command=lambda : window_manager("cadastro"))
		btn_login.pack(side="left")
		btn_cad.pack(side="right")

	def start(self):
		self.window.mainloop()

	def show(self):
		self.window.mainloop()

	def quit(self):
		print("Saindo... ... ...")
		self.window.destroy()

	def exit(self):
		self.window.destroy()

	def evtGetEntry(self, event):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"1"})
		print("---->  Status code:", response.status_code)

		if response.text == "OK" :
			self.rep.set("login bem sucedido!")
			time.sleep(1)
			window_manager("shop")

		else:
			self.rep.set("Credenciais Invalidas!")

	def btnGetEntry(self):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"1"})
		print("---->  Status code:", response.status_code)
		
		if response.text == "OK" :
			self.rep.set("login bem sucedido!")
			time.sleep(1)
			window_manager("shop")

		else:
			self.rep.set("Credenciais Invalidas!")
	
class WindowCad:

	def __init__(self, name:str)-> None:
		self.window = tk.Tk()
		self.window.title(name)

		frame_menu = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1, width=80, height=40)
		frame_middle = tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)
		frame_botton = tk.Frame(master=self.window, relief=tk.RAISED, width=80, height=40)
		frame_log =	tk.Frame(master=self.window, relief=tk.RAISED, borderwidth=1)

		frame_menu.pack(fill="x", padx=4, pady=2)
		frame_middle.pack(padx=4, pady=2)
		frame_botton.pack(fill="x", padx=4, pady=2)
		frame_log.pack(fill="x", padx=4, pady=2)

		for j in range(5):
			frame = tk.Frame(master=frame_menu, relief=tk.RAISED, borderwidth=1)
			frame.grid(row=0, column=j)
			btn = tk.Button(master=frame, text="btn")
			btn.pack()

		self.rep = tk.StringVar()
		self.rep.set("Log_cad")
		lbl_log = tk.Label(master=frame_log, textvariable=self.rep, height=3)

		lbl_user = tk.Label(master=frame_middle, text="user:")
		self.ent_user = tk.Entry(master=frame_middle, width=25)
		lbl_password = tk.Label(master=frame_middle, text="password:")
		self.ent_password = tk.Entry(master=frame_middle, width=25)

		self.ent_user.bind("<Return>", self.evtGetEntry)
		self.ent_password.bind("<Return>", self.evtGetEntry)

		lbl_log.pack()
		lbl_user.pack()
		self.ent_user.pack()
		lbl_password.pack()
		self.ent_password.pack()

		btn_sub = tk.Button(master=frame_botton, text="Submit", command=self.btnGetEntry)
		btn_sub.pack()
		

	def start(self):
		self.window.mainloop()

	def show(self):
		self.window.mainloop()

	def quit(self):
		self.window.destroy()

	def exit(self):
		self.window.destroy()

	def evtGetEntry(self, event):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"2"})
		print("---->  Status code:", response.status_code)

		if response.text == "OK" :
			self.rep.set("Cad OK")
		else:
			self.rep.set("Cad fail!")

	def btnGetEntry(self):

		name_user = self.ent_user.get()
		password = self.ent_password.get()
		response = requests.post("http://127.0.0.1:5000/my_endpoint", data={"name_user":str(name_user), "password":str(password), "extra":"2"})
		print("---->  Status code:", response.status_code)
		
		if response.text == "OK" :
			self.rep.set("Cad OK")
		else:
			self.rep.set("Cad fail!")

#["shop", "stock", "car", "finance", "gear", "login", "cadastro"]

class WindowShop(Window):
	def teste(self):
		print("Herança funciona bem.")

class WindowStock(Window):
	def teste(self):
		print("Herança funciona bem.")

class WindowCar(Window):
	def teste(self):
		print("Herança funciona bem.")

class WindowFinance(Window):
	def teste(self):
		print("Herança funciona bem.")

class WindowGear(Window):
	def teste(self):
		print("Herança funciona bem.")


if __name__ == "__main__" :

	current_window.append(WindowLogin("login"))
	print(current_window, end="\n")
	#print(type(current_window[0]), end="\n")
	current_window[0].show()
	


	