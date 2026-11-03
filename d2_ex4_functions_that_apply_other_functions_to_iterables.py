# "higher-order" functions

lst.sort(key=sort_fn)           # in-place sorting

# exact același lucru ca mai sus, doar că operează
# asupra oricărui iterabil.
sorted(iterable, key=sort_fn)   # returnează o listă nouă

filter(filter_fn, iterable)     # returnează iterator

map(func, iterable)             # aplică func la elemente,
                                # returnează iterator

enumerate(iterable)             # construiește iterator în jurul unui iterabil
                                # fiecare element este tupla (index, elem_original)

# aplică o funcție în mod repetat unui
# iterabil, până îl reduce la o singură valoare
from functools import reduce

