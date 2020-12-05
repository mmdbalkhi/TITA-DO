"""crate with python3, this is a moduls tita do Ask name, and criptographi Name!"""

from hashlib import sha3_512
from os.path import exists
from pickle import dump, load
from models.enigma import Enigma_starter


def sha_maker(data):
    '''sha maker func'''
    hash = sha3_512()
    hash.update(data.encode("utf-8"))
    hash = hash.hexdigest()
    return hash

def ask_name():
    '''ask_name fun'''
    input_name = Enigma_starter(str(input("hello! What is your Name? = ")))
    input_pass = Enigma_starter(str(input("hello! What is your passport? = ")))
    input_name = sha_maker(input_name)
    input_pass = sha_maker(input_pass)

    if exists('./Data/user.Tita') == True:
        with open("./Data/user.Tita", "r") as file:
            #f.write(one_line)
            current_name = file.read()
            while current_name != input_name:
                print("Your name is different\nPlease enter a correct Name!")
                input_name = str(input("What is your  name? = "))
                
                if current_name == input_name:
                    print("OK!\nYour name is correct")
                    file_p = open('./Data/pass.Tita', 'rb')
                    password = load(file_p)
                    file_p.close()

                    if password == input_pass:
                        print("Your Ok! wellcome!")
                        return True

                if current_name != input_name:
                    print("Access denied\nYou can't access and use progeam")
                    return False

    if exists('./Data/user.Tita') == False:
        with open("./Data/user.Tita", "w") as file:
            file_p = open('./Data/pass.Tita', 'wb')
            dump(str(input_pass), file_p)
            str(file.write(input_name))
            print("your user is Crated \n \t\t welcome!")