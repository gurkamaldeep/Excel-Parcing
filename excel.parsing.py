#This script takes an email address as an input and checks whether it is
#present in the excel sheet or not

from xlrd import open_workbook
import xlsxwriter
from Tkinter import *
import tkSimpleDialog
import tkMessageBox

workbok = open_workbook('E:/job/contacs.xlsx', 'rb')
count = 0
sheet1 = workbok.sheet_by_index(0)

#tkinter
root = Tk()
w = Label(root, text = "My program")
w.pack()
while True:    
    email = tkSimpleDialog.askstring('Email', 'Enter the email')
    if email == 'x':
        break


    #xl_book = raw_input('enter email: ')
    #print xl_book

    #converting data
    x =  str(sheet1.col_values(1,1,500))

    #formatting data
    y =  x.strip("'[]u',")
    z = y.replace("u'", '')
    init =  z.replace("', ", '\n')
    finl = init.replace(", ", '\n')
    #counting = count(finl)

    #checking condition to match
    for each in finl.split():
        if each == email:
            count += 1
            present = count , 'Record already present'
            tkMessageBox.showinfo('Result',  present)
        
            '''workbook = xlsxwriter.Workbook('E:/job/contacs.xlsx', 'rb')
            worksheet.write('B%s' %count, email)
'''


            
        
