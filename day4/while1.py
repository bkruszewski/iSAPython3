# pętla while

# ta pętla będzie działać w nieskończoność, bo nie aktualizujemy
# warunku sprawdzanego przez while - jest on zawsze prawdziwy
# while True:
#     print(100)

# musimy sami zapewnić zmianę warunku while
stan = True
while stan:
    print(100)
    stan = False

liczba = 1

while liczba <= 100:
    print(liczba)
    liczba += 1
