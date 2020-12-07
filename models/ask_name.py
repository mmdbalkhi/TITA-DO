"""crate with python3, this is a moduls tita do Ask name, and criptographi Name!"""

from hashlib import sha3_512
from os.path import exists
from models.enigma import Enigma_starter


def sha_maker(data):
    '''sha maker func'''
    hash = sha3_512()
    hash.update(data.encode("utf-8"))
    hash = hash.hexdigest()
    return hash

def ask_name():
    '''ask_name fun'''
    input_name = Enigma_starter(str(input("hello! What is your password? = ")))
    input_name = sha_maker(input_name)

    if exists('./Data/pass.Tita') == True:
        with open("./Data/pass.Tita", "r") as file:
            #f.write(one_line)
            current_name = file.read()
            while current_name != input_name:
                print("Your name is different\nPlease enter a correct password!")
                input_name = str(input("What is your password? = "))
                if current_name == input_name:
                    print("OK!\nYour password is correct")
                    return True
                if current_name != input_name:
                    print("Access denied\nYou can't access and use progeam")
                    return False

    if exists('./Data/pass.Tita') == False:
        with open("./Data/pass.Tita", "w") as file:
            str(file.write(input_name))
            print("your password is Crated \n \t\t welcome!")
