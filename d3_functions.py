# funcție fără argumente
def nume():
    print("m-am executat")

# funcție cu argumente
def multiply(a, b):
    return a * b

# Scrieți două funcții de conversie
# între metri și feet

M_TO_FT = 3.28

def m_to_ft(m):
    return m * M_TO_FT

def ft_to_m(ft):
    return ft / M_TO_FT

print(m_to_ft(10))
print(ft_to_m(32.8))

# Scrieți o funcție
def get_greeting_for_hour(hour):
    pass # no-op statement
# care primește ca număr întreg
# argumentul `hour`
# și returnează string-ul de salut
# potrivit orei respective

def get_greeting_for_hour(hour):
    if 5 <= hour < 10:
        return "Buna dimineata"
    elif 10 <= hour < 18:
        return "Buna ziua"
    elif 18 <= hour < 22:
        return "Buna seara"
    else:
        return "Noapte buna"

# Exercițiu suplimentar:
# știind că:
# - în modulul `datetime` există clasa `datetime`
# - `datetime` are metoda `now()`
# - ce returnează un obiect datetime ce are atributul `hour`
#
# știind că sintaxa de import dintr-un modul este
# from module import symbol
#
# și știind că sintaxa de acces după atribut este
# object.attribute

# scrieți o funcție
def get_current_greeting():
    pass
# ce returnează salutul corect pentru ora curentă a zilei.
# folosiți în interiorul acestei funcții un call către
# funcția scrisă mai sus `get_greeting_for_hour(hour)`

# 1. importăm clasa datetime
from datetime import datetime
# 2. aflăm timestamp-ul curent
now = datetime.now()
# accesăm atributul hour
now.hour


def get_current_greeting():
    # vom afla ora curentă
    now = datetime.now()
    hour = now.hour
    return get_greeting_for_hour(hour)

# nu faceți așa ceva, că... readability matters
def get_current_greeting():
    return get_greeting_for_hour(datetime.now().hour)

print(get_current_greeting())

# Scrieți o funcție
def get_user_name():
    pass
# ce promptează utilizatorul pt. numele său
# și îl returnează

def get_user_name():
    return input("Numele tău? ")

# Scrieți o funcție
def greet_user():
    pass
# ce:
# - folosește get_user_name() pentru a afla numele
# - folosește get_current_greeting() pentru a afla salutul curent
# - și apoi face print expresiei
#   "<greeting> <name>!"

# the glue function, tieing everything together
def greet_user():
    name = get_user_name()
    greeting = get_current_greeting()

    print(greeting + " " + name + "!")
    print(
        "%s %s!" % (greeting, name) # old-school string interpolation
    )
    # new-school string interpolation (formatting)
    "{} {}!".format(greeting, name)
    "{greet} {name}!".format(greet=greeting, name=name)
    # ultima variațiune: "f-string"
    # date fiind variabilele existente pe stack `name` și `greeting`
    print(
        f"{greeting} {name}!"
    )



greet_user()