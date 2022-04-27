from re import A


class Meccsek:
    fordulo: str
    hazaiGol: int
    vendegGol: int
    hazaiFelido: int
    vendegFelido: int
    hazaiCsapat: str
    vendegCsapat: str

    def __init__(self, sor: str) -> None:
        darabolt = sor.split(" ")

        self.fordulo = darabolt[0]
        self.hazaiGol = int(darabolt[1])
        self.vendegGol = int(darabolt[2])
        self.hazaiFelido = int(darabolt[3])
        self.vendegFelido = int(darabolt[4])
        self.hazaiCsapat = darabolt[5]
        self.vendegCsapat = darabolt[6].strip()

def felidoDiff(merkozes: Meccsek) -> None:
    if merkozes.hazaiFelido - merkozes.vendegFelido > 0 and merkozes.hazaiGol - merkozes.vendegGol < 0:
        print(merkozes.hazaiCsapat, merkozes.vendegCsapat, merkozes.fordulo, "hazai-vendeg")
    elif merkozes.hazaiFelido - merkozes.vendegFelido < 0 and merkozes.hazaiGol - merkozes.vendegGol > 0:
        print(merkozes.hazaiCsapat, merkozes.vendegCsapat, merkozes.fordulo, "vendeg-hazai")

file = open("meccs.txt", "r", encoding="utf-8")
file.readline()

meccsekObjList: list[Meccsek] = []

for i in file:
    meccsekObjList.append(Meccsek(i))

# 0. feladat: hány mérkőzés volt
print(len(meccsekObjList), "mérkőzés volt.")

# 1. feladat: kérj be egy fordulószámot, írd ki a forduló mérkőzéseinek eredményeit
keresettFordulo = input("Kérem adja meg a forduló számát (1-20): ")
for i in meccsekObjList:
    if i.fordulo == keresettFordulo:
        print(i.hazaiCsapat, "-", i.vendegCsapat.strip(), ": ", i.hazaiGol, "-", i.vendegGol, " (", i.hazaiFelido, "-", i.vendegFelido, ")", sep="")

# 2. feladat: kérjünk be a felhasználótól egy csapat nevet, írjuk ki hogy résztvettek-e
keresettCsapat = input("Kérem adjon meg egy csapatnevet: ")
vanKeresettCsapat = False

for i in meccsekObjList:
    if i.hazaiCsapat == keresettCsapat or i.vendegCsapat == keresettCsapat:
        vanKeresettCsapat = True

if vanKeresettCsapat:
    print(keresettCsapat, "részt vett.")
else:
    print(keresettCsapat, "nem vett részt.")

# 3. feladat: mikor volt olyan, hogy sikerült fordítani az álláson az első félidőhöz képest
for i in meccsekObjList:
    felidoDiff(i)

# 4. feladat: hány gólt lőttek a Nyulak, vendég pályán
nyulGolok = 0
for i in meccsekObjList:
    if i.vendegCsapat.strip() == "Nyulak":
        nyulGolok += i.vendegGol

print("A Nyulak", nyulGolok, "db gólt lőttek vendég pályán")