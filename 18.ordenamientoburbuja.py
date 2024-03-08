import random


def ordenamiento_de_burbuja(lista):
    n = len(lista) #Obtenemos la longitud de la lista

    for i in range(n): #Va a recorrer la lista en un rango (según la longitud de n)(ej: n es 10). Pero, no recorre todo el rango de una sola vez, sino que recorre 0 y ejecuta el bucle interno
        for j in range(0, n - i - 1): #Ahora j va a recorrer la lista en un rango desde 0, hasta n -1 
            # O(n) * O(n) = O(n * n) = O(n**2)

            if lista[j] > lista[j + 1]: #Si j es mayor que el j de al lado sumado 1. Es decir si 5 es j y al ser sumado queda en 6
                lista[j], lista[j + 1] = lista[j + 1], lista[j] #Entonces los vamos a reasignar donde el número 6 (el 5 sumado con 1) queda antes

    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(lista_ordenada)

    # 3,2,5,4,1
    # 0,1,2,3,4
    # 0
    # Inicia 0. 
    # 0(cero es un elemento de la lista, equivale a 1)
    # n - 1 (el primer recorrido) 4
    # entonces j se mueve en 3,2,5,4,1
    # si j es mayor que j+1. Es decir j esta en 3 y j si 3+1 = (4). No lo reacomoda porque no es mayor que 4
    # Sigue el 2
    # Si 3(j+1) es mayor que 2, lo reacomoda. 
    # Como si es mayor, mueve el 3(j+1) a la posición anterior. Como se encontraba el 3, este ahora pasa a un posición adelante
    # Y el dos queda en la posición anterior. Sucesivamente hasta que el mayor quede al final y el menor al principio.