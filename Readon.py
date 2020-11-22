# Scraping Libraries
software_name = "Readon!"
import sys
import requests
import urllib.request
from bs4 import BeautifulSoup
import gdown
import re

# GUI Libraries
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd 
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askdirectory


# Numpy
import numpy as np 

tfe_url = "https://iasbano.com/financial-express-upsc.php#download_the_hindu"
tfe_name = "The Financial Express"

th_url = "https://www.iasbano.com/upsc_thehindu_free_download.php"
th_name = "The Hindu"

dca_url = "https://iasbano.com/Daily_current_affairs_upsc.php#download_now"
dca_name = "Daily Current Affairs"

dmp_url = "https://iasbano.com/upsc_mains_practice.php#download_now"
dmp_name = "Daily Mains Practice"

global destination


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def Download(url, name):
	# global destination
	###############################################
	# The Financial Express
	###############################################
	# print(url)
	try:
		url = urllib.request.urlopen(url).read().decode('UTF-8')
		# print(url)
		data = url
		soup = BeautifulSoup(data, 'html.parser')
		# print(soup)
		link_class_tags = soup.find_all(class_="btn teal white-text waves-effect")
		# print(link_class_tags)
		linklist = []
		for link in link_class_tags:
			linklist.append(link.get('href'))
		download_url = []
		# print(linklist)	essential for debugging :)

		for i in linklist:
			x = re.search('https://drive.google.com/file/d/', i)
			if x is None:	
				x = re.search('https://drive.google.com/open\?id=', i)
				
			y = re.search("/view\?usp=drivesdk", i)
			# y = re.search("/view", i)
			if y is None:
				download_url.append('https://drive.google.com/uc?id=' + i[x.end():])
			else:
				download_url.append('https://drive.google.com/uc?id=' + i[x.end():y.start()])
		# print(download_url)
		print("Downloading ---- " + name)
		# destination = 'C:/Users/Tanishq Sharma/Desktop/The Hindu/' + name + '.pdf'
		destination = destinationFolderPath + '/' + name + '.pdf'	
		gdown.download(download_url[0], destination, quiet=False)	
	except:
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		print("Please check your internet connection")
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
	else:
		pass
	finally:
		pass

def buttonEnabler():
	tfe_button.configure(state='normal')
	th_button.configure(state='normal')
	dca_button.configure(state='normal')
	dmp_button.configure(state='normal')
	doAll_button.configure(state='normal')

def destinationSelector():
	global destinationFolderPath
	destinationFolderPath = askdirectory()
	# buttonEnabler()

root = Tk()

fontStyle3 = tkFont.Font(family="Lucida Grande", size=40, weight = tkFont.BOLD) 
software_label = Label(root, text = software_name, bg = 'black', fg = 'red', font = fontStyle3).place(x = 165,y = 10)  

y = np.linspace(90, 400, 6)
buttonColor = "yellow"
buttonTextColor = "black"

fontStyle3 = tkFont.Font(family="Lucida Grande", size=14, weight = tkFont.BOLD) 

tfe_label = Label(root, text = "The Financial Express :", bg = 'black', fg = 'red', font = fontStyle3).place(x = 50,y = y[0])  


tfe_button = Button(root, text = 'Download', font = fontStyle3, width = 12, height = 1, padx = 10, pady = 2, bg = buttonColor, fg = buttonTextColor, command = lambda : combine_funcs(destinationSelector(), Download(tfe_url, tfe_name)))
tfe_button.configure(state='normal')
tfe_button.pack()
tfe_button.place(x = 300, y = y[0]-4)

###########################################
th_label = Label(root, text = "The Hindu :", bg = 'black', fg = 'red', font = fontStyle3).place(x = 50,y = y[1])  


th_button = Button(root, text = 'Download', font = fontStyle3, width = 12, height = 1, padx = 10, pady = 2, bg = buttonColor, fg = buttonTextColor, command = lambda : combine_funcs(destinationSelector(), Download(th_url, th_name)))
th_button.configure(state='normal')
th_button.pack()
th_button.place(x = 300, y = y[1]-4)

###########################################
dca_label = Label(root, text = "Daily Current Affairs :", bg = 'black', fg = 'red', font = fontStyle3).place(x = 50,y = y[2])  


dca_button = Button(root, text = 'Download', font = fontStyle3, width = 12, height = 1, padx = 10, pady = 2, bg = buttonColor, fg = buttonTextColor, command = lambda : combine_funcs(destinationSelector(), Download(dca_url, dca_name)))
dca_button.configure(state='normal')
dca_button.pack()
dca_button.place(x = 300, y = y[2]-4)

###########################################
dmp_label = Label(root, text = "Daily Mains Practice :", bg = 'black', fg = 'red', font = fontStyle3).place(x = 50,y = y[3])  


dmp_button = Button(root, text = 'Download', font = fontStyle3, width = 12, height = 1, padx = 10, pady = 2, bg = buttonColor, fg = buttonTextColor, command = lambda : combine_funcs(destinationSelector(), Download(dmp_url, dmp_name)))
dmp_button.configure(state='normal')
dmp_button.pack()
dmp_button.place(x = 300, y = y[3]-4)

###########################################
# doAll_label = Label(root, text = "Download All :", bg = 'black', fg = 'red', font = fontStyle3).place(x = 50,y = y[4])  


doAll_button = Button(root, text = 'Download All', font = fontStyle3, width = 12, height = 1, padx = 10, pady = 2, bg = "#14b5d0", fg = 'black', command = lambda : combine_funcs(destinationSelector(), Download(dca_url, dca_name), Download(tfe_url, tfe_name), Download(th_url, th_name), Download(dmp_url, dmp_name)))
doAll_button.configure(state='normal')
doAll_button.pack()
doAll_button.place(x = 300, y = y[4]-4)

###########################################
# destination_label = Label(root, text = "Download Destination :", bg = 'black', fg = 'red', font = fontStyle3).place(x = 50,y = y[5])  


# destination_button = Button(root, text = 'Choose', font = fontStyle3, width = 12, height = 1, padx = 10, pady = 2, bg = buttonColor, fg = buttonTextColor, command = destinationSelector)
# destination_button.configure(state='normal')
# destination_button.pack()
# destination_button.place(x = 300, y = y[5]-4)



def quitWin():
	#print('quit')
	root.update_idletasks()
	root.quit()
	root.quit()
	root.destroy()

ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen
w = 530
h = 400 
x = (ws/2) - (w/7)
y = (hs/2) - (h/2)
root.title('Readon!')
root.configure(bg='black')
root.geometry("%dx%d+%d+%d" %(w, h, x, y))
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quitWin)
root.mainloop()