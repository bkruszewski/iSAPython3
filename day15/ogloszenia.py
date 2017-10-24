from day15.ogloszenie import Ogloszenie
from bs4 import BeautifulSoup
import requests

adres = "https://www.otodom.pl/wynajem/mieszkanie/gdansk/?search[description]=1&search[dist]=0&search[district_id]=16"

# żadamy nasz adres
# odpowiedź serwera zapisujemy do zmiennej
response = requests.get(adres)

# sprawdzamy czy odpowiedź jest status 200
# jeśli nie to ta metoda wyrzuci wyjątek
response.raise_for_status()

# jeśli status jest ok, to program
# wykona kolejne linijki

# tworzymy zupę ;)
soup = BeautifulSoup(response.text, 'html.parser')

# print(response.text)

# za pomocą zupy wyszukujemy odpowiedni element
# znalezione elementy są w zmiennej
ads = soup.select(".offer-item-header a")

# z każdego ogłoszenia możemy wyszczególnić różne elementy
for ad in ads:
    print(ad)
    print(ad.getText())
    print(ad.get('href'))
    print("-------\n")
    # z każdego elementu tworzymy instancje naszej klasy Ogloszenie
    o = Ogloszenie(ad.getText(), ad.get("href"))
    print(o.opis)

# wszystkie ogłoszenia zapisujemy do pliku
Ogloszenie.zapisz_ogloszenia("ogloszenia.dat")
