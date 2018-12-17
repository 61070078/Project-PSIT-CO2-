""" Save graph to SVG function """
import csv
import os
import pygal as py

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

def svg_carbon():
    line_chart = py.Line(x_label_rotation=90)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(1958, 2019))
    line_chart.add('CARBON', vars_data1)
    line_chart.render_to_file('../Web/SVG/carbom.svg')
    return '[ (CARBON) Save successfully ]'

def svg_tem():
    line_chart = py.Line(x_label_rotation=90)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(1880, 2018))
    line_chart.add('Temperature', new_vars_data2)
    line_chart.render_to_file('../Web/SVG/tem.svg')
    return '[ (Temperature) Save successfully ]'

def svg_arc():
    line_chart = py.Line(x_label_rotation=90)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(1979, 2018))
    line_chart.add('Arctic', vars_data3)
    line_chart.render_to_file('../Web/SVG/arc.svg')
    return '[ (Arctic) Save successfully ]'

def svg_sea():
    line_chart = py.Line(x_label_rotation=90)
    line_chart.title = 'Browser usage evolution (in %)'
    line_chart.x_labels = map(str, range(1993, 2018))
    line_chart.add('Sea', new_vars_data4)
    line_chart.render_to_file('../Web/SVG/sea.svg')
    return '[ (Sea) Save successfully ]'

def svg_main():
    print(svg_carbon())
    print(svg_tem())
    print(svg_arc())
    print(svg_sea())
    input("Enter to Main Manu")