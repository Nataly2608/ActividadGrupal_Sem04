def Div_n_Conq(lista, culpable, inicio=0):

    # Si la lista ya está vacía significa que el número no existe
    if len(lista) == 0:
        return False

    # Obtengo la posición del elemento que está en el medio
    medio = len(lista) // 2

    # Muestro el número central que se está evaluando
    print("Número del medio:", lista[medio])

    # Si encontré el número, devuelvo su posición
    if lista[medio] == culpable:
        return inicio + medio

    # Si el número es menor, busco solo en la mitad izquierda
    elif culpable < lista[medio]:
        return Div_n_Conq(lista[:medio], culpable, inicio)

    # Si el número es mayor, busco solo en la mitad derecha
    else:
        return Div_n_Conq(
            lista[medio + 1:],
            culpable,
            inicio + medio + 1
        )

# Lista ordenada donde se realizará la búsqueda
numeros = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 58, 65, 80, 98]

# Pido al usuario el número que desea buscar
dnc = int(input("Ingrese el número a buscar: "))

# Llamo a la función para iniciar la búsqueda
posicion = Div_n_Conq(numeros, dnc)

# Verifico si el número fue encontrado
if posicion is not False:
    print(f"El número {dnc} sí está en la lista.")
    print(f"Posición: {posicion}")
else:
    print(f"El número {dnc} no está en la lista.")