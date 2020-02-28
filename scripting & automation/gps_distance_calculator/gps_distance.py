# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:02:13 2020

@author: simiyu
"""

import glob
from tkinter import messagebox
from tkinter.filedialog import *

from math import radians, sin, cos, acos



def calculate_distance(lat1, long1, lat2, long2, result):
    try:

        if not lat1.strip() or not long1.strip() or not lat2.strip() or not long2.strip():
            messagebox.showerror("Error", "You must provide all gps coordinates !!")
            return

        lt1 = radians(float(lat1))
        lg1 = radians(float(long1))
        lt2 = radians(float(lat2))
        lg2 = radians(float(long2))

        dist = 6371.01 * acos(sin(lt1) * sin(lt2) + cos(lt1) * cos(lt2) * cos(lg1 - lg2))
        result.set("The distance is %.2fkm." % dist)
    except Exception as e:
        messagebox.showerror("Error", "Make Sure You Provide Valid Coordinates!!")


def set_output_folder(output_folder):
    dirname = askdirectory(initialdir="/", title="Select Directory In which you want to save the output file")
    output_folder.set(dirname)


def main():
    root = Tk()
    root.geometry('500x500')
    root.title("Distance Calculator")
    root['bg'] = 'gray62'

    window_height = 250
    window_width = 550

    lat1 = StringVar()
    long1 = StringVar()
    lat2 = StringVar()
    long2 = StringVar()
    result = StringVar()

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_cordinate = int((screen_width / 2) - (window_width / 2))
    y_cordinate = int((screen_height / 2) - (window_height / 2))

    root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
    Label(root, text="Location ONE Latitude:", background='gray62').place(x=15, y=20)
    Entry(root, width=40, background='white', foreground='black', borderwidth=2, textvariable=lat1).place(x=270, y=20)
    Label(root, text="Location ONE Longitude:", background='gray62').place(x=15, y=50)
    Entry(root, width=40, background='white', foreground='black', borderwidth=2, textvariable=long1).place(x=270, y=50)

    Label(root, text="Location TWO Latitude:", background='gray62').place(x=15, y=80)
    Entry(root, width=40, background='white', foreground='black', borderwidth=2, textvariable=lat2).place(x=270, y=80)
    Label(root, text="Location TWO Longitude:", background='gray62').place(x=15, y=110)
    Entry(root, width=40, background='white', foreground='black', borderwidth=2, textvariable=long2).place(x=270, y=110)

    Button(root, text='Calculate Distance', width=34, bg='green', fg='white',
           command=lambda: calculate_distance(lat1.get(), long1.get(), lat2.get(), long2.get(), result)).place(x=270, y=150)

    Label(root, text="Result ", background='gray62').place(x=15, y=180)
    Entry(root, width=40, background='white', foreground='black', borderwidth=2, textvariable=result, state='disabled').place(x=270, y=180)

    root.mainloop()


if __name__ == '__main__':
    main()
