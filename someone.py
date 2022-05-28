from random import choice
from random import choice
from time import sleep
from colorama import init,Fore
init()

file = open("list.txt","r",encoding='utf-8')
content = file.read()
content = content.splitlines()
file.close

def chose_someone():
    global someone
    someone = choice(content)
    someone = someone.split(".")

def get_last_name():
    global someone
    return someone[0]

def get_first_name():
    global someone
    return someone[1]

def get_class():
    global someone
    return someone[2]

def print_list():
    input("")
    while True:
        someone = choice(content)
        someone = someone.split(".")
        print("Nom: " + Fore.CYAN + someone[0] + Fore.WHITE + "   Prenom: " + Fore.CYAN + someone[1] + Fore.WHITE + "   Classe: " + Fore.CYAN + someone[2] + Fore.WHITE)
        sleep(.1)
