def mcd_iterativo(a, b):
    """
    Calcula el MCD (Máximo Común Divisor) entre dos números usando un bucle iterativo.
    """
    while b != 0:
        a, b = b, a % b
    return a
if __name__ == "__main__":
    a = 48
    b = 18
    print("MCD recursivo de", a, "y", b, "es:", mcd_recursivo(a, b))
    print("MCD iterativo de", a, "y", b, "es:", mcd_iterativo(a, b))
