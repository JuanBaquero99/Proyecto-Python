import random

class Borrachos: 
    def __init__(self, nombre):
        self.nombre = nombre

class BorrachoTradicional(Borrachos):  # Corregido el nombre de la clase y agregada la herencia
    def __init__(self, nombre):
        super().__init__(nombre)

    def camina(self):  # Movido dentro de la clase y corregida la indentación
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])  # Corregida la tupla de opciones

#README
#1. Definimos la clase de borracho
#2. La iniciamos con un argumento de valor y el nombre
#3. Ahora definimos la subclase heredada de borracho tradicional
#4. el cual se incializa y recibe los dos parametros
#5. el super permite reutilizar el método de la clase base (Borrachos)
#6. Es decir su self.nombre es el nombre
#7. Se define como va a caminar, en una selección random
#8. Se mueve en los ejes X y Y tanto a la derecha como a la izquierda