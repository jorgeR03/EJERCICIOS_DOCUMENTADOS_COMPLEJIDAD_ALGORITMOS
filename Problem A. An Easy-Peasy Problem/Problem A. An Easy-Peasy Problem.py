# Peasy.py

# Leer la entrada
s1, s2 = map(int, input().split())

# Verificar si al menos la mitad de los solves fueron en la primera mitad
if s1 * 2 >= s2:
    print("E")
else:
    print("H")
