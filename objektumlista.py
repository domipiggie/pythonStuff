class NobelDijasok:
    ev: int
    nev: str
    szulHal: str
    orszagkod: str
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(";")
        self.ev = adatok[0]
        self.nev = adatok[1]
        self.szulHal = adatok[2]
        self.orszagkod = adatok[3]

def setSecondLine() -> None:
    f1.seek(0, 0)
    f1.readline()

# file megnyitása
f1 = open("orvosi_nobeldijak.txt", "r", encoding="utf-8")
f1.readline()

# üres objektumlista létrehozása
# ez egy olyan lista, ami sok NobelDijasok objektumot tartalmaz
osszesNobelDijas: list[NobelDijasok] = []

# objektum lista feltöltése
for i in f1:
    EgyEmber = NobelDijasok(i.strip())
    osszesNobelDijas.append(EgyEmber)

print(len(osszesNobelDijas))

print(osszesNobelDijas[10].nev)

for i in osszesNobelDijas:
    print(i.ev)

for i in range(0, len(osszesNobelDijas)):
    print(osszesNobelDijas[i].nev)