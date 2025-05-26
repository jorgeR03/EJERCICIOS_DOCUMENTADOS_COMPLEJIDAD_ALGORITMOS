# Importa la librería random para generar números aleatorios (crucial para la genética)
import random

# Importa tkinter para crear la interfaz gráfica del tablero
import tkinter as tk

# ----------- FUNCIÓN PARA EVALUAR LA CALIDAD DE UNA SOLUCIÓN -----------
def evaluar_aptitud(tablero):
    """
    Calcula la aptitud de un individuo (una posible solución del tablero).
    La aptitud es el número de pares de reinas que NO se atacan.
    """
    ataques = 0  # Contador de ataques entre reinas

    # Comparamos todas las combinaciones de pares de reinas
    for i in range(8):
        for j in range(i + 1, 8):
            # Verifica si dos reinas están en la misma fila
            misma_fila = tablero[i] == tablero[j]

            # Verifica si están en la misma diagonal
            misma_diagonal = abs(tablero[i] - tablero[j]) == abs(i - j)

            # Si están en conflicto, suma un ataque
            if misma_fila or misma_diagonal:
                ataques += 1

    # El máximo de combinaciones entre 8 reinas es 28 (8C2), por eso se resta
    return 28 - ataques

# ----------- CREA UNA SOLUCIÓN ALEATORIA (INDIVIDUO) -----------
def generar_individuo():
    """
    Crea un individuo aleatorio (una solución con 8 reinas).
    Cada número representa la fila en la que está la reina en una columna.
    """
    return [random.randint(0, 7) for _ in range(8)]  # Lista de 8 enteros aleatorios

# ----------- SELECCIÓN DE LOS MEJORES INDIVIDUOS -----------
def elegir_padres(poblacion):
    """
    Ordena la población según su aptitud y devuelve los 3 mejores.
    """
    # Se ordena la población según su aptitud (mejor primero)
    return sorted(poblacion, key=lambda x: evaluar_aptitud(x), reverse=True)[:3]

# ----------- CRUCE ENTRE DOS PADRES PARA CREAR UN HIJO -----------
def cruzar(p1, p2):
    """
    Realiza cruce entre dos padres para generar un hijo.
    Se corta en un punto aleatorio y se mezcla mitad de un padre con la otra mitad del otro.
    """
    corte = random.randint(1, 6)  # Punto de cruce aleatorio (entre 1 y 6)
    hijo = p1[:corte] + p2[corte:]  # Se toma la parte izquierda de p1 y derecha de p2
    return hijo

# ----------- MUTACIÓN DE UN INDIVIDUO -----------
def aplicar_mutacion(individuo, prob=0.3):
    """
    Modifica aleatoriamente una reina si se cumple una probabilidad (30% por defecto).
    Sirve para introducir variación genética y evitar estancamientos.
    """
    if random.random() < prob:
        columna = random.randint(0, 7)  # Selecciona una columna al azar
        fila = random.randint(0, 7)     # Cambia su fila por una nueva aleatoria
        individuo[columna] = fila       # Aplica el cambio
    return individuo

# ----------- ALGORITMO GENÉTICO PRINCIPAL -----------
def resolver_8_reinas():
    """
    Ejecuta el algoritmo genético hasta encontrar una solución perfecta (aptitud = 28).
    Devuelve la mejor solución encontrada.
    """
    # Se crea una población inicial de 80 individuos
    poblacion = [generar_individuo() for _ in range(80)]
    ciclos = 0  # Contador de generaciones

    while True:
        ciclos += 1  # Avanza a la siguiente generación
        padres = elegir_padres(poblacion)  # Se seleccionan los 3 mejores individuos

        # Si el mejor tiene aptitud 28, hemos encontrado la solución
        if evaluar_aptitud(padres[0]) == 28:
            print(f"¡Solución encontrada en la generación {ciclos}!")
            return padres[0]

        # Creamos una nueva generación vacía
        nueva_generacion = []

        # Mientras no tengamos 80 nuevos individuos:
        while len(nueva_generacion) < 80:
            # Seleccionamos dos padres distintos
            p1, p2 = random.sample(padres, 2)

            # Se cruzan para formar un hijo
            hijo = cruzar(p1, p2)

            # Posible mutación en el hijo
            hijo = aplicar_mutacion(hijo)

            # Agrega el nuevo hijo a la nueva generación
            nueva_generacion.append(hijo)

        # Reemplazamos la población anterior con la nueva
        poblacion = nueva_generacion

# ----------- INTERFAZ GRÁFICA CON TKINTER -----------
def mostrar_tablero(solucion):
    """
    Muestra en pantalla el tablero con las 8 reinas ubicadas según la solución.
    """
    app = tk.Tk()  # Crea la ventana principal
    app.title("Problema de clase: Las 8 reinas")  # Título de la ventana

    lado = 60  # Tamaño de cada casilla (60x60 pixeles)
    tablero = tk.Canvas(app, width=lado * 8, height=lado * 8)  # Área de dibujo
    tablero.pack()  # Agrega el canvas a la ventana

    # Dibuja el tablero casilla por casilla
    for fila in range(8):
        for col in range(8):
            # Alterna colores para simular un tablero de ajedrez
            color = "black" if (fila + col) % 2 == 0 else "blue"
            x1 = col * lado
            y1 = fila * lado
            x2 = x1 + lado
            y2 = y1 + lado
            tablero.create_rectangle(x1, y1, x2, y2, fill=color)  # Crea una casilla

    # Dibuja las reinas en la posición correspondiente
    for col, fila in enumerate(solucion):
        # Calcula el centro de la casilla donde poner la reina
        cx = col * lado + lado // 2
        cy = fila * lado + lado // 2
        tablero.create_text(cx, cy, text="♛", font=("Helvetica", 32), fill="pink")  # Dibuja la reina

    app.mainloop()  # Inicia la ventana gráfica

# ----------- PROGRAMA PRINCIPAL (punto de entrada) -----------
if __name__ == "__main__":
    # Se llama al algoritmo genético y se obtiene la solución
    solucion_final = resolver_8_reinas()

    # Imprime en consola la ubicación de cada reina por columna
    print("Posiciones de las reinas (columna: fila):")
    for i, fila in enumerate(solucion_final):
        print(f"Columna {i}: Fila {fila}")

    # Llama a la función para mostrar el tablero gráficamente
    mostrar_tablero(solucion_final)
