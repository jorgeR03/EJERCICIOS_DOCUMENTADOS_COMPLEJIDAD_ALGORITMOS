import heapq # Para implementar la cola de prioridad (min-heap)
import math  # Para usar math.inf como infinito

def dijkstra(grafo, origen):
    """
    Implementa el algoritmo de Dijkstra para encontrar los caminos más cortos
    desde un nodo origen a todos los demás nodos en un grafo.

    Args:
        grafo (dict): Representación del grafo usando una lista de adyacencia.
                      El formato esperado es:
                      {
                          nodo_A: [(costo_AB, nodo_B), (costo_AC, nodo_C), ...],
                          nodo_B: [(costo_BA, nodo_A), ...],
                          ...
                      }
                      Donde 'costo_AB' es el peso de la arista entre nodo_A y nodo_B.
        origen (any): El nodo desde el cual calcular los caminos más cortos.
                      Debe ser una de las claves en el diccionario 'grafo'.

    Returns:
        tuple: (distancias, predecesores)
            distancias (dict): Un diccionario donde las claves son los nodos y los
                               valores son las distancias más cortas desde el 'origen'.
            predecesores (dict): Un diccionario para reconstruir los caminos.
                                 predecesores[nodo] es el nodo anterior a 'nodo'
                                 en el camino más corto desde el 'origen'.
    """
    if origen not in grafo:
        raise ValueError(f"El nodo de origen '{origen}' no se encuentra en el grafo.")

    # 1. Inicialización (como en tu imagen)
    distancias = {nodo: math.inf for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    distancias[origen] = 0

    # 2. Cola de prioridad (min-heap) con nodos y sus distancias tentativas
    #    Almacenamos tuplas (distancia_actual, nodo)
    #    heapq es un min-heap, por lo que siempre extraerá el nodo con la menor distancia.
    cola_prioridad = [(0, origen)] # (distancia_desde_origen, nodo)

    nodos_procesados = set() # Para evitar procesar un nodo múltiples veces innecesariamente en algunas variantes

    while cola_prioridad:
        # Extraer el nodo con la menor distancia tentativa actual
        distancia_actual_u, u = heapq.heappop(cola_prioridad)

        # Si ya encontramos un camino más corto a 'u' antes y lo procesamos,
        # o si la distancia extraída es mayor que la ya conocida, lo ignoramos.
        # Esto es útil si un nodo se añade múltiples veces a la cola con diferentes distancias.
        if u in nodos_procesados or distancia_actual_u > distancias[u]:
            continue
        
        nodos_procesados.add(u)


        # Para cada vecino 'v' del nodo actual 'u'
        if u in grafo: # Asegurarse de que el nodo u tiene vecinos definidos
            for peso_uv, v in grafo[u]:
                if v not in distancias:
                    # Si el vecino v no estaba inicialmente en la lista de nodos del grafo
                    # (podría pasar si el grafo no lista todos los nodos como claves principales)
                    # lo inicializamos. Esto es más robusto.
                    distancias[v] = math.inf
                    predecesores[v] = None

                # Relajación de la arista (u, v)
                # Si encontramos un camino más corto a 'v' a través de 'u'
                if distancias[u] + peso_uv < distancias[v]:
                    distancias[v] = distancias[u] + peso_uv
                    predecesores[v] = u
                    # Añadir 'v' a la cola de prioridad con su nueva distancia
                    heapq.heappush(cola_prioridad, (distancias[v], v))
    
    return distancias, predecesores

def obtener_camino(predecesores, origen, destino):
    """
    Reconstruye el camino más corto desde el origen hasta el destino
    utilizando el diccionario de predecesores devuelto por Dijkstra.
    """
    camino = []
    nodo_actual = destino
    if predecesores.get(destino) is None and destino != origen : # El get es por si destino no está en predecesores
        return None # No hay camino al destino

    while nodo_actual is not None:
        camino.append(nodo_actual)
        if nodo_actual == origen:
            break
        nodo_actual = predecesores[nodo_actual]
        # Si el nodo_actual se vuelve None y no hemos llegado al origen, significa que no hay camino
        if nodo_actual is None and camino[-1] != origen:
             return None # No hay camino completo

    if camino[-1] != origen: # Si el último elemento no es el origen, no se encontró camino
        return None

    return camino[::-1] # Devolver el camino en el orden correcto (origen -> destino)


# --- Ejemplo de Uso ---
if __name__ == "__main__":
    # Definimos un grafo de ejemplo.
    # Las claves son los nodos. Los valores son listas de tuplas (peso, nodo_vecino).
    mi_grafo = {
        'A': [(1, 'B'), (4, 'C')],
        'B': [(1, 'A'), (2, 'C'), (5, 'D')],
        'C': [(4, 'A'), (2, 'B'), (1, 'D'), (3, 'E')],
        'D': [(5, 'B'), (1, 'C'), (6, 'E')],
        'E': [(3, 'C'), (6, 'D'), (2, 'F')],
        'F': [(2, 'E')] # 'F' es un nodo, pero no tiene salidas a otros nuevos
    }
    # Asegurarse de que todos los nodos referenciados estén como claves principales
    # para una inicialización completa en Dijkstra si no se maneja internamente.
    # En esta implementación, se maneja si un vecino no está como clave principal.

    nodo_origen = 'A'
    print(f"Calculando caminos más cortos desde el nodo: {nodo_origen}\n")

    distancias_resultado, predecesores_resultado = dijkstra(mi_grafo, nodo_origen)

    print("Distancias desde el origen:")
    for nodo, distancia in distancias_resultado.items():
        print(f"  Distancia a {nodo}: {distancia}")

    print("\nCaminos más cortos desde el origen:")
    for nodo_destino in mi_grafo: # Iteramos por todos los nodos conocidos del grafo
        if nodo_destino == nodo_origen:
            print(f"  A {nodo_destino}: [ '{nodo_origen}' ] (es el origen)")
            continue
        
        camino = obtener_camino(predecesores_resultado, nodo_origen, nodo_destino)
        if camino:
            print(f"  A {nodo_destino}: {camino} (Costo total: {distancias_resultado[nodo_destino]})")
        else:
            print(f"  A {nodo_destino}: No hay camino encontrado.")
    
    # Ejemplo de un nodo que podría no ser alcanzable si modificamos el grafo
    # (En este grafo, todos son alcanzables desde A)

    print("\n--- Para el Problema del Viajante (TSP) ---")
    print("Recuerda que el código para la heurística del vecino más cercano")
    print("se proporcionó en la respuesta anterior.")
    print("Ese algoritmo es diferente y se usa para un problema diferente (encontrar un tour).")