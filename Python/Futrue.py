import matplotlib.pyplot as plt
import csv
import numpy as np
import os

year_data4_test = 1993
sumvars = 0
row_list = []
sumvars_list = []
row = 0
years_data1 = []
vars_data1 = []
years_data2 = []
vars_data2 = []
years_data3 = []
vars_data3 = []
years_data4 = []
vars_data4 = []

with open('../Data/carbon.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data1 = int(line[0])
        var_data1 = float(line[1])
        years_data1.append(year_data1)
        vars_data1.append(var_data1)

with open('../Data/temperature.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data2 = int(line[0])
        var_data2 = float(line[1])
        years_data2.append(year_data2)
        vars_data2.append(var_data2)

with open('../Data/arctic.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data3 = int(line[0])
        var_data3 = float(line[1])
        years_data3.append(year_data3)
        vars_data3.append(var_data3)

with open('../Data/sea.txt') as csvfile:
    readfile = csv.reader(csvfile, delimiter=',')

    for line in readfile:
        year_data4 = int(line[0])
        var_data4 = float(line[1])
        if year_data4 == year_data4_test:
            sumvars += var_data4
            row += 1
        else:
            row_list.append(row+1)
            row = 0
            sumvars_list.append(sumvars)
            sumvars = 0
            sumvars += var_data4
            year_data4_test = year_data4
    row_list.append(row+1)
    sumvars_list.append(sumvars)

def cal2semple():
    for i in range(len(sumvars_list)):
        num_a = sumvars_list[i]
        num_b = row_list[i]
        vars_data4.append((int((num_a/num_b)*100))/100)
    for i in range(1993, 2019):
        years_data4.append(i)

def cal_main(year, value, future):
    value_of_number = len(year)
    sum_value = sum(value)
    sum_year = 0
    sum_year_2 = 0
    sum_num_year = 0
    num_count = 1
    for i in range(1, len(year)+1):
        sum_year += i
    for i in range(1, len(year)+1):
        sum_year_2 += i**2
    for i in range(len(year)):
        sum_num_year += num_count * value[i]
        num_count += 1
    b = ((len(year)*sum_num_year)-(sum_year*sum_value))/\
        ((len(year)*sum_year_2)-(sum_year**2))
    a = ((sum_value)-(b*sum_year))/(len(year))
    c = (future - year[0])+1
    z = a + (b*c)
    return z

def cls():
    """ clear moniter in terminal """
    os.system("cls")
    os.system("clear") # clear the moniter function

def newdata_1(future_input):
    futrue_new_value = cal_main(years_data1, vars_data1, future_input)
    print(futrue_new_value, end=" ")

def newdata_2(future_input):
    futrue_new_value = cal_main(years_data2, vars_data2, future_input)
    print(futrue_new_value, end=" ")

def newdata_3(future_input):
    futrue_new_value = cal_main(years_data3, vars_data3, future_input)
    print(futrue_new_value, end=" ")

def newdata_4(future_input):
    futrue_new_value = cal_main(years_data4, vars_data4, future_input)
    print(futrue_new_value, end=" ")

def futrue_function():
    cal2semple()
    print("Carbon(1), Temperature(2), Arctic(3), Sea(4), Back(0)")
    select = int(input("Select Data: "))
    cls()
    if select == 1:
        future_input = int(input("Yesr: "))
        print("Value in the future: ", end="")
        newdata_1(future_input)
        print("parts per million")
        input("Enter to Main Manu")
    elif select == 2:
        future_input = int(input("Yesr: "))
        print("Value in the future: ", end="")
        newdata_2(future_input)
        print("Temperature Anomaly (C)")
        input("Enter to Main Manu")
    elif select == 3:
        future_input = int(input("Yesr: "))
        print("Value in the future: ", end="")
        newdata_3(future_input)
        print("Square KM")
        input("Enter to Main Manu")
    elif select == 4:
        future_input = int(input("Yesr: "))
        print("Value in the future: ", end="")
        newdata_4(future_input)
        print("Sea Height (mm)")
        input("Enter to Main Manu")
    elif select == 0:
        pass
    else:
        print("Out of range")
