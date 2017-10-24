import os

from day14.downloads import pobierz_foto
from day15.ms_cv import get_pic_info
from day15.foto_opis import describe_picture

pics = [
'https://qph.ec.quoracdn.net/main-qimg-71e8b8cddfce751d8e0a8ed45b316731-c',
'https://i.pinimg.com/originals/7c/3a/ed/7c3aedde4dbf1c38e5d34a554a8cb4eb.jpg',
'http://cdn30.us1.fansshare.com/image/vladimirputin/vladimir-putin-walking-away-from-things-2125699510.jpg',
'http://s.eatthis-cdn.com/media/images/ext/543627202/happy-people-friends.jpg',
'http://ocdn.eu/jcmsprzegladsportowy-transforms/1/HpvktoATGh0dHA6Ly9vY2RuLmV1L2pjbXNwcnplZ2xhZHNwb3J0b3d5L2E2YTU1NDJlLThhYjMtNGNjNi1iZGUxLThiOTAyM2QwYzU5OS5qcGeRkwIAzQQa'
]

# utworzymy podfolder na zdjęcia jeśli nie istnieje
podfolder = ".//opisane_fotki"
if not os.path.exists(podfolder):
    os.mkdir(podfolder)

name_pattern = "{katalog}//pic{nr}.jpg"

# name_pattern = ".\opisane_fotki\pic{nr}.jpg"

for i, pic_url in enumerate(pics):

    img_saved = name_pattern.format(katalog= podfolder, nr= i + 1)
    print(f"-------- Zdjęcie {i + 1} ---------")
    print(f"Analizuję zdjęcie")
    img_data = get_pic_info(pic_url, img_saved)

    print(f"Pobieram zdjęcie")
    pobierz_foto(pic_url, img_saved)

    describe_picture(img_saved, img_data)
