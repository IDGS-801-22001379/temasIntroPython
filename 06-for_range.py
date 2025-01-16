'''
range(20) # 123 .... 19
x = range(10, 29)
y = range(1, 20, 2)

for i in range(20):
    print(i) # 0,1,2,3, 4 . ... 19 
'''
#Usando el ciclo for que se multipliquen del 1 al 10 la multiplicacion por ejemplo
#por ejemplo si pido la tabla del 1 se van a hacer por ejemplo 1 x 1 = 1..hasta la tabla... 1 x 10 = 10 
#y el final para salir 
#commt for 15/01/2025



while True:  
    print("Elige una opcion:")
    print("1. Generar tabla de multiplicar")
    print("2. Salir del programa")
    
    opcion = int(input("Ingresa tu opcion: "))  
    
    if opcion == 1:
        num = int(input("Ingresa el numero para generar la tabla de multiplicar: "))  
        for i in range(1, 11):  # Genera la tabla del 1 al 10
            print(f"{num} x {i} = {num * i}")  # Muestra la tabla
        print("Tabla de multiplicar generada. Presiona Enter para continuar...")
        input()  
    
    if opcion == 2:
        print("Saliste del programa fin :)")
        break  