def odwroc_str(zdanie):
    return zdanie[::-1]

# print(odwroc_str("Stół z powyłamywanymi nogami"))

# mogę wykorzystać zdefiniowaną funkcję wewnątrz definicji innej funkcji
def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return odwroc_str(zdanie)

# print(odwroc_input())

