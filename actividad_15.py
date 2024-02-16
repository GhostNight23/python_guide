"""
    Ejercicio 5.
    En este ejercicio, los estudiantes deben crear un programa en Python que verifique si una palabra ingresada por el usuario está 
    presente en una tupla predefinida de palabras. El programa debe informar al usuario si la palabra está o no en la tupla.
"""

palabras = ("manzana","uva","naranja","pera","coco")

print("Coloque una palabra")
palabra_buscar = input()

if(palabra_buscar in palabras):
    print("La palabra está en la tupla.")
else:
    print("La palabra no está en la tupla.")