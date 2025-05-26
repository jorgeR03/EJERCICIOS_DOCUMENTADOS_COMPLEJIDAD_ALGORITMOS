#Realizar un algoritmo para encontrar el valor mínimo en una lista

def encontrarMIn(lista):    #1 -> Inicializar variable minimo 
    minimo = lista[0]
    for numero in lista:    #2 -> Recorrer lista 
        if numero < minimo: #3 -> Validar si numero actual < minimo actual 
            minimo = numero #4 -> Actualizar el valor para minimo
    return minimo           #5 -> Retornar el valor minimo de la lista. 
print("El numero de ls lista es"(encontrarMIn));