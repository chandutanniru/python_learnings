#what is file handling?
#handling certine file which is not python file.
#pdf,xcel,json--etc
#to handle the file in python we required a inbuilt function which is "open function"
#while you handling the file we will be having 4 modes.
#Modes:- r,a,w,x
#x-mode--> it is used to create a new file.
#f = open('trail.txt', 'x').
#W - mode--> over write mode.
"""f = open('trail.txt','w')
f.write("i am applying write mode to my file,"
        "if i write one more time my content can be overwritten")
f.close()"""
# r-->read mode--> to read the content in file
#by default when you use the open function it is in read mode.

#f = open('trail.txt','r')
#print(f.read())
#f.close()

#write mode:-
#f = open('trail.txt','w')
#f.write("i am over writing my content in the file"
        #"so the previous content can be over written")
#f.close()

#a-mode-->append mode
#f = open('trail.txt','a')
#f.write('i am adding extra content at end of the existing content')
#f.close()
#read the file
"""f = open('trail.txt')
print(f.read())
f.close()"""
#=====================================================================================================================================
#05-08-2024
#to read xcel file use "xlrd" libraray
#what is xlrd?
"""import xlrd
#xlrd is a library for reading the data and formatting information from excel file. it supports .xls format only
loc = "C:\\Users\\chand\\Downloads\\Financial Sample (1).xls"
#use the xlrd.ope_workbook to read the xls file
wb=xlrd.open_workbook(loc)
#how to access the perticular sheet data?
sheet = wb.sheet_by_index(0)
#reed data sell wise
#i want to know how many rows and columns in given file?
print(sheet.nrows)
print(sheet.ncols)
#read the particular cell
#cell_value(row, col)
#indexing can be start from zero
print(sheet.cell_value(7,2)) #7th row second column
#print the entire rows
print(sheet.row_values(0))
print(sheet.col_values(1))
#extract all the data in console.
for x in range(sheet.nrows):
    print(sheet.row_values(x))"""
#ITERATORS:-
#what is iterators?
#iteraters helps you to take large bunch of data in limited memory space.
#means it breaks the large data in to tiny chunks.
#in iterators we are having 2 protocols
#1. __iter__()
#2. __next__()
"""l = ['apple','banana','mango','kiwi','orange']
for x in l:
#x is iter over each and every element in collection.
    print(x)"""
"""x = iter(l)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""

"""class Number:
    def __iter__(self):
        self.intial = 0
        return self
    def __next__(self):
        if self.intial <= 5:
            x = self.intial
            self.intial += 1    #self,intial+1
            return x
        else:
            StopIteration("are you stupid")
n = Number()
#for x in n:
#   print(x)
x = iter(n)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))"""
#pip package
#pickling
#connecting with you mysql by using python
#python json
#practical examples on four pillers of opps.
#============================================================================================================================

#Genarators
"""A genarater is a function that returns an iterator that produce a sequence of values when iterated over."""
#when we have to use this generators?
"""generators are use when we want to produce large sequence of values, 
we dont want to store all of them in the memory at once"""
#use "def", instead of "return" use the "yield"
"""def my_generator(n):
    value = 0
#loop until counter is less than n
    while value  < n:
        yield value
        value += 1   #value+1
#iterate over your generator to generate sequence of values
for value in my_generator(9):
    print(value)"""
"""Note:- when you are using integer directly in to for loop it through an error use it with range function 
when you are using generators then instead return use yield it support int object in for loop"""

#pickling:-
"""the process of converting any type of object in python
for example (list,tuple,set--etc)on to bytes is known as plickling"""

"""when it comes to python these pickling conversions is known as
serialisation, deserialisation."""
#what is bites?
#0's and 1's is known as bytes
#to do the pickling use package called "pickle".
#conversion of 2D data formate to 1D data and store it --->serialisation
#qnd in same time conversion 1D data in to 2D is known as pickle --->deserialisation

import pickle
#open a pickle file.txt
pickle_file = open("pickle2.txt","wb")   #wb is known as work and bites
#use pickle.dump to dump the file
my_dict = "C:\\Users\\chand\\Downloads\\python programs for practice.docx"
pickle.dump(my_dict,pickle_file)
#pickle.dump(collection_name,pickle_file name(where you want to store
#in the above step you dump the data in to serialisation
#if you want to read or visualise real data then follow the
pickle_file = open("pickle2.txt","rb")
#load the data that you have stored
new_dict = pickle.load(pickle_file)
print(new_dict)
#step1:- import pickle library
#step2:- creating a pickle file in "wb" (work and byte)
#step3:- use "pickle.dump" to convert the data.
#step4:- read the actual data by using open("pickle filename","rb")
#step5:- after that load the load into new_file
#step6:- print the file
#======================================================================================================07-08-2024
#python pip:- it is basically package manager for python package or module
#what is package?
#package is basically something that contains all the files you needed.
#so packages contains all the files you need for certain modules.
#what is module.
#modules are code libraries which you can include in your project
#Numpy
#Pandas
#Matplotlib and Seaborn
#Pendulum
#Ptyhon image processing
#Movie py
#Tkinter
#Pyqt
#Py32
#Py test
#how to install this packages?
"""pt -m pip install "package name" when you use CMD"""
"""!pip install "package name" ---> colab notebook and jupiter notebook"""
#What is global and local packages?
import camelcase
x = camelcase.CamelCase()
a = "hi there! these is the message to check each word of the letters are capitalize"
print(x.hump(a))
#how to uninstall package from cmd?
#py -m unstall "package name"
#how to check what are all packages present in your system
#py -m pip list
#how to upgrade your pip?
#py -m pip install --upgrade pip
#how to check the version of your pip
#py -m pip --version
#========Json=======
#java script object notation
#it is basically a syntax that storing and exchanging the data.
"""{"first_name":"chandu,
    "last_name":"t",
    address:{street: 3rd bsnl office,
            "city": }"""
import json
#what is parse?
#it is a method where one string of data is converting into another form of data
"""person = {'name':'andrew',
          'language':['english','french']}
print(type(person))
#convert this into jason formate
person_dict = json.dumps(person)
print(person_dict)
print(type(person_dict))

#lets open a json file by using  "with open"
loc = "C:\\Users\\chand\\Downloads\\sample1.json"
with open(loc) as f:
    data = json.load(f) #--->it converts the json data into dictionary
print(data)
print(type(data))"""

#data structures:
#linked list
#hash map
#trees
#arrays
















































































































