"""
    Ejercicio 3.
    Escribe un programa en Python que calcule el promedio de una lista de números. Debes seguir estos pasos:


        1. Crea una lista llamada numeros que contenga al menos cinco números enteros.

        2. Inicializa una variable llamada suma en 0.

        3. Utiliza un ciclo for para iterar a través de la lista numeros y suma cada número a la variable suma.

        4. Después del ciclo for, divide la variable suma entre la cantidad de números en la lista (que puedes obtener usando la función len(numeros)).

        5. Imprime el resultado como el promedio de los números en la lista.
"""

print("¿Cuantas calificaciones hay?")
cantidad = int(input())
calificaciones = []
promedio = 0


for contador in range(1, cantidad + 1):
    print(f"Ingrese la calificacion {contador}: ")
    calificacion = float(input())
    calificaciones.append(calificacion)
    promedio += calificacion

promedio = promedio / cantidad
print(f"El promedio de la clase fue: {promedio}")