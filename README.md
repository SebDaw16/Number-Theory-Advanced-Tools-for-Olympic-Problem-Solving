# Number-Theory-Advanced-Tools-for-Olympic-Problem-Solving

Context

Number Theory Advanced Tools for Olympic Problem Solving (NTATOPS) is a tool that will help you in certain calculations for your Number Theory Problems. Sometimes there's not enough time to prove your hypothesis in a certain amount of time. This program will make some calculations easier. It won't solve the whole problem but it can help you determining advanced calculations that must be done in few time.

NTATOPS includes:
1. Determining whether a number is prime or not.
2. Determining the quadratic reciprocals of a number given a certain module.
3. Turning a given number into a selected base.
4. Descomposition of large numbers.
5. Residue Chinese Theorem given some modular equations.
6. Providing the gcd and the lcm of the given numbers.

NTATOPS will also provide interesting Number Theory Problems from Previous Olympiads for training. It will also have documents with the definitions of each section of the menu.

NTATOPS comes in five different languages: English, Spanish, German, French and Dutch.

Instructions (Algorithm):

NTATOPS will first ask the user which language prefers to use.
The options are English, Spanish, German, French and Dutch. 
The interphase will be in the language selected.

NTATOPS will deploy a menu in which there are the 6 tools, a section with interesting Number Theory problems and a section with definitions.

-If the 6 tools section is chosen. Then, a menu will be deployed in which it includes:
  -1. Determining whether a number is prime or not:
    The user will provide a number.
    NTATOPS will first search the nearest entire square root of the number given.
    Then it'll try to divide the number given by lower prime numbers.
    If one of the modular divisions is 0, then it's composite.
    Else is prime.
  -2. Determining the quadratic reciprocals of a number given a certain module.
    The user will provide a number.
    The user will provide a module.
    If the number and the module share divisors, then the user should try again.
    Else, calculate which number should be multiplied by the first number so that the module gives 1.
    Print number.
  -3. Turning a given number into a selected base.
    The user will provide a number.
    The user will provide a base.
    NTATOPS will use the Legendre symbol to transform the given number into the required base.
    Print number.
  -4. Descomposition of a large number.
    The user will provide a number.
    NTATOPS will use all the division properties to find each divisor of the number.
    NTATOPS will then express the number as its factorial descomposition and print it.
  -5. Residue Chinese Theorem given some modular equations.
    The user will provide some modular equations.
    NTATOPS will use the Residue Chinese Theorem to determine whether it has a solution or not.
    Print if it has a solution.
  -6. Providing the gcd and the lcm of the given numbers.
    The user will choose between two options: gcd or lcm.
    If the user chooses gcd, NTATOPS will ask for numbers.
    Then, NTATOPS will descompose the numbers, find the gcd and print it.
    If the user chooses lcm, NTATOPS will ask for numbers.
    Then, NTATOPS will search common multiples and print the least one.

  -If the section with interesting Number Theory Problems is selected:
   NTATOPS will provide files of problems coming from previous International Math Olympiad problems, IMO Shortlists and 
   Alexey Beshenov's problems.

  -If the section with definitions is selected:
   NTATOPS will provide files with definitions of certain Number Theory topics like Alexey Beshenov's quadratic reciprocals, Residue Chinese Theorem, divisibility, modules and prime numbers.

   In further editions of NTATOPS, it will be included Number Theory Functions such as Tau Function and Phi Function.
    

