import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud = int(input("Ingresa la longitud de la contraseña que deseas generar: "))
contrasena_generada = generar_contrasena(longitud)
print("La contraseña generada es:", contrasena_generada)

#README
#1. con la función que recibe un parametro 
#2. Los caracteres son iguales a la importación de strings con los ASCII que incluye todos los carecteres, con digitos y puntuación
#3. join concatena con el espacio en una elección random de caracteres que seran iterados en i según el rango de la longitud
