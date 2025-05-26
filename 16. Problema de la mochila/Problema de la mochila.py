# Descripción: Implementación del problema de la mochila 0/1
#              utilizando programación dinámica.

def problema_mochila_01(valores, pesos, capacidad_maxima):
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica.

    Args:
        valores (list): Una lista de enteros representando los valores de los artículos.
        pesos (list): Una lista de enteros representando los pesos de los artículos.
                        Debe tener la misma longitud que 'valores'.
        capacidad_maxima (int): La capacidad máxima de peso de la mochila.

    Returns:
        int: El valor máximo que se puede obtener sin exceder la capacidad_maxima.
        list: Una lista de los índices de los artículos seleccionados para obtener el valor máximo.
              (Los índices corresponden a la posición en las listas 'valores' y 'pesos').

    Ejemplo:
        valores = [60, 100, 120]
        pesos = [10, 20, 30]
        capacidad_maxima = 50
        max_valor, articulos_seleccionados = problema_mochila_01(valores, pesos, capacidad_maxima)
        # max_valor será 220 (artículos 2 y 3, con valores 100 + 120)
        # articulos_seleccionados podría ser [1, 2] (índices de los artículos)
    """
    num_articulos = len(valores)

    # dp[i][w] almacenará el valor máximo que se puede obtener usando los primeros 'i' artículos
    # con una capacidad de mochila de 'w'.
    # Inicializamos una tabla (matriz) con ceros.
    # Las filas representan los artículos (desde 0 hasta num_articulos).
    # Las columnas representan las capacidades (desde 0 hasta capacidad_maxima).
    dp = [[0 for _ in range(capacidad_maxima + 1)] for _ in range(num_articulos + 1)]

    # Llenamos la tabla dp de abajo hacia arriba (o de arriba hacia abajo, según la perspectiva)
    for i in range(1, num_articulos + 1):  # Iterar sobre los artículos (el artículo i-1 en las listas originales)
        # valor_actual y peso_actual corresponden al artículo (i-1)
        # porque los índices de la lista son base 0, y en la tabla dp,
        # la fila 'i' considera hasta el artículo 'i'.
        valor_actual = valores[i-1]
        peso_actual = pesos[i-1]

        for w in range(capacidad_maxima + 1):  # Iterar sobre las posibles capacidades de la mochila
            # Opción 1: No incluir el artículo actual (i-1)
            # El valor es el mismo que se podía obtener con los (i-1) artículos anteriores
            # y la misma capacidad 'w'.
            valor_sin_incluir_actual = dp[i-1][w]

            # Opción 2: Incluir el artículo actual (i-1), si su peso no excede la capacidad 'w'
            valor_incluyendo_actual = 0
            if peso_actual <= w:
                # Si incluimos el artículo actual, su valor se suma al valor máximo
                # que se podía obtener con los (i-1) artículos anteriores y la capacidad restante
                # (w - peso_actual).
                valor_incluyendo_actual = valor_actual + dp[i-1][w - peso_actual]

            # Elegimos la opción que maximice el valor
            dp[i][w] = max(valor_sin_incluir_actual, valor_incluyendo_actual)

    # El valor máximo estará en la última celda de la tabla,
    # que considera todos los artículos y la capacidad máxima total.
    max_valor_obtenido = dp[num_articulos][capacidad_maxima]

    # --- Reconstrucción de los artículos seleccionados ---
    # Para saber qué artículos se incluyeron, necesitamos rastrear hacia atrás en la tabla dp.
    articulos_seleccionados_indices = []
    capacidad_restante = capacidad_maxima
    # Empezamos desde el último artículo y la capacidad máxima
    for i in range(num_articulos, 0, -1):
        # Si el valor en dp[i][capacidad_restante] es diferente de dp[i-1][capacidad_restante],
        # significa que el artículo 'i-1' (índice original) fue incluido.
        if dp[i][capacidad_restante] != dp[i-1][capacidad_restante]:
            articulos_seleccionados_indices.append(i-1) # Guardamos el índice original del artículo
            capacidad_restante -= pesos[i-1] # Reducimos la capacidad por el peso del artículo incluido

        if capacidad_restante <= 0: # Si ya no queda capacidad, terminamos
            break
    
    articulos_seleccionados_indices.reverse() # Los índices se obtienen en orden inverso

    return max_valor_obtenido, articulos_seleccionados_indices

def ejecutar_problema_mochila():
    """Función principal para probar el algoritmo del problema de la mochila."""
    print("--- Problema de la Mochila 0/1 (Programación Dinámica) ---")

    # Ejemplo 1
    valores1 = [60, 100, 120]
    pesos1 = [10, 20, 30]
    capacidad1 = 50
    print(f"\nEjemplo 1:")
    print(f"Valores: {valores1}")
    print(f"Pesos: {pesos1}")
    print(f"Capacidad máxima: {capacidad1}")
    max_val1, items1 = problema_mochila_01(valores1, pesos1, capacidad1)
    print(f"Valor máximo obtenido: {max_val1}")
    print(f"Índices de artículos seleccionados: {items1}")
    if items1:
        print(f"  (Pesos: {[pesos1[i] for i in items1]}, Valores: {[valores1[i] for i in items1]})")


    # Ejemplo 2
    valores2 = [10, 40, 30, 50]
    pesos2 = [5, 4, 6, 3]
    capacidad2 = 10
    print(f"\nEjemplo 2:")
    print(f"Valores: {valores2}")
    print(f"Pesos: {pesos2}")
    print(f"Capacidad máxima: {capacidad2}")
    max_val2, items2 = problema_mochila_01(valores2, pesos2, capacidad2)
    print(f"Valor máximo obtenido: {max_val2}")
    print(f"Índices de artículos seleccionados: {items2}")
    if items2:
        print(f"  (Pesos: {[pesos2[i] for i in items2]}, Valores: {[valores2[i] for i in items2]})")


    # Ejemplo 3: Un caso donde no se puede tomar nada
    valores3 = [10, 20]
    pesos3 = [15, 25]
    capacidad3 = 10
    print(f"\nEjemplo 3:")
    print(f"Valores: {valores3}")
    print(f"Pesos: {pesos3}")
    print(f"Capacidad máxima: {capacidad3}")
    max_val3, items3 = problema_mochila_01(valores3, pesos3, capacidad3)
    print(f"Valor máximo obtenido: {max_val3}")
    print(f"Índices de artículos seleccionados: {items3}")
    if items3:
        print(f"  (Pesos: {[pesos3[i] for i in items3]}, Valores: {[valores3[i] for i in items3]})")
    else:
        print("  (Ningún artículo seleccionado)")
        
    print("-" * 30)

# --- Ejecución de la prueba ---
if __name__ == "__main__":
    ejecutar_problema_mochila()