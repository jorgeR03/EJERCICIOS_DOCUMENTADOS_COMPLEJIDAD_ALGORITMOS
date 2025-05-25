def solve_age_expression():
    """
    Lee las edades y determina si existen los factores 'a' y 'k'.
    """
    # Lee la entrada: Edad Dr. O, Edad Alyssa, Edad Konari
    # Se asume que la entrada es una línea con tres enteros separados por espacios.
    dr_o_age, alyssa_age, konari_age = map(int, input().split())

    found_solution = False

    # Queremos encontrar a > 0 y k > 0.
    # a * alyssa_age + k * konari_age = dr_o_age
    # Como k >= 1, entonces k * konari_age >= konari_age.
    # Por lo tanto, a * alyssa_age <= dr_o_age - konari_age.
    # Esto implica que a <= (dr_o_age - konari_age) / alyssa_age.
    # Iteramos 'a' desde 1 hasta este límite superior.

    # Calculamos el valor máximo posible para 'a'.
    # 'a' debe ser al menos 1.
    # Si (dr_o_age - konari_age) < alyssa_age, entonces (dr_o_age - konari_age) // alyssa_age será 0,
    # lo que significa que no hay un 'a >= 1' posible.
    max_a_val = 0
    if dr_o_age - konari_age >= alyssa_age: # Asegura que el numerador sea suficiente para al menos un 'a=1'
        max_a_val = (dr_o_age - konari_age) // alyssa_age
    
    # Iteramos por todos los posibles valores positivos de 'a'
    for a in range(1, max_a_val + 1):
        # Calculamos la parte de la edad cubierta por el factor de Alyssa
        term_alyssa = a * alyssa_age
        
        # Calculamos la edad restante que debe ser cubierta por el factor de Konari
        remaining_for_konari = dr_o_age - term_alyssa
        
        # Verificamos si esta edad restante puede ser formada por k * konari_age,
        # donde 'k' debe ser un entero positivo.
        # 1. remaining_for_konari debe ser positivo (para que k sea positivo).
        # 2. remaining_for_konari debe ser divisible exactamente por konari_age.
        if remaining_for_konari > 0 and remaining_for_konari % konari_age == 0:
            # Si ambas condiciones se cumplen, hemos encontrado 'a' y 'k' válidos.
            # k = remaining_for_konari // konari_age (será > 0)
            found_solution = True
            break  # Salimos del bucle ya que hemos encontrado una solución

    # Imprimimos el resultado según las especificaciones del problema
    if found_solution:
        print(1)
    else:
        print(0)

# Llamamos a la función principal para ejecutar la solución
if __name__ == "__main__":
    solve_age_expression()