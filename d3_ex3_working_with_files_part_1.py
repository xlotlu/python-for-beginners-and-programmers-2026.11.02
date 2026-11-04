f = open("concepts-and-notes.md")

print(f.read())
# .read() va returna un string gol
# dacă a ajuns la finalul fișierului.

# dar poate veni un alt proces
# să facă append la fișier

# util de știut că există,
# în practică sunt șanse minime să le folosiți:
f.tell() # poziția internă a cursorului
position = 0
f.seek(position) # mută cursorul la acest byte

#.read() primește parametru opțional size,
#util pentru chunked reading:
chunk = 100

content = f.read(chunk)
while content:
    print("»", content)
    content = f.read(chunk)

# work on this:
# citiți fișierul iterând în el
# și aflați care sunt sursele de newline-uri duplicate.
#
# și implementați o strategie să nu mai fie duplicate.

f = open("concepts-and-notes.md")
for line in f:
    print(line.removesuffix("\n"))



### concluzie:
# în practică veți face
# ori 1:
contents = f.read() # și "consumați" tot fișierul o dată

# use-case:
# vom folosi tot conținutul și nu avem limitări de memorie
# - un fișier template

# exemplu:

f = open("template.html", 'w')
content = """<html>
{title}
<p>{body}</p>
</html>"""
f.write(content)
f.close()

# are sens să citim tot content-ul:
f = open("template.html", 'r')
template = f.read()
print(
    template.format(title="Un titlu", body="Mult, mult\nmult conținut")
)



# ori 2:
for line in f:
    # do stuff with..
    line
# use-case:
# - log-uri
# - inputul este line-oriented, și facem search

# (ori poate, poate, în cazuri foarte rare, 3: chunked reading)
# (  adică f.read(chunksize)  )



### modul write

f = open("filename", 'w') # atenție! trunchează instant fișierul (sau îl creează)
f.write("some content")   # nu ajunge imediat pe disc.

f.flush()                 # golește buffer-ul (ajunge pe disc)
                          # vrem să facem flush explicit doar în cazuri f. speciale
                          # exemplu: când scriem log-uri

f.close()                 # închide file pointer-ul
                          # (și face implicit flush)
