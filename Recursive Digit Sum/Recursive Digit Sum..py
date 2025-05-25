# Definimos la función que calcula el super dígito
def superDigit(n, k):
    
    # Función que suma los dígitos de un número
    def digit_sum(x):
        # Convertimos el número a texto,para poder recorrerlo dígito por dígito
        # Luego convertimos cada dígito en número y lo sumamos
        return sum(int(d) for d in str(x))  

    # PASO 1: Sumamos los dígitos de 'n' una vez y multiplicamos por 'k'
    # Esto nos evita escribir el número muchas veces
    initial_sum = digit_sum(n) * k  

    # PASO 2: Definimos una función que repite el proceso hasta obtener un solo dígito
    def recursive_super_digit(x):
        # Si el número ya tiene un solo dígito, lo devolvemos como resultado final
        if x < 10:  
            return x  
        # Si el número aún tiene más de un dígito, seguimos sumando los dígitos
        return recursive_super_digit(digit_sum(x))  
    
    # Llamamos a la función recursiva para obtener el super dígito final
    return recursive_super_digit(initial_sum)  

# Código principal que toma la entrada y escribe la salida 
if __name__ == '__main__':
    import os
    import sys
    
    # Abre el archivo donde se escribirá la salida (necesario para HackerRank)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  
    
    # Lee la entrada del usuario (dos valores: un número n y un número k)
    first_multiple_input = input().rstrip().split()  

    # El primer valor es 'n', lo dejamos como texto
    n = first_multiple_input[0]  
    
    # El segundo valor es 'k', lo convertimos a número
    k = int(first_multiple_input[1])  
    
    # Llamamos a la función para calcular el super dígito
    result = superDigit(n, k)  
    
    # Escribimos el resultado en el archivo de salida para HackerRank
    fptr.write(str(result) + '\n')  
    
    # Cerramos el archivo de salida
    fptr.close()

