import os

# sumar
def funcion1():
    os.system('cls') 
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    res = num1 + num2  
    print(f'Resultado: {res}')
    input("Presiona Enter para continuar.")

# restar
def funcion2():
    os.system('cls')  
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    res = num1 - num2  
    print(f'Resultado: {res}')
    input("Presiona Enter para continuar..")

# multiplicar
def funcion3():
    os.system('cls')  
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    res = num1 * num2  
    print(f'Resultado: {res}')
    input("Presiona Enter para continuar.")

#  dividir
def funcion4():
    os.system('cls')  
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))
    if num2 != 0:  # en esta parte Valida que no se divida entre cero
        res = num1 / num2
        print(f'Resultado: {res}')
    else:
        print("Error: No se puede dividir entre cero.")
    input("Presiona Enter para continuar ")


def run():
    while True:
        os.system('cls')  
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Salir')

        op = int(input('Selecciona una opcion: '))

        if op == 1:
            funcion1()
        if op == 2:
            funcion2()
        if op == 3:
            funcion3()
        if op == 4:
            funcion4()
        if op == 5:
            print("Saliste del programa\n")
            break
        


if __name__ == "__main__":
    run()

