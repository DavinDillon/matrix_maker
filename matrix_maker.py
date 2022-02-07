import math
import numpy as np
from scipy.linalg import inv

def is_number(x):
    try:
        float(x)
        num = True
    except:
        num = False
    return num

def get_rows():    # ask user for number of rows
    
    rows_found = False

    while not rows_found:
        rows = input('How many rows?   ')
        if rows.isdigit():
            rows = float(rows)
            rows_found = True
    return rows

def get_cols():     # ask user for number of columns
    cols_found = False
    while not cols_found:
        cols = input('How many columns?   ')
        if cols.isdigit():
            cols = float(cols)
            cols_found = True
    return cols


def frm():       # function to create a new matrix
    rows = get_rows()
    cols = get_cols()
    values = [0] * int(rows) #initialize outside list
    # if you want to enter by columns you can just enter the values in
    # the columns as rows and use the transpose
    for i in range(int(rows)):
        values[i] = input(f'Enter row {i+1}, separated by commas:  ')
        values[i] = values[i].split(',') # create inside lists by separating user input strings

    for j in range(int(rows)):
        for m in range(int(cols)):
            values[j][m] = float(values[j][m])  # converts all values to float for numpy
    
    return np.array(values) 
