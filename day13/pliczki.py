import shutil, os, send2trash

print(shutil.disk_usage('.'))

print("\nJestem w: ", end='')
print(os.getcwd())

# os.mkdir("./moj_folder")

#shutil.copytree("c:\\folder", "c:\\folder2")

# os.unlink("aaa.txt")

# os.rmdir("./moj_folder")

# for element in os.listdir():
#     print(element)

for biezacy_folder, podfoldery, pliki in os.walk("../"):
    # print(f"Obecny folder: {biezacy_folder}")
    #
    # for podfolder in podfoldery:
    #     print(f"Podfolder {podfolder} wew. {biezacy_folder}")

    for plik in pliki:
        print(os.path.abspath(plik))
        # print(f"Plik {plik} wew. folderu {biezacy_folder}")





