# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b) 

# READ ----------------

file_info = open('Modules VS Packages.txt');
print(file_info) 
#<_io.TextIOWrapper name='Modules VS Packages.txt' mode='r' encoding='cp1252'>

# text = file_info.read();
text = file_info.read(10); # print the first 10 characters
print('HI', text)

# f = open('Modules VS Packages','w');
# f.write('nothing');
line = file_info.readline()
print(line)

lines = file_info.readlines()  # returns lines with additional line breaks
lines = file_info.read().splitlines()  # not have additional line breaks
print(lines)
print(type(lines)) # <class 'list'>

file_info.close()

# file closes the files by itself
with open('file1.txt') as f:
    lines = f.read().splitlines()
    print(lines)


# WRITE ----------------
    
with open('file1.txt','a') as f:
    f.write(' is impossibe.')

with open('file2.txt','w') as f:
    f.write('This text will be written in a newly created file')


# DELETE ----------------
    
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')    
    

# ---------------- JSON FILES ----------------

import json

# python dictionary
person = {
    "name": "Aditya",
    "country": "India",
    "branch": "Indore",
    "skills": ["Java", "JS", "Backend", "Python"]
}

# File with .json

with open('MyInfo.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=True, indent=4)
    # there is no binary representation in JSON. Therefore all strings should be valid unicode points.
    # ensure_ascii does two things : Ensuring your output is valid ascii characters (even if they have unicode inside) and allow the function to return an unicode object.

# Changing JSON to Dictionary

person_json = json.dumps(person, indent=4) # dumps() stores data into a string file
print(type(person_json))
print(person_json)

# File with csv Extension
# CSV stands for comma separated values.



import csv
with open('../Pandas/Churn_Modelling.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

    import xlrd
    excel_book = xlrd.open_workbook('sample.xls')
    print(excel_book.nsheets)
    print(excel_book.sheet_names)

    import xml.etree.ElementTree as ET
    tree = ET.parse('info.xml')
    root = tree.getroot()
    print('Root tag:', root.tag)
    print('Attribute:', root.attrib)
    for child in root:
        print('field: ', child.tag)
