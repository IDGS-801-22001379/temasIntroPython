'''
x = 0

while x < 10:
    print(x)
    x = x + 1 

'''

''''''''' operaciones de multiplicaccion de a x b utilizando sumas 
a = 3
b = 4
salida: 3+3+3+3= 12

se tiene que har con wile y ban a hacer datos que se van a pedir,
y luego hacer el contador el valor de a y de esa manera sale el 3 
4 veces y se combierte en un string, 

'''

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

# en esta parte se van a inicializar las variables 
resultado = 0
operacion = ""
contador = 0

while contador < b:
    resultado += a   #en esta parte se suma 'a' al resultado
    operacion += str(a)
    if contador < b - 1:
        operacion += " + "
    contador += 1 #inclementa el contador 


print(f"la multiplicación {operacion} es: {resultado}")





