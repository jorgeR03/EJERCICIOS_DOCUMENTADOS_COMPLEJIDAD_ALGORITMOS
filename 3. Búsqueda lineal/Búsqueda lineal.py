def busqueda_lineal(lista, objetivo):
    # Recorremos cada elemento de la lista
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  # Si encontramos el objetivo, devolvemos su posición
    return -1  # Si no lo encontramos, devolvemos -1

# Ejemplo de uso
if __name__ == '__main__':
    numeros = [4, 8, 15, 16, 23, 42]
    valor_a_buscar = 23

    resultado = busqueda_lineal(numeros, valor_a_buscar)

    if resultado != -1:
        print(f"El número {valor_a_buscar} se encontró en la posición {resultado}.")
    else:
        print(f"El número {valor_a_buscar} no está en la lista.")
