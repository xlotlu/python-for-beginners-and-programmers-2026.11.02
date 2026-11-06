# Exercițiu:

#1. creați un modul numit `config`
# în folderul curent,
# în care adăugați
# TODOS_URL = 'https://jsonplaceholder.typicode.com/todos'
#
# apoi în fișierul curent faceți
import config
print(config.TODOS_URL)

#2. instalați library-ul "requests"
# cu comanda de sistem
# pip install requests

import requests

"""
response = requests.get(url)

response.content # bytes.
# ^ asta vrem când am downloadat un fișier binar

response.text # str.
# ^ bytes-ii gata decodați.
#   asta vrem când accesăm o pagină html
#   sau un alt format plain text
#
#   nu îl vrem pe el când lucrăm cu json

# în mod normal am face cu json așa:
import json

data = json.loads(response.content)
# doar că nu este nevoie să facem asta,
# pentru că library-ul requests are convenience method:
response.json()
"""

#3. scrieți o funcție
def save_todos(url, filename, completed=False):
    pass
# care încarcă TODO-urile de la `url`-ul dat,
# filtrează elementele cu `completed` respectiv,
# și le salvează `filename`, câte unul pe linie,
# în forma "<id>: <title>"
#
# scrieți cel mai concis cod posibil
# care să fie readable.
#
# testați cu:

def save_todos(url, filename, completed=False):
    response = requests.get(url)

    with open(filename, "w", encoding="utf-8") as f:
        for todo in response.json():
            if todo['completed'] is completed:
                f.write(f"{todo['id']}: {todo['title']}\n")

save_todos(config.TODOS_URL, "todos.txt")

# mai compact, sau cel puțin diferit:
TODO_LINE = "{id}: {title}\n"

def save_todos(url, filename, completed=False):
    response = requests.get(url)
    data = filter(
        lambda item: item['completed'] is completed,
        response.json()
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(
            TODO_LINE.format(**todo)
            for todo in data
        )


# despre path-uri:

# escape sequences
"\n" "\r" "\t"
"\x5a" # byte-ul 5a (hexadecimal)
"\u0219"  # caracterul unicode de la poziția respectivă în hexa
          # când indexul are 2 bytes
"\U0001F3A9"  # caracterul unicode, indexul 4 bytes
"\N{TOP HAT}" # numele din unicode standard
"\N{LATIN capital LETTER S WITH COMMA BELOW}"
"\\" # escaping the slash

#sau "raw string":
r"C:\Users\Eu\Desktop\myfile.txt"

# Exercițiu
# dat fiind un folder ce nu știm dacă există
# vrem să salvăm TODO-urile în el,
# fiecare într-un fișier, în format json.

#scrieți în config
#TODO_DIR = r"C:\Users\...\Desktop\work\todos"
#from config import TODO_DIR
import config

def save_todos(url, parent_dir):
    pass

# Q: cum creăm un tree de directoare părinte?
# A: am putea face așa
from pathlib import Path

todo_dir = Path(config.TODO_DIR)
for ancestor in reversed(todo_dir.parents):
    if not ancestor.exists():
        ancestor.mkdir()

# doar că nu este nevoie, pentru că avem
# o variantă mult mai simplă:
todo_dir = Path(config.TODO_DIR)
#todo_dir.mkdir() # va crăpa cu FileNotFoundError
                  # pentru că nu există directorul părinte

#todo_dir.mkdir(parents=True)  # va crea toată structura părinte
# doar că... a doua oară:
#todo_dir.mkdir(parents=True)  # va crăpa cu FileExistsError
#todo_dir.mkdir(parents=True, exist_ok=False)

# also, obiectele Path suportă operatorul '/' :
todo_dir / "subdir" / "alt dir" / "my.json"

import json
from pathlib import Path
import requests

import config


# strategie?
def save_todos_as_json(url, parent_dir):
    # 1. verificăm că avem director în care să scriem
    todo_dir = Path(parent_dir)
    todo_dir.mkdir(parents=True, exist_ok=True)

    # 2. încărcăm TODOS cu requests
    response = requests.get(url)
    data = response.json()

    # 3. iterăm
    for todo in data:
        # 4. pentru fiecare TODO creăm un fișier nou
        #    cu numele "<id>.json"
        fname = todo_dir / f"{todo['id']}.json"
        with open(fname, 'w', encoding="utf-8") as f:
            # 5. în care scriem cu json.dump
            json.dump(todo, f, indent=2)

save_todos_as_json(config.TODOS_URL, config.TODO_DIR)

# TODO: Modificați funcția de mai sus
# astfel încât să salveze fișierele în
# config.TODO_DIR/completed, respectiv
# config.TODO_DIR/pending
