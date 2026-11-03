# dată fiind
lst = ["ala", "bala", "porto"]
# și
def func(a, b, c):
    print(a, b, c)

func(*lst) # despachetează argumentele
# echivalent cu:
func("ala", "bala", "porto")

# vs.
a, b, *rest = lst # iterable unpacking
func(*lst) # argument unpacking

# exemplu:
print(range(5), sep="  |  ")
# vs.
print(*range(5), sep="  |  ")
