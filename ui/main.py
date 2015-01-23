import sys

from logic.edulogic import edulogic

savedSinceLastChange = False

## Start education
e = edulogic()

def main():



    cmd = ''
    cmd = raw_input('Enter commmand: ')
    menu(cmd)


def createSchool():

    input_dic = {}

    input_var = raw_input("Enter Institution name: ")
    input_dic['school'] = input_var

    input_var = raw_input("Enter start year: ")
    input_dic['startYear'] = input_var

    input_var = raw_input("Enter end year: ")
    input_dic['endYear'] = input_var

    input_var = raw_input("Enter title: ")
    input_dic['title'] = input_var

    input_var = raw_input("Enter description: ")
    input_dic['description'] = input_var

    input_var = raw_input("Complete [y/N]: ")
    if input_var == 'y' or input_var == 'Y':
        input_dic['complete'] = True
    else:
        input_dic['complete'] = False

    e.CreateSchool(input_dic)


## Help functions
def menu(cmd):
    print("" + cmd)
    if cmd == 'e':
        createSchool()
    elif cmd == 's':
        ## Implement save function
        print('NOT IMPLEMENTED')
    elif cmd == 'h':
        PrintMenu()
    elif cmd == 'q':
        if IsItSavedMenu():
            ## implement save function
            print('Application closed')
         ##implement is it saved and quit function
    else:
        print("ENTER PROPER COMMAND")

    cmd = raw_input('Enter commmand: ')
    if not cmd == 'x':
        menu(cmd)

def IsItSavedMenu():
    if not savedSinceLastChange:
       input_var = input('Your changes is not saved, do you want to save this [Y/n]')
       if input_var == 'N' or input_var == 'n':
           return false
    return true


def PrintMenu():
    print('e: Create edcutaion')
    print('s: Create School')
    print('q: Quite application')
    print('h: print menu')
