import heapq

# Grafo basado en la imagen, representado como un diccionario de listas de tuplas (adyacencia)
grafo = {
    'A': [('B', 1), ('E', 3)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('B', 2), ('D', 2), ('F', 3)],
    'D': [('B', 5), ('C', 2)],
    'E': [('A', 3), ('F', 1)],
    'F': [('C', 3), ('E', 1), ('G', 5), ('H', 3)],
    'G': [('F', 5), ('H', 2)],
    'H': [('F', 3), ('G', 2)]
}

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[inicio] = 0

    cola = [(0, inicio)]
    visitados = set()

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual]:
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola, (nueva_distancia, vecino))

    # Imprimir resultados como en la imagen: [distancia, predecesor]
    for nodo in sorted(grafo.keys()):
        print(f"{nodo}: [{distancias[nodo]}, {predecesores[nodo]}]")

# Ejecutamos el algoritmo desde A
dijkstra(grafo, 'A')
