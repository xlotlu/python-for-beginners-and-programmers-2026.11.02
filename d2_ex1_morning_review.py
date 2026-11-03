#1. Repetați (concatenați cu sine) string-ul "tralala" de 7 ori.
"tralala" * 7

#2. Obțineți partea întreagă a împărțirii lui 17 la 4.
17 // 4
int(17 / 4)

#3. Obțineți restul împărțirii lui 17 la 4.
17 % 4

#4. Setați variabilele
name = "Jane"
is_student = True

# și folosiți-le într-un condițional care să facă print
# pe un branch unui string de forma
# "<name> is a student."
# și pe celălalt branch
# "<name> is not a student".
#
# repetați apoi codul cu variabilele
name = "Andrew"
is_student = False
#
# folosiți oricare din formele de string interpolation.

name = "Jane"
is_student = True

if is_student:
   print(f"{name} is a student")
else:
   print (f"{name} is not a student")

name = "Andrew"
is_student = False

if is_student:
   print(f"{name} is a student")
else:
   print (f"{name} is not a student")

#5. Scrieți o funcție cube(x) ce calculează
# x la puterea a 3a.
def cube(x):
   return x ** 3


#6. Luați un număr întreg ca input de la utilizator
# și folosiți funcția de mai sus pentru a face
# output string-ului
# "Cubul numărului <number> este <cub>."
# Folosiți f-string pentru interpolare.
# Nu uitați că în interiorul acoladelor f-string-ului
# se execută cod Python.
num = int(input("Spune un număr "))
print(f"Cubul numărului {num} este {cube(num)}.")


#7. Construiți o listă formată din pătratele
# numerelor impare de la 1 la 10.
odd_squares = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_squares.append(x ** 2)
print(odd_squares)


#8. Dat fiind string-ul
s = "Bună dimineața!"

# - obțineți al 7lea caracter din string
s[6]

# - obțineți penultimul caracter din string
s[-2]

# 8.5 Dată fiind lista
cities = [
   'Cluj-Napoca', 'Timișoara', 'Iași', 'Constanța', 'Brașov',
   'Craiova', 'Galați', 'Oradea', 'Ploiești', 'Brăila', 'Arad',
   'Pitești', 'Sibiu', 'Bacău', 'Târgu Mureș', 'Baia Mare', 'Buzău',
   'Satu Mare', 'Suceava', 'Focșani',
]
# iterați în listă în timp ce o consumați
# și printați elementele care încep cu litera "C"

# metodă brută:
while cities:
    elem = cities[0]
    del cities[0]
    print(len(cities), elem)

# mai elegant, știind că există .pop():
while cities:
    elem = cities.pop()
    print(len(cities), elem)


#9. [opțional] [pentru cine a terminat]
# Scrieți o funcție
def format_minutes(total):
    pass
# ce returnează un string formatat de forma
# "HH:MM". Exemplu:
format_minutes(2) == "00:02"
format_minutes(61) == "01:01"
format_minutes(132) == "02:12"


def pad_number(num):
    if num < 10:
        return "0" + str(num)
    return num

def format_minutes(total):
    #hours = total // 60
    #minutes = total % 60
    hours, minutes = divmod(132, 60)

    return "%s:%s" % (
        pad_number(hours),
        pad_number(minutes)
    )
    return f"{pad_number(hours)}:{pad_number(minutes)}"


def format_minutes(total):
    hours, minutes = divmod(total, 60)

    return f"{hours:02d}:{minutes:02d}"

# don't do this, pt. că readability
def format_minutes(total):
    return "{:02d}:{:02d}".format(*divmod(total, 60))


#10. [extra-opțional]
# Scrieți o funcție
def get_seconds_from_now(timespec):
    pass
# ce returnează numărul de secunde din momentul curent
# până la prima apariție a `timespec`, unde acesta
# este de forma "HH:MM:SS" sau "HH:MM" sau "HH".
#
# Hint #1: metoda `datetime.time.fromisoformat()`
# Hint #2: `datetime.datetime.now()`
# Hint #3: două obiecte de tip `datetime.datetime`
#          au o diferență de tip `datetime.timedelta`

# "10:21" --> 42 secunde
# "10:19" --> 86300 secunde