"""save data data in TITA-DO project
"""
from os.path import exists
from sys import exit
from enigma import Enigma_starter

def enigma(word):
    return Enigma_starter(word)
'''
print("please Enter alphabet a short!")
number = 0
while True:
    todo = str(input('YourTodo?'))
    if todo != 'exit' and todo != 'show now':
        print(todo)
        number += 1
        file = open("Data.tita", "a")
        file.writelines(todo)
        file.writelines('\n')
        file.close()
    if todo == 'exit':
        close = str(input('Ary you sure? yes or no? \n'))
        if close == 'yes':
            print('goodbye!')
            exit()
    if todo == 'Show now':
        print('showed!')
        print(todo)
        if exists('Data.tita'):
            with open("Data.tita", "r") as file:
                print(file.read())
                file.close()
'''
print(Enigma_starter("""a
x
zx
zsd
asd
a
c
vc"""))