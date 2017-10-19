import requests

def pobierz_foto(link, sciezka):

    response = requests.get(link)

    if response.status_code == 200:

        bajty = 0

        try:
            with open(sciezka, 'wb') as plik:
                for part in response.iter_content(100000):
                    ilosc = plik.write(part)
                    bajty += ilosc
        except FileNotFoundError:
            # tutaj tworzymy foldery
            bajty = 99999


    print(f"Zapisano {bajty} bajtów")


def main():
    link = "http://www.smiley.com/sites/default/files/BRAND_SMILEY_MAIN.jpg"
    pobierz_foto(link, "smiley.jpg")

if __name__ == "__main__":
    main()



