
#Yup-d GUI ver. 1.0

from Yup_d import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog

class App:

    def __init__(self, root):
        
        self.OUTPUT_DIRECTORY = ".\output"

        #setting title
        root.title("Yup-d "+ "" +" ver1.0")
        #setting icon
        root.iconbitmap("icon.ico")
        #setting window 
        width=473
        height=176
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        ft = tkFont.Font(family='Arial',size=10)

        GLabel_20=tk.Label(root)
        GLabel_20["anchor"] = "center"
        GLabel_20["font"] = ft
        GLabel_20["fg"] = "#333333"
        GLabel_20["justify"] = "left"
        GLabel_20["text"] = self.OUTPUT_DIRECTORY
        GLabel_20.place(x=120,y=150,width=350,height=20)

        GButton_269=tk.Button(root)
        GButton_269["relief"] = "groove"
        GButton_269["bg"] = "#f0f0f0"
        GButton_269["font"] = ft
        GButton_269["fg"] = "#000000"
        GButton_269["justify"] = "center"
        GButton_269["text"] = "Select Output Directory"
        GButton_269.place(x=10,y=110,width=146,height=30)
        GButton_269["command"] = lambda:[self.GButton_269_command(filedialog.askdirectory())]

        GLabel_185=tk.Label(root)
        GLabel_185["font"] = ft
        GLabel_185["fg"] = "#333333"
        GLabel_185["justify"] = "center"
        GLabel_185["text"] = "Output Directory :"
        GLabel_185.place(x=10,y=150,width=106,height=20)

        GLineEdit_810=tk.Entry(root)
        GLineEdit_810["borderwidth"] = "0px"
        GLineEdit_810["font"] = ft
        GLineEdit_810["fg"] = "#333333"
        GLineEdit_810["justify"] = "center"
        GLineEdit_810["text"] = "Entry"
        GLineEdit_810.place(x=30,y=10,width=430,height=20)

        GLabel_299=tk.Label(root)
        GLabel_299["font"] = ft
        GLabel_299["fg"] = "#333333"
        GLabel_299["justify"] = "center"
        GLabel_299["text"] = "URL"
        GLabel_299.place(x=4,y=10,width=30,height=20)

        GButton_497=tk.Button(root)
        GButton_497["relief"] = "groove"
        GButton_497["bg"] = "#f0f0f0"
        GButton_497["font"] = ft
        GButton_497["fg"] = "#000000"
        GButton_497["justify"] = "center"
        GButton_497["text"] = "Start Download"
        GButton_497.place(x=10,y=80,width=100,height=25)
        GButton_497["command"] = lambda:[self.GButton_497_command(GLineEdit_810.get())]
    
    def GButton_497_command(self, u):
        
        root.title("Yup-d "+" ver1.0" + " - Downloading - please wait")
        Download_Process(u, self.OUTPUT_DIRECTORY)
        root.title("Yup-d "+ "" +" ver1.0")
    

    def GButton_269_command(self, OL):

        self.OUTPUT_DIRECTORY = OL
        print(OL)

        GLabel_20=tk.Label(root)
        GLabel_20["anchor"] = "center"
        GLabel_20["font"] = tkFont.Font(family='Arial',size=10)
        GLabel_20["fg"] = "#333333"
        GLabel_20["justify"] = "left"
        GLabel_20["text"] = self.OUTPUT_DIRECTORY
        GLabel_20.place(x=120,y=150,width=350,height=20)

    
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
