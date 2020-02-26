# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:13:03 2020

@author: simiyu
"""

from tkinter import *
from tkinter import messagebox
import pandas as pd
from tkinter.filedialog import *
from pathlib import Path
import xlsxwriter

root = Tk()
root.geometry('500x500')
root.title("STUDENTS TEST SCORES SUMMARY")

window_height = 400
window_width = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


#Get Cell Value
def getCellValue(df, index, column):
    return df.at[index, column]

def get_stats(student_df, maths_df, reading_df, writing_df):
    new_df = pd.DataFrame()
    for index, row in student_df.iterrows():
        st_no = index
        name = str(row['First Name'])+'   '+str(row['Surname'])
        math_ = getCellValue(maths_df, index, 'Score')
        read_ = getCellValue(reading_df, index, 'Score')
        write_ = getCellValue(writing_df, index, 'Score')
        tot_score = math_+read_+write_
        mean_score = round((tot_score/3),3)
        new_df = new_df.append({'st_no' : st_no , 'name' : name, 'math_' : math_,
                                'read_' : read_, 'write_' : write_, 'tot_score' : tot_score, 'mean_score' : mean_score} , ignore_index=True)

    return new_df.sort_values(by='mean_score',ascending=False)



def create_file(df):
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('data/Output.xlsx')
    boq = workbook.add_worksheet('SUMMARY')
    # Create a format to use in the merged range.
    merge_format = workbook.add_format({'bold': 1, 'border': 1, 'align': 'center', 'valign': 'vcenter', 'text_wrap': True})
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1, 'border': 1})

    boq.write('B3', 'Student No.', merge_format)
    boq.write('C3', 'Name', merge_format)
    boq.merge_range('E2:G2', 'Scores', merge_format)
    boq.write('D3', 'Maths', merge_format)
    boq.write('E3', 'Reading', merge_format)
    boq.write('F3', 'Writing', merge_format)
    boq.write('G3', 'Total Score', merge_format)
    boq.merge_range('H2:I2', 'Performance', merge_format)
    boq.write('H3', 'Mean Score', merge_format)
    boq.write('I3', 'Rank/Position', merge_format)
    i = 4
    for index, row in df.iterrows():
        boq.write('B'+str(i), row['st_no'], bold)
        boq.write('C'+str(i), row['name'], bold)
        boq.write('D'+str(i), row['math_'], bold)
        boq.write('E'+str(i), row['read_'], bold)
        boq.write('F'+str(i), row['write_'], bold)
        boq.write('G'+str(i), row['tot_score'], bold)
        boq.write('H'+str(i), row['mean_score'], bold)
        boq.write('I'+str(i), i-3, bold)
        i = i+1


    boq.set_column(1, 8, 30)

    workbook.close()




def process_file():
    try:
        #load file using pandas
        st_data = pd.read_excel('data/students.xlsx', index_col='Student_Id')
        maths_data = pd.read_excel('data/maths_scores.xlsx', index_col='Student_Id')
        rad_data = pd.read_excel('data/reading_scores.xlsx', index_col='Student_Id')
        write_data = pd.read_excel('data/writing_scores.xlsx', index_col='Student_Id')

        new_data = get_stats(st_data, maths_data, rad_data, write_data)
        create_file(new_data)

        file_path = Path('data/students.xlsx')
        messagebox.showinfo("Info","Done Successfully, Check Out "+str(file_path.parent)+"/Output.xlsx !!!")
    except Exception as e:
        print (str(e))
        messagebox.showerror("Error", "Make Sure You have all correct files in data folder!!")




label_0 = Label(root, text="Click the button below",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


Button(root, text='Process Files',width=20,bg='brown',fg='white',command = lambda:process_file()).place(x=180,y=150)

root.mainloop()
