class Autok:
    nap: int
    oraPerc: str
    percek: int
    rendszam: str
    szemelyAzonosito: str
    kmOra: int
    irany: int
    
    def __init__(self, sor: str) -> None:
        adatok = sor.split(" ")
        self.nap = int(adatok[0])
        self.oraPerc = adatok[1]
        
        oraPercList = adatok[1].split(":")
        self.percek = int(oraPercList[0]) + int(oraPercList[1])
        
        self.rendszam = adatok[2]
        self.szemelyAzonosito = adatok[3]
        self.kmOra = int(adatok[4])
        self.irany = int(adatok[5])

# 1: Olvassa be és tárolja el az autok.txt fájl tartalmát!
f1 = open("autok.txt", "r")
autokLista: list[Autok] = []

for i in f1:
    autokLista.append(Autok(i))

# 2: Adja meg, hogy melyik autót vitték el utoljára a parkolóból! Az eredményt a mintának megfelelően írja a képernyőre!
utoljaraElvittAuto: Autok = None

for i in autokLista:
    # Ha még nincs vizsgált autó, akkor beállítjuk a jelenlegit
    if utoljaraElvittAuto == None:
        utoljaraElvittAuto = i
    # Ha az autó kifelé megy, a nap vagy az idő későbbi mint a jelenlegi utoljára elvitt aotó, akkor beállítjuk a most vizsgáltra
    elif i.irany == 0 and (i.nap >= utoljaraElvittAuto.nap or i.percek > utoljaraElvittAuto.percek):
        utoljaraElvittAuto = i

print("2. feladat\n", utoljaraElvittAuto.nap, ". nap rendszám: ", utoljaraElvittAuto.rendszam, sep="")

# 3: Kérjen be egy napot és írja ki a képernyőre a minta szerint, hogy mely autókat vitték ki és hozták vissza az adott napon!
print("3. feladat")
keresettNap = int(input("Nap: "))
print("Forgalom a(z) ", keresettNap, ". napon:", sep="")

for i in autokLista:
    if i.nap == keresettNap and i.irany == 0:
        print(i.oraPerc, i.rendszam, i.szemelyAzonosito, "ki")
    elif i.nap == keresettNap and i.irany == 1:
        print(i.oraPerc, i.rendszam, i.szemelyAzonosito, "be")

# 4: Adja meg, hogy hány autó nem volt bent a hónap végén a parkolóban!
kintLevoAutok: list[str] = []

for i in autokLista:
    if i.irany == 0:
        kintLevoAutok.append(i.rendszam)
    elif i.irany == 1 and len(kintLevoAutok) > 0:
        for j in range(len(kintLevoAutok)):
            if len(kintLevoAutok) > j and kintLevoAutok[j] == i.rendszam:
                kintLevoAutok.pop(j)

print("4. feladat\nA hónap végén", len(kintLevoAutok), "autót nem hoztak vissza.")

# 5: Készítsen statisztikát, és írja ki a képernyőre mind a 10 autó esetén az ebben a hónapban
#megtett távolságot kilométerben! A hónap végén még kint lévő autók esetén az utolsó
#rögzített kilométerállással számoljon! A kiírásban az autók sorrendje tetszőleges lehet.
print("5. feladat")
rendszamLista: list[str] = []

for i in autokLista:
    if i.rendszam not in rendszamLista:
        rendszamLista.append(i.rendszam)

for j in rendszamLista:
    min: int = None
    max: int = 0

    for i in autokLista:
        if i.rendszam == j:
            if i.irany == 0 and min == None:
                min = i.kmOra
            elif i.irany == 1 and i.kmOra > max:
                max = i.kmOra

    print(j, max-min, "km")

# 6: Határozza meg, melyik személy volt az, aki az autó egy elvitele alatt a leghosszabb
#távolságot tette meg! A személy azonosítóját és a megtett kilométert a minta szerint írja a
#képernyőre! (Több legnagyobb érték esetén bármelyiket kiírhatja.)



# 7: Az autók esetén egy havi menetlevelet kell készíteni! Kérjen be a felhasználótól egy
#rendszámot! Készítsen egy X_menetlevel.txt állományt, amelybe elkészíti az adott
#rendszámú autó menetlevelét! (Az X helyére az autó rendszáma kerüljön!) A fájlba
#soronként tabulátorral elválasztva a személy azonosítóját, a kivitel időpontját (nap.
#óra:perc), a kilométerszámláló állását, a visszahozatal időpontját (nap. óra:perc), és
#a kilométerszámláló állását írja a minta szerint! (A tabulátor karakter ASCII-kódja: 9.)

