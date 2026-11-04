# 1. dat fiind string-ul
s = "my.name@my.domain.example.com"
# obțineți username-ul și domeniul.
# apoi obțineți TLD-ul (top-level domain).

username, domain = s.split('@')
tld = domain.split('.')[-1]
# sau
_, tld = domain.rsplit('.', 1)

# 2. dată fiind lista de tuple de forma (nume, vârstă)
candidates = [
    ('Dragoș', 42),
    ('Ana', 74),
    ('Mircea', 31),
    ('Carmen', 17),
    ('Andreea', 38),
    ('Vasi', 61),
]
# creați două liste noi `accepted` și `rejected`
# astfel încât persoanele cu vârsta între 18 și 60 de ani
# să fie accepted, iar restul rejected.
#
# iterați în lista inițială astfel încât să o consumați
# (la sfârșit rămâne goală)

accepted = []
rejected = []
while candidates:
    c = candidates.pop()

    if 18 <= c[1] <= 60:
        accepted.append(c)
    else:
        rejected.append(c)

print(accepted)
print(rejected)
# problema potențială: sunt de la coadă la cap.
# Q: dacă am vrea să îi avem în ordine?
# A1: .pop(0) --> rezultă în O(n!)
# A2: facem candidates.reverse()
#     sau accepted.reverse() și rejected.reverse()


# 3. dată fiind structura de date ce conține liste
# de forma [name, age, hobbies]
friends = [
    ["Jane", 20, ["reading", "hiking", "biking"]],
    ["Mike", 17, ["hiking", "fishing"]],
    ["Anna", 25, []],
    ["Sam", 40, ["playing guitar"]],
    ["Dan", 34, ["painting", "reading"]],
]
# scrieți o funcție
def get_friend_by_name(friends, name):
    pass
# ce primind o structură de date ca mai sus
# returnează elementul-listă corespunzător numelui
# respectiv.

def get_friend_by_name(friends, name):
    for f in friends:
        if f[0] == name:
            return f

# versiune alternativă, încercând să facem one-liner,
# îl abuzăm pe filter(), dar pentru a nu itera
# în tot dataset-ul, luăm prima valoare cu next:

def get_friend_by_name(friends, name):
    #return list(filter(lambda elem: elem[0] == name, friends))[0]
    # ^^ varianta aceasta ar itera inutil în toată lista.

    # acesta este un iterator
    it = filter(lambda elem: elem[0] == name,
                friends)

    # nu putem să facem return(next(it)) direct, pentru că...
    try:
        return next(it)
    except StopIteration:
        # înseamnă că nu a existat nici-un element
        return


# Folosind funcția de mai sus:
# a) accesați-o pe Jane și îmbătrâniți-o cu un an.
jane = get_friend_by_name(friends, "Jane")
jane[1] += 1

# b) adăugați hobbyu-urilor Annei "reading" și "cooking"
# într-o singură operațiune.
anna = get_friend_by_name(friends, "Anna")
anna[2].extend(["reading", "cooking"])

# c) ștergeti-i lui Mike ultimul hobby
mike = get_friend_by_name(friends, "Mike")
del mike[2][-1]

# d) inspectați lista inițială `friends`.
# Explicați schimbările.

# Răspuns: references all the way down.

# Adăugați un prieten nou
["Ginger", 22, ["reading", "cooking", "hiking"]]
friends.append(["Ginger", 22, ["reading", "cooking", "hiking"]])


# 4. Scrieți o funcție
def find_friends_by_hobby(friends, hobby):
    pass
# ce returnează un subset al `friends`
# cu prieteni care au respectivul `hobby`.
#
# folosiți `filter()`.

def find_friends_by_hobby(friends, hobby):
    return filter(
        lambda friend: hobby in friend[2],
        friends
    )

# 5. Scrieți o funcție
def find_friends_by_age(friends, min_age=None, max_age=None):
    pass
# ce filtrează prietenii cu vârsta cuprinsă între
# `min_age` și `max_age`.
# scrieți-o în varianta iterativă cu `.append()`
# și apoi în varianta cu `filter()`.

# v.1: trișăm cu infinit:
import math

def find_friends_by_age(friends, min_age=-math.inf, max_age=math.inf):
    filtered = []

    for friend in friends:
        if min_age <= friend[1] <= max_age:
            filtered.append(friend)
    return filtered

# v.2: simplificăm condiționalul ieșind din bucla curentă
#      pentru valori care nu ne interesează
def find_friends_by_age(friends, min_age=None, max_age=None):
    result = []

    for friend in friends:
        age = friend[1]

        if min_age is not None and age < min_age:
            continue

        if max_age is not None and age > max_age:
            continue

        result.append(friend)

    return result

# v.3: if complex
def find_friends_by_age(friends, min_age=None, max_age=None):
    result = []

    for friend in friends:
        age = friend[1]

        if (
            (
                min_age is None
                or age >= min_age
            ) and (
                max_age is None
                or age <= max_age
            )
        ):
            result.append(friend)

    return result

# v.3: mutăm condiționalul în funcție de filtrare
def find_friends_by_age(friends, min_age=None, max_age=None):
    def filter_func(friend):
        return (
            (
                min_age is None
                or friend[1] >= min_age
            ) and (
                max_age is None
                or friend[1] <= max_age
            )
        )

    return filter(filter_func, friends)


# v.4: cu funcții parțiale pentru a aplica condiția
def find_friends_by_age(friends, min_age=None, max_age=None):
    def min_func(friend):
        return (
            min_age is None
            or friend[1] >= min_age
        )

    def max_func(friend):
        return (
            max_age is None
            or friend[1] <= max_age
        )

    return filter(
        lambda friend: min_func(friend) and max_func(friend),
        friends
    )

# v.5: funcții definite condițional
def find_friends_by_age(friends, min_age=None, max_age=None):
    if min_age is None:
        def min_func(friend):
            return True
    else:
        def min_func(friend):
            return friend[1] >= min_age

    if max_age is None:
        def max_func(friend):
            return True
    else:
        def max_func(friend):
            return friend[1] <= max_age

    return filter(
        lambda friend: min_func(friend) and max_func(friend),
        friends
    )

# v.6: funcții definite condițional, dar mai scurt
#      (ok, not readable)
def find_friends_by_age(friends, min_age=None, max_age=None):
    min_func = (
        (lambda friend: True)
        if min_age is None
        else (lambda friend: friend[1] >= min_age)
    )
    max_func = (
        (lambda friend: True)
        if max_age is None
        else (lambda friend: friend[1] <= max_age)
    )

    return filter(
        lambda friend: min_func(friend) and max_func(friend),
        friends
    )

# Chain-uiți funcțiile `find_friends_by_age` și `find_friends_by_hobby`
# astfel încât să obțineți toți prietenii mai în vârstă de 20 de ani
# care sunt pasionați de `hiking`.
#
# Adăugați-le tuturor un element nou:
{"buddy": True}
#
# Inspectați lista inițială `friends`.

for f in find_friends_by_hobby(
    find_friends_by_age(friends, 20),
    'hiking'
):
    f.append({"buddy": True})
