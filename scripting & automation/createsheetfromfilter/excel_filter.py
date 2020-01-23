# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 21:06:09 2020

@author: simiyu
"""

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

#file path
fpath = 'PayrollReport.xlsx'
#load file using pandas
data = pd.read_excel(fpath, index_col=None)


#Get Columns for a job code
def getByJobCode(df, jcode):
    choice = df.loc[df['Job Code'] == jcode]
    return choice

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

#Save Records
def saveRecords(df, codelist):
    if(len(codelist) > 0):
        i = 0
        while i < len(codelist):
            selectedf = getByJobCode(df, codelist[i])
            # Convert the dataframe to an XlsxWriter Excel object.
            selectedf.to_excel(writer, sheet_name=codelist[i])
            i+=1


# number of elements 
n = int(input("How Many Job Codes Do You Wish To Enter? : ")) 
  
# Below line read inputs from user using map() function  
a = list(map(str,input("\nEnter the Job Codes Separated With Single Spaces : ").strip().split()))[:n] 
  
#Saving Records
saveRecords(data, a)
print("\nList of Job Codes - ", a) 


# Close the Pandas Excel writer and output the Excel file.
writer.save()








