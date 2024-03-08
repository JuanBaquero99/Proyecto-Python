def ordenamiento_por_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual

# Lista de ejemplo
lista = [7, 3, 2, 9, 8]
print("Lista original:", lista)

# Llamamos a la función de ordenamiento por inserción
ordenamiento_por_insercion(lista)
print("Lista ordenada:", lista)