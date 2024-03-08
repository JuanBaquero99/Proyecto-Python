def divide_elementos (lista, divisor):
    try:
     return [i / divisor for i in lista]
    except ZeroDivisionError as e:
       print(e)
       return list

lista =list(range(10))
divisor = 0

print (divide_elementos(lista, divisor))

#README
# try y except van a atrapar el error que da dividir por 0 (ZeroDivisionError) lo va a dejar pasar
# el print nos va a permitir ver como el error retorna y deja continuar la ejecución. Asimismo cual error se esta guardando
# Hay que tener cuidado al momento de silenciar estos errores porque nos pueden crear bugs
# Una buena práctica de programación es ser claro con la definición del error
# Y no silenciar cualquier error


