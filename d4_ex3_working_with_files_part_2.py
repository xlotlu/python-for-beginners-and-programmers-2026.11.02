# de acum încolo, când lucrăm cu fișiere, vom folosi sintaxa
with open("filename", 'w', encoding="utf-8") as f:
    print("do something with", f)

# Scrieți o funcție
def grep(filename, match):
    pass

# ce printează toate liniile din fișierul `filename`
# care conțin substring-ul `match`.

# 1) folosiți sintaxa de context manager
# 2) nu uitați că fișierul este iterabil
# 3) cum aflăm dacă un string conține un substring?

def grep(filename, match):
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            if match in line:
                print(line.removesuffix("\n"))

# testați cu:
grep('concepts-and-notes.md', "data")

# Vrem temă pentru acasă? Dacă da:
# rescrieți funcția grep astfel încât
# să colorizeze match-urile:
def grep(filename, match, color=False):
    pass

# Task:
# modificați funcția grep
# pentru a returna o listă de linii.
#
# folosiți list comprehension.

# [element for element in iterable if condition]

def grep(filename, match):
    with open(filename, 'r', encoding="utf-8") as f:
        return [
            line.removesuffix("\n")
            for line in f
            if match in line
        ]
print("\n".join(grep('concepts-and-notes.md', "data")))
for l in grep('concepts-and-notes.md', "data"):
    print("»", l)

# Q: dar "tuple comprehension"?
# A: nu există

def grep(filename, match):
    with open(filename, 'r', encoding="utf-8") as f:
        return (
            line.removesuffix("\n")
            for line in f
            if match in line
        )

# concept: generatori
lst = range(5)
(x**2 for x in lst) # aceasta este o expresie generator

# generatorii sunt un caz particular de iterator.
# deci ei nu rulează codul din spate până când nu sunt iterați.

genobj = grep('concepts-and-notes.md', "data")
try:
    list(genobj) # raises ValueError
except ValueError as err:
    print(err) # I/O operation on closed file.

# Q: ce facem când chiar vrem un iterator?
# A: nu mai folosim context manager, pentru că el
#    închide fișierul.

def grep(filename, match):
    f = open(filename, 'r', encoding="utf-8")
    return (
        line.removesuffix("\n")
        for line in f
        if match in line
    )
list(grep('concepts-and-notes.md', "data"))

# Q: atunci nu creăm memory leaks / riscăm să ajungem la open file limit?
# A: în Python modern, nu. s-a îmbunătățit masiv situația,
#    la garbage collection vor fi închiși automat.

# Exercițiu:
# modificați funcția grep astfel încât să aibă semnătura:
def grep(filename, match, insensitive=False):
    pass
# insensitive = True --> face matching pe upper/lower-case.
grep('concepts-and-notes.md', "python", True)

def grep(filename, match, insensitive=False):
    # first things first: ne normalizăm input-ul
    if insensitive:
        match = match.lower()

    f = open(filename, 'r', encoding="utf-8")

    results = []
    for line in f:
        # normalizăm condițional și pe line:
        mline = line.lower() if insensitive else line

        if match in mline:
            results.append(line.removesuffix("\n"))

    return results
# dacă o vrem cu comprehension?
def grep(filename, match, insensitive=False):
    # first things first: ne normalizăm input-ul
    if insensitive:
        match = match.lower()

    f = open(filename, 'r', encoding="utf-8")

    return (
        line.removesuffix("\n")
        for line in f
        if match in (line.lower() if insensitive else line)
    )
# not very readable, dar o facem pt. că
# chiar voiam un generator

# TODO: există o modalitate de a construi generatori
#       fără a fi blocați de sintaxa de comprehension?
#    A: da. pornind de la funcția clasică iterativă.
#       în loc de a face append, facem..... yield
def grep(filename, match, insensitive=False):
    if insensitive:
        match = match.lower()

    f = open(filename, 'r', encoding="utf-8")

    for line in f:
        mline = line.lower() if insensitive else line

        if match in mline:
            # new statement: yield
            yield line.removesuffix("\n")

genobj = grep('concepts-and-notes.md', "python", True)
next(genobj) # este iterator


### rewind.
# scrieți o funcție care numără de câte ori apare
# fiecare cuvânt într-un fișier.
def count_words(filename):
    pass
# Q: ce data structure folosim pentru a avea mapping
#    cuvânt : nr. de apariții?
# A: dict

import re

def split_words(txt):
    return re.findall(r'\w+', txt)
    # r'..' <-- raw string
    # în regexps, '\w' înseamnă "word character": alfanumerice și _
    #             iar + înseamnă cel puțin un item
# folosiți funcția de mai sus pentru split

def count_words(filename):
    counts = {}

    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()

    words = split_words(content) # o listă

    for word in words:
        # dacă nu există, inițializez
        if word not in counts:
            counts[word] = 0

        # în toate cazurile incrementez
        counts[word] += 1

    return counts

print(count_words('concepts-and-notes.md'))

# cerințe în plus: insensitive
def count_words(filename, insensitive=False):
    counts = {}

    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()

        # normalizăm
        if insensitive:
            content = content.lower()

    words = split_words(content)

    for word in words:
        #if insensitive:
        #    word = word.lower()

        if word not in counts:
            counts[word] = 0

        counts[word] += 1

    return counts

# Task:
# scrieți o funcție
def sort_dictionary(d, descending=True):
    pass
# ce returnează un dicționar nou
# cu perechile cheie - element sortate
# descrescător (default), sau crescător
# dacă descending = False

# Strategie:
# ne luăm după `.items()`
# avem `sorted()` pe orice fel de iterabil, cu key=func
# la final avem o listă de tuple
# pe care o facem dict.

def sort_dictionary(d, descending=True):
    items = d.items()

    sorted_items = sorted(
        items,
        key=lambda item: item[1],
        reverse=descending
    )

    return dict(sorted_items)

sort_dictionary(
    count_words("concepts-and-notes.md", insensitive=True),
    descending=False,
)