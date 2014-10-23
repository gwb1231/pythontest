__author__ = 'Geoffrey'

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

# Create Geoff's Window
root = Tk()
root.title("Geoff's Awesome Window")
root.option_add('*tearoff', FALSE)


#determine what OS user is using to give them the right menu
osver = root.tk.call('tk', 'windowingsystem')
print ('running' + ' ' + osver)


def fileSave():
    filename = filedialog.asksaveasfilename(defaultextension = '.txt', filetypes = [('Text File','.txt')])
    print(filename)
def openFile():
    filename = filedialog.askopenfilename()
    print(filename)
def askDirectory():
    dirnam = filedialog.askdirectory()
    print(dirnam)


menubar = Menu(root)
#Create System Menu Bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Open Directory", command=askDirectory)
filemenu.add_command(label="Save", command=fileSave)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu = menubar)
root.mainloop()