import sys

from logic import edulogic

savedSinceLastChange = False

def main():
    cmd = ''
    cmd = input('Enter commmand: ')
    while not cmd == 'x':
        menu(cmd)

def createSchool():

    input_dic = {}

    input_var = input("Enter Institution name: ")
    input_dic['school'] = input_var

    input_var = input("Enter start year: ")
    input_dic['start_year'] = input_var

    input_var = input("Enter end year: ")
    input_dic['end_year'] = input_var

    input_var = input("Enter description: ")
    input_dic['description'] = input_var

    input_var = input("Complete [y/N]: ")
    if input_var == 'y' or input_var == 'Y':
        input_dic['complete'] = True
    else:
        input_dic['complete'] = False

    edulogic.CreateSchool(input_dic)








## Help functions
def menu(cmd):
    if cmd == 'e':
        createSchool()
    elif cmd == 's':
        ## Implement save function
        print('NOT IMPLEMENTED')
    elif cmd == 'q':
        if IsItSavedMenu():
            ## implement save function
            print('Application closed')
        ##implement is it saved and quit function
    else:
        print("ENTER PROPER COMMAND")
    cmd = input('Enter commmand: ')
    menu(cmd)

def IsItSavedMenu():
    if not savedSinceLastChange:
       input_var = input('Your changes is not saved, do you want to save this [Y/n]')
       if input_var == 'N' or input_var == 'n':
           return false
    return true
