def devolver_cambio(monto, monedas):
    """
    Devuelve una lista de monedas que suman el monto dado,
    usando la menor cantidad posible (estrategia voraz).

    Parámetros:
    - monto (int): cantidad de cambio a devolver en centavos.
    - monedas (list[int]): lista de denominaciones disponibles (de mayor a menor).

    Retorna:
    - list[int]: monedas que componen el cambio.
    """
    resultado = []
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)
    return resultado
