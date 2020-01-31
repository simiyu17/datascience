# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:53:54 2020

@author: simiyu
"""

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# importing os module
import os


#Update Cell Value
def setCellValue(df, index, column, new_value):
    result = df
    result.at[index, column]= new_value
    return result

#Get Cell Value
def getCellValue(df, index, column):
    return df.at[index, column]

#Create A new Column
def createNewRecord(df, values_list, index):
    df = setCellValue(df, index, 'First Name', values_list[0])
    df = setCellValue(df, index, 'Surname', values_list[1])
    df = setCellValue(df, index, 'Country', values_list[2])
    return df

#Get a dataframe total row count
def getDataFrameCount(df):
    return len(df)

#Get single row for index value
def getRowByIndex(df, index):
    choice = df.loc[index]
    return choice

#Get records for column value
def getByColumn(df, col, col_value):
    choice = df.loc[df[col] == col_value]
    return choice

#Get single row for index value
def dropRowByIndex(df, indces_list):
    choice = df.drop(indces_list)
    return choice


def main():
    #file path
    fpath = 'data.xlsx'
    #load file using pandas
    data = pd.read_excel(fpath, index_col='Id')
    data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
    print (data.head())
    print("**** Follow the prompts carefully to create, Read , Update  or delete record(s) to an Excel File ****")

    choice = str(input("Enter 'CREATE' for Adding, 'READ' for Retrieving, 'UPDATE' for Updating and 'DELETE' for Deletion  : "))

    if(choice != 'CREATE' and choice != 'READ' and choice != 'UPDATE' and choice != 'DELETE'):
        main()



    if(choice == 'CREATE'):
        # Enter Destination
        user_records=[]
        rId = 'R'+str(getDataFrameCount(data)+1)
        #user_records.append(rId)
        fname = str(input("Enter First Name : "))
        user_records.append(fname)
        sname = str(input("Enter Surname : "))
        user_records.append(sname)
        country = str(input("Enter Country : "))
        user_records.append(country)

        print(user_records)

        data.set_index = None
        data = createNewRecord(data, user_records, rId)
        data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
        os.remove('data.xlsx')
        data.to_excel('data.xlsx')

    if(choice == 'DELETE'):
        Rindex = str(input("Enter Id for the record you wish to drop : "))
        row_df = getRowByIndex(data, Rindex)
        if getDataFrameCount(row_df) < 1:
            print('Record Not Found')
            main()
        else:
            data = dropRowByIndex(data, [Rindex])
            data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
            os.remove('data.xlsx')
            data.set_index = None
            data.to_excel('data.xlsx')
            print('Done Successfully')


    if(choice == 'UPDATE'):
         # Enter Destination
        user_records=[]
        Rindex = str(input("Enter Id for the record you wish to update : "))
        row_df = getRowByIndex(data, Rindex)
        if getDataFrameCount(row_df) < 1:
            print('Record Not Found')
            main()
        else:

            fname = str(input("Enter First Name (Leave blank to leave as is): "))
            if not fname.strip():
                fname = getCellValue(data, Rindex, 'First Name')
            user_records.append(fname)
            sname = str(input("Enter Surname (Leave blank to leave as is): "))
            if not sname.strip():
                sname = getCellValue(data, Rindex, 'Surname')
            user_records.append(sname)
            country = str(input("Enter Country (Leave blank to leave as is): "))
            if not country.strip():
                country = getCellValue(data, Rindex, 'Country')
            user_records.append(country)

            print(user_records)
            data = dropRowByIndex(data, [Rindex])
            data.set_index = None
            data = createNewRecord(data, user_records, Rindex)
            data = data[data.columns.drop(list(data.filter(regex='Unnamed')))]
            os.remove('data.xlsx')
            data.to_excel('data.xlsx')


    if(choice == 'READ'):
        option = str(input("Enter 'BYID' to read by Id or 'MANY' to read by any column : "))
        if(option != 'BYID' and option != 'MANY'):
            main()

        if(option == 'BYID'):
            Rindex = str(input("Enter Id for the record you wish to view : "))
            row_df = getRowByIndex(data, Rindex)
            if getDataFrameCount(row_df) < 1:
                print('Record Not Found')
                main()
            else:
                print('Record Found')
                print(row_df.head())

        if(option == 'MANY'):
            filter_col = str(input("Enter Column By Which You Wish To Filter Records With : "))
            if filter_col in data.columns:
                col_val = str(input("Enter "+str(filter_col)+"  Value To Filter Records With : "))
                recs = getByColumn(data, filter_col, col_val)
                found_recs = getDataFrameCount(recs)
                if found_recs < 1:
                    print('No Records Found')
                else:
                    print('Records Found')
                    recs = recs[recs.columns.drop(list(recs.filter(regex='Unnamed')))]
                    print(recs)
            else:
                print('No column Found By The name '+str(filter_col))
                main()



if __name__ == '__main__':
    main()

