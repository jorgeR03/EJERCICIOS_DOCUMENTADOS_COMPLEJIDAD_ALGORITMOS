# Definir el tablero de Sudoku con 9x9 casillas, los ceros representan espacios vacíos
sudoku = [
    [1, 0, 4, 0, 2, 0, 5, 0, 3],
    [0, 8, 0, 3, 0, 1, 0, 0, 0],
    [2, 9, 3, 0, 0, 5, 0, 0, 1],
    [0, 0, 2, 0, 6, 0, 0, 0, 5],
    [0, 0, 0, 4, 0, 8, 0, 0, 0],
    [9, 0, 0, 0, 5, 0, 7, 0, 0],
    [5, 0, 0, 6, 0, 0, 8, 3, 2],
    [0, 0, 0, 5, 0, 2, 0, 4, 0],
    [4, 0, 8, 0, 3, 0, 9, 0, 6]
]


# Función para imprimir el tablero de Sudoku de forma ordenada
def imprimir_sudoku(tablero):
    for fila in tablero:  # Recorre cada fila del Sudoku
        print(" ".join(str(num) for num in fila))  # Convierte cada número en string y los imprime separados por espacios
    print()  # Imprimir una línea en blanco para separar el tablero

# Función para verificar si un número puede ser colocado en una celda específica
def es_valido(tablero, fila, col, num):
    # Verificar si el número ya está en la fila
    if num in tablero[fila]:  # Si el número ya está en la fila, no es válido
        return False
    
    # Verificar si el número ya está en la columna
    for i in range(9):  # Recorre cada fila en la columna específica
        if tablero[i][col] == num:  # Si encuentra el número en la columna, no es válido
            return False
    
    # Verificar si el número ya está en la subcuadrícula 3x3
    inicio_fila = (fila // 3) * 3  # Calcula el inicio de la subcuadrícula en la fila
    inicio_col = (col // 3) * 3  # Calcula el inicio de la subcuadrícula en la columna
    for i in range(3):  # Recorre las 3 filas del bloque 3x3
        for j in range(3):  # Recorre las 3 columnas del bloque 3x3
            if tablero[inicio_fila + i][inicio_col + j] == num:  # Si el número ya está en la subcuadrícula, no es válido
                return False
    
    # Si pasó todas las verificaciones, el número es válido
    return True

# Función para resolver el Sudoku usando fuerza bruta
def resolver_sudoku(tablero):
    for fila in range(9):  # Iterar por cada fila
        for col in range(9):  # Iterar por cada columna
            if tablero[fila][col] == 0:  # Si la celda está vacía (contiene un 0)
                for num in range(1, 10):  # Probar números del 1 al 9
                    if es_valido(tablero, fila, col, num):  # Verificar si el número es válido en la celda
                        tablero[fila][col] = num  # Asignar el número en la celda
                        if resolver_sudoku(tablero):  # Llamado recursivo para intentar resolver el resto del Sudoku
                            return True  # Si encuentra una solución, terminar
                        tablero[fila][col] = 0  # Si no funciona, deshacer el cambio 
                return False  # Si ningún número funciona, devolver falso para retroceder
    return True  # Si se llenó todo correctamente, devolver verdadero


# Resolver el Sudoku y mostrar la solución si es posible
if resolver_sudoku(sudoku):  # Llamada a la función que resuelve el Sudoku
    print("Sudoku resuelto:")  # Mensaje indicando que se ha resuelto el Sudoku
    imprimir_sudoku(sudoku)  # Llamada a la función para imprimir el Sudoku resuelto
else:
    print("No hay solución para este Sudoku")  # Mensaje en caso de que el Sudoku no tenga solución
