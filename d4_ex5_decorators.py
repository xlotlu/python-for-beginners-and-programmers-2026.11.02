# un decorator este o funcție
# ce primește ca argument o funcție
# și returnează o funcție

# acest pattern ne permite să "decorăm"
# funcția inițială with new behaviour.
# Exemplu:

from functools import cache

from random import randint

def myfunc():
    return randint(1, 100)

myfunc_decorated = cache(myfunc)


def myfunc(a, b):
    return randint(a, b)
myfunc_decorated = cache(myfunc)

# ce-ar fi dacă, intrăm în codul vechi
# și ne modificăm behaviour-ul funcției existente
# "in-place"

def myfunc(a, b):
    return randint(a, b)
myfunc = cache(myfunc)

# aceasta de mai sus este perfect echivalentă cu
@cache
def myfunc(a, b):
    return randint(a, b)

# vedem că sintaxa
# @decorator
# def func():...
# este doar syntactic sugar pentru:
# func = decorator(func)

from functools import lru_cache

@lru_cache(maxsize=3)
def myfunc(a, b):
    return randint(a, b)

# echivalent cu:
myfunc = lru_cache(maxsize=3)(myfunc)


@lru_cache
def myfunc(a, b):
    return randint(a, b)
myfunc = lru_cache(myfunc)

# Temă pentru acasă, după curs:
# Scrieți un decorator cu argumente opționale,
# ce funcționează și așa:
#@mydeco(arg="ceva")
#def myfunc():
#    pass
# și așa:
#@mydeco
#def myfunc():
#    pass


# scriem primul nostru decorator

def deco(func):
    def _inner(*args, **kwargs):
        # aici avem ocazia să customizăm ce se întămplă
        # înainte de execuție
        print("» am intrat în funcția decorată")

        retval = func(*args, **kwargs)

        # aici avem ocazia să facem ceva cu rezultatul
        print("» ies din funcție, rezultatul a fost", repr(retval))

        return retval

    return _inner

@deco
def myfunc():
    print('--- myfunc se execută')
    return 42

# după pauză:
# scrieți un decorator care cronometrează timpul de execuție
# al funcțiilor decorate, și îl printează

# ce avem nevoie?
import datetime as dt
dt.datetime.now()
# diferența a două datetime-uri este un obiect timedelta
# care are metoda .total_seconds()


# pt. cei care au terminat exercițiul:
# 1) faceți print la milisecunde
# 2) dacă funcția pe care o decorați primește argumente și kwargs??!?
#    în traducere: cum scriem un decorator care se poate aplica oricărei
#                  funcții, indiferent de semnătură?

import sys

def timeit(func):
    def _inner(*args, **kwargs):
        start = dt.datetime.now()

        retval = func(*args, **kwargs)

        end = dt.datetime.now()

        delta = end - start
        delta_ms = delta.total_seconds() * 1000

        # vrem să avem în output:
        # - numele funcției
        # - modulul funcției
        # - argumentele primite
        # - return value
        # - durata de execuție

        print(
            "Executed » {module}.{function}({args}) --> {result} :: {delta}ms".format(
                module=func.__module__,
                function=func.__name__,
                args=(args, kwargs), # TODO: format this nicely
                result=repr(retval),
                delta=delta_ms,
            ),
            file=sys.stderr
        )

        return retval

    return _inner

from random import randint
from time import sleep

@timeit
def sleepy(a, b):
    sleep(randint(a, b) / 100)

    return a * b
