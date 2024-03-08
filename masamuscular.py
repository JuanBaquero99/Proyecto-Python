def imc(altura, peso):
    masa = peso / (altura ** 2)
    return masa

if __name__ == '__main__':
    altura = float(input('Cual es su altura en metros: '))
    peso = float(input('Cual es su peso en kilogramos: '))
    resultado = imc(altura, peso)
    print("Su Índice de Masa Corporal (IMC) es:", resultado)
