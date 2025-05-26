def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio  # Encontrado
        elif lista[medio] < objetivo:
            izquierda = medio + 1  # Buscar en la mitad derecha
        else:
            derecha = medio - 1  # Buscar en la mitad izquierda

    return -1  # No encontrado

# Ejemplo de uso
if __name__ == '__main__':
    numeros = [3, 8, 15, 16, 23, 42]
    valor_a_buscar = 15

    resultado = busqueda_binaria(numeros, valor_a_buscar)

    if resultado != -1:
        print(f"El número {valor_a_buscar} se encontró en la posición {resultado}.")
    else:
        print(f"El número {valor_a_buscar} no está en la lista.")
