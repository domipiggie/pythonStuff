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
        self.vendegCsapat = darabolt[6]

file = open("meccs.txt", "r", encoding="utf-8")
file.readline()

meccsekObjList: list[Meccsek] = []

for i in file:
    meccsekObjList.append(Meccsek(i))

# 0. feladat: hány mérkőzés volt
print(len(meccsekObjList), "mérkőzés volt.")

# 2. feladat: kérj be egy fordulószámot, írd ki a forduló mérkőzéseinek eredményeit
keresettFordulo = input("Kérem adja meg a forduló számát (1-20): ")
for i in meccsekObjList:
    if i.fordulo == keresettFordulo:
        print(i.hazaiCsapat, "-", i.vendegCsapat.strip(), ": ", i.hazaiGol, "-", i.vendegGol, " (", i.hazaiFelido, "-", i.vendegFelido, ")", sep="")

# 3. feladat: 