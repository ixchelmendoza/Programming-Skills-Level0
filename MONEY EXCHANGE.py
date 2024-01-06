import sys

class ConvertidorDivisas:
    tasas_cambio = {'CLP': 1, 'ARS': 9.65, 'USD': 0.001, 'EUR': 0.0009, 'TRY': 0.008, 'GBP': 0.0008}
    limites = {'CLP': (1000, 1000000), 'ARS': (100, 10000), 'USD': (10, 1000), 'EUR': (10, 1000), 'TRY': (50, 5000), 'GBP': (8, 800)}

    def mostrar_menu(self):
        print("\nMenú de Convertidor de Divisas:\n1. Convertir Moneda\n2. Salir")

    def convertir_moneda(self):
        moneda_inicial, moneda_destino = input("Moneda inicial y moneda destino (ej. CLP USD): ").split()
        cantidad = float(input("Cantidad a convertir: "))

        if moneda_inicial not in self.tasas_cambio or moneda_destino not in self.tasas_cambio:
            print("Moneda no válida. Elige una moneda válida.")
            return

        if not self.limites[moneda_inicial][0] <= cantidad <= self.limites[moneda_inicial][1]:
            print("Cantidad fuera de los límites permitidos.")
            return

        cantidad_convertida = cantidad * self.tasas_cambio[moneda_destino]

        print(f"\n{cantidad} {moneda_inicial} es equivalente a {cantidad_convertida:.2f} {moneda_destino}")

        if input("¿Retirar fondos? (sí/no): ").lower() == 'sí':
            comision = cantidad * 0.01
            cantidad_retirada = cantidad - comision
            print(f"Se aplicó una comisión del 1%. Cantidad a retirar: {cantidad_retirada:.2f} {moneda_inicial}")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingresa tu opción (1 o 2): ")

            if opcion == "1":
                self.convertir_moneda()
            elif opcion == "2":
                print("Saliendo del convertidor de divisas. ¡Gracias!")
                sys.exit()
            else:
                print("Opción no válida. Ingresa 1 o 2.")

if __name__ == "__main__":
    ConvertidorDivisas().ejecutar()
