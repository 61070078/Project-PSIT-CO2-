""" main file """
import graph as g
import Futrue as f
import svg as s
import os

def main_function():
    cls()
    while True:
        cls()
        print("Graph(1), Futrue(2), Save Graph To SVG(3), Exit(0)")
        select_function = input("Select : ")
        if select_function == '0':
            cls()
            break
        elif select_function == '1':
            cls()
            g.graph_function()
        elif select_function == '2':
            cls()
            f.futrue_function()
        elif select_function == '3':
            cls()
            s.svg_main()
        else:
            cls()
            print("Out of range")

def cls():
    """ clear moniter in terminal """
    os.system("cls")
    os.system("clear") # clear the moniter function

main_function()
