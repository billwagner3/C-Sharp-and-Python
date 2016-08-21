import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3


gui = tk.Tk()
frame = Frame(gui)
scrollbar = Scrollbar(frame, orient=VERTICAL)
frame.config(width=800, height=400, bd=10)
frame.grid()

text_Data = StringVar()
text_Data2 = StringVar()
text_Data3 = StringVar()
conn = sqlite3.connect('Password_storage.db')
list1 = Listbox(frame, yscrollcommand=scrollbar.set, width=40, height=10, bd=10)


def connect():
	get_list = list1.get(0, END)
	list1.bind('<ButtonRelease-1>', get_list)
	list1.grid(column=1, row=2, rowspan=2, padx=20)

connect()


def database_table():
	conn.execute("CREATE TABLE if not exists \
	PASSWORD_STORAGE(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
	COMPANY_OR_ACCOUNT TEXT, USER_NAME BLOB,PASSWORD BLOB);")


def db_input():
	content = text_Data.get()
	content2 = text_Data2.get()
	content3 = text_Data3.get()

	# Below is for splitting the db entry, but since we're doing each entry in its own box,  sn't necessary
	# content = content.split(',')
	# content2 = content2.split(',')
	# content3 = content3.split(',')

	c = conn.cursor()
	database_table()
	c.execute("INSERT INTO PASSWORD_STORAGE(company_or_account, user_name, password) VALUES (?,?,?)",
	          (content, content2, content3))
	list1.insert(END, content, content2, content3)
	conn.commit()


def db_transfer():
	# self.conn()
	btext = text_Data.get()
	btext2 = text_Data2.get()
	btext3 = text_Data3.get()
	print(btext, btext2, btext3)
	Label(frame, text=btext)
	Label(frame, text=btext2)
	Label(frame, text=btext3)

	db_input()


def db_lookup():
	with conn:
		search = text_Data.get()
		search = search.split(',')
		c = conn.cursor()
		x = c.execute("SELECT * FROM PASSWORD_STORAGE WHERE company_or_account =?", search)
		search = x.fetchall()
		for item in search:
			list1.insert(END, item[0], item[1], item[2], item[3])
		print(search)
 

def db_to_gui():
	with conn:
		c = conn.cursor()
		list_loadr = c.execute("SELECT * FROM password_storage")
		list_load = list_loadr.fetchall()
		li = list_load
		print(li)
		for item in li:
			list1.insert(END, item[0], item[1], item[2], item[3])
		scrollbar.config(command=list1.yview)
		scrollbar.grid(column=1, row=1, rowspan=3, sticky=E, ipady=60)



class Gui:
	def __init__(self):
		gui.title("Shelley's Password Data")
		self.f = frame.configure(bg='#00334d')
		self.gui_Header = Label(frame, text="Password Input, Transfer and Retrieval                                      \n\n\n\n\n\n\n\n")
		self.gui_Header.config(bg='#00334d', fg='#ffffcc')
		self.gui_Header.grid(column=0, row=0)
		self.trans_DB = ttk.Button(frame, text='Transfer to DB', command=db_transfer)
		self.trans_DB.grid(column=0, row=3, sticky=S + W, padx=10, pady=10)
		self.FirstL = Label(frame, text="                       Company", bg='#00334d', fg='#ffffcc')
		self.FirstL.grid(column=0, row=2, sticky=N + W)
		self.bEntry = Entry(frame, textvariable=text_Data, width=30)
		self.bEntry.grid(column=0, row=2, sticky=N + E)
		self.bEntry3 = Entry(frame, textvariable=text_Data2, width=30)
		self.bEntry3.grid(column=0, row=2, sticky=E)
		self.bEntry2 = Entry(frame, textvariable=text_Data3, width=30)
		self.bEntry2.grid(column=0, row=2, sticky=S + E)
		self.SecondL = Label(frame, text="                       Username", bg='#00334d', fg='#ffffcc')
		self.SecondL.grid(column=0, row=2, sticky=W)
		self.ThirdL = Label(frame, text="                       Password", bg='#00334d', fg='#ffffcc')
		self.ThirdL.grid(column=0, row=2, sticky=S + W)
		self.deleteButton = ttk.Button(frame, text='Clear Fields', command=self.delete_entry)
		self.deleteButton.grid(column=0, row=3)
		self.win_deleteButton = ttk.Button(frame, text='Clear Window', command=self.win_delete)
		self.win_deleteButton.grid(column=0, row=3, sticky=E)
		self.search_button = ttk.Button(frame, text='Search', command=db_lookup)
		self.search_button.grid(column=0, row=3, sticky=S + E, padx=10, pady=10)
		self.DB_trans_gui = ttk.Button(frame, text='DB Transfer to GUI', command=db_to_gui)
		self.DB_trans_gui.grid(column=0, row=3, sticky=S, padx=10, pady=10)

	def delete_entry(self):
		self.bEntry.delete(0, END)
		self.bEntry2.delete(0, END)
		self.bEntry3.delete(0, END)

	@staticmethod
	def win_delete():
		list1.delete(0, END)

i = frame.grid_info()
print(i)
s = frame.grid_size()
print(s)
GUI = Gui()
gui.mainloop()
