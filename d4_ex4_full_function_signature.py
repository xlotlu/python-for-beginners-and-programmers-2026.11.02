def myfunc(a, b):
    print("» a", a)
    print("» b", b)

myfunc(1, 2)
myfunc(a=1, b=2)
myfunc(b=2, a=1)
# myfunc(b=2, 1) # invalid


# funcții care primesc oricâte argumente
# aceasta se numește positional argument packing
def myfunc(a, b, *args):
    print("» a", a)
    print("» b", b)
    print("» args", args)

myfunc(1, 2, 3, 4, 5)


# keyword arguments
def myfunc(a, b, kwarg1="default 1", kwarg2="default 2"):
    print("» a", a)
    print("» b", b)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)

myfunc(1, 2, kwarg1="o valoare")
# merge specificat și pozițional
myfunc(1, 2, "o valoare")

# contrastăm cu existența *args:
def myfunc(a, b, *args, kwarg1="default 1", kwarg2="default 2"):
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)

myfunc(1, 2, "o valoare") # ultimul argument se va duce în *args
# dacă vrem să pasăm keyword arg value:
myfunc(1, 2, kwarg1="o valoare")

# aceasta se numește keyword argument packing
def myfunc(a, b, *args, kwarg1="default 1", kwarg2="default 2", **kwargs):
    print("» a", a)
    print("» b", b)
    print("» args", args)
    print("» kwarg1", kwarg1)
    print("» kwarg2", kwarg2)
    print("» kwargs", kwargs) # acesta este dicționar

myfunc(1, 2, altceva="o valoare", și_ceva="altă valoare")


### folosirea funcției

# 1.
# pot să pasez unei funcții un iterabil
# astfel încât fiecare element să fie aplicat
# ca argument individual

def func(a, b, c):
    print(a)
    print(b)
    print(c)

lst = ["ala", "bala", "porto"]
func(*lst) # acesta se numește argument unpacking
# este echivalent cu:
func("ala", "bala", "porto")

# 2.
# pot să pasez unei funcții un dicționar
# astfel încât fiecare pereche cheie - valoare
# să fie aplicată drept keyword argument

opts = {
    'sep': ' :: ',
    'end': '  «««\n',
}
print("bla", "bli", "blu", **opts)
# este echivalent cu:
print("bla", "bli", "blu", sep=' :: ', end='  «««\n')



### dacă vrem să forțăm anumite argumente
### să fie pasate doar ca poziționale, sau ca kwargs

# 1. vrem argumente positional-only:
def func(a, b, /):
    pass

func(1, 2)     # valid
# func(1, b=2) # invalid. TypeError.

# 2. vrem argumente keyword-only
def func(*, kw1=None, kw2=None):
    pass

#func(1, 2)         # invalid. TypeError.
func(kw2="altceva") # valid

# combinându-le:
def sorted(iterable, /, *, key=None, reverse=False):
    pass