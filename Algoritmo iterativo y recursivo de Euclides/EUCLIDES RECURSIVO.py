def mcd_recursivo(a, b):
    """
    Calcula el MCD (Máximo Común Divisor) entre dos números usando recursión.
    """
    if b == 0:
        return a
    else:
        return mcd_recursivo(b, a % b)
if __name__ == "__main__":
    a = 48
    b = 18
    print("MCD recursivo de", a, "y", b, "es:", mcd_recursivo(a, b))
    print("MCD iterativo de", a, "y", b, "es:", mcd_iterativo(a, b))
