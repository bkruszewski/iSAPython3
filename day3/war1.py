# if

# if True:
#     pass

x = 5
# y = int(input("podaj liczbe całkowitą: "))
y = input("podaj liczbe całkowitą: ")

# print(y)
# print(type(y))

if y.isnumeric():
    print("To jest liczba")

if x < int(y):
    print(f"{x} jest mniejsza od Twojej liczby")

    if int(y) > 10:
        print("Twoja liczba jest większa od 10")

print("koniec programu")