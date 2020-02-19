# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:38:44 2020

@author: simiyu
"""


from tkinter import *
from tkinter import messagebox
import pandas as pd
from tkinter.filedialog import *
from pathlib import Path

root = Tk()
root.geometry('500x500')
root.title("JSON <- -> CSV Conversion")

window_height = 400
window_width = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

radio_var = IntVar()


def process_file():
    global selection
    selection = radio_var.get()
    if selection == 5 :
        messagebox.showerror("Error", "You did not select what you want to do !!")
        return
    try:
        if selection == 1:
            dirname = askopenfilename(initialdir = "/",title = "Select a JSON file",filetypes = (("Json files","*.json"),("Json files","*.json")))
            #load file using pandas
            data = pd.read_json(str(dirname))
            data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
            file_path = Path(str(dirname))
            data.to_csv(str(file_path.parent)+"/Output.csv")
            messagebox.showinfo("Info","Done Successfully, Check Out "+str(file_path.parent)+"/Output.csv !!!")


        if selection ==2:
            dirname = askopenfilename(initialdir = "/",title = "Select a CSV file",filetypes = (("CSV files","*.csv"),("CSV files","*.csv")))
            data = pd.read_csv(str(dirname),index_col=None)
            data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
            file_path = Path(str(dirname))
            data.to_json(str(file_path.parent)+"/Output.json")
            messagebox.showinfo("Info","Done Successfully, Check Out "+str(file_path.parent)+"/Output.json !!!")
    except Exception as e:
        print (str(e))
        messagebox.showerror("Error", "Make Sure You Selected a valid file")




label_0 = Label(root, text="What do you want to do?",width=20,font=("bold", 20)).place(x=90,y=53)

Radiobutton(root,  text="Convert Json to Csv",  padx = 20, variable=radio_var,  value=1).place(x=90,y=100)
Radiobutton(root,  text="Convert Csv to Json",    padx = 20, variable=radio_var,  value=2).place(x=90,y=120)

Button(root, text='Select File To Convert',width=20,bg='brown',fg='white',command = lambda:process_file()).place(x=180,y=150)

root.mainloop()