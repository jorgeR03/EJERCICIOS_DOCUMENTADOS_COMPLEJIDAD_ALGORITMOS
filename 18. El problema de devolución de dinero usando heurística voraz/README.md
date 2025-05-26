## Introducción: El Dilema del Cambio

Imagina que eres cajero y alguien te paga con un billete, pero la cuenta es menor. Tu objetivo es devolver el cambio **usando la menor cantidad de monedas posible**.

Por ejemplo, si tienes que devolver **87 centavos** y tus monedas disponibles son de:
```
[50, 25, 10, 5, 1]
```
la mejor combinación es:
```
1 moneda de 50
1 moneda de 25
1 moneda de 10
1 moneda de 1
```

Este tipo de problema es clásico en programación y se puede resolver usando una **heurística voraz** (greedy algorithm).

---

## ¿Qué es una Estrategia Voraz?

Un algoritmo voraz toma decisiones paso a paso, **eligiendo en cada momento la opción que parece ser la mejor** (en este caso, la moneda más grande que no exceda el monto restante).

No siempre garantiza la solución óptima para cualquier conjunto de monedas, pero **funciona perfectamente con sistemas como el monetario decimal moderno**, donde las denominaciones están diseñadas para que la estrategia voraz funcione.

---

## Enfoque: Algoritmo Greedy para el Cambio

###  Objetivo
Dado un valor de cambio a devolver y una lista de denominaciones de monedas disponibles, devolver la cantidad mínima de monedas posibles.

### Implementación

```python
def devolver_cambio(monto, monedas):
    """
    Devuelve una lista de monedas que suman el monto dado, usando la menor cantidad posible (estrategia voraz).
    """
    resultado = []
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)
    return resultado
```

###  Ventajas
- Simple y rápido.
- Muy efectivo en sistemas de monedas "bien diseñados".

###  Desventajas
- No siempre garantiza la mejor solución si las monedas no son estándares. Por ejemplo, con monedas de [1, 3, 4], para devolver 6, la mejor solución es [3, 3], pero el algoritmo voraz puede dar [4, 1, 1].

---

## Ejemplo de Uso

```python
monedas = [50, 25, 10, 5, 1]
monto = 87

cambio = devolver_cambio(monto, monedas)
print("Cambio para", monto, "centavos:", cambio)
```

**Salida esperada:**

```
Cambio para 87 centavos: [50, 25, 10, 1, 1]
```

---

## Análisis de Complejidad

- **Tiempo:** `O(n × k)`, donde `n` es el número de denominaciones y `k` es el número de monedas necesarias.
- **Espacio:** `O(k)` para almacenar el resultado.

---

## Conclusión: Simplicidad que Funciona

El algoritmo voraz para devolver cambio es un ejemplo perfecto de cómo una decisión "localmente óptima" puede llevar a soluciones eficientes y prácticas. En sistemas monetarios reales, **la heurística funciona muy bien**, siendo la base de software en cajas registradoras, máquinas expendedoras y cajeros automáticos.
