# Concepte

în Python totul este un obiect

variabila este o referință către un obiect din memorie

în Python totul(!) este o referință către obiectul din spate

operatorii sunt dependenți de data type-ul asupra cărora acționează

reprezentare a unui data type: felul în care apare în terminalul de Python

iterator = un obiect iterabil, care execută cod în timpul iterației
           și își suspendă execuția după fiecare element returnat

Python is self-documenting

în Python totul poate fi evaluat în context boolean

în Python operatorii execută de fapt o metodă
a obiectului asupra căruia operează

callable = o funcție (sau metodă), o clasă
           [!!] oare poate să mai și altceva?


# De citit

(măcar o dată în viața de programator Python)

The Styleguide:
https://peps.python.org/pep-0008/

String formatting examples:
https://docs.python.org/3/library/string.html#format-examples


# Data types

int
float
str
bool

tuple
list    # mutable


# Operatori

## specifici Python

//  partea întreagă a împărțirii
%   restul împărțirii
**  ridicare la putere

## în context boolean

and
or
not

in          # element in iterable, unde este suportat
not in

is
is not

# Debugging essentials

print()
help()
type()      returnează clasa din care a fost instanțiat obiectul
dir(object) toate atributele obiectului
locals()    variabilele definite local
globals()   variabilele definite global

# Excepții importante

SyntaxError     evident

NameError:      simbolul nu a fost definit
TypeError:      apare când a existat o operațiune
                invalidă între două data type-uri;
                și apare când un callable primește
                argumente invalide
ValueError:     când valoarea respectivă este invalidă
                în context

IndexError:     când indexul accesat nu există
KeyError:       când cheia respectivă nu există
                

# pachete utile / importante

un package se instalează cu:

pip install nume_pachet # (în system shell)


ipython
rich


from rich import pretty
pretty.install()

# lucrat cu VSCode:

Ctrl+F5         run file
Shift+Enter     execute selection


# varia

There are 2 very difficult problems in computing:
- naming things
- cache invalidation
- off-by-one errors
