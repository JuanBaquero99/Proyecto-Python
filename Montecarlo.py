import random
import collections

PALOS = ['espada', 'corazon', 'rombo', 'trebol']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jota', 'reina', 'rey']

def crear_baraja():
    barajas = []
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo, valor))

    return barajas

def obtener_mano(barajas, tamano_mano):
    mano = random.sample(barajas, tamano_mano)
    
    return mano

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = []
    for _ in range(intentos):
        mano = obtener_mano(barajas, tamano_mano)
        manos.append(mano)

    pares = 0
    for mano in manos:
        valores = []
        for carta in mano:
            valores.append(carta[1])

        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val == 2:
                pares += 1
                break

    probabilidad_par = pares / intentos
    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')


if __name__ == '__main__':
    tamano_mano = int(input('De cuantas barajas sera la mano: '))
    intentos = int(input('Cuantos intentos para calcular la probabilidad: '))

    main(tamano_mano, intentos)

#README
#1. Se crean las listas donde estaran los palos referentes al tipo de carta y los valores de número o letra
#2. La función de baraja va tener una lista vacia que se ira llenando con la iteración que se haga en palos y valores
#2.1. Hace todas las combinaciones de barajas la lista palo valor, palo valo, etc
#3. Valor que se agrega con append y retorna.
#4. La función con la que se obtiene la mano recibe la baraja (carta individual y el tamaño de la mano)
#5. Ahora se usa el random con el sample, que basicamente lo que hace es que si vi recibe valores al azar
#6. Los valores al azar que se usan, no se repiten. No vuelven a salir doble as rojo por ejemplo.
#7. En ese random se recibe las cartas y el tamaño, las cartas que se van a recibir
#8. Ahora si el main, que es una función principal que reune las otras funciones
#9. crea la baraja (la carta que se recibe) lista para ser llenada. 
#10. Al igual las manos, que es el total de las cartas. 
#11. Va iterar sin guardar en variable en un rango definido por la cantidad de intentos de la simulación
#12. la mano sera entonces la función de obtener mano que trae las cartas y el tamaño de la mano
#13. Y eso sera agregado con append a la lista de mano
#14. Ahora la que nos va a permitir encontrar los pares de cartas
#15. Donde guarda la variable iterando en la lista que ya fue llenada en manos
#16. Va a guardar los valores correpsondientes a numeros y letras 
#17. va a iterar y guardar en carta según el recorrido en mano 
#18. con append sera guardado en valores lo que recorrio carta en la posición 1 (Recordar que 1 es el valor 0 es carta)
#19. el contador usa la función que permite crear un diccionario extrayendo los valores
#20. ahora va a iterar y recoger en val a lo que acceda en el contador de los valores del diccionario
#21. Luego, si encuentra 2 (par) va a sumar 1 a la variable par
#22. La probabilidad de pares se encuentra por tanto diviendo los pares con los intentos
