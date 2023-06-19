class Klass:
    def __init__(self, adat1, adat2, adat3,):
        self.adat1 = adat1
        self.adat2 = adat2
        self.adat3 = adat3

    # print
    def __str__(self):
        return f"Klass objektum:\n\Adat1:{self.adat1}\n\Adat2:{self.adat2}\n\Adat3:{self.adat3}"
    

    # Listák esetén -> []
    def __repr__(self):
        return f"{self.adat1}"

adatok = []

f = open("./peldafolder/pelda.txt", "r", encoding="utf-8")
f.readline() # Első sor (fejléc) átugrása
for sor in f:
    sor = sor.strip().split(";")
    adatok.append(
        Klass(
            sor[0],
            int(sor[1]),
            int(sor[2]),
            int(sor[3])
        )
    )
f.close()


"""
print(f"3. feladat: A világranglistán {len(adatok)} csapat szerepel")

summa = 0
for adat in adatok:
    summa += adat.pontszam

print(f"4. feladat: A csapatok átlagos pontszáma {round(summa/len(adatok), 2)} pont")

# Legnagyobb változás
legnagyobb_valtozas = adatok[0]
for adat in adatok:
    if adat.valtozas > legnagyobb_valtozas.valtozas:
        legnagyobb_valtozas = adat

print("5.feladat: A legtöbbet javító csapat:")
print(f"\tHelyezés: {legnagyobb_valtozas.helyezes}")
print(f"\tCsapat: {legnagyobb_valtozas.csapat}")
print(f"\tPontszám: {legnagyobb_valtozas.pontszam}")
"""