# starter download Python Packages
#   * pandas from python packages
#   * openpyxl form python packages
#   * pip install tksheet from terminal
#   * pip install pyinstaller form terminal
#   * tabulate from python packages

# import library
import pandas as pd                                          # import data from excel
import tkinter as tk                                         # create GUI in python
from tkinter import filedialog                               # use command tkinter read path-file
from tabulate import tabulate
import numpy as np

def openfile():
    file_path = filedialog.askopenfilename()  # select file path (find)
    return file_path

# configuration link between file.excel into python file
root = tk.Tk()
root.withdraw()
excel_file = openfile()
df = pd.read_excel(excel_file, header=None)                 # Read file from selected file-path

# create class predict data
class age:
    # create information variable
    def __init__(self, data, age):
            self.data = data
            self.age = age
    # create show variable
    def __repr__(self):
        return "%s" % (self.data)
# create class process data
class optimal:
    # create information variable
    def __init__(self, data, index):
        self.data = data
        self.index = index
    # create show variable
    def __repr__(self):
        return "[%s, %s]" % (self.data, self.index)

# set variable type global (hit,fault and input data frame)
global page_hit, page_miss, input_frame
data_process = []                                          # save data from excel
data_frame = []                                            # save frame and data 2D-Array
input_frame = 0                                            # user input for amount of frame in page fault
page_hit = 0                                               # page hit
page_miss = 0                                              # page fault

# function input data(all) from excel
def input_data():
    for i in range(0,len(df)):                             # condition 0 -> all number from excel
        data_process.append(df.at[i, 0])                   # append data into array(data_process)

# function box-collect data
def create_memory(num_frame):                              # input variable number frame by main function
    for i in range(num_frame):                             # loop 0 -> number frame
        data_frame.append(age(None, None))                 # set variable box-collect data ( [data,predict] )

# function object self(age)
def check_age(self):
    return self.age

# function object self(index)
def check_index(self):
    return self.index

# function optimal process
def optimal_process(self,loop):
    ref = []                                             # 2D-array Reference

    for i in range(len(data_frame)):                     # check box-collect data
        reset = 0
        for n_data in range(loop,len(data_process)):                      # loop number box none
            if data_process[n_data] == data_frame[i].data:                # if data_check have data in box-collect data
                ref.append(optimal(data_process[n_data],n_data))          # append into array ref [data,age(predict)]
                reset += 1                                                # break loop n_data
                break
        if reset == 0:                                                 # if data_check predict non-fount data_check
            ref.append(optimal(data_frame[i].data ,len(data_process))) # append in to array ref [data,50] 50: status non-fount
    ref.sort(key=check_index)                                          # sort array ref (min -> max)
    data_frame.sort(key=check_age)                                     # sort array data_frame (mix -> max)
    q = 0
    for check_data in range(len(ref) - 1, -1, -1):                     # check data
        for n_frame in range(len(data_frame)-1,-1,-1):                 # check frame

            if data_frame[n_frame].data == ref[check_data].data:       # if data in frame have from data in ref
                data_frame[n_frame].data = self
                data_frame[n_frame].age = 0
                q = 1                                                  # break loop n_frame
                break
        if q == 1:                                                     # break loop check_data
            break
    print(f"Reference: {ref} \n")                                      # show data reference

# main function
input_data()                                                           # into function input data
print(f"Data[{len(data_process)}]: {data_process}")                    # show lengths_data and data

# select frame memory
input_frame = int(input("input desire amount of frame: "))
create_memory(input_frame)                                          # into function box-collect data and input variable
print(f"default frame [data,frequency]: {data_frame}")              # print default box-collect data (first-process)

for i in range (0,len(data_process)):                               # loop 0 -> max lengths data from excel
    p = 0

    # loop check hit-frame
    for n_frame in range(len(data_frame)):
        if data_process[i] == data_frame[n_frame].data:             # if data_check have data into data_frame
            page_hit += 1                                           # hit = hit + 1
            p = 1                                                   # break loop n_frame
            break
    # else condition (miss-frame or page fault)
    if p == 0:
        k = 0
        for n_data in range(len(data_frame)):                      # check index_data
            if data_frame[n_data].data == None:                    # if new data into box-collect data
                data_frame[n_data] = (age(data_process[i], 0))     # append data in frame and set frequency = 0
                page_miss += 1                                     # miss = miss + 1
                k += 1                                             # break loop n_data
                break
        if k == 0:
            optimal_process(data_process[i],i)
            page_miss += 1

        for j in range(len(data_frame)):                         # check index_data
            if data_frame[j].data != None:                       # if data have into box-collect data
                data_frame[j].age += 1                           # age++ (data old)
    columns = ['Step', 'box-collect','data_check' ,'page-hit', 'page-fault']
    arr = np.array([[i+1,data_frame,data_process[i],page_hit,page_miss]])
# show data step by step (num-step, data(check_process), data_frame, number page-hit and number page-fault)
    print(tabulate(arr,headers=columns, tablefmt="fancy_grid", showindex="always"))
