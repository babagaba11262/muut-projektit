# Tehdään numeroiden lajittelu ohjelma.
# 1. käy läpi numerot alkaen 0 tai siitä mihin on jääty, joka katsotaan numerolajittelu_teksti tiedostosta.
# 2. jokaisen numeron kohdalla tehdään tarkistuksia ->
#    -jaollisuus (numeroon itseensä asti, eli onko kokonaisluku)
#    -onko neliöjuuri tasaluku
#    -logaritmi (tämä vaatii hieman miettimistä mitä kaikkea tästä halutaan)
#       log* hakee luvusta sen exponentin mikä tulee kun * korotetaan tähän exponenttiin.
#       esim log2 8 = 3 koska 2*2*2 = 8
     

#    Läpi käytyjen lukujen tallennus:
#    -tallennetaan tekstitiedostoon
#    -1 luku joka riville, luvun perään : ja sen jälkeen luvun tagit ja muut tiedot, eroteltuna ; esim.
#    KL = kokonaisluku, LOG:X, TSQR = Tasainen neliöjuuri,


#    Kerättyjen tietojen näyttäminen:
#    graafinen ikkuna, josta voi hakea jotain numeroa, tai katsella isoa listaa, jota voi suodattaa. suodattimet voi
#    kääntää ympäri, eli voi päättää näytetäänkö luvut jotka ovat alkulukuja vai ne jotka eivät ole

#    Muuta
#    tekstitiedoston kokoa pitää seurata, ja laittaa joku raja sen koolle.


class NumeronLajittelu:


#ensin tehdään funktio, joka pyörittää lukuja
def numeropyoritys(raja):
    numero = 0
    while numero <= raja:
        numero += 1

    return numero

#tehdään userimput funktio, joka sisältää myös perus virheentarkistus systeemit
def userinput():
    a

#tehdään funktio joka katsoo onko luku kokonaisluku


def kokonaisluku(luku):

    a = True
    tags = ""
    while a is True:
        for a2 in range(0, luku, 1):
            if luku % a2 == 0:
                tags = "KL"

        a = False
    return tags

