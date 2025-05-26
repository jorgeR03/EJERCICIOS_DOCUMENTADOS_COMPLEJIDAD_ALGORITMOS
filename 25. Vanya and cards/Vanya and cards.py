import math

def min_cards_needed(n, x, cards):
    # Calcular la suma absoluta total
    total_sum = abs(sum(cards))

    # Determinar el número mínimo de cartas necesarias
    min_cards = math.ceil(total_sum / x)

    return min_cards

# Leer entrada
n, x = map(int, input().split())  # Leer n y x
cards = list(map(int, input().split()))  # Leer la lista de valores de las cartas

# Imprimir el resultado
print(min_cards_needed(n, x, cards))
