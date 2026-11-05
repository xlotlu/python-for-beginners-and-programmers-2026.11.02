### exceptions ###

# excepțiile sunt instanțe ale unor clase
ValueError("Mesajul meu de excepție")

# ce au ele special:
# moștenesc de la clasa Exception

# implicație:
# putem să ne facem noi excepțiile noastre custom

# in Python, exceptions are used for flow control
# (adică, la fel cu if)
# și sunt folosite pentru comunicare

class MyOwnException(Exception):
    pass

# forma fundamentală
try:
    # statements
    pass
except MyOwnException:
    # statements
    pass


# exemplu de comunicare "laterală" (adică nu este via return)
try:
    open("/tmp/non-existant.txt")
except FileNotFoundError:
    print("nu există acest fișier, vreți să îl creați")

# ce avem mai sus ar fi putut fi rezolvat cu:
import os.path

if not os.path.exists("/tmp/non-existant.txt"):
    print("nu există acest fișier, vreți să îl creați")


# forma completă:

d = {
    1: ["a", "b"],
    2: "etc."
}

try:
    item = d[1]
    subitem = item[0]
except IndexError:
    pass
except KeyError:
    pass
# ^^ deci putem avea mai multe branch-uri de except
# putem și să tratăm într-un singur bloc
# cu mai multe feluri de excepție:
except ValueError, ZeroDivisionError:
    pass
#except:     # catch-all
#    # do NOT do this, unless at top-level code,
#    # atenție, în forma asta, probably never a good idea
#    pass
except Exception as exc:
    # acesta este un catch-all care capturează excepția
    # într-o variabilă, și acum putem să facem ceva
    # cu ea. spre exemplu, logging.
    print("eroare", type(exc), exc)

# acestea îi împlinesc rostul:
else:
    # se execută doar când nu a existat o excepție
    # aici scriem cod pe care normal l-am fi pus la coada
    # codului din try.

    # do_something_with(item)
    pass

finally:
    # se execută întotdeauna, chiar dacă a fost sau nu
    # o excepție. utilă pentru operațiuni gen cleanup.
    pass


### formele în care poate să apară:

# 1)
try:
    pass
except: # cu toate formele posibile
    pass

# 2)
try:
    pass
finally:
    # fără except handling, dar cu procedură de cleanup
    pass

# 3)
try:
    pass
except:
    pass
else:
    pass

# 4)
try:
    pass
except:
    pass
finally:
    pass

# 5)
try:
    pass
except:
    pass
else:
    pass
finally:
    pass
