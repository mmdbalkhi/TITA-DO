"""crate with python3, this is a moduls tita do, Enigma simulator! crptugraphi for data!"""
from random import shuffle
from pickle import dump, load

alphabet = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()-_=+\|}]{["':;?/>.<, '''
cipher = ''''''


File = open('./Data/Enigma.Eng', 'ab')
r1 = list(alphabet)
shuffle(r1)
r1 = ''.join(r1)
r2 = list(alphabet)
shuffle(r2)
r2 = ''.join(r2)

rotor_genarator()


file = open('./Data/Enigma.Tita', 'rb')
file = open("./Data/Enigma.Eng", "rb")
Rotor1, Rotor2, Rotor3 = load(file)
file.close()
#print ('rotor is ....',Rotor1,'  ' ,Rotor2,'  ' ,Rotor3)
#print(len(alphabet))

def reflector(char):
    '''reflector func'''
    return alphabet[len(alphabet)-alphabet.find(char)-1]

def enigma_one_char(char):
    '''enigma_one_char func'''
    char1 = Rotor1[alphabet.find(char)]
    char2 = Rotor2[alphabet.find(char1)]
    char3 = Rotor3[alphabet.find(char2)]
    reflected = reflector(char3)
    char3 = alphabet[Rotor3.find(reflected)]
    char2 = alphabet[Rotor2.find(char3)]
    char1 = alphabet[Rotor1.find(char2)]

    return char1

state = 0
def rotate_rotors():
    '''enigma_one_char'''
    global Rotor1, Rotor2, Rotor3
    Rotor1 = Rotor1[1:] + Rotor1[0]
    if state % 26:
        Rotor2 = Rotor2[1:] + Rotor2[0]
    if state % (26 * 26):
        Rotor3 = Rotor3[1:] + Rotor3[0]


def Enigma_starter(plain):
    global state, cipher
    for char in plain:
        state += 1
        cipher += enigma_one_char(char)
        rotate_rotors()

    # that's print!
    return(cipher)
