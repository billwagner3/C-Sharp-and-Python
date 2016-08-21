import sys
from tkinter import *
from tkinter import ttk
import webbrowser
import sqlite3

conn = sqlite3.connect('content_storage.db')
web_Gui = Tk()
 
#create table
def database_Table():
    conn.execute("CREATE TABLE if not exists \
    CONTENT_STORAGE(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    CONTENT BLOB);")

def browser_Input():
    btext =  text_Data.get()
    blabel2 = Label(web_Gui,text=btext).pack()
    f=open('Sale Page.html', 'w')
    message = text_Data.get()
    f.write(message)
    f.close()
    webbrowser.open_new_tab('Sale Page.html')

def db_Input():
    conn = sqlite3.connect('content_storage.db')
    c = conn.cursor()
    content = text_Data.get()
    c.execute("INSERT INTO CONTENT_STORAGE(content)VALUES(?)",
              (content,))
    conn.commit()

def DB_Transfer():
    btext =  text_Data.get()
    blabel2 = Label(web_Gui,text=btext).pack()
    database_Table()
    db_Input()

list = Listbox(web_Gui, width = 60)
get_list = list.get(0,END)
list.pack(side = BOTTOM)

list.bind('<ButtonRelease-1>',get_list)

def DB_to_Gui():
    conn = sqlite3.connect('content_storage.db')
    with conn:
        c = conn.cursor()
        list_loadr = c.execute("SELECT * FROM content_storage")
        list_load = list_loadr.fetchall()
        li = list_load
        for item in li:
            list.insert(END, item)
    conn.close()

def Gui_to_Browser():
    conn = sqlite3.connect('content_storage.db')
    with conn:
        c = conn.cursor()
        list_loadr = c.execute("SELECT * FROM content_storage")
        list_load = list_loadr.fetchall()
        li = list_load
        for item in li:
            list.insert(END, item)
    conn.close() 
    f=open('Sale Page.html','w')
    message2=li
    for item in message2:
        line=item[1]+"<br/>"
        f.write(line)
    f.close()
    webbrowser.open_new_tab('Sale Page.html')
       
text_Data = StringVar()

web_Gui.geometry('700x400+200+200')
web_Gui.title("Website Data GUI")
gui_Header = Label(web_Gui, text='Web Browser Input and Transfer').pack()
trans_B = ttk.Button(web_Gui, text='Transfer To Browser', command = browser_Input).pack(side=TOP)
trans_DB = ttk.Button(web_Gui, text = 'Transfer to DB',
                  command = DB_Transfer).pack(side=TOP)
bEntry = Entry(web_Gui, textvariable=text_Data, width=50)
bEntry.pack(side=TOP)
DB_trans_gui = ttk.Button(web_Gui, text = 'DB Transfer to GUI',command=DB_to_Gui).pack(side=BOTTOM)
GUI_trans_Browser = ttk.Button(web_Gui, text = 'GUI Transfer to Browser',command=Gui_to_Browser).pack(side=BOTTOM)

