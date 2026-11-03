def menu():
    print("Choose a language: ")
    print("1. English")
    print("2. Spanish")
    print("3. German")
    print("4. French")
    print("5. Dutch")

def main():
    menu()
    opt=int(input())
    if opt==1:
        "In English"
        mainEng()
    elif opt==2:
        "En Español"
        mainEsp()
    elif opt==3:
        "Auf Deutsch"
        mainDeu()
    elif opt==4:
        "En Français"
        mainFra()
    elif opt==5:
        "Op Nederlands"
        mainNed()
    else:
        return print("Input a valid option from 1 to 5")
        
def menuEng0():
    print("Choose an option: ")
    print("1. Number Theory Advanced Tools for Olympic Problem Solving")
    print("2. Interesting Number Theory Olympic Problems")
    print("3. Number Theory Definitions")

def mainEng():
    menuEng0()
    opt11=int(input())
    if opt11==1:
        menuEng1()
    elif opt11==2:
        "2"
    elif opt11==3:
        "3"
    else:
        return print ("Input a valid option from 1 to 3")

def menuEsp0():
    print("Escoge una opción: ")
    print("1. Herramientas Avanzadas de Teoría de Números para la Resolución de Problemas")
    print("2. Interesantes Problemas Olímpicos de Teoría de Números")
    print("3. Definiciones de Teoría de Números")

def mainEsp():
    menuEsp0()
    opt21=int(input())
    if opt21==1:
        menuEsp1()
    elif opt21==2:
        "2"
    elif opt21==3:
        "3"
    else:
        return print ("Escoge una opción válida entre 1 y 3")
    
def menuDeu0():
    print("Wählen Sie eine Option: ")
    print("1. Fortgeschrittene Werkzeuge für die Zahlentheorie zur Olympischen Problemlösung")
    print("2. Interessante Zahlentheorie Olympische Probleme")
    print("3. Zahlentheorie Definitionen")

def mainDeu():
    menuDeu0()
    opt31=int(input())
    if opt31==1:
        menuDeu1()
    elif opt31==2:
        "2"
    elif opt31==3:
        "3"
    else:
        return print ("Geben Sie eine gültige Option von 1 bis 3 ein")    

def menuFra0():
    print("Choisissez une option: ")
    print("1. Outils Avancés de Théorie des Nombres pour la Résolution de Problèmes Olympiques")
    print("2. Problémes Interessantes de Théorie des Nombres")
    print("3. Définitions de Théorie des Nombres")

def mainFra():
    menuFra0()
    opt41=int(input())
    if opt41==1:
        menuFra1()
    elif opt41==2:
        "2"
    elif opt41==3:
        "3"
    else:
        return print ("Entrez une option valide de 1 à 3")

def menuNed0():
    print("Kies een optie: ")
    print("1. Geavanceerde Tools voor het Oplossen van Olympische Problemen")
    print("2. Interessante Olympische Problemen met Getaltheorie")
    print("3. Definities van Getaltheorie")

def mainNed():
    menuNed0()
    opt51=int(input())
    if opt51==1:
        menuNed1()
    elif opt51==2:
        "2"
    elif opt51==3:
        "3"
    else:
        return print ("Voer een geldige optie in van 1 tot 3")

def menuEng1():
    print("Choose an option: ")
    print("1. Determine whether a number is prime or not.")
    print("2. Determining the quadratic reciprocals of a number given a certain module.")
    print("3. Turning a given number into a selected base.")
    print("4. Descomposition of large numbers.")
    print("5. Residue Chinese Theorem given some modular equations.")
    print("6. Providing the gcd and the lcm of the given numbers.")

def mainEng1():
    menuEng1()
    opt12=int(input())
    if opt12==1:
        prime1 = int(input("Provide a number to calculate whether it is prime or not (between 1 and 10000): "))
        prime_numberEng(prime1)

"""
Algorithm for prime_number function:
First, ask for an integer between 1 and 10,000.
Then descart number 1 and the prime numbers from 2 to 97.
Then descart the multiples of the prime numbers from 2 to 97.
Print whether is prime or not.
"""

def prime_numberEng(prime1):
    if prime1<1 or prime1>10000:
        print("Input a number between 1 and 10000.")
        return

    if prime1==1:
        print(f"Number {prime1} is not prime")
        return

    if prime1 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print(f"Number {prime1} is prime")
        return

    if (prime1%2==0 or prime1%3==0 or prime1%5==0 or prime1%7==0 or prime1%11==0 or prime1%13==0 or
        prime1%17==0 or prime1%19==0 or prime1%23==0 or prime1%29==0 or prime1%31==0 or prime1%37==0 or
        prime1%23==0 or prime1%29==0 or prime1%31==0 or prime1%37==0 or prime1%41==0 or prime1%43==0 or
        prime1%47==0 or prime1%53==0 or prime1%59==0 or prime1%61==0 or prime1%67==0 or prime1%71==0 or
        prime1%73==0 or prime1%79==0 or prime1%83==0 or prime1%89==0 or prime1%97==0):
        print(f"Number {prime1} is not prime")
    else:
        print(f"Number {prime1} is prime")

prime_numberEng(prime1)

def prime_numberEsp(prime2):
    if prime2<1 or prime2>10000:
        print("Escribe un número entre 1 y 10000.")
        return

    if prime2==1:
        print(f"El número {prime2} no es primo")
        return

    if prime2 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print(f"El número {prime2} es primo")
        return

    if (prime2%2==0 or prime2%3==0 or prime2%5==0 or prime2%7==0 or prime2%11==0 or prime2%13==0 or
        prime2%17==0 or prime2%19==0 or prime2%23==0 or prime2%29==0 or prime2%31==0 or prime2%37==0 or
        prime2%23==0 or prime2%29==0 or prime2%31==0 or prime2%37==0 or prime2%41==0 or prime2%43==0 or
        prime2%47==0 or prime2%53==0 or prime2%59==0 or prime2%61==0 or prime2%67==0 or prime2%71==0 or
        prime2%73==0 or prime2%79==0 or prime2%83==0 or prime2%89==0 or prime2%97==0):
        print(f"El número {prime2} no es primo")
    else:
        print(f"El número {prime2} es primo")

prime_numberEsp(prime2)

def prime_numberDeu(prime3):
    if prime3<1 or prime3>10000:
        print("Geben Sie eine Zahl zwischen 1 und 10000 ein.")
        return

    if prime3==1:
        print(f"Zahl {prime3} ist keine Primzahl")
        return

    if prime3 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print(f"Zahl {prime3} ist eine Primzahl")
        return

    if (prime3%2==0 or prime3%3==0 or prime3%5==0 or prime3%7==0 or prime3%11==0 or prime3%13==0 or
        prime3%17==0 or prime3%19==0 or prime3%23==0 or prime3%29==0 or prime3%31==0 or prime3%37==0 or
        prime3%23==0 or prime3%29==0 or prime3%31==0 or prime3%37==0 or prime3%41==0 or prime3%43==0 or
        prime3%47==0 or prime3%53==0 or prime3%59==0 or prime3%61==0 or prime3%67==0 or prime3%71==0 or
        prime3%73==0 or prime3%79==0 or prime3%83==0 or prime3%89==0 or prime3%97==0):
        print(f"Zahl {prime3} ist keine Primzahl")
    else:
        print(f"Zahl {prime3} ist keine Primzahl")

prime_numberDeu(prime3)

def prime_numberFra(prime4):
    if prime4<1 or prime4>10000:
        print("Entrez un nombre entre 1 et 10000.")
        return

    if prime4==1:
        print(f"Le nombre {prime4} n'est pas un premier")
        return

    if prime4 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print(f"Le nombre {prime4} est premier")
        return

    if (prime4%2==0 or prime4%3==0 or prime4%5==0 or prime4%7==0 or prime4%11==0 or prime4%13==0 or
        prime4%17==0 or prime4%19==0 or prime4%23==0 or prime4%29==0 or prime4%31==0 or prime4%37==0 or
        prime4%23==0 or prime4%29==0 or prime4%31==0 or prime4%37==0 or prime4%41==0 or prime4%43==0 or
        prime4%47==0 or prime4%53==0 or prime4%59==0 or prime4%61==0 or prime4%67==0 or prime4%71==0 or
        prime4%73==0 or prime4%79==0 or prime4%83==0 or prime4%89==0 or prime4%97==0):
        print(f"Le nombre {prime4} n'est pas premier")
    else:
        print(f"Le nombre {prime4} est premier")

prime_numberFra(prime4)

def prime_numberNed(prime5):
    if prime5<1 or prime5>10000:
        print("Voer een getal in tussen 1 en 10000.")
        return

    if prime5==1:
        print(f"Getal {prime5} is geen priemgetal")
        return

    if prime5 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        print(f"Getal {prime5} is een priemgetal")
        return

    if (prime5%2==0 or prime5%3==0 or prime5%5==0 or prime5%7==0 or prime5%11==0 or prime5%13==0 or
        prime5%17==0 or prime5%19==0 or prime5%23==0 or prime5%29==0 or prime5%31==0 or prime5%37==0 or
        prime5%23==0 or prime5%29==0 or prime5%31==0 or prime5%37==0 or prime5%41==0 or prime5%43==0 or
        prime5%47==0 or prime5%53==0 or prime5%59==0 or prime5%61==0 or prime5%67==0 or prime5%71==0 or
        prime5%73==0 or prime5%79==0 or prime5%83==0 or prime5%89==0 or prime5%97==0):
        print(f"Getal {prime5} is geen priemgetal")
    else:
        print(f"Getal {prime5} is een priemgetal")

prime_numberNed(prime5)

"""
Algorithm for quadratic reciprocals
First, we ask for the numbers
Secondly, we create an empty list for x
We search a x between the range of the module to search a quadratic reciprocal
Then we prove that it exists
"""
number = int(input("Enter the number: "))
module = int(input("Enter the module: "))

def quadratic_reciprocalsEng(a, m):
    solutions = []    
    inverse = None

    for x in range(1, m):
        if (a*x)% m == 1:
            inverse=x
            break

    if inverse is None:
        print(f"{a} has no modular inverse module {m}.")
        return

    print(f"The modular inverse of {a} module {m} is {inverse}.")

    for x in range(m):
        if (x*x) % m == inverse:
            solutions.append(x)

    if solutions:
        print(f"Quadratic reciprocals: {solutions}")
    else:
        print("There are no quadratic reciprocals.")
quadratic_reciprocals(number, module)

def number_to_baseEng(number4, base):
    digits = "0123456789"
    result = ""

    while number4>0:
        remainder=number4%base
        result=digits[remainder]+result
        number=number//base

    return result


def base_mainEng():
    number=int(input("Enter a decimal number: "))
    base=int(input("Enter the base (2-10): "))

    if base<2 or base>10:
        print("Invalid base.")
    elif number==0:
        print("Result: 0")
    else:
        result=number_to_baseEng(number4, base)
        print("Result:", result)


base_mainEng()

def chineseTheorem(equations):
    M=1
    for equation in equations:
        M=M*equation[1]
    x=0
    for equation in equations:
        a=equation[0]
        m=equation[1]
        M_k=M//m
        inverse=0
        for i in range(1, m):
            if (M_k*i)%m==1:
                inverse=i
                break
        x=x+a*M_k*inverse
    return x%M
    
n=int(input("How many equations? "))
equations=[]
for i in range(n):
    print("Equation", i + 1)
    a=int(input("Remainder: "))
    m=int(input("Modulo: "))
    equations.append([a, m])
result=chineseTheorem(equations)
print("The solution is:", result)
