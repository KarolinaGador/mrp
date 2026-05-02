import math


dane_produkcji = {
    "Stół":  {"czas": 1, "magazyn": 0, "zapas": 0, "wielkosc_partii": 1},
    "Blat":  {"czas": 2, "magazyn": 5, "zapas": 2, "wielkosc_partii": 1},
    "Noga":  {"czas": 1, "magazyn": 10, "zapas": 4, "wielkosc_partii": 4}
}


struktura = {
    "Stół": [("Blat", 1), ("Noga", 4)]
}

def mrp():
   
    ile = int(input("Ile stołów chcesz wyprodukować? "))
    dzien_oddania = int(input("Na który dzień mają być gotowe?(liczba) "))
    zadania = [("Stół", ile, dzien_oddania)]
    print("\nELEMENT | BRUTTO | NETTO | PRODUKCJA | START | KONIEC")
    
    while zadania:
        
        nazwa, zapotrzebowanie_brutto, termin_zakonczenia = zadania.pop(0)
        info = dane_produkcji[nazwa]
        dostepne_w_magazynie = max(0, info["magazyn"] - info["zapas"])
        zapotrzebowanie_netto = max(0, zapotrzebowanie_brutto - dostepne_w_magazynie)
        ilosc_do_produkcji = math.ceil(zapotrzebowanie_netto / info["wielkosc_partii"]) * info["wielkosc_partii"]
        dzien_rozpoczecia = termin_zakonczenia - info["czas"]

        
        print(nazwa, "|", zapotrzebowanie_brutto, "|", zapotrzebowanie_netto, "|", ilosc_do_produkcji, "|", dzien_rozpoczecia, "|", termin_zakonczenia)

        
        if nazwa in struktura and ilosc_do_produkcji > 0:
            for komp, mnoznik in struktura[nazwa]:
                nowe_brutto = ilosc_do_produkcji * mnoznik
                
                zadania.append((komp, nowe_brutto, dzien_rozpoczecia))

if __name__ == "__main__":
    mrp()
