print("Salutare lume!")

name = "Ionuț"
greeting = "Salutare " + name + "!"

print(greeting)


# next step:
# îl întrebăm pe utilizator care este numele său

# funcția input are sens doar la interacțiunea
# cu utilizatorul în terminal.
#
# input value-ul său este ce a scris utilizatorul.

# Task:
# faceți operațiune de salutare a utilizatorului,
# după ce în prealabil i-ați cerut numele.
# - întrebați-l care este numele
# - setați-l într-o variabilă
# - creați string-ul de salut
# - și printați-l

print("Cum te numești?")
name = input()
greeting = "Salut " + name + "!"
print(greeting)

# renunțăm la print-ul inițial,
# și facem promptarea direct din interiorul
# lui input()
name = input("Cum te numești? ")
# folosim string interpolation
greeting = "Salut %s!" % name
print(greeting)

# dacă am vrea să scriem totul într-o singură linie?
print("Salut %s!" % input("Cum te numești? "))
