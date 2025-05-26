# --------------------------------------------------------------------------
# Algoritmo 2: Heurística del Vecino Más Cercano para el Problema del Viajante (TSP)
# --------------------------------------------------------------------------
import math # Usaremos math.inf para representar infinito

def heuristica_vecino_mas_cercano_tsp(matriz_distancias, nodo_inicio_tsp=0):
    """
    Resuelve el Problema del Viajante (TSP) utilizando la heurística del vecino más cercano.

    Args:
        matriz_distancias (list of list of int/float):
            Matriz de adyacencia donde matriz_distancias[i][j] es la distancia de ciudad 'i' a 'j'.
        nodo_inicio_tsp (int): Índice del nodo (ciudad) desde donde comenzar el recorrido.

    Returns:
        tuple: (ruta_tsp, distancia_total_tsp)
            ruta_tsp (list): La secuencia de índices de nodos visitados en el recorrido.
            distancia_total_tsp (float): La distancia total del recorrido encontrado.
    """
    num_nodos_tsp = len(matriz_distancias)
    if num_nodos_tsp == 0:
        return [], 0
    if not all(len(fila) == num_nodos_tsp for fila in matriz_distancias):
        raise ValueError("La matriz de distancias para TSP debe ser cuadrada.")

    visitados_tsp = [False] * num_nodos_tsp
    ruta_tsp = []
    distancia_total_tsp = 0.0

    nodo_actual_tsp = nodo_inicio_tsp
    ruta_tsp.append(nodo_actual_tsp)
    visitados_tsp[nodo_actual_tsp] = True

    for _ in range(num_nodos_tsp - 1): # Necesitamos visitar num_nodos_tsp - 1 nodos más
        nodo_siguiente_tsp = -1
        distancia_minima_al_siguiente_tsp = math.inf

        for candidato_siguiente_tsp in range(num_nodos_tsp):
            if not visitados_tsp[candidato_siguiente_tsp]:
                distancia_candidato_tsp = matriz_distancias[nodo_actual_tsp][candidato_siguiente_tsp]
                if distancia_candidato_tsp < distancia_minima_al_siguiente_tsp:
                    distancia_minima_al_siguiente_tsp = distancia_candidato_tsp
                    nodo_siguiente_tsp = candidato_siguiente_tsp
        
        if nodo_siguiente_tsp == -1:
            # No se encontró un siguiente nodo no visitado (grafo no completamente conectado para TSP)
            # Esto no debería ocurrir en un TSP clásico donde todos los nodos son alcanzables.
            # Podríamos lanzar un error o manejarlo según el caso.
            # Por ahora, si sucede, el tour se interrumpe.
            print("Advertencia: Tour TSP interrumpido, no se encontró siguiente nodo no visitado.")
            break 
            
        distancia_total_tsp += distancia_minima_al_siguiente_tsp
        nodo_actual_tsp = nodo_siguiente_tsp
        ruta_tsp.append(nodo_actual_tsp)
        visitados_tsp[nodo_actual_tsp] = True

    # Regresar al nodo de inicio para completar el ciclo del TSP
    if len(ruta_tsp) == num_nodos_tsp: # Solo si se visitaron todos los nodos
        distancia_total_tsp += matriz_distancias[nodo_actual_tsp][nodo_inicio_tsp]
        ruta_tsp.append(nodo_inicio_tsp) # Añadir el nodo de inicio al final para cerrar el ciclo
    else:
        # Si el tour no pudo visitar todos los nodos, no se completa el ciclo al inicio.
        # La ruta devuelta será parcial.
        pass


    return ruta_tsp, distancia_total_tsp

# --- Ejemplo de Uso para TSP con Vecino Más Cercano ---
if __name__ == "__main__":
    print("--- EJEMPLO HEURÍSTICA VECINO MÁS CERCANO (TSP) ---")
    # Matriz de distancias para TSP. Supongamos 4 puntos de interés en Rionegro.
    # 0: UCO, 1: Parque Principal, 2: Hospital SJD, 3: Aeropuerto JMC
    # Las distancias son simétricas aquí por simplicidad.
    distancias_ciudades = [
        [0, 10, 12, 25], # Distancias desde UCO a UCO, Parque, Hospital, Aeropuerto
        [10, 0, 5, 20],  # Distancias desde Parque a UCO, Parque, Hospital, Aeropuerto
        [12, 5, 0, 18],  # Distancias desde Hospital a UCO, Parque, Hospital, Aeropuerto
        [25, 20, 18, 0]   # Distancias desde Aeropuerto a UCO, Parque, Hospital, Aeropuerto
    ]
    
    # Para mapear índices a nombres para una salida más clara
    nombres_ciudades = {0: 'UCO', 1: 'ParquePrincipal', 2: 'HospitalSJD', 3: 'AeropuertoJMC'}

    # Probar comenzando desde cada ciudad para ver cómo varía la heurística
    for i in range(len(distancias_ciudades)):
        ruta_encontrada, costo_total = heuristica_vecino_mas_cercano_tsp(distancias_ciudades, nodo_inicio_tsp=i)
        
        # Convertir ruta de índices a nombres
        ruta_con_nombres = [nombres_ciudades[idx] for idx in ruta_encontrada]

        print(f"Tour TSP comenzando en '{nombres_ciudades[i]}': {' -> '.join(ruta_con_nombres)}")
        print(f"Costo total del tour: {costo_total}")
        print("-" * 20)