import random

def busqueda_binaria(lista, comienzo, final, objetivo): #Recibimos una lista y com,fin,obj
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}') #para ver la operación. Si venimos de un len, se le resta -1
    if comienzo > final: #Si el comienzo es más grande que el final significa que no se encontro
        return False

    medio = (comienzo + final) // 2 #Dividir la lista en 2. (0 + 100 // 2 == 50 (mitad))

    if lista[medio] == objetivo: #Si en la lista medio esta el objetivo 
        return True
    elif lista[medio] < objetivo: #Si el objetivo es menor que medio
        return busqueda_binaria(lista, medio + 1, final, objetivo) #Hacemos lista más a la derecha, es decir que si la mitad es 50, sumado queda 51, siendo el comienzo y retorna a la función.
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo) #Si no lo movemos al otro lado, es decir que el final es 49.  


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

    #README
    #1. La función va a recibir la lista que digite la persona, inicia desde 0, su final es la longitud de la lista
    #2. La longitu con len es interpretada de acuerdo a lo que el usuario digite
    #3. La función va a determinar, restar y dividir comienzo y final (ej: 100//2 = 50) (ej. Nuestro objetivo es 80)
    #4. Luego en esa lista en la mitad va determinar si esta el objetivo
    #5. Si el objetivo es mayor que esa mitad, va a hacer uso de una función recursiva que se va retornar
    #5. Esa función va a determinar la lista, el medio (divido) le va a sumar uno (51) va a dejar su final (ej:100)
    #6. Luego esa mitad (51-100) va ser divida en 2 (75). Ahi sigue dos caminos la busqueda de 75 de nuevo hasta 100
    #7. Entre más pequeño determina si esta o no esta
    #8. La otra función recursiva cumple el mismo objetivo pero a la izquierda (restando) retorna el procedimiento