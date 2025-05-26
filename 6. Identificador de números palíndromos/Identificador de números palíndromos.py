def es_palindromo(numero):
    """
    Verifica si un número es palíndromo.

    Args:
        numero (int): El número a verificar.

    Returns:
        bool: True si es palíndromo, False en caso contrario.

    Ejemplo:
        es_palindromo(121) -> True
        es_palindromo(123) -> False
    """
    str_numero = str(numero)
    return str_numero == str_numero[::-1] # Compara la cadena con su inversa

def ejecutar_verificador_palindromo():
    """Prueba el identificador de palíndromos."""
    print("--- Verificador de Números Palíndromos ---")
    try:
        numero_ingresado = int(input("Introduce un número entero: "))
        if es_palindromo(numero_ingresado):
            print(f"El número {numero_ingresado} es palíndromo.")
        else:
            print(f"El número {numero_ingresado} no es palíndromo.")
    except ValueError:
        print("Entrada inválida. Introduce un número entero.")
    print("-" * 30)

# --- Punto 2: Removedor de duplicados en una lista ordenada ---
# Elimina duplicados de una lista ordenada, manteniendo el orden.

def eliminar_duplicados_lista_ordenada(lista_ordenada):
    """
    Elimina duplicados en una lista ordenada.

    Args:
        lista_ordenada (list): Lista ordenada.

    Returns:
        list: Nueva lista sin duplicados.

    Complejidad: Tiempo O(n), Espacio O(k) (k = elementos únicos).
    Ejemplo:
        eliminar_duplicados_lista_ordenada([1, 1, 2, 3, 3]) -> [1, 2, 3]
    """
    if not lista_ordenada:
        return []

    unicos = [lista_ordenada[0]] # Inicia con el primer elemento
    for i in range(1, len(lista_ordenada)):
        if lista_ordenada[i] != unicos[-1]: # Compara con el último único añadido
            unicos.append(lista_ordenada[i])
    return unicos

def ejecutar_eliminador_duplicados():
    """Prueba el eliminador de duplicados."""
    print("\n--- Eliminador de Duplicados en Lista Ordenada ---")
    lista_ejemplo = [1, 1, 2, 2, 2, 3, 4, 4, 5, 6, 6, 6]
    print(f"Lista original: {lista_ejemplo}")
    lista_filtrada = eliminar_duplicados_lista_ordenada(lista_ejemplo)
    print(f"Lista sin duplicados: {lista_filtrada}")
    print("-" * 30)

# --- Punto 3: Remover elementos de una lista ---
# Elimina todas las apariciones de un valor específico en una lista.

def remover_ocurrencias_de_lista(lista_nums, valor_a_eliminar):
    """
    Elimina todas las ocurrencias de 'valor_a_eliminar' en 'lista_nums'.

    Args:
        lista_nums (list): La lista de origen.
        valor_a_eliminar: El valor a eliminar.

    Returns:
        tuple: (cantidad_restante, nueva_lista_filtrada)

    Complejidad: Tiempo O(n), Espacio O(k) (k = elementos no eliminados).
    Ejemplo:
        remover_ocurrencias_de_lista([0, 1, 2, 2, 3], 2) -> (3, [0, 1, 3])
    """
    filtrada = [elem for elem in lista_nums if elem != valor_a_eliminar]
    return len(filtrada), filtrada

def ejecutar_removedor_elementos():
    """Prueba el removedor de elementos."""
    print("\n--- Removedor de Elementos de una Lista ---")
    nums_ejemplo = [0, 1, 2, 2, 3, 0, 4, 2]
    val_ejemplo = 2
    print(f"Lista original: {nums_ejemplo}, Valor a eliminar: {val_ejemplo}")
    k, lista_modificada = remover_ocurrencias_de_lista(nums_ejemplo, val_ejemplo)
    print(f"Elementos restantes: {k}, Lista modificada: {lista_modificada}")
    print("-" * 30)

# --- Punto 4: Combinaciones de letras con los números de un teléfono ---
# Genera combinaciones de letras de un teclado telefónico.

def combinaciones_letras_telefono(digitos_str):
    """
    Genera combinaciones de letras para dígitos telefónicos.

    Args:
        digitos_str (str): Cadena de dígitos (ej. "23").

    Returns:
        list: Lista de combinaciones de letras.

    Complejidad: Tiempo O(4^N * N), Espacio O(4^N * N).
    Ejemplo:
        combinaciones_letras_telefono("23") -> ['ad', 'ae', 'af', ..., 'cf']
    """
    if not digitos_str:
        return []

    mapeo_teclado = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }
    resultados = []

    def backtrack(idx, comb_actual):
        """Función recursiva (backtracking) para construir combinaciones."""
        if idx == len(digitos_str):
            resultados.append(comb_actual)
            return

        digito = digitos_str[idx]
        if digito not in mapeo_teclado: # Maneja dígitos no válidos (ej. '0', '1')
            backtrack(idx + 1, comb_actual) # Omite el dígito inválido
            return

        for letra in mapeo_teclado[digito]:
            backtrack(idx + 1, comb_actual + letra)

    backtrack(0, "")
    return resultados

def ejecutar_combinaciones_telefono():
    """Prueba las combinaciones telefónicas."""
    print("\n--- Combinaciones de Letras del Teclado Telefónico ---")
    digitos_1 = "23"
    print(f"Dígitos: '{digitos_1}' -> Combinaciones: {combinaciones_letras_telefono(digitos_1)}")
    digitos_2 = "7"
    print(f"Dígitos: '{digitos_2}' -> Combinaciones: {combinaciones_letras_telefono(digitos_2)}")
    print("-" * 30)

# --- Ejecución de las pruebas ---
if __name__ == "__main__":
    ejecutar_verificador_palindromo()
    ejecutar_eliminador_duplicados()
    ejecutar_removedor_elementos()
    ejecutar_combinaciones_telefono()