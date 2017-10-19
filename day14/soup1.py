import requests
from bs4 import BeautifulSoup

response = requests.get("http://trojmiasto.pl")

response.raise_for_status()
#
# with open("trojmiasto", "w", encoding="utf-8") as plik:
#     plik.write(response.text)

trojmiasto_zupa = BeautifulSoup(response.text, "html.parser")

linki = trojmiasto_zupa.select(".news-list a")
# print(linki)

for link in linki:
    # print(link.getText())
    # print(str(link))
    # print(link.attrs)

    print(f"Wiadomość: {link.get('title')}")
    print(link.get("href"))
    print("------------------\n")
