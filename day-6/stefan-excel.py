#!/usr/bin/env python

# You'll need to pip import openpyxl
import openpyxl

excelFile = openpyxl.load_workbook('stefan-data.xlsx')

sheet1 = excelFile.active

for row in sheet1.iter_rows():
    for cell in row:
        if cell.value == 0:
            cell.value = '<10'
        elif cell.value == 1:
            cell.value = '20'
        elif cell.value == 2:
            cell.value = '40'
        elif cell.value == 3:
            cell.value = '80'
        elif cell.value == 4:
            cell.value = '160'
        elif cell.value == 5:
            cell.value = '320'
        elif cell.value == 6:
            cell.value = '640'
        elif cell.value == 7:
            cell.value = '1280'
        elif cell.value == 0.5:
            cell.value = '10'
        elif cell.value == 1.5:
            cell.value = '30'
        elif cell.value == 2.5:
            cell.value = '60'
        elif cell.value == 3.5:
            cell.value = '120'
        elif cell.value == 4.5:
            cell.value = '240'
        elif cell.value == 5.5:
            cell.value = '480'
        elif cell.value == 6.5:
            cell.value = '960'
        elif cell.value == 7.5:
            cell.value = '1920'
        elif cell.value == 8.5:
            cell.value = '2560'

excelFile.save('stefan-new-data.xlsx')
