""" main file """
import graph as g
import Futrue as f
import os

def main_function():
    cls()
    while True:
        print("First Function(1), Futrue(2) Exit(0)")
        select_function = int(input("Select : "))
        if select_function == 0:
            break
        elif select_function == 1:
            g.graph_function()
        elif select_function == 2:
            f.futrue_function()
        else:
            print("Out of range")
        cls()

def cls():
    """ clear moniter in terminal """
    os.system("cls")
    os.system("clear") # clear the moniter function

main_function()
