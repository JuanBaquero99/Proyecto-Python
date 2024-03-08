class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x 
        delta_y = self.y - otra_coordenada.y 

        return (delta_x**2 + delta_y**2)**0.5

#1. Aqui se define la clase coordenadas
#2. la función se inicializa y va agregar las cordenadas X y Y
#3. Se definen los valores self de X y Y
#4. El self es para acceder a los atributos y métodos de la clase
#5. Se define el movimiento, de acuerdo al self como la coordenada y los deltas como el movimiento
#6. se retorna ese valor de acuerdo a la suma 
#7. Se define la distancia de acuerdo a su parametro de coordenada y la otra coordenada, es decir la que surgio
#8. Los deltas son la resta de la posición inicial menos la nueva coordenada. En eso encontramos la diferencia
#9. ahora retorna esos valores pero al cuadrado, método de pitagoras