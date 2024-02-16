#En este código aprenderemos el manejo de otra estructura de control, el ciclo for. Este se caracteriza por las repeticiones con final predefinido.

frutas = ['manzana', 'pera', 'uva']
contador = 0

#Bucle for que itera sobre la lista de frutas
for fruta in frutas:
    contador += 1
    print(f"fruta #{contador}: {fruta}")