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

def cal_main(year, value):
    future = int(input())
    sum_value = sum(value)
    sum_year = sum(year)
    sum_year_2 = 0
    sum_num_year = 0
    for i in year:
        sum_year_2 += i**2
    for i in range(len(year)):
        sum_num_year += (year[i]*value[i])
    b = ((len(year)*sum_num_year)-(sum_year*sum_value))/\
    ((len(year)*sum_year_2)-(sum_year**2))
    a = ((sum_value)-(b*sum_year))/(len(year))
    print(sum_value, sum_year, sum_num_year, sum_year_2)
    print(a)
    print(b)
    print("y = %.2f + %.2f(n)" %(a, b))
    z = a + (b*future)
    print("%.2f" %(z))

def main_function():
    print(years_data1, vars_data1)
    cal2semple()
    # print(vars_data4, vars_data3, vars_data2, vars_data1)
    cal_main(years_data1, vars_data1)
main_function()