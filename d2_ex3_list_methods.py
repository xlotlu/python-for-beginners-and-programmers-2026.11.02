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
dq.popleft("ceva")

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
