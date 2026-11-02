# acestea se numesc "sequences"
# - str
# - tuple  # este immutable
# - list   # este mutable

s = "Bună ziua, este un vânt frumos"
tup = ("elem 1", "elem 2", "elem 3")
lst = ["un elem", "doi elem", "trei elem"]

# sequences au următoarele în comun:
# 0. sunt colecții ordonate
# 1. sunt iterabile

for elem in s:
    # iterează caracter cu caracter
    print(elem)

# 2. au o lungime dată, ce poate fi aflată
#    cu funcția len()

print(len(s), len(tup), len(lst))

# 3. sunt accesibile după index
#    (notă: indexul poate să fie negativ)
s[0], tup[1], lst[2]

# cum accesez ultimul element dintr-un sequence?
lst[-1]

# 4. când accesăm un index care nu există,
#    ne dau excepție IndexError
#lst[5]

# 5. toate suportă metodele `.count()` și `.index()`
s.count("n")
s.count("un") # merge și pe substring
lst.count("un elem")

s.index("ziua") # 5
#s.index("ziuax") # ValueError
lst.index("un elem") # 0
lst.index("un elemx") # ValueError

# 6. suportă operatorii `in` și `not in`
"un elem" in lst


# alt datatype iterabil: range.
range(10)    # ultima valoare exclusivă
range(5, 10) # prima valoare inclusivă

# ținând cont că step default este 1,
# cum iterăm de la 10 la 0 inclusiv
list(range(10, -1, -1))

# exemplu de iterabil care poate fi
# nesfârșit
from itertools import repeat
# repeat("ceva") # <-- nesfârșit.
for elem in repeat('ceva', 5):
    print(elem)


# să iterăm pe o structură de date
# bi-dimensională

# dată fiind structura de date
# a cărei elemente sunt tuple de forma
# (name, distance)
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
# iterați prin aceasta
# și faceți print orașelor cu distanță
# mai mică decât 300.

# 1. iterăm
for elem in cities:
    # 2. fiecare element va fi tupla (name, distance)
    # 3. aflăm distanța folosind index access
    name = elem[0]
    distance = elem[1]
    # 4. facem condițional
    if distance < 300:
        # 5. dacă da, print
        print(name)

# vrem să creăm o funcție de filtrare
def filter_cities_by_distance(lst, distance):
    pass
# ce returnează o listă nouă cu orașele filtrate
# folosiți metoda .append(elem) a listei

def filter_cities_by_distance(lst, distance):
    pass

def filter_cities_by_distance(lst, distance):
    # pattern de acumulare:
    # 1. ne inițializăm obiectul
    out = []
    # 2. iterăm în sursă
    for elem in lst:
        # 3. condițional
        if elem[1] < distance:
            # 4. acumulăm
            out.append(elem)

    # 5. returnăm obiectul
    return out

x, y = 200, 120 # "iterable unpacking"
x, y, z = range(3)
# dacă ne interesează primele 3:
x, y, z, *remaining = range(20)
# dacă ne interesează ultimele 3:
*_, x, y, z = range(20)
# dacă ne interesează primele și ultimele:
a, b, *rest, c, d = range(20)

# folosim iterable unpacking
# pt. a înfrumuseța funcția
def filter_cities_by_distance(lst, distance):
    out = []
    for elem in lst:
        _, dist = elem
        if dist < distance:
            out.append(elem)