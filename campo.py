from borracho import BorrachoTradicional
from campo.borracho import Campo 
from coordenadas import Coordenada 
from bokeh.plotting import figure, show

def graficar(x, y):
    grafica = figure(title='Camino aleatorio', x_axis_label='pasos', y_axis_label='distancia')
    grafica.line(x, y, legend_label='distancia media', line_width=2)
    show(grafica)

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    distancias_media_por_caminata = []
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_por_caminata.append(distancia_media)
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
    graficar(distancias_de_caminata, distancias_media_por_caminata)

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)


#1. Importamos los otros modulos
#2. La función de caminata inicia esta dada por los valores del método campo al obtener las coordenadas del (borrracho), método importado
#3. La función de simular caminata va a recibir los pasos, numero de intentos y el tipo de borrachos
#4 El borracho va a ser el importado que le vamos a asignar un nuevo nombre
#5. El origen va a ser de lo importado del método de obtención de coordenadas que inicia en 0
#6. Las distancias se van a ir almacenando
#7. La función caminata su inicio va a estar dado por el método importado de campo donde se obtiene según la posición de borracho
#8. Va a recorrer con el fo sin asignar una variable en un rango que depende del número de intentos, es decir cuantas veces va a correr el loop
#9. se va a añadir un campo con el método importado 
#10. Al campo le va añadir el borracho con el borracho en el origen
#11. La simulacion de caminata es igual a la caminata recibiendo el campo, el borracho y los pasos
#12. Luego a las distancias se le va a agregar con el append y el round 1 permite que no tenga decimales
#13. Ahora recore en pasos según la distancia de caminata
#14. Las distancias que son la simulacion es decir los pasos, el numero de intentos y el tipo de borracho
#15. La distancia media que con el round lo deja en entero que es igual a la suma de las distancias divido entre cuantas distancias se recorrio 
#16. Se redondea a 4 decimales. 
#17. La maxima se saca con la función de max
#18. La minima con la función min   