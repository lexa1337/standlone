from requests import *
from colorama import Fore, Back, Style
from os import system
system('cls')

print(Fore.RED + '''  ██████ ▄▄▄█████▓ ▄▄▄       ███▄    █ ▓█████▄  ██▓     ▒█████   ███▄    █ ▓█████ 
▒██    ▒ ▓  ██▒ ▓▒▒████▄     ██ ▀█   █ ▒██▀ ██▌▓██▒    ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ 
░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▓██  ▀█ ██▒░██   █▌▒██░    ▒██░  ██▒▓██  ▀█ ██▒▒███   
  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█▄   ▌▒██░    ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ 
▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒▒██░   ▓██░░▒████▓ ░██████▒░ ████▓▒░▒██░   ▓██░░▒████▒
▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░   ▒ ▒  ▒▒▓  ▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░
░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░
░  ░  ░    ░        ░   ▒      ░   ░ ░  ░ ░  ░   ░ ░   ░ ░ ░ ▒     ░   ░ ░    ░   
      ░                 ░  ░         ░    ░        ░  ░    ░ ░           ░    ░  ░
                                        ░                                         ''')

print(Fore.GREEN + 'Index Stealer By Lexa')
site = input(Fore.WHITE + 'enter the url of the site whose index you want to steal >> ')
index = get(f'{site}')
with open ("index.txt", "a+") as file:
    file.write(index.text)