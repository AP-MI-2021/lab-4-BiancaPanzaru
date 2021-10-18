def CitireLista():
    lst=[]
    givenString=input("Dati lista, cu elementele separate prin virgula: ")
    numberAsString=givenString.split(",")
    for x in numberAsString:
        lst.append(int(x))
    return lst


def is_Prime(x):
    """
    Determina daca un numar este prim
    :param x: numar intreg
    :return: True, daca x este un numar prim sau False, in caz contrar
    """
    if x < 2:
        return False
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def test_is_Prime():
    assert is_Prime(2) is True
    assert is_Prime(17) is True
    assert is_Prime(15) is False


def eliminareNrPrime(lst):
    """
    Eliminare numere prime din lista
    :param lst: lista cu numere intregi
    :return: lista dupa stergerea numerelor prime
    """
    newlst1 = []
    for i in lst:
        if is_Prime(i) is False:
            newlst1.append(i)
    return newlst1

def test_eliminareNrPrime():
    assert eliminareNrPrime([8,18,7,8,5]) == [8,18,8]
    assert eliminareNrPrime([8,9,6,5,3]) == [8,9,6]

def mediaAritmetica(lst):
    """
    Determina media aritmetica a numerelor din lista
    :param lst: lista cu nr. intregi
    :return: media aritmetica a numerelor
    """
    sum = 0
    for i in lst:
        sum = sum + i
    return float(sum / len(lst))

def test_Aritmetica():
    assert mediaAritmetica([2,3,5,6]) == 4.0
    assert mediaAritmetica([2,5]) == 3.5

def nrDivizori(x):
    """
    Determina nr de divizori propprii ai lui x
    :param x: numarul intreg
    :return: numarul de divizori proprii
    """
    d = 0
    for i in range (2, x//2+1):
        if x % i == 0:
            d = d + 1
    return d

def test_nrDiv():
    assert nrDivizori(16) == 3
    assert nrDivizori(2) == 0

def inseraredivizoriinLista(lst):
    """
    Dupa fiecare nr din lista va fi inserat numarul sau de divizori
    :param lst: lista cu numere intregi
    :return: lista modificata
    """
    newlst=[]
    for x in lst:
        newlst.append(x)
        newlst.append(nrDivizori(x))
    return newlst

def test_inserare():
    assert inseraredivizoriinLista([2,3,4]) == [2,0,3,0,4,1]
    assert inseraredivizoriinLista([19,5,24,12,9]) == [19, 0, 5, 0, 24, 6, 12, 4, 9, 1]

def aparitii(lst, n):
    """
    Determina numarul de aparitii ale elementului n in lista
    :param lst: lista cu numere intregi
    :param n: numar intreg
    :return: numarul de aparitii
    """
    nr = 0
    for i in lst:
        if i == n:
            nr = nr + 1
    return nr

def test_aparitii():
    assert aparitii([2,3,4,5,4,1],4) == 2


def printMenu():
    print("1. Citire lista")
    print("2. Afișarea listei după eliminarea numerelor prime din listă")
    print("3. Să se afișeze dacă media aritmetică a numerelor este mai mare decât un număr n dat.")
    print("4. Afișarea listei obținută prin adăugarea după fiecare element numărul de divizori proprii ai elementului")
    print("x.Iesire")


def main():
    lst=[]
    while True:
        printMenu()
        optiune = input("Alegeti optiune: ")
        if optiune == "1":
            lst=CitireLista()
        elif optiune == "2":
            print(eliminareNrPrime(lst))
        elif optiune == "3":
            n=int(input("Dati numarul: "))
            if mediaAritmetica(lst) > n:
                print("DA")
            else:
                print("NU")
        elif optiune == "4":
            print(inseraredivizoriinLista(lst))
        elif optiune == "x":
            break
        else:
            print("Optiune invalida. Reincercati!")

if __name__ == "__main__":
    test_is_Prime()
    test_eliminareNrPrime()
    test_Aritmetica()
    test_nrDiv()
    test_inserare()
    test_aparitii()
    main()