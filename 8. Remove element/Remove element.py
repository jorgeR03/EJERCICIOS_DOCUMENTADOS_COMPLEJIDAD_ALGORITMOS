def remove_element(nums, val):

    # índice para la posición donde se colocará el siguiente valor diferente de 'val'
    i = 0

    # recorremos el arreglo completo
    for j in range(len(nums)):
        # si el elemento actual no es igual a 'val', lo copiamos en la posición 'i' y avanzamos 'i'
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    # al finalizar, 'i' contiene la cantidad de elementos distintos a 'val'
    return i


nums = [3, 2, 2, 3, 4, 2, 5]
val = 2

# Llamamos a la función para eliminar todas las ocurrencias de 2
k = remove_element(nums, val)

print(f"Número de elementos distintos a {val}: {k}")
print(f"Arreglo modificado con los primeros {k} elementos válidos: {nums[:k]}")