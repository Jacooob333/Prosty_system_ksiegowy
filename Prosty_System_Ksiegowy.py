saldo_komisu_rowerowego = 10000.0
historia = []

magazyn_komisu = [
    {
        "nazwa_roweru": "Giant Roam 4 Disc",
        "rok_produkcji": 2020,
        "ilosc_dostepnych_egzemplarzy": 3,
        "cena_zakupu": 1200.0
    },
    {
        "nazwa_roweru": "Giant Talon",
        "rok_produkcji": 2022,
        "ilosc_dostepnych_egzemplarzy": 5,
        "cena_zakupu": 1600.0
    },
    {
        "nazwa_roweru": "Monteria massive",
        "rok_produkcji": 2019,
        "ilosc_dostepnych_egzemplarzy": 4,
        "cena_zakupu": 800.0
    },
    {
        "nazwa_roweru": "Maxim mc",
        "rok_produkcji": 2021,
        "ilosc_dostepnych_egzemplarzy": 2,
        "cena_zakupu": 900.0
    },
    {
        "nazwa_roweru": "Roomet rambler",
        "rok_produkcji": 2024,
        "ilosc_dostepnych_egzemplarzy": 10,
        "cena_zakupu": 1050.0
    },
]

while True:
    print("Witaj drogi użytkowniku w programie do zarządzania komisem rowerowym!")
    wyb_uzyt = input("Proszę podać jedną z podanych komend:\n"
                     "1. Zmiana salda komisu.\n"
                     "2. Sprzedaż Roweru.\n"
                     "3. Zakup Roweru do magazynu.\n"
                     "4. Sprawdzenie stanu konta komisu.\n"
                     "5. Całkowity stan magazynu.\n"
                     "6. Szczegóły produktu.\n"
                     "7. Historia działań programu.\n"
                     "8. Zakończenie działania programu!\n")

    if wyb_uzyt in ("1", "Zmiana salda komisu"):
        kwota = float(input("Proszę podać kwotę, o jaką zamierzasz zmienić saldo komisu: "))
        if saldo_komisu_rowerowego + kwota < 0:
            print("Niestety środki na koncie są niewystarczające!")
            historia.append("Wyjęcie z konta zbyt dużej kwoty.")
        else:
            saldo_komisu_rowerowego += kwota
            historia.append(f"Saldo komisu zostało zmienione o {kwota}")

    elif wyb_uzyt in ("2", "Sprzedaż Roweru"):
        nazwa_roweru = input("Proszę podać pełną nazwę roweru, którego masz zamiar zakupić z magazynu:")
        rok_produkcji = int(input("Proszę podać rok produkcji roweru, którego masz zamiar zakupić z magazynu:"))
        znaleziono_rower = False
        for rower in magazyn_komisu:
            if rower.get("nazwa_roweru") == nazwa_roweru and rower.get("rok_produkcji") == rok_produkcji:
                if rower.get("ilosc_dostepnych_egzemplarzy") >= 1:
                    rower["ilosc_dostepnych_egzemplarzy"] -= 1
                    saldo_komisu_rowerowego += rower.get("cena_zakupu")
                    print(f"Właśnie zakupiłeś rower {nazwa_roweru}!")
                    historia.append(f"Został zakupiony rower {nazwa_roweru} z magazynu komisu!")
                else:
                    print("Na ten moment podany rower jest całkowicie niedostępny! Proszę wrócić w innym terminie lub wybrać inny rower!")
                    historia.append(f"Próba zakupu roweru, lecz brak go na stanie!")
                znaleziono_rower = True
                break
        if not znaleziono_rower:
            print("Nie posiadamy takiego roweru!")
            historia.append("Próba zakpu roweru, którego nie mieliśmy w komisie!")

    elif wyb_uzyt in ("3", "Zakup Roweru do magazynu"):
        nazwa_roweru = input("Proszę podać pełną nazwę roweru, którego masz zamiar zakupić do magazynu:")
        rok_produkcji = int(input("Proszę podać rok produkcji roweru, którego masz zamiar zakupić do magazynu:"))
        ilosc_dostepnych_egzemplarzy = int(input("Proszę podać ilość rowerów, które masz zamiar zakupić do magazynu:"))
        cena_zakupu = int(input("Proszę podać cenę zakupu roweru, którego masz zamiar zakupić do magazynu:"))

        if ilosc_dostepnych_egzemplarzy * cena_zakupu > saldo_komisu_rowerowego:
            print("Komis nie stać na wybrany zakup!")
            historia.append(f"Próba zakupu rowerów, przez komis lecz nie starczyło środków na tranzakcje!")

            continue
        magazyn_komisu.append({
            "nazwa_roweru": nazwa_roweru,
            "rok_produkcji": rok_produkcji,
            "ilosc_dostepnych_egzemplarzy": ilosc_dostepnych_egzemplarzy,
            "cena_zakupu": cena_zakupu

        })
        saldo_komisu_rowerowego -= ilosc_dostepnych_egzemplarzy * cena_zakupu
        historia.append(f"Pomyślne zakupienie roweru/rowerów przez komis!")

    elif wyb_uzyt in ("4", "Sprawdzenie stanu konta komisu"):
        print(saldo_komisu_rowerowego)

    elif wyb_uzyt in ("5", "Całkowity stan magazynu"):
        for rower in magazyn_komisu:
            print(rower)

    elif wyb_uzyt in ("6", "Szczegóły produktu"):
        wybrany_rower = input("Podaj proszę nazwę roweru do wyszukania z magazynu: ")
        znaleziono_rower = False
        for rower in magazyn_komisu:
            if rower.get("nazwa_roweru") == wybrany_rower:
                print(rower)
                znaleziono_rower = True
                break
        if not znaleziono_rower:
            print("Nie posiadamy takiego roweru!")

    elif wyb_uzyt in ("7", "Historia działań programu"):
        od = input("Proszę podaj początkowy zakres historii działań: ")
        do = input("Proszę podaj końcowy zakres historii działań: ")

        if not od:
            od = 0
        else:
            od = int(od)
        if not do:
            do = len(historia)
        else:
            do = int(do)

        if od < 0 or do > len(historia) or od >= do:
            print(f"Wpisałeś niepoprawny zakres historii działań! Liczba działań wykonanych to: {len(historia)}")
        else:
            print("Lista wykonanych zadań:")
            for wyk in range(od, do):
                print(f"{wyk}: {historia[wyk]}")



    elif wyb_uzyt in ("8", "Zakończenie działania programu"):
        break

    else:
        print("Nie ma takiej komendy!!!")