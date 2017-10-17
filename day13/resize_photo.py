import os
from PIL import Image


folder = r"c:\fotki"
root = "obrazek"
nowa_szer = 800

for nr, foto in enumerate(os.listdir(folder)):

    ext = os.path.splitext(foto)[1]

    zdjecie = Image.open(os.path.join(folder, foto))

    ratio = zdjecie.width / zdjecie.height

    nowa_wys = round(nowa_szer / ratio)

    male_foto = zdjecie.resize((nowa_szer, nowa_wys))

    nowy_plik = f"{root}{nr + 1}.{ext}"

    male_foto.save(os.path.join(folder, nowy_plik))

    zdjecie.close()


