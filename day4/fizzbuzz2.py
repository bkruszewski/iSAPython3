# drukuj liczby od 1 do 100
# jesli podzielna przez 3 drukuj Fizz
# jesli podzielna przez 5 drukuj Buzz
# jesli podzielna przez 3 i 5 drukuj FizzBuzz

# to jest druga możliwość
# tutaj używamy continue

for i in range(1,101):
    if i % 3 == 0 and i %5 ==0:
        print('FizzBuzz')
        continue
    if i % 3 == 0:
        print('Fizz')
        continue
    if i % 5 == 0:
        print('Buzz')
        continue
    print(i)

# zadanie w domu pozbyc sie jednego ifa

# napisać FizzBuzz z użyciem while




