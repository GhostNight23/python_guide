"""
    Ejercicio 4.
    En esta tarea, se te pide crear un programa en Python que cuente desde 1 hasta un número límite ingresado por el usuario. 
    El programa debe utilizar un bucle while para llevar a cabo el conteo y mostrar los números en orden ascendente. 
    Una vez que se alcance el número límite, el programa debe imprimir "Conteo completado".
"""

print("Coloca el limite de tu conteo")
limite = int(input())

contador = 1

print("Inicia conteo")
while(contador <= limite):
    print(contador)
    contador += 1

print("Conteo completado")
