from utilities import unos_pozitivnog_cijelog_broja, unos_datuma
from .korisnik import Korisnik
from zdravstvena import Zdravstvena
def unos_korisnika(redni_broj):

    ime = input(f"Unesite ime {redni_broj}. korisnika: ").title()
    prezime = input(f"Unesite prezime {redni_broj}. korisnika: ").title()
    telefon = unos_pozitivnog_cijelog_broja(f"Unesite telefon {redni_broj}. korisnika: ")
    email = input(f"Unesite email {redni_broj}. korisnika: ").strip()
    oib = int(input("Unesite oib: "))
    datum_izdavanja = unos_datuma("Unesite dan izdavanja zdravstvene iskaznice: ")

    zdravstvena = Zdravstvena(oib, datum_izdavanja)

    return Korisnik(ime, prezime, email, telefon, zdravstvena)