def megoldas():
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

    # 4: készítsen egy függvényt, amely megkapja a versenyző időeredményét, majd visszaadja az időt órában
    def idoOraban(ido):
        hms = list(map(int, ido.split(":")))
        secs = hms[2] + hms[1] * 60 + hms[0] * 3600
        return secs/3600

    # file megnyitása
    f1 = open("ub2017egyeni.txt", "r", encoding="utf-8")

    # objektum lista létrehozása
    osszesEredmeny: list[Eredmeny] = []

    # objektum lista feltöltése
    f1.readline()
    for i in f1:
        osszesEredmeny.append(Eredmeny(i.strip()))

    # lista hosszának kiíratása
    print("A listában", len(osszesEredmeny), "eredmény van.")

    # 1: hány női sportoló teljesítette a teljes távot
    noiTeljesTav = 0

    for i in osszesEredmeny:
        if i.kategoria == "Noi" and i.tavSzazalek == 100:
            noiTeljesTav += 1

    print(noiTeljesTav)

    # 2: kérj be egy nevet, határozd meg hogy indult-e. ha indult, mekkorat távot teljesített
    keresettNev = input("Kérem adja meg a keresett sportoló nevét: ")
    vanKeresett = False

    for i in osszesEredmeny:
        if i.nev == keresettNev:
            if i.tavSzazalek == 100:
                print(keresettNev, ": indult, teljesítette", sep="")
            else:
                print(keresettNev, ": indult, nem teljesítette", sep="")
            vanKeresett = True

    if not vanKeresett:
        print(keresettNev, ": nem indult", sep="")

    # 3: írassa ki az első sportoló idejét órában
    ido = osszesEredmeny[0].ido
    hms = list(map(int, ido.split(":")))
    secs = hms[2] + hms[1] * 60 + hms[0] * 3600
    print(round(secs/3600, 2))

    # 5: írassa ki a teljes távot teljesítő, férfi sportolók átlagos idejét órában
    idokSzama = 0
    osszesitettIdokOraban = 0

    for i in osszesEredmeny:
        if i.kategoria == "Ferfi" and i.tavSzazalek == 100:
            idokSzama += 1
            osszesitettIdokOraban += idoOraban(i.ido)

    print(round(osszesitettIdokOraban/idokSzama, 2))