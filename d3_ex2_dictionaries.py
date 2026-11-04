# dicționarul:
{"cheie": "valoare", "cheie 2": "valoare 2"}

d = {"cheie": "valoare", "cheie 2": "valoare 2"}

# item access:
d['cheie']
d['cheie 2']
#d['cheie 3'] # raises KeyError

# item assignment
# o cheie care există:
d['cheie'] = "Valoare Nouă"
# o cheie care nu există:
d['cheie x'] = "Altă Valoare"

# metode:

d.pop('cheie') # returnează valoarea pentru acea cheie
               # dacă cheia nu există: KeyError

key, value = d.popitem()  # returnează o tuplă key-value
                          # de la final
# ^^ util în situații în care vrem să consumăm dicționarul

# când vrem să obținem întotdeauna o valoare,
# chiar dacă cheia nu există:
d.get('abc')

v = d.get('abc', 'Un DEFAULT')
# este echivalent cu:
try:
    v = d['abc']
except KeyError:
    v = 'Un DEFAULT'

# alte metode
d.clear()   # obvious
d.copy()    # shallow copy

# shallow copy explained
d = {"cheie": [1, 2, 3], "cheie 2": "whatever"}
dc = d.copy()
d['cheie'] is dc['cheie']

# notă latarală:
# există și deep copy
from copy import copy, deepcopy

dc = deepcopy(d)
d['cheie'] is not dc['cheie'] #  is _not_



d = {"cheie": "valoare", "cheie 2": "valoare 2", "cheie 3": "valoare 3"}

# setdefault este inversul lui get
d.setdefault('cheie', 'Un DEFAULT') # returnează "valoare", nu suprascrie
d.setdefault('cheie X', 'Un DEFAULT') # returnează 'Un DEFAULT', a creat cheia
# echivalent cu:
if "cheie" not in d:
    d["cheie"] = 'Un DEFAULT'
# și apoi mai face și return cu valoarea existentă sau asignată

# update modifică valorile pentru cheile existente
# și creează chei-valori noi pentru cele inexistente
d.update(
    {
        'cheie': "valoare NOUĂ",
        'cheie 4': "ceva nou",
        'cheie 5': "etc",
        'cheie 2': "valoare Tot NOUĂ",
    }
)

# clasa sursă:
dict

# inițializare alternativă:
d = dict(key_1="value 1", key_2="value 2")

# aceeași semnătura și la .update()
d.update(key_2="modified", key_3="new")


# Exercițiu:
# dat fiind
cities = [
    ('Cluj-Napoca', 450),
    ('Timișoara', 550),
    ('Iași', 390),
    ('Constanța', 225),
    ('Brașov', 170),
    ('Craiova', 230),
    ('Galați', 250),
    ('Oradea', 600),
    ('Ploiești', 60),
    ('Brăila', 200),
    ('Arad', 530),
    ('Pitești', 120),
    ('Sibiu', 280),
    ('Bacău', 300),
    ('Târgu Mureș', 340),
    ('Baia Mare', 600),
    ('Buzău', 110),
    ('Satu Mare', 640),
    ('Suceava', 450),
    ('Focșani', 190),
]
# creați un dicționar nou
# unde cheia este numele orașului, și valoare distanța

# acumulare în dicționar:
dcities = {}
# iterăm în sursă
for elem in cities:
    name, distance = elem
    # asignăm
    dcities[name] = distance

# notă laterală:
# iterable unpacking (adică multiple variable assignment)
# funcționează și inline în for:
for name, distance in cities:
    dcities[name] = distance

# altă metodă de inițializare:
# dat fiind un iterabil cu elementele alt iterabil
# de câte 2 valori:
dcities = dict(cities)


# există două modalități de a lucra cu dicționare:
# 1) dicționarul este sursă de date în stil id -- valoare
# 2) în stil row-uri, și în acest caz dataset-ul
#    este o listă de dicționare ("o listă de obiecte")

# Exercițiu:
# dat fiind lista `cities` de mai sus,
# creați o listă `cities_dicts` ale cărei elemente
# sunt dicționare de forma
# {'name': ..., 'distance': ...}

cities_dicts = []
for name, distance in cities:
    d = {
        'name': name,
        'distance': distance,
    }
    cities_dicts.append(d)
print(cities_dicts)


# dat fiind acest dataset
cities = [
    ('Cluj-Napoca', 450, 190, 217000),
    ('Timișoara', 550, 136, 391000),
    ('Iași', 390, 101, 460000),
    ('Constanța', 225, 746, 119000),
    ('Brașov', 170, 186, 517000),
    ('Craiova', 230, 661, 402000),
    ('Galați', 250, 758, 450000),
    ('Oradea', 600, 401, 460000),
    ('Ploiești', 60, 687, 343000),
    ('Brăila', 200, 759, 507000),
    ('Arad', 530, 405, 264000),
    ('Pitești', 120, 703, 462000),
    ('Sibiu', 280, 487, 481000),
    ('Bacău', 300, 390, 254000),
    ('Târgu Mureș', 340, 201, 455000),
    ('Baia Mare', 600, 588, 288000),
    ('Buzău', 110, 578, 390000),
    ('Satu Mare', 640, 580, 328000),
    ('Suceava', 450, 759, 172000),
    ('Focșani', 190, 736, 448000),
    ('Cluj-Napoca', 451, 552, 272000)
]
# creați o listă de dicționare
# cu cheile
columns = ['name', 'distance', 'altitude', 'population']

[
    {
        'name': 'Cluj-Napoca',
        'distance': 450,
        'altitude': 190,
        'population': 217000,
    },
    # ....
]

# iterăm pe columns,
# coloana e variabila -- cheie,

# ne trebuie un index
# pt. fiecare element,
# key = column[idx]
# value = element[idx]

# v.1: obținem indexul din range()
lst = []
for city in cities:
    temp = {}

    for idx in range(len(columns)):
        key = columns[idx]
        value = city[idx]

        temp[key] = value
    lst.append(temp)
print(lst)

# v.2: obținem indexul cu enumerate()
lst = []
for city in cities:
    temp = {}

    for idx, key in enumerate(columns):
        value = city[idx]

        temp[key] = value
    lst.append(temp)
print(lst)

# v.3: folosim zip()
#      (și abilitatea dicționarului de a fi instanțiat
#      dintr-un iterabil ce conține elemente (key, value) )
lst = []
for city in cities:
    lst.append(dict(
        zip(columns, city)
    ))
print(lst)

# dacă vrem să ne protejăm în caz că
# columns și elementele au lungimi diferite:
# zip(columns, city, strict=True)


# Concept nou:
# list comprehension

source = [1, 2, 3, 4, 5]
result = [] # pătratele numerelor din source

for elem in source:
    result.append(elem ** 2)

print(result)

# se poate scrie ca un one-liner astfel:
[   elem ** 2  for elem in source     ]



source = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [] # pătratele numerelor impare din source

for elem in source:
    if elem % 2:
        result.append(elem ** 2)

print(result)

[   elem ** 2  for elem in source if elem % 2  ]

[
    elem ** 2
    for elem in source
    if elem % 2
]

# exemplu de for în for în comprehension
lst = [
    [1, 2, 3],
    [12, 13, 14, 15],
    [23, 24]
]
[x for sublst in lst for x in sublst if x % 2]


# haideți să facem one-liner din:
lst = []
for city in cities:
    lst.append(dict(
        zip(columns, city)
    ))
print(lst)

print(
    [dict(zip(columns, city)) for city in cities]
)

# dat fiind dataset-ul friends
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# și dată fiind funcția
def get_friend_by_name(friends, name):
    for f in friends:
        if f[0] == name:
            return f

# cum putem optimiza accesul funcției
# astfel încât să nu facă search în toată lista sursă
# la fiecare call?

# soluție: ne transformăm lista în avans într-un
#          dicționar intermediar
_friends_dict = {}

for f in friends:
    name = f[0]
    _friends_dict[name] = f

def get_friend_by_name(friends, name):
    return _friends_dict[name]
# să nu uităm ce se întâmplă când nu există:
# v.1
def get_friend_by_name(friends, name):
    if name not in friends:
        return
    return _friends_dict[name]
# v.2
def get_friend_by_name(friends, name):
    try:
        return _friends_dict[name]
    except KeyError:
        return

# problem: totul este legat de acest dataset.
# get_friend_by_name() va da rezultate eronate pt. alte date.


# vreau un cache care se populează la runtime
# (deci nu îl pre-populez cu un dicționar complet)
_cache = {}
def get_friend_by_name(friends, name):
    # dacă am făcut deja lookup pe name
    # vreau să returnez din cache.
    if name in _cache:
        return _cache[name]

    # altfel, algoritmul obișnuit:
    for f in friends:
        if f[0] == name:
            # dar înainte de return să nu uităm
            # să populăm cache-ul
            _cache[name] = f

            return f

# micro-îmbunătățire:
# să fac variabila `_cache` să nu îmi polueze global namespace.
# răspuns: îl adaug pe _cache drept atribut al funcției:
def get_friend_by_name(friends, name):
    _cache = get_friend_by_name._cache

    if name in _cache:
        return _cache[name]

    for f in friends:
        if f[0] == name:
            _cache[name] = f
            return f

get_friend_by_name._cache = {}


# metodele de iterare pe dicționar
d = {"cheie": "valoare", "cheie 2": "valoare 2", "cheie 3": "valoare 3"}

# este default iterabil după chei
for key in d:
    print(key)

# explicit după cheie
for key in d.keys():
    print(key)

# iterare după valori
for value in d.values():
    print(value)

# în același timp după cheie și valoare:
for item in d.items():
    print(item)

for key, value in d.items():
    print(key, value, sep=" :: ")


# 1. transformați pe friends într-o listă de dicționare
# cu cheile
keys = 'name', 'age', 'hobbies'
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]

friends_as_dicts = [
    dict(zip(keys, elem))
    for elem in friends
]

# dat fiind dicționarul
occupations = {
    "Sam": "gardner",
    "Jane": "nurse",
    "Mike": "firefighter",
    "Anna": "boat captain",
    "Dan": "venture capitalist",
}
# setați fiecărui element de mai sus
# cheia 'occupation' cu valoarea potrivită.

# vreau să îl transform pe friends_as_dicts
# într-un dicționar de dicționare

dfr_as_d = {}
for elem in friends_as_dicts:
    name = elem['name']

    dfr_as_d[name] = elem

# introducem dict comprehension:
dfr_as_d = {
    elem['name']: elem
    for elem in friends_as_dicts
}

# updatăm cerința:
# dat fiind `dfr_as_d`
# puneți fiecărui prieten cheia "occupation"
for name, occ in occupations.items():
    dfr_as_d[name]['occupation'] = occ
