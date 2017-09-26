import sys
import os


print("foldery robocze Python:", sys.path)
print("aktualny folder roboczy:", os.getcwd())

# podajac ścieżki pamiętać o znakach specjalnych - trzeba escape'ować
print("c:\torba")
print("c:\\torba")
print(r"c:\torba")