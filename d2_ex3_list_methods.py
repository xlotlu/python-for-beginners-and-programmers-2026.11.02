lst = ["ala", "bala", "porto", "cala", "trala"]

lst.count("ala")
lst.index("bala") # și opțional start position
                  # raises ValueError

lst.append("elem") # adaugă un element în coadă
lst.pop()          # returnează și șterge ultimul element

# notă de implementare:
# .pop() fără argument index și .append()
# nu forțează re-indexarea listei.

# pe când
lst.insert(1, "elem")
# și
lst.pop(1)
# forțează re-indexarea listei

# echivalentul pop-ului
def pop(lst, idx):
    elem = lst[idx]
    del lst[idx]
    return elem

# LIFO: last in - first out
lst = []
lst.append("un elem")
lst.append("doi elem")
lst.append("trei elem")

lst.pop() # "trei elem"
lst.pop() # "doi elem"
lst.pop() # "un elem"

# FIFO: first in - first out
lst = []
lst.append("un elem")
lst.append("doi elem")
lst.append("trei elem")

lst.pop(0) # "un elem"      # implică re-indexare
lst.pop(0) # "doi elem"
lst.pop(0) # "trei elem"

# FIFO cu insert(0) ?
lst = []
lst.insert(0, "un elem")    # implică re-indexare
lst.insert(0, "doi elem")
lst.insert(0, "trei elem")

lst.pop()   # "un elem"
# etc.


####
# sidetrack: deque

# pentru cazurile f. speciale
# de implementare FIFO / LILO
# când performanța _chiar_ contează
from collections import deque

# deque este linked list, înseamnă
# că operațiunile de append / left-append
# pop / left-pop nu aduc penalitate
#
# downside: index access este penalizat sever

dq = deque(range(10))
dq.appendleft("ceva")
dq.popleft()

# notă despre deque, are opțional maxlen
# cu care se pot face
# - ring buffer
# - moving window

# / end sidetrack
####


lst.extend(("ceva", "altceva")) # extinde lista cu elementele din iterabil

lst.remove("ceva") # șterge prima apariție a lui "ceva"
                   # raises ValueError

# re-implementare de remove
def remove(lst, elem):
    # aflăm indexul
    idx = lst.index(elem)
    # ștergem din listă
    del lst[idx]


####


lst.copy() # creates a _shallow_ copy

lst.reverse() # self-explanatory
              # O(n) ?


# lst.sort cu key

# întrucât totul este obiect,
# funcțiile sunt obiecte,
# deci pot fi pasate ca argumente altor funcții

def myfunc(elem):
    # o funcție ce sortează după lungimea elementului
    return len(elem)
lst.sort(key=myfunc)
print(lst)

"""
funcția key generează în spate perechi
cheie-valoare:

3: "ala"
4: "bala"
5: "porto"
4: "cala"
5: "trala"

și apoi face comparație pe chei
"""

# dată fiind lista
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
# sortați-o în ordinea crescătoare a distanțelor

# lst.sort(key=sorting_function)
# unde sorting_function primește un element
# și returnează o valoare, pe care se execută sortarea

def sorting_function(elem):
    return elem[1]
cities.sort(key=sorting_function)

print(cities)

# scrieți o funcție
def filter_cities(lst, distance):
    pass
# ce returnează o listă nouă cu elementele
# (oraș, distanță) cu distanța <= distance

def filter_cities(lst, distance):
    result = []
    for city in lst:
        if city[1] <= distance:
           result.append(city)
    return result

print(
    filter_cities(cities, 100)
)
print(
    filter_cities(cities, 200)
)
print(
    filter_cities(cities, 300)
)

# exemplu cu filter:
def filter_less_than_200(item):
    return item[1] < 200

for elem in filter(filter_less_than_200, cities):
    print(elem)


# funcția rescrisă cu filter,
# ne bazam pe abilitatea de a construi o funcție
# dinamic în interiorul altei funcții
def filter_cities(lst, distance):
    def filter_fn(item):
        return item[1] < distance

    return filter(filter_fn, lst)

# concept nou:
# lambda function. sintaxa:
# lambda <arguments>: return_value
lambda: 5                   # o funcție ce returnează 5
lambda x, y: x * y          # o funcție ce înmulțește x cu y

myfunc = lambda x, y: x * y
myfunc(2, 3)

# rescrieți filter_cities cu lambda
def filter_cities(lst, distance):
    return filter(
        lambda item: item[1] < distance,
        lst
    )

# modificați funcția de mai sus
# astfel încât:
# 0) să filtreze după `distance`
# 1) să returneze elementele în ordinea
#    descrescătoare a distanței, și
# 2) să accepte argumentul opțional `limit`
#    care limitează numărul de elemente
#    din lista rezultată
def filter_cities(lst, distance, limit=None):
    filtered = filter(
        lambda item: item[1] < distance,
        lst
    )
    result = list(filtered)
    result.sort(key=lambda item: item[1], reverse=True)

    if limit is None:
        return result
    else:
        return result[:limit]

# concept:
# ternary operator


# exemplu:
# filter_cities(cities, 200, limit=2)
#   --> [('Buzău', 110), ('Ploiești', 60)]




