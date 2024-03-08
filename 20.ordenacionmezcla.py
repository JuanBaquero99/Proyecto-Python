import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1: #Si la lista tiene un tamaño mayor a 1
        medio = len(lista) // 2 #El medio vendría siendo la longitud de la lista divido 2
        izquierda = lista[:medio] #Sublista donde inicia desde 0 hasta la mitad
        derecha = lista[medio:] #Sublista donde inicia desde mitad hasta cero 
        print(izquierda, '*' * 5, derecha)

        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda) #Llama a la función de ordenamiento pero esta vez el parametro que recibe es sublista izquierda
        ordenamiento_por_mezcla(derecha) #Llama a la función de ordenamiento pero esta vez el parametros que recibe es sublista derecha

        # Iteradores para recorrer las dos sublistas
        i = 0 
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha): # va operar mientras i sea menor al tamaño de la lista de la izquierda y j igual (tengan longitudes iguales tanto i como j)
            if izquierda[i] < derecha[j]: # si el elemento izquierda(i) es mayor que derecha(j) 
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)

    #Readme
    #1. Hay que pensar que al volverse más pequeño tiene un crecimiento algoritmo. Ya que cada vez hace más pasos el programa para dividir
    #2. Define una función que su parametro es la lista
    #3. Si la longitud de la lista es mayo que 1, retorna el valor a lista
    #4. Medio es la longitud de la lista divido en 2
    #5. Izquierda vendría siendo el inicio de la lista hasta el medio que definimos anteriormente
    #6. Derecha vendría siendo el inicio de medio hasta el final de la lista
    #7. Llamanos dos funciones recursivas (es decir, estamos usando el modelo de la función anterior)
    #8. La diferencia es que estas funciones reciben como parametro lo que se definio en la varibale izquierda derecha 
    #9. Iterador para la lista principal (k) es decir la que se va a ir armando
    #10. Iteradores para las sublistas (las que se van a ir diviendo gracias a las funciones recursivas)
    #11. El while va a recorrer mientras las sublistas izquierda y derecha tengan menos elemento que i y j.
    #12. Si el elemento (i) donde se esta iterando, es mayor que la derecha, se agrega a la lista k. 
    #13. La iteración de i se la suma un elemento para seguir avanzando a la siguiente posición
    #14. Es decir que se agregue un elemento a la izquierda o derecha, se suma 1 a la iteración para que inicie desde el siguiente elemento en la lista y no vuelta a comenzar desde 0
    #15. Luego los elementos restantes de la izquierda se agregan a la nueva lista k 
    #16. Luego los elementos restantes de la derecha se agregan a la nueva lista k
    #17. Conforme se va sumando a la 1 a la iteración de i, j y k para que avancen al siguiente elemento de la lista
    #18. Retorna a lista para iniciar de nuevo el proceso
    #19. Hasta que al final todo queda agregado a la lista principal pero en orden 

