import random

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        tiro = random.choice([1, 2, 3, 4, 5, 6])
        secuencia_de_tiros.append(tiro)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)

    tiros_con_1 = 0
    for tiro in tiros:
        if 1 not in tiro:
            tiros_con_1 += 1

    probabilidad_tiros_con_1 = tiros_con_1 / numero_de_intentos
    print(f'Probabilidad de no obtener por lo menos un 1 en {numero_de_tiros} tiros = {probabilidad_tiros_con_1}')



if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)

#README
#1. La función tirar dado recibe el parametro de numero de tiros
#2. Y secuencia de tiros es una lista que se va a llenar
#3. Va a hacer un recorrido en el rango del numero de tiros (lo escogido por la persona)
#4. Tiro que va a ser en una elección random de 1 a 6 (la cantidad de caras del dado)
#5. A la secuencua de tiros se va a agregar de acuerdo al tiro que reciba es su parametro 
#6. retorna a secuencia de tiros.
#7. Se define el main, recibe parametros de numero de tiros y el numero de intentos
#8. Tiros sera una lista para llenar.
#9. Va a hacer un recorrido en el rango de número de intentos (lo escogido por la persona)
#10. la secuencia de tiros se le asigna tirar dado con su parametro de numero de tiros.
#11. A tiros se le agrega segun la secuencia de tiros
#12. tiros con 1 inicia vacia
#13. para el recorrido de tiro en tiros. Si 1 no esta en tiro, se le suma a tiros con 1
#14. la probabilidad de tiros con 1 es determinada por los tiros con 1 divido por el número de intento. Esto saca el porcentaje de probabilidad
#15. En conclusión esta recibiendo el número de tiros y cuantas veces lo va a intentar (es decir cuantas veces va a tirar el dado para encontrar 1)
#16. El número de intentos es las veces que la simulación va a volver a iniciar hasta acercarse al 1 de acuerdo a la caida del dado
#17. Con la función vamos a recibir el tiro del dado que va a ir almacenando los resultados tiros que va dando
#18. Y así puede ir almacenando que números caen (como 1)
#19. Luego con la cantidad de tiros y la cantidad de veces que se va a ejecutar, en una función recursiva
#20. Es decir, va a recibir la cantidad de dados, las simulaciones. Va a escoger los números al azar que va a ir almacenando
#21. Es tiros luego seran almacenados en otra lista donde no recoge los números del 1 al 6 al azar, sino que recoge como tal los itentos
#21. Al final, si al recorrer los dados que caen no estan en uno, se dividen por el número de intentos 
#22. Asi obtenemos que La probabilidad de obtener por lo menos un 1 en el numero de tiros tiene un probabilidad