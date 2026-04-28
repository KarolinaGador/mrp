import math

def mrp():
    print("BLAT")
    czas_blat = int(input("Czas produkcji blatu (dni): "))
    magazyn_blat = int(input("Stan magazynowy blatu: "))
    zapas_blat = int(input("Zapas bezpieczeństwa blatu: "))
    
    print("NOGA")
    czas_noga = int(input("Czas dostawy nóg (dni): "))
    magazyn_noga = int(input("Stan magazynowy nóg: "))
    zapas_noga = int(input("Zapas bezpieczeństwa nóg: "))
    partia_noga = int(input("Wielkość partii dla nóg (np. 4): "))

    dane = {
        "Stół":  {"czas": 1, "magazyn": 0, "zapas": 0, "partia": 1},
        "Blat":  {"czas": czas_blat, "magazyn": magazyn_blat, "zapas": zapas_blat, "partia": 1},
        "Noga":  {"czas": czas_noga, "magazyn": magazyn_noga, "zapas": zapas_noga, "partia": partia_noga}
    }

    struktura = {
        "Stół": [("Blat", 1), ("Noga", 4)]
    }

    ile = int(input("Ile stołów chcesz wyprodukować? "))
    dzien_oddania = int(input("Na który dzień mają być gotowe? "))

    zadania = [("Stół", ile, dzien_oddania)]
    
    print("\nELEMENT | BRUTTO | NETTO | PRODUKCJA | START | KONIEC")

    while zadania:
        nazwa, zapotrzebowanie_brutto, termin_zakonczenia = zadania.pop(0)
        info = dane[nazwa]
        dostepne_w_magazynie = max(0, info["magazyn"] - info["zapas"])
        zapotrzebowanie_netto = max(0, zapotrzebowanie_brutto - dostepne_w_magazynie)
        ilosc_do_produkcji = math.ceil(zapotrzebowanie_netto / info["partia"]) * info["partia"]
        dzien_rozpoczecia = termin_zakonczenia - info["czas"]

        print(nazwa, "|", zapotrzebowanie_brutto, "|", zapotrzebowanie_netto, "|", ilosc_do_produkcji, "|", dzien_rozpoczecia, "|", termin_zakonczenia)

        if nazwa in struktura and ilosc_do_produkcji > 0:
            for komp, mnoznik in struktura[nazwa]:
                nowe_brutto = ilosc_do_produkcji * mnoznik
                zadania.append((komp, nowe_brutto, dzien_rozpoczecia))

if __name__ == "__main__":
    mrp()