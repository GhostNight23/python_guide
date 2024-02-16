"""
    Ejercicio 2.
    Escribe un programa Python que solicite al usuario ingresar un número entero y luego determine en qué rango se encuentra ese número 
    utilizando la declaración match. El programa debe imprimir un mensaje que indique el rango al que pertenece el número.

        1.   Pídele al usuario que ingrese un número entero.

        2.  Utiliza la declaración match para clasificar el número en uno de los siguientes rangos:

            Rango 1: Números negativos (menores que 0).

            Rango 2: Números entre 0 (incluido) y 10 (excluido).

            Rango 3: Números mayores o iguales a 10.

    3.  Imprime un mensaje que indique en qué rango se encuentra el número ingresado.
"""

print("Escribe un numero entero")
numero = int(input())

match numero:
    case numero if(numero < 0):
        print(f"{numero} es menor que 0")
    case numero if(numero >=0 and numero<=10):
        print(f"{numero} esta entre 0 y 10")
    case numero if(numero >=10):
        print(f"{numero} es mayor a 10")