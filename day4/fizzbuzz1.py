# FizzBuzz
# drukuj liczby od 1 do 100
# jesli podzielna przez 3 drukuj Fizz
# jesli podzielna przez 5 drukuj Buzz
# jesli podzielna przez 3 i 5 drukuj FizzBuzz

# to jest jedno z możliwych rozwiązań
# zobacz plik fizzbuzz2.py aby zobaczyć inne

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


# zadanie do domu pozbyć się jednego sprawdzenia warunku!
