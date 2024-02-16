"""
    Ejercicio 1.
    Eres un profesor y deseas crear un programa en Python para evaluar las calificaciones de los estudiantes. El programa debe solicitar al usuario que ingrese su calificación como un número decimal. Luego, debe mostrar un mensaje que refleje su rendimiento de acuerdo con ciertos criterios:


        1. Si la calificación es igual o mayor a 90, mostrar "¡Felicidades! Has aprobado con una calificación sobresaliente."

        2. Si la calificación es igual o mayor a 70 pero menor que 90, mostrar "Has aprobado satisfactoriamente."

        3. Si la calificación es igual o mayor a 60 pero menor que 70, mostrar "Has aprobado, pero necesitas mejorar un poco."

        4. Si la calificación es menor que 60, mostrar "Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación."
"""
nombre = "generico"

print("Hola soy el profesor " + nombre + " y te voy a evaluar")
print("¿Cual es tu calificación del 0 al 100?")

calificacion = float(input())

if(calificacion >= 90):
    print("¡Felicidades! Has aprobado con una calificación sobresaliente.")

elif(calificacion >= 70 and calificacion < 90):
    print("Has aprobado satisfactoriamente.")

elif(calificacion >=60 and calificacion < 70):
    print("Has aprobado, pero necesitas mejorar un poco.")

else:
    print("Lo siento, has suspendido. Debes esforzarte más en la próxima evaluación.")
    
print("Tu calificación fue: " + str(calificacion))