#NTATOPS English, Inglés, Anglais, Englisch, Engels, Bahasa Inggris
import math
#Download sympy as pip install sympy
from sympy import gcd, lcm

def menuLanguage():
    print("Choose a language: ")
    print("1. English")
    print("2. Spanish")
    print("3. German")
    print("4. French")
    print("5. Dutch")

def main():
    menuLanguage()
    opt=int(input())
    if opt==1:
        #English
        mainEng()
    elif opt==2:
        #Español
        #mainEsp()
        2
    elif opt==3:
        #Deutsch
        #mainDeu()
        3
    elif opt==4:
        #Français
        #mainFra()
        4
    elif opt==5:
        #Nederlands
        #mainNed()
        5
    else:
        return print("Input a valid option from 1 to 5")
        
def menuEnglish():
    print("Choose an option: ")
    print("1. Number Theory Advanced Tools for Olympic Problem Solving")
    print("2. Interesting Number Theory Olympic Problems")
    print("3. Number Theory Definitions")

def mainEng():
    menuEnglish()
    opt1E=int(input())
    if opt1E==1:
        mainEng1()
    elif opt1E==2:
        "2"
    elif opt1E==3:
        "3"
    else:
        return print ("Input a valid option from 1 to 3")
#1
def prime_numberEng(prime1E):
    if prime1E==1:
        print(f"Number {prime1E} is not prime")
        return
    else:
        for i in range(2, int(math.sqrt(prime1E))+1):
            if prime1E%i==0:
                print(f"Number {prime1E} is not prime")
                return
            else:
                print(f"Number {prime1E} is prime")
                return
#2
def quadratic_reciprocalsEng(number1E, module1E):
    solutionsEng=[]    
    inverse1E=None
    for x in range(1, module1E):
        if (number1E*x)%module1E==1:
            inverse1E=x
            break
    if inverse1E is None:
        print(f"{number1E} has no modular inverse module {module1E}.")
        return
    print(f"The modular inverse of {number1E} module {module1E} is {inverse1E}.")
    for x in range(module1E):
        if (x*x)%module1E==inverse1E:
            solutionsEng.append(x)
    if solutionsEng:
        print(f"Quadratic reciprocals: {solutionsEng}")
    else:
        print("There are no quadratic reciprocals.")
#3
def number_to_baseEng(number2E, base1E):
    digitsE="0123456789"
    result1E=""
    while number2E>0:
        remainder=number2E%base1E
        result1E=digitsE[remainder]+result1E
        number2E=number2E//base1E
    return print(f"Number {number2E} in base {base1E}: {result1E}")
#4
def descomposition_numbersEng(number3E):
    factorsE=[]
    divisorE=2
    while number3E>1:
        if number3E%divisorE==0:
            factorsE.append(str(divisorE))
            number3E//=divisorE   
        else:
            divisorE=divisorE+1
    result2E=" * ".join(factorsE )
    return result2E
#5
def chineseTheoremEng(equationsE):
    M_E=1
    for equation in equationsE:
        M_E=M_E*equation[1]
    x=0
    for equation in equationsE:
        a_E=equation[0]
        m_E=equation[1]
        M_k=M_E//m_E
        inverse2E=0
        for i in range(1, m_E):
            if (M_k*i)%m_E==1:
                inverse2E=i
                break
        x=x+a_E*M_k*inverse2E
    return x%M_E
#6
def gcd_and_lcmEng(number4E, number5E):
    print(f"gcd({number4E}, {number5E})={gcd(number4E, number5E)}")
    print(f"lcm({number4E}, {number5E})={lcm(number4E, number5E)}")

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
    opt2E=int(input())
    if opt2E==1:
        prime1E=int(input("Provide a number to calculate whether it is prime or not (between 1 and 10000): "))
        if prime1E<1 or prime1E>10000:
            print("Input a number between 1 and 10000.")
            return
        else:
            prime_numberEng(prime1E)
    elif opt2E==2:
        number1E=int(input("Enter the number: "))
        module1E=int(input("Enter the module: "))
        if number1E<2 or module1E<2:
            print("Input a number greater than 1 for both the number and the module.")
            return
        else:
            quadratic_reciprocalsEng(number1E, module1E)
    elif opt2E==3:
        number2E=int(input("Enter the number: "))
        base1E=int(input("Enter the base (2-10): "))
        if number2E<1 or base1E<2 or base1E>10:
            print("Input a non-negative number and a base between 2 and 10.")
            return
        else:
            number_to_baseEng(number2E, base1E)
    elif opt2E==4:
        number3E=int(input("Enter the number: "))
        if number3E<2:
            print("Input a number greater than 1.")
            return
        else:
            result2E=descomposition_numbersEng(number3E)
            print(f"{number3E}={result2E}")
    elif opt2E==5:
        n_E=int(input("How many equations? "))
        if n_E<1:
            print("Input a number greater than 0.")
            return
        else:
            equationsE=[]
            for i in range(n_E):
                print("Equation", i+1)
                a_E=int(input("Remainder: "))
                m_E=int(input("Modulo: "))
                equationsE.append([a_E, m_E])
            result2E=chineseTheoremEng(equationsE)
            print("The solution is:", result2E)
    elif opt2E==6:
        number4E=int(input("Enter the first number: "))
        number5E=int(input("Enter the second number: "))
        if number4E<2 or number5E<2:
            print("Input a number greater than 1 for both numbers.")
            return
        else:
            gcd_and_lcmEng(number4E, number5E)
    else:
        return print ("Input a valid option from 1 to 6")
