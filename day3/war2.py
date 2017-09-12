# elif

x = int(input("podaj liczbę x: "))
y = int(input("podaj liczbę y: "))

if x == y:
    print("liczby są równe")

if x > 5:
    x += 1 # x = x + 1
    print("x jest równy", x)
elif x == 3:
    x *= 2
    print("x jest równy", x)

print("koniec programu")

