#while conditie:
#    statements

# numărăm de la 5 la 0 inclusiv
x = 5
while x >= 0:
    print(x)
    #x = x - 1
    x -= 1

# loop = while sau for
# poate fi întrerupt cu
# break - oprește toată execuția
#         while-ului
# continue - continuă iterația următoare
#            (restul liniilor de cod
#             nu se execută)

# modificați acest while
# pentru a printa doar numerele pare

x = 5
while x >= 0:
    # atenție, probabil ne-am introdus un bug
    x -= 1
    if x % 2 == 1:
        continue
    print(x)

x = 5
while x >= 0:
    if x % 2 == 0:
        print(x)

    x -= 1

x = 5
while True:
    print(x)
    
    if x == 0:
        break
    
    x -= 1