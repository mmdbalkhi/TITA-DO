"""save data data in TITA-DO project
"""
from os.path import exists
from sys import exit
print("please Enter alphabet a short!")

while True:
    todo = str(input('YourTodo?'))

    file = open("Data.tita')", "a")
    file.writelines(todo)
    file.writelines('\n')
    file.close()
    if todo == 'exit':
        close = str(input('Ary you sure?'))
        if close == 'ok':
            print('goodbye!')
            exit()
    elif todo == 'Show now':
        print('showed!')
        print(todo)
        if exists('Data.tita'):
            with open("Data.tita", "r") as file:

                print(file.read())
                file.close()
    else:
        print("hello!")
        #break
