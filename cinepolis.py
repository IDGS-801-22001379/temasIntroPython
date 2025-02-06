import os

class Cinepolis:
    def __init__(self):
        self.ventas = []
        
        with open("ticketDeCompra.txt", "w") as file:
            file.write("")

    def calcular_costo_total(self, nombre, cantidad_boletos, usa_cineco):
        precio_boleta = 12
        total = precio_boleta * cantidad_boletos
        descuento = 0

        if cantidad_boletos > 5:
            descuento = total * 0.15
        if 3 <= cantidad_boletos <= 5:
            descuento = total * 0.10

        total -= descuento

        if usa_cineco:
            descuento_cineco = total * 0.10
            total -= descuento_cineco

        self.ventas.append((nombre, cantidad_boletos, total))

        with open("ticketDeCompra.txt", "a") as file:
            file.write(f"Nombre: {nombre}\nBoletos: {cantidad_boletos}\nTotal: ${total:.2f}\n\n")

        print(f"\nResumen de la compra para {nombre}:")
        print(f"Cantidad de boletos: {cantidad_boletos}")
        print(f"Total a pagar: ${total:.2f}\n")

    def mostrar_tabla(self):
        print("\nResumen de Ventas:")
        print("{:<15} {:<10} {:<10}".format("Nombre", "Boletos", "Total"))
        print("-" * 35)
        for venta in self.ventas:
            print("{:<15} {:<10} {:<10.2f}".format(venta[0], venta[1], venta[2]))
        print("-" * 35)

    def menu(self):
        while True:
            print("\n1. Comprar boletos\n2. Terminar y mostrar ventas\n")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                nombre = input("Ingrese su nombre: ")

                while True:
                    try:
                        personas = int(input("Ingrese el total de personas (incluyéndose): "))
                        if personas > 0:
                            max_boletos = personas * 7
                            break
                        print("Debe haber al menos una persona.")
                    except ValueError:
                        print("Opción no válida. Ingrese un número válido.")

                cantidad_boletos = 0

                while cantidad_boletos == 0 or cantidad_boletos > max_boletos:
                    try:
                        cantidad_boletos = int(input(f"¿Cuántos boletos desea comprar? (Máximo permitido: {max_boletos}) "))

                        if cantidad_boletos > max_boletos:
                            print(f"No puede comprar más de {max_boletos} boletos.")
                            while True:
                                print("1. Cambiar número de boletos")
                                print("2. Cambiar número de personas")
                                opcion_cambio = input("Seleccione una opción: ")

                                if opcion_cambio == "1":
                                    while True:
                                        try:
                                            nueva_cantidad = int(input("Ingrese la nueva cantidad de boletos: "))
                                            if nueva_cantidad <= max_boletos:
                                                cantidad_boletos = nueva_cantidad
                                                break
                                            print(f"No puede comprar más de {max_boletos} boletos.")
                                        except ValueError:
                                            print("Opción no válida. Ingrese un número válido.")
                                    break

                                if opcion_cambio == "2":
                                    while True:
                                        try:
                                            nueva_personas = int(input("Ingrese el nuevo número total de personas: "))
                                            if nueva_personas > 0:
                                                personas = nueva_personas
                                                max_boletos = personas * 7
                                                break
                                            print("Debe haber al menos una persona.")
                                        except ValueError:
                                            print("Opción no válida. Ingrese un número válido.")
                                    break

                                print("Opción no válida. Intente nuevamente.")
                    except ValueError:
                        print("Opción no válida. Ingrese un número válido.")

                # Menú de pago
                while True:
                    print("\nSeleccione método de pago:")
                    print("1. Efectivo")
                    print("2. Tarjeta Cineco")
                    metodo_pago = input("Ingrese el número de su opción: ")
                    
                    if metodo_pago == "1":
                        usa_cineco = False
                        break
                    if metodo_pago == "2":
                        usa_cineco = True
                        break
                    
                    print("Opción no válida. Intente nuevamente.")

                self.calcular_costo_total(nombre, cantidad_boletos, usa_cineco)

            if opcion == "2":
                self.mostrar_tabla()
                print("Gracias por usar el sistema de Cinepolis.")
                break

            print("Opciónes no valida.")

def main():
    cinepolis = Cinepolis()
    cinepolis.menu()

if __name__ == "__main__":
    main()








