import os

import sys
from PIL import Image


# folder = r"c:\fotki"
# root = "obrazek"
# nowa_szer = 800

def resize(root, nowa_szer):

    folder = os.getcwd()

    for nr, foto in enumerate(os.listdir(folder)):

        # oddzielamy rozszerzenie
        ext = os.path.splitext(foto)[1]

        # jesli rozszerzenie nie jest zdjeciem to kolejny plik
        if ext.lower() not in ["png", "jpg", "jpeg", "bmp"]:
            continue

        zdjecie = Image.open(os.path.join(folder, foto))

        # obliczamy proporcje i obliczamy nową wysokość
        ratio = zdjecie.width / zdjecie.height
        nowa_wys = round(nowa_szer / ratio)

        # tworzymy zdjęcie ze zmienionym rozmiarem
        male_foto = zdjecie.resize((nowa_szer, nowa_wys))

        # tworzymy nową nazwę zdjęcia
        nowy_plik = f"{root}{nr + 1}.{ext}"

        # zapisujemy zmienione zdjęcie
        male_foto.save(os.path.join(folder, nowy_plik))

        zdjecie.close()

def main():

    if len(sys.argv) != 3:
        print("Użycie:\npython resize_photo.py nazwa szerokosc")
        print("nazwa - wspólny człon dla plików, szerokość - nowa szerokość")
        print("Zdjęcie zostanie przeskalowane odpowiednio")

    root = sys.argv[1].strip()
    nowa_szer = sys.argv[2].strip()

    resize(root, nowa_szer)

if __name__ == '__main__':
    main()