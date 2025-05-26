def bubble_sort(arr):
    n = len(arr)
    # Repetimos el proceso n-1 veces
    for i in range(n - 1):
        # En cada pasada comparamos elementos adyacentes
        for j in range(n - 1 - i):  # Podemos evitar comparar los últimos elementos ya ordenados
            if arr[j] > arr[j + 1]:
                # Si están en el orden incorrecto, los intercambiamos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

if __name__ == '__main__':
    bubble_sort([31415926535897932384626433832795, 1, 3, 10, 3, 5])
