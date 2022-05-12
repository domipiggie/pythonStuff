#file megnyitása
file = open("orvosi_nobeldijak.txt", "r", encoding="utf-8")

#lista létrehozása a sorok számára
lista = []

#első sor beolvasá(sa (fejléc)
file.readline()


#lista feltöltése
for sor in file:
    lista.append(sor.strip().split(";"))


#hány angol lóbeldíjas van
angolok = 0

for sor in lista:
    if sor[3] == "GB":
        angolok += 1

print("1. feladat:\n", angolok, "db angol Nóbeldíjas van.")


#kik kaptak 1920 előtt nóbeldíjat
print("\n2. feladat")
for sor in lista:
    if int(sor[0]) < 1905:
        print(sor[1])


#írjuk ki az A betűvel kezdődő nevűeket
print("\n3. feladat")
for sor in lista:
    if sor[1][0] == "A":
        print(sor[1])


#azok neve akik még élnek, és hány évesek
for sor in lista:
    szulHal = sor[2].split("-")
    if szulHal[1] == "":
        print(sor[1], 2022-int(szulHal[0]))


#file bezárása mert mért ne
file.close()