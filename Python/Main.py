""" main file """
import graph as g
import os

def main_function():
    cls()
    while True:
        print("First Function(1), Exit(0)")
        select_function = int(input("Select : "))
        if select_function == 0:
            break
        elif select_function == 1:
            g.function_1()
        else:
            print("Out of range")
        cls()

def cls():
    """ clear moniter in terminal """
    os.system("cls")
    os.system("clear") # clear the moniter function

main_function()
