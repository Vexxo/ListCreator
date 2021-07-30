import sys
import keyboard
import os


os.system('title Press [Q] to exit or [P] to make a new list.')


def list():
    userinput = input("Enter list of words or numbers you would like turned into a formatted list: ")
    words = userinput  
    words_list = words.split()
    print(words_list)

list()



while True:
    if keyboard.is_pressed('Q'):
        sys.exit()
    elif keyboard.is_pressed('P'):
        list()
    

