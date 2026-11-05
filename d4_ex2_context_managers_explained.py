### pe vremuri făceam așa...

f = open("testing.txt", 'w')

# facem tot felul de chestii
f.write("chestii")
# și tot felul de alte chestii

# întotdeauna, absolut necesar, făceam
f.close()


# întrebare? dacă în codul dintre open și close
# a apărut o excepție?

# răspuns: vrem să rulăm close() întotdeauna.
# deci:


f = open("testing.txt", 'w')

try:
    # facem tot felul de chestii
    f.write("chestii")
    # și tot felul de alte chestii
finally:
    f.close()


f1 = open("testing1.txt", 'w')
f2 = open("testing1.txt", 'w')


try:
    # facem tot felul de chestii
    f.write("chestii")
    # și tot felul de alte chestii
finally:
    f1.close()
    f2.close()

try:
    # operațiuni cu f1

    try:
        # opearțiuni cu f2
        pass
    finally:
        f2.close()
finally:
    f1.close()


### zilele acestea în schimb facem așa:
with open("testing.txt", 'w') as f:
    print("doing something with", f)
    # și gata

# `with` introduce un "context manager".
# un context manager garantează că se execută
#  cod specific la intrarea în context,
#  și că se execută cod specific la ieșirea din context.

# "garantează" = chiar dacă a existat o excepție
# "cod specific" = context manager-ul decide ce înseamnă asta.

# detaliu de implementare: un ctx manager implementează metodele
# __enter__ și __exit__


# în cazul particular al obiectelor returnate de open()
# acestea fac self.close() în __exit__

# alt exemplu:
# tranzacție în sql: garantează atomicitate
#      ---> implică: begin transaction (care poate fi automat)
#                    și la sfârșit commit sau rollback


# [TODO Ionuț: cleanup!]

import sqlite3
con = sqlite3.connect("my.db")
con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
con.commit()
con.rollback()
con.execute('INSERT INTO lang(name) VALUES("one language")')
con.execute('INSERT INTO lang(name) VALUES("two language")')
con.execute('SELECT * from lang')
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
con.execute('INSERT INTO lang(name) VALUES("two language")')
con.execute('INSERT INTO lang(name) VALUES("two language")')
try:
    con.execute('INSERT INTO lang(name) VALUES("two language")')
except sqlite3.IntegrityError:
    print("există deja ăsta")

con = sqlite3.connect("my.db")
import sqlite3
con = sqlite3.connect("my.db")
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
con.execute('INSERT INTO lang(name) VALUES("one language")')
try:
    con.execute('INSERT INTO lang(name) VALUES("two language")')
except sqlite3.IntegrityError:
    print("există deja ăsta")
con.commit()

import sqlite3
con = sqlite3.connect("my.db")
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
with con:
    con.execute('INSERT INTO lang(name) VALUES("three language")')
    con.execute('INSERT INTO lang(name) VALUES("four language")')
con.execute('INSERT INTO lang(name) VALUES("one language")')

import sqlite3
con = sqlite3.connect("my.db")
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
with con:
    con.execute('INSERT INTO lang(name) VALUES("should work language")')
    con.execute('INSERT INTO lang(name) VALUES("should really work language")')
    1 / 0
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
con.execute('INSERT INTO lang(name) VALUES("should work language")')
con.execute('INSERT INTO lang(name) VALUES("should really work language")')
1 / 0
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
con.rollback()
cursor = con.execute('SELECT * from lang')
for elem in cursor:
    print(elem)
%hist