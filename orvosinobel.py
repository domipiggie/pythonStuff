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

# file sorainak feldolgozása
for i in f1:
    # objektum
    EgyEmber = NobelDijasok(i.strip())
    
    # nevek kiíratása
    print(EgyEmber.nev)

# 1. Hány Nobel díjas van
nobelekSzama = 0

setSecondLine()

for i in f1:
    nobelekSzama += 1

print("Össesen", nobelekSzama, "db Nobel díjas van.")


# 2. Hány magyar Nobel díjas van
magyarNobelekSzama = 0

setSecondLine()

for i in f1:
    EgyEmber = NobelDijasok(i.strip())
    
    if EgyEmber.orszagkod == "H":
        magyarNobelekSzama += 1

print(magyarNobelekSzama, "db magyar Nobel dijas van.")

# 3. Mikor kapták az első Nobel dijat
evek = []

setSecondLine()

for i in f1:
    EgyEmber = NobelDijasok(i.strip())
    evek.append(EgyEmber.ev)

print("A legelső Nobelt", min(evek), "-ban/ben kapták")

# 4. Szerepel-e a listában Otto nevű ember?
isArchibald = False

setSecondLine()

for i in f1:
    EgyEmber = NobelDijasok(i.strip())
    
    if "Otto" in EgyEmber.nev:
        isArchibald = True

if isArchibald:
    print("A listában szerepel Otto nevű ember.")
else:
    print("A listában nem szerepel Otto nevű ember.")

# 5. Írasd ki soronként, hogy hány éves korában halt meg a díjazott. (Ha még él, ne írj ki semmit.)
setSecondLine()

for i in f1:
    EgyEmber = NobelDijasok(i.strip())
    
    szulHalSzeletelt = EgyEmber.szulHal.split("-")
    
    if szulHalSzeletelt[1] != "":
        eves = int(szulHalSzeletelt[1]) - int(szulHalSzeletelt[0])
        print(EgyEmber.nev, eves, "évesen halt meg.")