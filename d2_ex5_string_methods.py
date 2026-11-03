s = "Bună seara, acesta este un text"

### cele mai importante

s.split() # făra argumente, splitează după whitespace
# ^^ comportament foarte special față de forma
#    cu argument

# s.split() are argument opțional maxsplit:
s = "/path/to/some directory/file.txt"
s.split('/', 1)
# și are prietenul .rsplit()
folder, file = s.rsplit('/', 1)




header = "|   Name   |  Home Address     |   Phone   |"
# numele coloanelor?
header.split("|")
# fără primul și ultimul element
header.split("|")[1:-1]
# aplicând strip:
columns = list(map(
    str.strip,
    header.split("|")[1:-1]
))

# .join() este inversul lui .split()
" | ".join(columns)


### utilitarele importante

s = "O poveste este toată"
s.replace("este", "e")
# înlocuiește toate aparițiile


s.strip() # face cleanup de whitespace
          # la început și la sfârșit
s.strip(" #!") # curăță orice caracter din listă

# are prietenii .lstrip() și .rstrip()
# use-case:
int("00004230".lstrip("0"))



s.index("este") # prima apariție a substr-ului
s.find("este")  # același lucru
#  ^^ există amândouă pentru conveniență.
#     .index() raises ValueError when not found
#     .find()  returns -1        when not found

# .find() și .index() au start și stop
# și au prietenii .rfind(), .rindex()


s.count("e")

s.lower()
s.upper()


### rarely used:
s.center(20, ' '), s.ljust(20, ' '), s.rjust(20, ' ')


### the boolean ones:
# important:
"1234".isdigit()


### 


# mini-task:
# obțineți string-ul format din elementele lui
# range(5, 10), lipite prin "-"
"|".join(map(str, range(10)))
