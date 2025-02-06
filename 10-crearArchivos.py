from io import open 
import math

#math.sqrt()
#math.pow()

lectura = ""
texto = open("archivo.txt", "r")
#texto.write("hola, soy un archivo de taxto\n")
#texto.write("hola, mundo2\n")
#lectura = texto.read()
#lectura = texto.readline()
lectura = texto.readlines()


print(type(lectura))
for i in lectura:
    print(i)

texto.close()
