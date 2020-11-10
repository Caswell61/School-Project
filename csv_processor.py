## Author: Nick Caswell
## Class: CSc 110
## Description: This program takes a data set from a .csv file,
##              and performs operations on it based on user input.
##

def open_csv_data(name):
    '''
    This function opens and formats the data set properly into a 2D list of
    floats.
    name: A string representing the name of the file requested.
    '''
    file_open = open(name, 'r')
    file_data = file_open.readlines()
    data_list = []
    for line in file_data:
        line = line.strip('\n').split(',')
        num_list = []
        for x in line:
            num_list.append(float(x))
        data_list.append(num_list)
    return data_list

def columns(data_list, which_col):
    '''
    This function takes the data set and creates a new list of floats
    depending on the column the user requested.
    data_list: A 2D list of floats from the requested file name.
    which_col: An integer from the user, determining which column
               they want operated upon.
    '''
    new_col_list = []
    which_col -= 1
    for data in data_list:
        new_col_list.append(data[which_col])
    return new_col_list

def operations(column_list, operation):
    '''
    This function handles all of the operations that the user might request,
    minimum, maximum, or average. It returns a float value depending on what
    the user wanted done to the data.
    column_list: A list of floats from the specific column the user wanted
                 operated on.
    operation: A user generated string, either min, max or avg.
    '''
    if operation.lower() == 'min':
        val = -1
        for x in column_list:
            if val == -1:
                val = x
            elif val > x:
                val = x
    elif operation.lower() == 'max':
        val = -1
        for x in column_list:
            if val == -1:
                val = x
            elif val < x:
                val = x
    elif operation.lower() == 'avg':
        total = 0
        for x in column_list:
            total += x
        val = total / len(column_list)
    return val

def output(operation, column_number, value):
    '''
    This function prints the correct output depending on the users
    desired operation.
    operation: A user generated string, either min, max or avg.
    column_number: A user generated integer, the column that the
                   user wanted operated upon.
    value: A float calculated from the desired column.
    '''
    if operation.lower() == 'min':
        print("The minimum value in column", column_number, "is:", value)
    elif operation.lower() == 'max':
        print("The maximum value in column", column_number, "is:", value)
    elif operation.lower() == 'avg':
        print("The average for column", column_number, "is:", value)

def main():
    file_name = input("Enter CSV file name: \n")
    column_num = int(input('Enter column number: \n'))
    column_op = input('Enter column operation: \n')
    data = open_csv_data(file_name)
    column_list = columns(data, column_num)
    desired_value = operations(column_list, column_op)
    output(column_op, column_num, desired_value)
main()
