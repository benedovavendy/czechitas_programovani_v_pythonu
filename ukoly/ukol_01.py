# TODO zkontrolovat správnou strukturu kódu
# importy
# konstanty, globalni promenne
# definice trid, funkci
# klasicky kod


### trida Zvire

class Zvire:
    def __init__(self, jmeno, druh, vaha):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha
    
    def __str__(self):
        return f'{self.jmeno} je {self.druh} a váží {self.vaha} kg.'
    
    def export_to_dict(self):
        return {
                'jmeno': self.jmeno,
                'druh': self.druh,
                'vaha': self.vaha
            }

# pavouk = Zvire('Adolf', 'Tarantule Velká', 0.1)
# pavouk_export = pavouk.export_to_dict()
# assert pavouk_export['jmeno'] == 'Adolf'
# assert pavouk_export['druh'] == 'Tarantule Velká'
# assert pavouk_export['vaha'] == 0.1
# print(pavouk_export['jmeno'])
# print(pavouk_export['druh'])
# print(pavouk_export['vaha'])

zvirata_dict = [
    {'jmeno': 'Růženka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},

]

list_zvirat = []
for zvire in zvirata_dict:
    list_zvirat.append(Zvire(zvire['jmeno'], zvire['druh'], zvire['vaha']))

# print(list_zvirat)
# print(list_zvirat[0].jmeno)
# print(list_zvirat[1].druh)
# print(list_zvirat[2].vaha)

# Zvire class
# zvire = Zvire('Láďa', 'Koala', 15)
# assert hasattr(zvire, 'jmeno')
# assert hasattr(zvire, 'druh')
# assert hasattr(zvire, 'vaha')
# assert isinstance(zvire.jmeno, str)
# assert isinstance(zvire.druh, str)
# assert isinstance(zvire.vaha, int)
# assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}


### trida Zamestnanec

class Zamestnanec:
    def __init__(self, cele_jmeno, rocni_plat, pozice):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice

    def __str__(self):
        return f'{self.cele_jmeno} s ročním platem {self.rocni_plat} Kč pracuje na pozici {self.pozice}.'

    def ziskej_inicialy(self):
        if ' ' in self.cele_jmeno:
            return f'{self.cele_jmeno.split()[0][0]}.{self.cele_jmeno.split()[1][0]}.'
        else:
            pass

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]

list_zamestnancu = []
for zamestnanec in zamestnanci_dict:
    list_zamestnancu.append(Zamestnanec(zamestnanec['cele_jmeno'], zamestnanec['rocni_plat'], zamestnanec['pozice']))

# print(list_zamestnancu)
# print(list_zamestnancu[0].cele_jmeno)
# print(list_zamestnancu[1].rocni_plat)
# print(list_zamestnancu[2].pozice)

# Zamestnanec class
# zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programator')
# assert hasattr(zamestnanec, 'cele_jmeno')
# assert hasattr(zamestnanec, 'rocni_plat')
# assert hasattr(zamestnanec, 'pozice')
# assert isinstance(zamestnanec.cele_jmeno, str)
# assert isinstance(zamestnanec.rocni_plat, int)
# assert isinstance(zamestnanec.pozice, str)
# assert zamestnanec.ziskej_inicialy() == 'P.N.'


### trida Reditel

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno, rocni_plat, oblibene_zvire, pozice = 'Reditel'):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire
    
# Priklad vytvoreni objektu (klidne zkopiruj)
# zvire = Zvire('Adolf', 'Tarantule Velká', 0.1)
# reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)
# assert reditel.pozice == 'Reditel'
# assert isinstance(reditel.oblibene_zvire, Zvire)

# print(reditel.pozice)
# print(reditel.cele_jmeno)
# print(reditel.ziskej_inicialy())

# zvire = Zvire('Lev', 'Lvice', 150)
# reditel = Reditel('Jan Novotny', 800000, zvire)
# assert isinstance(reditel.oblibene_zvire, Zvire)

# print(reditel.pozice)
# print(reditel.cele_jmeno)
# print(reditel.ziskej_inicialy())


### trida Zoo

class Zoo():
    def __init__(self, nazev, adresa, reditel, zamestnanci, zvirata):
        self.nazev = nazev
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    def vaha_vsech_zvirat_v_zoo(self):
        vaha_zvirat = 0
        for zvire in self.zvirata:
            vaha_zvirat += zvire.vaha
        return vaha_zvirat

    def mesicni_naklady_na_zamestnance(self):
        naklady_na_zamestnance = 0
        for zamestnanec in self.zamestnanci:
            naklady_na_zamestnance += zamestnanec.rocni_plat
        naklady_na_zamestnance += reditel.rocni_plat
        return naklady_na_zamestnance / 12

# zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, list_zamestnancu, list_zvirat)

# print(zoo.reditel)
# print('Celková váha zvířat v ZOO:', zoo.vaha_vsech_zvirat_v_zoo())
# print('Měsíční náklady na zaměstnance:', zoo.mesicni_naklady_na_zamestnance())

# print(150+20+300+700)
# print(700000+600000+650000+800000)

# Zoo class
# zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
# assert hasattr(zoo, 'nazev')
# assert hasattr(zoo, 'adresa')
# assert hasattr(zoo, 'reditel')
# assert hasattr(zoo, 'zamestnanci')
# assert hasattr(zoo, 'zvirata')
# assert isinstance(zoo.nazev, str)
# assert isinstance(zoo.adresa, str)
# assert isinstance(zoo.reditel, Reditel)
# assert isinstance(zoo.zamestnanci, list)
# assert isinstance(zoo.zvirata, list)
# assert zoo.vaha_vsech_zvirat_v_zoo() == 150
# assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12