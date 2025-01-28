class Distancia:
    def __init__(self):
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

    def pedir_coordenadas(self):
        self.x1 = float(input("Ingrese la coordenada x1: "))
        self.x2 = float(input("Ingrese la coordenada x2: "))
        self.y1 = float(input("Ingrese la coordenada y1: "))
        self.y2 = float(input("Ingrese la coordenada y2: "))

    def calcular_distancia(self):
        self.d = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        print("La distancia es: {:.2f}".format(self.d))

def main():
    obj = Distancia()    
    obj.pedir_coordenadas() 
    obj.calcular_distancia()

if __name__ == "__main__":
    main()

        
    
