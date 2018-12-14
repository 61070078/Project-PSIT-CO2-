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
new_vars_data2 = []
years_data3 = []
vars_data3 = []
years_data4 = []
vars_data4 = []
new_vars_data4 = []

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
cal2semple()

def data4_change():
    first_data4 = vars_data4[0]
    for i in vars_data4:
        value = i - (first_data4)
        new_vars_data4.append((int(value*100))/100)
data4_change()

def data2_change():
    first_data2 = vars_data2[0]
    for i in vars_data2:
        value = i - (first_data2)
        new_vars_data2.append((int(value*100))/100)
data2_change()

def all_graph():
    fig = plt.figure()
    fig.add_subplot(221)
    plt.plot(years_data1, vars_data1)
    plt.ylabel("CO2 (parts per million)")
    plt.title("Carbon")
    fig.add_subplot(222)
    plt.plot(years_data2, new_vars_data2)
    plt.title("Global Temperature")
    plt.ylabel("Temperature Anomaly (C)")
    fig.add_subplot(223)
    plt.plot(years_data3, vars_data3)
    plt.title("Arctic Sea Ice")
    plt.xlabel("YEAR")
    plt.ylabel("Square KM")
    fig.add_subplot(224)
    plt.plot(years_data4, new_vars_data4)
    plt.title("Sea Level")
    plt.xlabel("YEAR")
    plt.ylabel("Sea Height (mm)")
    plt.show()

def graph_1(years, values):
    plt.plot(years, values)
    plt.xlabel("YEAR")
    plt.ylabel("CO2 (parts per million)")
    plt.title("Carbon")
    plt.show()

def graph_2(years, values):
    plt.plot(years, values)
    plt.title("Global Temperature")
    plt.xlabel("YEAR")
    plt.ylabel("Temperature Anomaly (C)")
    plt.show()

def graph_3(years, values):
    plt.plot(years, values)
    plt.title("Arctic Sea Ice")
    plt.xlabel("YEAR")
    plt.ylabel("Square KM")
    plt.show()

def graph_4(years, values):
    plt.plot(years, values)
    plt.title("Sea Level")
    plt.xlabel("YEAR")
    plt.ylabel("Sea Height (mm)")
    plt.show()

def graph_function():
    cls()
    print("Carbon(1), Temperature(2), Arctic(3), Sea(4), All Graph(5), Back(0)")
    select = int(input("Select : "))
    if select == 1:
        graph_1(years_data1, vars_data1)
    elif select == 2:
        graph_2(years_data2, new_vars_data2)
    elif select == 3:
        graph_3(years_data3, vars_data3)
    elif select == 4:
        graph_4(years_data4, new_vars_data4)
    elif select == 5:
        all_graph()
    else:
        print("Out of range")

def cls():
    """ clear moniter in terminal """
    os.system("cls")
    os.system("clear") # clear the moniter function

















