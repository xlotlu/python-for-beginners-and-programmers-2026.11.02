# toate blocurile care au sub-logică
# sunt finalizate cu :

# Python este whitespace-sensitive.
# tot ce se termină cu două puncte
# continuă cu blocul indentat

"""
if conditie:
    statement1
    statement2
else:
    statement1
    statement2
"""

# acesta este un multi-line string
# sintaxa în alte limbaje are fi:
"""
if(conditie) {
    statements
} else {
    statements
}
"""

"""
# variațiuni ale if-ului:
# 1) doar if
if conditie:
    statements

# 2) if și else
if conditie:
    statements
else:
    statements

# 3) if și unul sau mai multe elif-uri
if conditie_1:
    statement1
    statement2
elif conditie_2:
    statements

# 4) everything:
if conditie_1:
    statement1
    statement2
elif conditie_2:
    statements
elif conditie_3:
    statements
# ...
elif conditie_n:
    statements
else:
    statement1
    statement2
"""

# Exercițiu:
# scrieți un condițional
# care face print cu salutul potrivit
# orei primite

# între 5 și 10:  "Bună dimineața"
# între 10 și 18: "Bună ziua"
# între 18 și 22: "Bună seara"
# între 22 și 5:  "Noapte bună"

hour = 17

if hour >= 5 and hour < 10:
    print("Buna dimineata")
elif hour >= 10 and hour < 18:
    print("Buna ziua")
elif hour >=18 and hour < 22:
    print("Buna seara")
else:
    print("Noapte buna")

# Python suportă operator chaining.
# echivalent cu mai sus:
if 5 <= hour < 10:
    print("Buna dimineata")
elif 10 <= hour < 18:
    print("Buna ziua")
elif 18 <= hour < 22:
    print("Buna seara")
else:
    print("Noapte buna")


# dacă vrem să luăm ora de la utilizator?
hour = input("Care este ora? ")
# avem nevoie de "type casting"
# pentru că rezultatul lui `input()` este `str`
hour = int(hour)
