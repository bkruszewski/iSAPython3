# ten sam efekt za pomocą while i for

wyraz = "abrakadabra"

# while
indeks = 0
while indeks < len(wyraz):
    print(indeks, wyraz[indeks].upper())
    indeks += 1

# for z indeksem
indeks = 0
for c in wyraz:
    print(indeks, c)
    indeks += 1

# for z enumerate()
for i, l in enumerate(wyraz):
    print(i, l)
