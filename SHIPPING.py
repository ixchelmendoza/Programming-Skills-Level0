import sys
import random

class SistemaEnvio:
    def __init__(self):
        self.intentos_login = 0
        self.MAX_INTENTOS_LOGIN = 3
        self.inicio_sesion = False

    def login(self):
        while self.intentos_login < self.MAX_INTENTOS_LOGIN:
            usuario = input("Ingresa tu nombre de usuario: ")
            contrasena = input("Ingresa tu contraseña: ")

            # Supongamos un nombre de usuario y contraseña simples para el ejemplo
            if usuario == "usuario" and contrasena == "contrasena":
                print("Inicio de sesión exitoso.")
                self.inicio_sesion = True
                return True
            else:
                print("Nombre de usuario o contraseña incorrectos. Por favor, intenta nuevamente.")
                self.intentos_login += 1

        print("Demasiados intentos incorrectos. Sistema bloqueado.")
        sys.exit()

    def mostrar_menu(self):
        print("\nMenú del Sistema de Envío:")
        print("1. Enviar un Paquete")
        print("2. Salir")

    def enviar_paquete(self):
        nombre_remitente = input("Ingresa el nombre del remitente: ")
        nombre_destinatario = input("Ingresa el nombre del destinatario: ")
        peso = float(input("Ingresa el peso total del paquete (en kg): "))

        # Generar un número de paquete aleatorio
        numero_paquete = random.randint(1000, 9999)

        # Calcular el precio del envío ($2 por kg)
        precio_envio = peso * 2

        print(f"\n¡Paquete enviado con éxito!")
        print(f"Número de Paquete: {numero_paquete}")
        print(f"Remitente: {nombre_remitente}")
        print(f"Destinatario: {nombre_destinatario}")
        print(f"Peso Total: {peso} kg")
        print(f"Precio del Envío: ${precio_envio:.2f}")

    def ejecutar(self):
        if not self.inicio_sesion:
            self.login()

        while True:
            self.mostrar_menu()
            opcion = input("Ingresa tu opción (1 o 2): ")

            if opcion == "1":
                self.enviar_paquete()
            elif opcion == "2":
                print("Saliendo del sistema. ¡Gracias!")
                sys.exit()
            else:
                print("Opción no válida. Por favor, ingresa 1 o 2.")

            otra_operacion = input("¿Quieres realizar otra operación? (sí/no): ")
            if otra_operacion.lower() != 'sí':
                print("Saliendo del sistema. ¡Gracias!")
                sys.exit()

if __name__ == "__main__":
    sistema_envio = SistemaEnvio()
    sistema_envio.ejecutar()
