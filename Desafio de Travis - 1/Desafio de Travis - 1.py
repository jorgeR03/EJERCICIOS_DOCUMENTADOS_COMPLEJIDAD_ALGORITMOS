# Leer la entrada del usuario
s1, s2 = map(int, input().split())

# Verificar si al menos la mitad de los concursantes lo resolvieron en la primera mitad
if s1 >= s2 / 2:
    print("E")  # El problema es fácil
else:
    print("H")  # El problema es difícil
