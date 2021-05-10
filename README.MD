# InterCity Ticket Manager ( polish only )
to skrypt w `Pythonie`, który ma ułatwić podrójącym zarządzanie miejscówkami do biletów okresowych. Początkowo miał być wyłącznie do użytku własnego, jednak z czasem postanowiłem go udostępnić.
> Zaleca się sprawdzenie zgodności nazwy z tym co jest napisane na bilecie. Program był testowany jednak nie zmienia to faktu, że w takich kwestiach zalecana jest ostrożność.

## Po co? Co to robi?
Z powodu wprowadzenia obowiązku rezerwacji miejsca do biletów okresowych musiałem poświęcić kilkanaście minut, aby nabyć wszystkie bilety. Do tego przed odjazdem musiałem sprawdzać czy posiadam odpowiedni bilet i przy kontroli szukać go w plikach na telefonie. Skrypt przygotowany przeze mnie przyda się osobom, które bilety trzymają w plikach na urządzeniu mobilnym i chcą mieć do nich wygodny dostęp. Kompaktowy format plików pozwala na natychmiastowe odczytanie najważniejszych informacji: daty, czasu odjazdu i miejsca. Proste, a jednak może komuś ułatwić życie.

## Poradnik
- Umieść pliki z biletami ( nie zmieniaj ich nazw ) w folderze `tickets/`
- Uruchom dowolną konsolę `pythona` i zainstaluj pdfplumber komendą `pip install pdfplumber` (potrzebny do obsługi plików pdf)
- Uruchom `bilet.py` komendą `py bilet.py` lub `python3 bilet.py`
- W folderze z plikiem `bilet.py` powinny znajdować się wszystkie przerobione bilety

## Uwaga
Nie ponosze odpowiedzialności za wszelkie konsekwencje i błędy powstałe w wyniku wadliwego działa skryptu. Autor dołożył wszelkich starań i testował skrypt, jednak nie jest on idelany. Skrypt używany jest przez autora i stara się on dokładać wszelkich starań w celu ich wyeliminowania.

## Błędy i pytania
Proszę proszę kierować na adres `maciekcx11@outlook.com`. Za wszelką pomoc z góry dziękuję.

### Format biletów
- Miejscówka ( dodatkowy ) : dod_D-(MSCDZIEŃ)--T-(GODZ)--M--(MIEJSCE)-(WAGON).pdf
- Miesięczny: mie_od_(WAŻNY OD)-do_(WAŻNY DO).pdf
