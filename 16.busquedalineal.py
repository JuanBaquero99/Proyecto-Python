import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista: # O(n) tenemos un loop que su crecimiento depende del input de lista
        if elemento == objetivo: #Si el elemento es igual al objetivo
            match = True 
            break #Termina el programa

    return match

if __name__ == '__main__':

    tamaño_de_lista = int(input("De que tamaño sera la lista: ")) #Un input que nos da tamaño de la lista 
    objetivo = int(input('Que número quieres encontrar de 1 a 100: ')) #Aunque sea un input es un valor referencial 
    lista = [random.randint(0, 100) for i in range (tamaño_de_lista)] #Va arrojar números de 1 a 10 para i en un rango del input de tamaño que escoja la persona
    encontrado = busqueda_lineal(lista, objetivo) #Encontrar es el resultado de la función elemento == objetivo
    print (lista)
    print (f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')

#Readme 
#1. Es un crecimiento linea toda vez que el crecimiento esta dado al input que recibe. es Big O(n)
#2. Porque recibe un valor y de acuerdo a ese realiza el recorrido. Valor exacto que termina al momento de recorrer el rango del tamaño de la lista
#3. A diferencia si hubiera una condición que luego los multiplicara y diera un crecimiento exponencial
#4. Fijarnos que el algoritmo de Big O(n) se encuentra en la lista, porque es el elementos que crece de acuerdo al input

