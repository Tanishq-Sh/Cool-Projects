# Personal Dictionary Bank Game
# Overall Aim: To make a personal dictionary bank to add learned vocabulary to the bank & revise the same with random vocabulary!
# Bank will be based on Database 
software_name = "Personal Vocabulary Bank"

import random
import csv
import sqlite3 as sql
from sqlite3 import Error
from datetime import date
from datetime import datetime

def timestamp():
	now = datetime.now()
	return now

# GUI Libraries
from tkinter import * 
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd 
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory

def createConnection(db_file):
	""" Create a database connection to a SQLite database"""
	conn = None
	try:
		conn = sql.connect(db_file)
		print(sql.version)
	except Error as e:
		print(e)
	finally:
		if conn:
			conn.close

# if __name__ == '__main__':
	# createConnection(r"C:/Users/Tanishq Sharma/Desktop/Py/Personal Dictionary/dictData.db")
connection = sql.connect("C:/Users/Tanishq Sharma/Desktop/Py/Personal Dictionary/dictData.db")
# delete 

cursor = connection.cursor()
# cursor.execute("""DROP TABLE vocabulary;""")

# sql_command = """
# CREATE TABLE employee ( 
# staff_number INTEGER PRIMARY KEY, 
# fname VARCHAR(20), 
# lname VARCHAR(30), 
# gender CHAR(1), 
# joining DATE,
# birth_date DATE);"""

sql_command = """
CREATE TABLE vocabulary ( 
Entry_Number INTEGER PRIMARY KEY, 
Word VARCHAR(30), 
Meaning VARCHAR(60),  
Date_Added DATE);"""

try:
	cursor.execute(sql_command)
	# print("created")
except Exception as e:
	pass


# sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
#    VALUES (NULL, "William", "Shakespeare", "m", "1961-10-25");"""
# cursor.execute(sql_command)


# sql_command = """INSERT INTO employee (staff_number, fname, lname, gender, birth_date)
# VALUES (NULL, "Frank", "Schiller", "m", "1955-08-17");"""
# cursor.execute(sql_command)
# staff_data = [ ("William", "Shakespeare", "m", "1961-10-25"),
           # ("Frank", "Schiller", "m", "1955-08-17"),
           # ("Jane", "Wall", "f", "1989-03-14") ]

def database(w, m, da):
	format_str = """INSERT INTO vocabulary (Entry_Number, Word, Meaning, Date_Added)
	VALUES (NULL, "{word}", "{meaning}", "{dateadded}");"""
	sql_command = format_str.format(word=w, meaning=m, dateadded=da)
	cursor.execute(sql_command)
	connection.commit()
	# connection.commit()
# never forget this, if you want the changes to be saved:
# connection.close()

cursor.execute("SELECT * FROM vocabulary") 
print("fetchall:")
result = cursor.fetchall() 
for r in result:
    print(r)

cursor.execute("SELECT * FROM vocabulary") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)

root = Tk()

fontStyle3 = tkFont.Font(family="Lucida Handwriting", size=20, weight = tkFont.BOLD) 
software_label = Label(root, text = software_name, bg = 'black', fg = 'white', font = fontStyle3).place(x = 50,y = 10) 

fontStylep1 = tkFont.Font(family="Lucida Handwriting", size=14, weight = tkFont.BOLD)  
fontStylep2 = tkFont.Font(family="Lucida Grande", size=20)  

global User
User = tk.Label(root, text = "Word", bg = 'black', fg = 'orange', font = fontStylep1).place(x = 20, y = 110)    

global Passw
Passw = tk.Label(root, text = "Meaning", bg = 'black', fg = 'orange', font = fontStylep1).place(x = 20, y = 210)

global word
word = tk.Entry(root, text = 'User', width = 29, bg = 'white', fg = 'black', borderwidth = 1, font = fontStylep2) #Bearing diameter in mm
word.pack()
word.place(x = 200,y = 110)
# UserEntry.insert(0, 'Tanishq')

global meaning
meaning = tk.Entry(root, text = 'Passw', width = 29, bg = 'white', fg = 'black', borderwidth = 1, font = fontStylep2) #Bearing diameter in mm
meaning.pack()
meaning.place(x = 200,y = 210)
# PasswordEntry.insert(1, '1234') 

saveVocabButton = tk.Button(root, text="Save Vocab", width = 20, font = fontStylep1, bg = '#39ff14', fg = 'Black', borderwidth = 0,
                    command=lambda: database(word.get(), meaning.get(), timestamp()))
saveVocabButton.pack()
saveVocabButton.place(x = 180,y = 300)

def quitWin():
	#print('quit')
	root.update_idletasks()
	root.quit()
	root.quit()
	root.destroy()

ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
w = 800
h = 400 
x = (ws/2) - (w/7)
y = (hs/2) - (h/2)
root.title('Personal Vocabulary Bank')
root.configure(bg='black')
root.geometry("%dx%d+%d+%d" %(w, h, x, y))
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quitWin)
root.mainloop()	

