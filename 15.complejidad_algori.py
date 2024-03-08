import time
import sys
sys.setrecursionlimit(1000000)

def factorial(n): #función que recibe el parametro n
    respuesta = 1
    

    while n > 1: #mientras que n sea mayor que 1 ejecutar el ciclo
        respuesta *= n #Supongamos que n(3) es decir multiplicado por 1 
        n -= 1 # n(3) se le resta 1 (queda en 2) 
    
    return respuesta #Ese resultado se retorna, es decir vuelve a respuesta
    #Así sucesivamente hasta llegar a 1, cuando el sistema se detiene y da el resultado

def factorial_recursive(n):
    if n == 1: #Raiz de 1 es 1. Por lo tanto evitamos que el programa haga esfuerzos
        return 1

    return n * factorial_recursive(n - 1) #Ahora sabemos que n(3) multiplicado por factorial_recursive (n-1)
    #Devuelve el valor a n y continua la operación. 

#Aqui se definio una función mas eficaz. 

if __name__ == '__main__':
    n = 200000 #De acuerdo al valor se demora más o menos

    comienzo = time.time() #Dicha función de tiempo es importada. Mide tiempo de inicio
    factorial(n)
    final = time.time() #Mide tiempo en terminar 
    print(final - comienzo) #Para encontrar la diferencia restamos cuanto se demoro en iniciar con finalizar
    

    comienzo = time.time()
    factorial_recursive(n)
    final = time.time()
    print(final - comienzo)
    
    #README
    #1. Importante acá entender es que de acuerdo al número que reciba n realizara la operación de raíz
    #2. Es decir que entre más alto el valor más se demora
    #3. Aquí es donde se evalúa que algoritmo es más eficiente, por ejemplo el recursivo que es el el segundo
    #4 Por ejemplo si buscamos al raíz de 200000, con la primera función 13s y con la segunda 11s. 
    
    
    

