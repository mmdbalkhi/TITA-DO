"""crate with python3, this is a moduls tita do Ask name, and criptographi Name!"""

from moudul.enigma import Enigma_starter
from hashlib import sha3_512
from os.path import exists
from sys import exit

def sha_maker(data):
    hash = sha3_512()
    hash.update(data.encode("utf-8"))
    hash = hash.hexdigest()
    return hash

def ask_name():
    Name =Enigma_starter(str(input("hello! What is your password? = ")))
    Name = sha_maker(Name)
    if exists('./Data/pass.Tdo') == True:
        with open("./Data/pass.Tdo", "r") as file:
            #f.write(one_line)
            CurrentName = file.read()
            
            while CurrentName != Name:
                print("Your name is different\nPlease enter a correct password!")
                Name = str(input("What is your password? = "))
                if CurrentName == Name:
                    print("OK!\nYour password is correct")
                    return True
                if CurrentName != Name:
                    print("Access denied\nYou can't access and use progeam")
                    return False
                    exit()
    if exists('./Data/pass.Tdo') == False:
        with open("./Data/pass.Tdo", "w") as file:
            str(file.write(Name))
            print("your password is Crated \n \t\t welcome!")
