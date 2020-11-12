"""save data data in TITA-DO project

if exists('../Data/Data.tita') == True:
    with open("name.log", "r") as file:
        pass

if exists('name.log') == False:
    with open("name.log", "w") as file:
        pass"""
#from os.path import exists
#from sys import exit
print("please Enter alphabet a short!")

while True:
    todo = str(input('YourTodo?'))
    if todo == 'exit':
        close = str(input('Ary you sure?'))
        if close == 'ok':
            print('goodbye!')
            break
    elif todo == 'Show now':
        print('showed!')
        print(todo)
        #break
    else:
        print("hello!")
        #break
