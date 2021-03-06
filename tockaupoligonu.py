#trenutno radi samo za jednostavne (Jordanove) poligone (radi ponekad i za složene, osim ako se sijeku sami sa sobom)
#napravi_poligon() ne radi kako treba jer ga zezaju float vrijednosti

from presjeksegmenata import *

#funkcija koja vraća True/False ovisno pripada li dana točka danom poligonu
def tocka_u_poligonu(tocka,poligon):
    return tocka.pripada_poligonu(poligon)


#--------------------------------------------V I Z U A L I Z A C I J E -------------------------------------------------
#funkcija koja vraća True/False ovisno pripada li dana točka danom poligonu + vizualizacija
def v_tocka_u_poligonu(tocka,poligon):
    #određuje se pripadnost točke poligonu
    pripada=tocka.pripada_poligonu(poligon)

    #prikazuju se poligon, njegove točke i dana točka
    ax.fill([i.x for i in poligon.tocke], [i.y for i in poligon.tocke], facecolor="lightblue", edgecolor="blue")
    ax.scatter([i.x for i in poligon.tocke], [i.y for i in poligon.tocke],marker='.',color="blue")
    boja="black"
    if(pripada>-1):
        boja="red"
    ax.scatter(tocka.x, tocka.y, marker="o", color=boja)

    return pripada

#TESTNI PRIMJER :
# v_tocka_u_poligonu(Tocka(int(random()*100%20-10),int(random()*100%20-10),napravi_poligon())


#funkcija za testiranje + vizualizacija
def v_tocka_u_poligonu_test(br_tocaka):
    imena_tocaka = ascii_uppercase
    poligon=napravi_poligon()

    ax.fill([i.x for i in poligon.tocke], [i.y for i in poligon.tocke], facecolor="lightblue", edgecolor="blue")
    ax.scatter([i.x for i in poligon.tocke], [i.y for i in poligon.tocke],color="blue",marker=".")
    for i in range(0, len(poligon.tocke)):
        ax.annotate(imena_tocaka[i % len(imena_tocaka)], (poligon.tocke[i].x, poligon.tocke[i].y))

    for i in range(0, br_tocaka):
        tocka = Tocka(random() * 100 % 20 - 10, random() * 100 % 20 - 10)
        if (tocka.pripada_poligonu(poligon)>-1):
            ax.scatter(tocka.x, tocka.y, marker="o", color="red")
        else:
            ax.scatter(tocka.x, tocka.y, marker="o", color="black")

#TESTNI PRIMJER :
# v_tocka_u_poligonu_test(100)



def napravi_razlicitu_tocku(lista):
    tocka = Tocka(random() * 100 % 20 - 10, random() * 100 % 20 - 10)
    while (tocka in lista):
        tocka = Tocka(int(random() * 100 % 20 - 10), int(random() * 100 % 20 - 10))

    return tocka

def napravi_poligon():
    tocke = []

    for i in range(0, 3):
        tocke.append(napravi_razlicitu_tocku(tocke))

    for i in range(3, 6):
        duzine = Poligon(tocke).u_duzine()
        duzine.pop()
        zadnja_tocka = tocke[-1]
        tocka = napravi_razlicitu_tocku(tocke)
        while (len(presjek_duzine_i_skupa_duzina(Duzina(zadnja_tocka, tocka), duzine)) > 1):
            tocka = napravi_razlicitu_tocku(tocke)
        tocke.append(tocka)

    duzine = Poligon(tocke).u_duzine()
    duzina = duzine[-1]
    duzine.pop()

    pom = 0
    while (len(presjek_duzine_i_skupa_duzina(duzina, duzine)) > 2):
        tocka = napravi_razlicitu_tocku(tocke)
        while (len(presjek_duzine_i_skupa_duzina(Duzina(tocka, tocke[-1]), duzine)) > 1):
            tocka = napravi_razlicitu_tocku(tocke)
            pom += 1
            if (pom > 1000):
                break
        tocke.append(tocka)
        duzine = Poligon(tocke).u_duzine()
        duzina = duzine[-1]
        duzine.pop()

    return Poligon(tocke)



