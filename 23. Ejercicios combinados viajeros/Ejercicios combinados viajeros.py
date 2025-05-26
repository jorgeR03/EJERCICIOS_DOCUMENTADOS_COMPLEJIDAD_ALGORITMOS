# Definiciones de los algoritmos (previamente proporcionadas y documentadas)
import heapq
import math

# --- ALGORITMO 1: DIJKSTRA ---
def algoritmo_dijkstra(grafo, origen):
    """
    Implementa el algoritmo de Dijkstra para encontrar los caminos más cortos
    desde un nodo origen a todos los demás nodos en un grafo ponderado
    cuyos pesos en las aristas no son negativos.
    """
    if not grafo: 
        if origen is not None:
             # print(f"Advertencia: El grafo está vacío. No se puede procesar el origen '{origen}'.")
             return {origen: 0 if origen is not None else None}, {origen: None if origen is not None else None}
        return {}, {}

    all_nodes_in_graph = set(grafo.keys())
    for node_key in grafo: # Asegurar que todos los nodos referenciados estén en el conjunto
        for _, neighbor in grafo.get(node_key, []):
            all_nodes_in_graph.add(neighbor)
    if origen is not None and origen not in all_nodes_in_graph: # Añadir origen si no estaba como clave
         all_nodes_in_graph.add(origen)

    if not all_nodes_in_graph and origen is None: # No hay nodos ni origen
        return {}, {}
    if not all_nodes_in_graph and origen is not None: # No hay nodos pero se especificó origen
        return {origen: 0}, {origen: None}


    distancias = {nodo: math.inf for nodo in all_nodes_in_graph}
    predecesores = {nodo: None for nodo in all_nodes_in_graph}
    
    if origen is not None: # Origen debe ser válido para proceder
        distancias[origen] = 0
    else: # Si el origen es None, no se puede continuar de forma estándar.
        # print("Advertencia: Origen no especificado para Dijkstra.")
        return distancias, predecesores


    cola_prioridad = [(0, origen)]
    nodos_procesados = set()

    while cola_prioridad:
        distancia_actual_u, u = heapq.heappop(cola_prioridad)

        if u in nodos_procesados or distancia_actual_u > distancias.get(u, math.inf):
            continue
        nodos_procesados.add(u)

        for peso_uv, v in grafo.get(u, []): # Usar .get(u,[]) si u podría no estar en grafo (aunque all_nodes_in_graph debería cubrirlo)
            # Asegurar que el vecino v esté inicializado si no lo estaba
            if v not in distancias: 
                distancias[v] = math.inf
                predecesores[v] = None

            if distancias.get(u, math.inf) + peso_uv < distancias.get(v, math.inf):
                distancias[v] = distancias[u] + peso_uv
                predecesores[v] = u
                heapq.heappush(cola_prioridad, (distancias[v], v))
    
    return distancias, predecesores

def obtener_camino_dijkstra(predecesores_dict, distancias_dict, origen_node, destino_node):
    """
    Reconstruye el camino más corto desde el 'origen_node' hasta el 'destino_node'.
    """
    camino = []
    nodo_actual = destino_node
    
    # Si el destino es el origen
    if origen_node == destino_node:
        return [origen_node] if distancias_dict.get(origen_node) == 0 else None

    # Si el destino no es alcanzable (distancia infinita) o no tiene predecesor
    if distancias_dict.get(destino_node) == math.inf or predecesores_dict.get(destino_node) is None:
        # A menos que el destino sea el origen y no tenga predecesor (debería ser None para origen)
        if not (destino_node == origen_node and predecesores_dict.get(destino_node) is None):
             return None

    # Reconstruir camino
    while nodo_actual is not None:
        camino.append(nodo_actual)
        if nodo_actual == origen_node:
            break
        nodo_previo = predecesores_dict.get(nodo_actual)
        # Evitar bucles si hay un problema en los predecesores o si el camino no llega al origen
        if nodo_previo is not None and nodo_previo in camino:
            # print(f"Error: Bucle detectado en predecesores al reconstruir camino a {destino_node}")
            return None # Bucle detectado
        nodo_actual = nodo_previo
        
        if nodo_actual is None and (not camino or camino[-1] != origen_node): # Camino roto
             return None

    if not camino or camino[-1] != origen_node: # No se pudo formar el camino hasta el origen
        return None

    return camino[::-1]


# --- ALGORITMO 2: HEURÍSTICA DEL VECINO MÁS CERCANO (TSP) ---
def heuristica_vecino_mas_cercano_tsp(matriz_distancias, nodo_inicio_tsp=0):
    """
    Resuelve el Problema del Viajante (TSP) de forma aproximada utilizando la
    heurística del vecino más cercano.
    """
    num_nodos_tsp = len(matriz_distancias)
    if num_nodos_tsp == 0:
        return [], 0.0
    if not all(len(fila) == num_nodos_tsp for fila in matriz_distancias):
        raise ValueError("La matriz de distancias para TSP debe ser cuadrada.")

    visitados_tsp = [False] * num_nodos_tsp
    ruta_tsp = []
    distancia_total_tsp = 0.0

    nodo_actual_tsp = nodo_inicio_tsp
    if nodo_actual_tsp >= num_nodos_tsp or nodo_actual_tsp < 0: # Validar nodo de inicio
        raise ValueError(f"Nodo de inicio TSP ({nodo_inicio_tsp}) fuera de rango para {num_nodos_tsp} nodos.")

    ruta_tsp.append(nodo_actual_tsp)
    visitados_tsp[nodo_actual_tsp] = True

    for _ in range(num_nodos_tsp - 1): # Iterar N-1 veces para encontrar los siguientes nodos
        nodo_siguiente_tsp = -1
        distancia_minima_al_siguiente_tsp = math.inf

        for candidato_idx_tsp in range(num_nodos_tsp):
            if not visitados_tsp[candidato_idx_tsp]: # Si el candidato no ha sido visitado
                # Acceder a la distancia de forma segura
                if nodo_actual_tsp < len(matriz_distancias) and \
                   candidato_idx_tsp < len(matriz_distancias[nodo_actual_tsp]):
                    distancia_candidato_tsp = matriz_distancias[nodo_actual_tsp][candidato_idx_tsp]
                    
                    if not isinstance(distancia_candidato_tsp, (int, float)):
                        # print(f"Advertencia: Distancia no válida {distancia_candidato_tsp} de {nodo_actual_tsp} a {candidato_idx_tsp}")
                        continue # Ignorar si la distancia no es un número válido
                else:
                    # print(f"Advertencia: Índices fuera de rango al acceder a matriz_distancias[{nodo_actual_tsp}][{candidato_idx_tsp}]")
                    continue # Índices inválidos

                if distancia_candidato_tsp < distancia_minima_al_siguiente_tsp:
                    distancia_minima_al_siguiente_tsp = distancia_candidato_tsp
                    nodo_siguiente_tsp = candidato_idx_tsp
        
        if nodo_siguiente_tsp == -1: # No se encontró un siguiente nodo no visitado
            # print("Advertencia: Tour TSP interrumpido, no se pudo encontrar el siguiente nodo no visitado (grafo no completo para tour).")
            return ruta_tsp, distancia_total_tsp # Retorna el tour parcial formado hasta ahora
            
        distancia_total_tsp += distancia_minima_al_siguiente_tsp
        nodo_actual_tsp = nodo_siguiente_tsp
        ruta_tsp.append(nodo_actual_tsp)
        visitados_tsp[nodo_actual_tsp] = True
    
    # Regresar al nodo de inicio para completar el ciclo del TSP
    if len(ruta_tsp) == num_nodos_tsp: # Solo si se visitaron todos los nodos
        if nodo_actual_tsp < len(matriz_distancias) and \
           nodo_inicio_tsp < len(matriz_distancias[nodo_actual_tsp]):
            distancia_regreso = matriz_distancias[nodo_actual_tsp][nodo_inicio_tsp]
            if isinstance(distancia_regreso, (int, float)): # Asegurar que la distancia de regreso es válida
                 distancia_total_tsp += distancia_regreso
                 ruta_tsp.append(nodo_inicio_tsp) # Completar el ciclo
            else:
                # print(f"Advertencia: No se pudo completar el ciclo del TSP (distancia de regreso no válida de {nodo_actual_tsp} a {nodo_inicio_tsp}).")
                pass 
        else:
             # print(f"Advertencia: No se pudo completar el ciclo del TSP de regreso al nodo {nodo_inicio_tsp} (índices fuera de rango para distancia de regreso).")
             pass
    
    return ruta_tsp, distancia_total_tsp

# Matriz de distancias proporcionada por el usuario
matriz_distancias_usuario = [
    [ 0, 34, 56, 12, 78, 90, 43, 67, 23, 55 ],
    [ 34, 0, 64, 21, 12, 44, 90, 13, 45, 66 ],
    [ 56, 64, 0, 50, 34, 33, 76, 82, 28, 59 ],
    [ 12, 21, 50, 0, 22, 88, 16, 44, 73, 10 ],
    [ 78, 12, 34, 22, 0, 25, 90, 17, 65, 33 ],
    [ 90, 44, 33, 88, 25, 0, 14, 56, 32, 71 ],
    [ 43, 90, 76, 16, 90, 14, 0, 36, 48, 11 ],
    [ 67, 13, 82, 44, 17, 56, 36, 0, 20, 24 ],
    [ 23, 45, 28, 73, 65, 32, 48, 20, 0, 60 ],
    [ 55, 66, 59, 10, 33, 71, 11, 24, 60, 0 ]
]

print("--- CASO 1: Heurística del Vecino Más Cercano para TSP ---")
print(f"Matriz de distancias (10x10) utilizada.\n")

nodos_de_inicio_tsp = [0, 1, 2] 
for inicio_tsp in nodos_de_inicio_tsp:
    print(f"Calculando Tour TSP comenzando desde el nodo: {inicio_tsp}")
    ruta_tsp_resultado, distancia_total_tsp_resultado = heuristica_vecino_mas_cercano_tsp(matriz_distancias_usuario, inicio_tsp)
    print(f"  Ruta encontrada: {ruta_tsp_resultado}")
    print(f"  Distancia total del tour: {distancia_total_tsp_resultado}\n")

print("\n--- CASO 2: Algoritmo de Dijkstra ---")

num_nodos_dijkstra = len(matriz_distancias_usuario)
grafo_para_dijkstra = {i: [] for i in range(num_nodos_dijkstra)}

for i in range(num_nodos_dijkstra):
    for j in range(num_nodos_dijkstra):
        # Para Dijkstra, una arista existe si la distancia es > 0 (0 en diagonal es distancia a sí mismo)
        # Si la matriz usara 'math.inf' para 'sin conexión', la condición sería diferente.
        # Aquí, cualquier valor numérico positivo en la matriz es una arista.
        if matriz_distancias_usuario[i][j] > 0 : 
            grafo_para_dijkstra[i].append((matriz_distancias_usuario[i][j], j))

print("Grafo convertido a formato de lista de adyacencia (primeros nodos como ejemplo):")
for i in range(min(3, num_nodos_dijkstra)): 
    print(f"  Nodo {i}: {grafo_para_dijkstra[i]}")
print("...\n")

origen_dijkstra = 0
print(f"Calculando caminos más cortos con Dijkstra desde el nodo origen: {origen_dijkstra}\n")

# Llamada a Dijkstra
distancias_dijkstra, predecesores_dijkstra = algoritmo_dijkstra(grafo_para_dijkstra, origen_dijkstra)

print("Resultados de Dijkstra:")
# Ordenar por nodo destino para una salida consistente
sorted_destinos = sorted(distancias_dijkstra.keys())

for nodo_destino in sorted_destinos:
    # Usar los diccionarios correctos para obtener_camino_dijkstra
    camino_d = obtener_camino_dijkstra(predecesores_dijkstra, distancias_dijkstra, origen_dijkstra, nodo_destino)
    dist_d = distancias_dijkstra[nodo_destino]
    
    if camino_d:
        ruta_str = " -> ".join(map(str, camino_d))
        print(f"  Al nodo {nodo_destino}: Ruta = {ruta_str}, Distancia = {dist_d}")
    # No es necesario un elif para el origen aquí si obtener_camino_dijkstra lo maneja.
    # Si dist_d es infinito y camino_d es None, es inalcanzable.
    elif dist_d == math.inf :
        print(f"  Al nodo {nodo_destino}: No alcanzable, Distancia = {dist_d}")
    else: # Otros casos, por si acaso (ej. origen con camino None pero dist 0)
         print(f"  Al nodo {nodo_destino}: (caso no cubierto por formato std), Distancia = {dist_d}, Camino = {camino_d}")