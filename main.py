#   Razpoznavani jazyku
#   Lipina Ekaterina, 1.rocnik, 32. skipina
#   zimni semestr 2020/2021
#   Programování 1 NPRG030


import math

pocetJazyku = 8


def JakyJeJazykTextu(text):
    text = text.lower()
# prevadime do malych pismen

# Prace s Tabulkou Frekvence
    fileZTabulkou = open("FrequancyLetters.txt", "r", encoding='utf8')

# cte po radkach a zapisuje do seznamu
    tabulka = fileZTabulkou.readlines()

    fileZTabulkou.close()

# ma v sobe seznam vsech moznych pismen
    seznamVsechPismen = []
    for i in range(len(tabulka)):
        seznamVsechPismen.append(tabulka[i][0])

# mame tabulku v matrici
    for i in range(len(tabulka)):
        tabulka[i] = tabulka[i].split()

# kolikkrat se vzskytuje kazde pismeno v textu
    pocetPismenVTextu = {}
    for i in range(len(seznamVsechPismen)):
        pocetPismenVTextu[seznamVsechPismen[i]] = 0

    for i in range(len(seznamVsechPismen)):
        del tabulka[i][0]

# prevadime do realnych cisel
    for i in range(len(seznamVsechPismen)):
        for j in range(pocetJazyku):
            tabulka[i][j] = float(tabulka[i][j])

# pocita, kolik je kazdeho pismena v textu
    for i in range(len(text)):
        for j in range(len(seznamVsechPismen)):
            if text[i] == seznamVsechPismen[j]:
                pocetPismenVTextu[seznamVsechPismen[j]] += 1

    def pocitaniSkore(pocetPismenaVTextu, frekvenceVTabulce):
        skore = pocetPismenaVTextu * frekvenceVTabulce

        if skore == 0:
            skore = 0
        else:
            skore = math.log2(pocetPismenaVTextu * frekvenceVTabulce)

        return skore

# vypsani skore do seznamu
    skoreTextu1 = []
    skoreTextu = [None] * (pocetJazyku)
    for i in range(pocetJazyku):
        for j in range(len(seznamVsechPismen)):
            skoreTextu1.append(pocitaniSkore(pocetPismenVTextu[seznamVsechPismen[j]], tabulka[j][i]))
        skoreTextu[i] = skoreTextu1
        skoreTextu1 = []

# pocitani sumy skore
    summSkore = []
    for i in range(pocetJazyku):
        summ = 0
        for j in range(len(seznamVsechPismen)):
            summ += skoreTextu[i][j]

        summSkore.append(summ)

    jazyky = {summSkore[0]: 'English', summSkore[1]: 'Spanish', summSkore[2]: 'Turkish', summSkore[3]: 'Swedish',
              summSkore[4]: 'Polish', summSkore[5]: 'Danish', summSkore[6]: 'Icelandic', summSkore[7]: 'Czech'}

# jazyk s nejvzssim skore je jazyk textu
    return jazyky[max(summSkore)]


odkazNaTextFile = input("Nazev souboru s textem: ",)
fileZTextem = open(odkazNaTextFile, 'r')
text = fileZTextem.read()
fileZTextem.close()

print("Jazyk textu je: ", JakyJeJazykTextu(text))
