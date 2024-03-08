
class Campo:
    def __init__(self):
        self.coordenadas_de_borrachos = {}
    
    def anadir_borracho(self, borracho, coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada
    
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x, delta_y)
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada


    def obtener_coordenada(self, borracho):
        return self.coordenadas_de_borrachos[borracho]


#1. Se crea la clase campo
#2. Se inicializa la función que recibe el self
#3. Son las coordenadas del borracho que guarda en un diccionario
#4. Se define la función que añade borrachos donde recibe el self, el borracho y la coordenada
#5. Dicho diccionario de la cordenada indica que su llave es el borracho y su valor la coordenada
#6. Define el movimiento de borracho siendo aleatoria 
#7. la coordenada actual es la cordenada del borracho que esta esta en la llave del diccionario
#8. se obtiene la nueva coordenada que es el resultado de la cordenada actual diciendo que se mueva según los deltas
#9. la coordenada de borracho es la nueva coordenada obtenida
#10. Se define la función que nos permite obtener la coordenada
#11. Que retorna el valor de las coordenadas del borracho y el borracho