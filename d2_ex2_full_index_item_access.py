# full index access syntax

lst = ["ala", "bala", "porto", "cala", "trala"]

lst[0] # item access
# până ieri index access

# sintaxa:
# nume_de_variabilă[item-ul]

# indecșii pozitivi sau negativi
lst[-2]

# slice:
lst[1:3]

tup = ("elem 1", "elem 2", "elem 3", "elem 4")
tup[1:3]

"bună dimineața"[2:5]

# ca protocol în spate, sintaxa cu două puncte
# în interiorul parantezelor drepte
# creează un obiect de tip `slice`
# și face acces după item cu acest obiect


# într-un slice toate părțile sunt opționale (!)
# primele 3 elemente din lst:
lst[:3]
# ultimele 3 elemente din lst:
lst[-3:]

# forma completă a slice-ului este:
# start:stop:step

# ultimele două elemente în ordine inversă:
lst[-1:-3:-1]

s = "Cri cri toamnă gri"
# scris de la coadă la capăt:
s[-1:0:-1] # nu mere tot
s[::-1]

# assignment după index (item assignment)
lst = ["ala", "bala", "porto", "cala", "trala"]

lst[1] = "Altceva"

# sintaxa de acces și de assignment după index
# este universală (pentru cine o suportă)

d = {
    'k1': 20,
    'k2': 21,
}
d['k1'] = 50
# la dicționar assignment cu item care nu există
# creează acel item (cheie - valoare)
d['kx'] = 60

# la listă dacă facem assignment în afara listei,
# rezultă în IndexError:
try:
    lst[20] = "bau" # IndexError
except IndexError:
    print("nu am putut face assignment")


# deletion by index
del lst[1]
# in fact "deletion by item":
del d['kx']

# assignment după slice
lst[0:2] = "ceva", "și altceva"
lst[0:2] = range(10,12)


######
# really fun and complicated item access implementations
######

# ținând cont că:
# - vorbim despre `item` access,
# - că "item" depinde de context ce poate să fie
# - luăm exemplul dicționarului
#   (care suportă drept cheie aproape orice obiect de python)

d = {
    (0, 1): "un element",
    (2, 2): "alt element",
}
d[(0, 1)]
# este echivalent cu:
d[0, 1]

# luăm exemplul numpy
import numpy

arr = numpy.array([
    ["ab", "bc", "cd"],
    ["mn", "no", "op"],
    ["wx", "xy", "yz"],
])

arr[2, 1]   # row-ul 2, coloana 1
arr[2]      # row-ul 2
arr[:2]     # row-urile până la 2
arr[:2, :2] # row-urile până la 2, coloanele până la 2

# sintaxa de slice cu :
# este "syntactic sugar" pentru
# slice(start, stop, step)

lst[:3]
# echivalent cu
lst[    slice(None, 3)    ]

arr[1:, 1:]

arr[  ( slice(1, None)  ,  slice(1, None) )   ]

# ultima coloană din array?
arr[:, -1]

# sub-matricea cu ultimele două coloane?
arr[:, -2:]
