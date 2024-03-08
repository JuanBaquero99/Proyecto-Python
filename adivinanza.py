import random
 
seleccion = int(input('Escoge un número del 1 al 10: '))

numeros = [1,2,3,4,5,6,7,8,9,10]
ran = random.randint(0,10)

if seleccion == ran:
        print ('Adivinaste el número')
elif seleccion <= ran or seleccion >= ran:
    print ('No adivinaste')
        
print (f'El computador escogio: {ran}')


 
    