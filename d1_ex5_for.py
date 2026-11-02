#for item in iterable:
#    print("doing something with", item)

# lista este o colecție ordonată de obiecte:
lst1 = [1, 2, 3, 4, 5]
lst2 = ["ala", "bala", "porto", "cala"]
lst3 = [1, "ala", 2, "bala", "etc."]

for item in lst2:
    print("doing something with", item)

# cum iterați și prin lst1, și lst2, și lst3?
# (cu un for în for)
all_lists = [lst1, lst2, lst3]
for lst in all_lists:
    for elem in lst:
        print("»", elem)

# Exercițiu:
# dată fiind lista de orașe
cities = [ # în interiorul parantezelor nu am whitespace-sensitivity
    'Cluj-Napoca',
    'Timișoara',
    'Iași',
    'Constanța',
    'Brașov',
    'Craiova',
    'Galați',
    'Oradea',
    'Ploiești',
    'Brăila',
    'Arad',
    'Pitești',
    'Sibiu',
    'Bacău',
    'Târgu Mureș',
    'Baia Mare',
    'Buzău',
    'Satu Mare',
    'Suceava',
    'Focșani'
]
# printați orașele care încep cu litera "B"
# accesul după index se face cu sintaxa
# variabila[index]
s = "O poveste"
s[0] # "O"

# iterăm în orașe
# pentru fiecare element:
# - aflăm prima literă
# - verificăm dacă este "B"
# - dacă da, facem print elementului curent

for city in cities:
    l = city[0]
    if l == "B":
        print(city)

# transformați-o într-o funcție:
def filter_list_by_letter(lst, letter):
    pass
# testați cu:
filter_list_by_letter(cities, "C")

def filter_list_by_letter(lst, letter):
    for elem in lst:
        if elem[0] == letter:
            print(elem)
filter_list_by_letter(cities, "C")
