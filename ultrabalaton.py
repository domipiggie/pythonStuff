class Eredmeny:
    nev: str
    rajtszam: int
    kategoria: str
    ido: str
    tavSzazalek: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(";")
        self.nev = adatok[0]
        self.rajtszam = int(adatok[1])
        self.kategoria = adatok[2]
        self.ido = adatok[3]
        self.tavSzazalek = int(adatok[4])

#file megnyitása
f1 = open("ub2017egyeni.txt", "r", encoding="utf-8")

#változók
noiIndulok = 0
minSzazalek = 100
minIdoTav = [0]

#első sort beolvasom, hogy a 2. -ra ugorjon a mutató (az első sor csak fejléc)
f1.readline()
for i in f1:
    egyAdat = Eredmeny(i)
    print("Neve:", egyAdat.nev, "ideje:", egyAdat.ido)
    
    #Hány női induló volt a versenyen?
    if egyAdat.kategoria == "Noi":
        noiIndulok += 1
    
    #Mennyi a legkisebb százalék
    if egyAdat.tavSzazalek < minSzazalek:
        minSzazalek = egyAdat.tavSzazalek
    
    #Leghamarabb kiesett
    jelenlegiIdo = list(map(int,egyAdat.ido.split(":")))
    masodpercek = jelenlegiIdo[0] * 60 + jelenlegiIdo[1] * 60 + jelenlegiIdo[2]
    
    if masodpercek < minIdoTav[0] or minIdoTav[0] == 0:
        minIdoTav.clear()
        minIdoTav.append(masodpercek)
        minIdoTav.append(egyAdat.tavSzazalek)
    
    
print("A versenyen", noiIndulok, "női induló volt.")
print("A legkisebb százalék:", minSzazalek)

print(minIdoTav)