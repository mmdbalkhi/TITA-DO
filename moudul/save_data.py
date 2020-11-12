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
    if todo == 'exit' or 'quit' or 'Exit' or 'EXIT' or 'Quit' or 'Quit':
        todo = str(input('Ary you sure?'))
        if todo == 'ok' or 'yes' or 'Yes' or 'Ok':
            print('goodbye!')
            break
    elif todo == 'Show now' or 'show now' or 'SHOW NOW' or 'show Now' or 'Show Now':
        print('show')
        print(todo)
        #break
    else:
        print("hello!")
        #break