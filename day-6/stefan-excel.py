#!/usr/bin/env python

# You'll need to pip import openpyxl 
import openpyxl
import argparse

parser = argparse.ArgumentParser( 
    description='Script to convert HI data from lab readout to titers.',
    usage='python3  stefan-excel.py -e [table.xlsx]',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    '-e', action="store", default= None, required=True,
    help='location of Excel file to parse')

parser.add_argument(
    '-s', type=int, default=20,
    help='The starting dilution')




args = parser.parse_args()
std = args.s
stdh = std * 1.5
co = round(std // 2)
cutoff = '<%s' % co

table = openpyxl.load_workbook(args.e)

sheet1 = table.active

convert = {
    '0' : cutoff,
    '0.5' : co,
    '1' : std,
    '1.5' : stdh,
    '2' : std*(2**1),
    '2.5' : stdh*(2**1),
    '3' : std*(2**2),
    '3.5' : stdh*(2**2),
    '4' : std*(2**3),
    '4.5' : stdh*(2**3),
    '5' : std*(2**4),
    '5.5' : stdh*(2**4),
    '6' : std*(2**5),
    '6.5' : stdh*(2**5),
    '7' : std*(2**6),
    '7.5' : stdh*(2**6),
    '8' : std*(2**7),
    '8.5' : stdh*(2**7),
    '9' : std*(2**8),
    '9.5' : stdh*(2**8),
    '10' : std*(2**9),
    '10.5' : stdh*(2**9),
    '11' : std*(2**10),
    '11.5' : stdh*(2**10),
    '12' : std*(2**11),

}

for row in sheet1.iter_rows():
    for cell in row:
        cell.value = convert.get(str(cell.value), cell.value)
            


name, _ = args.e.split('.xlsx')

table.save('%s_py.xlsx' %name)
