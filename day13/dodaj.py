import sys


def dodaj(a, b):
    return a + b


def main():

    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    print(dodaj(x, y))



if __name__ == '__main__':
    main()
