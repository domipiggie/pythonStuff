# OSZTÁLY:

class Haromszog:
    a: int
    b: int
    c: int
    
    # konstruktor
    def __init__(self, sorom) -> None:
        self.a = int(sorom[0])
        self.b = int(sorom[1])
        self.c = int(sorom[2])    
        
    # osztály metódusa: szöveggel visszatérve megmondja, hogy a számok háromszöget alkotnak-e    
    def haromszoge(self) -> str:
        if self.a<self.b+self.c and self.b<self.a+self.c and self.c<self.a+self.b:
            return "Háromszöget alkotnak"
        else:
            return "Nem alkotnak háromszöget."
    
    # osztály metódusa: egész számként visszaadja a háromszög kerületét
    def kerulet(self)-> int:
        return self.a + self.b + self.c
    
    # osztály methódusa: logikai értékként visszaadja hogy derékszögű-e
    def derekszoge(self)->bool:
        return pow(self.a, 2) + pow(self.b, 2) == pow(self.c, 2)
    
    def vanilyenoldal(self, keresett):
        return self.a == int(keresett) or self.b == int(keresett) or self.c == int(keresett)

#file megnyitása
file = open("haromszog.txt", "r")
file.readline()

sorok = []

# 2D lista létrehozása
for sor in file:
    sorok.append(sor.strip().split("*"))

for i in sorok:
    # példányosítás
    egyHaromszog = Haromszog(i)
    
    isTriangle = egyHaromszog.haromszoge()
    print(isTriangle)
    
    if isTriangle == "Háromszöget alkotnak":
        print("A háromszög kerülete", egyHaromszog.kerulet())

# Kérj be 3 számot, írd ki hogy háromszög-e
oldalak = input("Kérem adja meg a háromszög 3 oldalát (forma: a,b,c):").split(",")

bekertHaromszog = Haromszog(oldalak)
print(bekertHaromszog.haromszoge())
print(bekertHaromszog.derekszoge())

keresettSzam = input("Keresett szám: ")
print(bekertHaromszog.vanilyenoldal(keresettSzam))