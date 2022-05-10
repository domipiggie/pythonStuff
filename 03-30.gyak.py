f1 = open("haromszogek.txt", "r", encoding="utf-8")

for i in f1:
    print(i.strip())

f1.seek(0, 0)
f1.readline()

print(f1.readline().strip())

harmadikSor = f1.readline().strip().split()
print(harmadikSor)
print(harmadikSor[1])

f2 = open("ki.txt", "w", encoding="utf-8")
f2.write(harmadikSor[1])
f2.close()

f1.seek(0, 0)
for i in range(0, 4):
    print(f1.readline().strip())