# Nombres: Abraham Camilo Corredor Duran-
#          Johan Santiago Mateus Alba- 
# Curso : Programación
# Grupo : 198
#comment
# Inicio del codigo

import logging
from abc import ABC, abstractmethod

# --- CONFIGURACIÓN DE LOGS ---
logging.basicConfig(
    filename='software_fj_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# --- EXCEPCIONES PERSONALIZADAS ---
class SoftwareFJError(Exception): pass
class DatoInvalidoError(SoftwareFJError): pass

# --- CLASES BASE Y SERVICIOS ---
class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

class Servicio(EntidadBase, ABC):
    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

class SalaReunion(Servicio):
    def calcular_costo(self, horas):
        return self.precio_base * horas

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        return self.precio_base * dias

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, sesiones):
        # Las asesorías tienen un cargo fijo administrativo de 10.000
        return (self.precio_base * sesiones) + 10.000

# --- CLASE CLIENTE ---
class Cliente:
    def __init__(self, nombre, correo):
        if not nombre or "@" not in correo:
            raise DatoInvalidoError("Datos de cliente mal formados.")
        self.__nombre = nombre  # Encapsulamiento privado
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

# --- SISTEMA INTEGRAL ---
class SistemaSoftwareFJ:
    def __init__(self):
        self.servicios = {
            "1": SalaReunion("S01", "Reserva de Sala", 50000),
            "2": AlquilerEquipo("E01", "Alquiler de PC/Proyector", 30000),
            "3": AsesoriaEspecializada("A01", "Asesoría Técnica", 80000)
        }
        self.reservas = []

    def ejecutar(self):
        print("--- BIENVENIDO Al SOFTWARE ---")
        
        try:
            # 1. Registro de Cliente
            nombre = input("Ingrese nombre del cliente: ")
            email = input("Ingrese correo electrónico: ")
            cliente = Cliente(nombre, email)

            # 2. Selección de Servicio
            print("\nServicios Disponibles:")
            for k, v in self.servicios.items():
                print(f"{k}. {v.nombre} (${v.precio_base})")
            
            opcion = input("Seleccione el tipo de servicio (1-3): ")
            if opcion not in self.servicios:
                raise DatoInvalidoError("Opción de servicio no válida.")

            servicio_elegido = self.servicios[opcion]

            # 3. Cantidad (Horas/Días/Sesiones)
            cantidad_str = input(f"Ingrese la cantidad (horas) para {servicio_elegido.nombre}: ")
            if not cantidad_str.isdigit():
                raise ValueError("La cantidad debe ser un número entero.")
            
            cantidad = int(cantidad_str)
            total = servicio_elegido.calcular_costo(cantidad)

            # 4. Confirmación y Almacenamiento
            reserva = {
                "cliente": cliente.nombre,
                "servicio": servicio_elegido.nombre,
                "total": total
            }
            self.reservas.append(reserva)

            print(f"\n--- RECIBO DE RESERVA ---")
            print(f"Cliente: {reserva['cliente']}")
            print(f"Servicio: {reserva['servicio']}")
            print(f"Total a Pagar: ${total}")

        except DatoInvalidoError as e:
            print(f"Error de validación: {e}")
            logging.error(f"Validación fallida: {e}")
        except ValueError as e:
            print("Error: Se esperaba un valor numérico.")
            logging.error(f"Error de valor: {e}")
        except Exception as e:
            # Encadenamiento y captura general para mantener la estabilidad
            print(f"Ocurrió un error inesperado. El sistema sigue activo.")
            logging.error(f"Error crítico: {e}", exc_info=True)
        finally:
            print("\nGracias por usar el sistema de Software.")

# --- INICIO DE LA APLICACIÓN ---
if __name__ == "__main__":
    app = SistemaSoftwareFJ()
    # Ciclo para que la app no se cierre tras un error
    while True:
        app.ejecutar()
        if input("\n¿Desea realizar otra operación? (si/no): ").lower() != 'si':
            break
    

import logging
from datetime import datetime

# ============================================================
# CONFIGURACIÓN DEL ARCHIVO LOG
# ============================================================


logging.basicConfig(
    filename="reservas.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ============================================================
# CLASE RESERVA
# ============================================================

class Reserva:

    # --------------------------------------------------------
    # Constructor
    # --------------------------------------------------------
 
    def __init__(self, cliente, servicio, duracion, costo_base):

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.costo_base = costo_base
        self.estado = "Pendiente"

        logging.info(f"Reserva creada para {self.cliente}")

    # --------------------------------------------------------
    # Método para confirmar la reserva
    # --------------------------------------------------------

    def confirmar(self):

        try:

            if self.estado == "Cancelada":
                raise Exception("No se puede confirmar una reserva cancelada")

            self.estado = "Confirmada"

            logging.info(
                f"Reserva confirmada para {self.cliente}"
            )

            print("Reserva confirmada correctamente")

        except Exception as error:

            logging.error(f"Error al confirmar reserva: {error}")
            print("Error:", error)

    # --------------------------------------------------------
    # Método para cancelar la reserva
    # --------------------------------------------------------

    def cancelar(self):

        try:

            if self.estado == "Cancelada":
                raise Exception("La reserva ya estaba cancelada")

            self.estado = "Cancelada"

            logging.info(
                f"Reserva cancelada para {self.cliente}"
            )

            print("Reserva cancelada correctamente")

        except Exception as error:

            logging.error(f"Error al cancelar reserva: {error}")
            print("Error:", error)

    # --------------------------------------------------------
    # Método para procesar la reserva
    # --------------------------------------------------------
  

    def procesar(self):

        try:

            if self.estado != "Confirmada":
                raise Exception(
                    "La reserva debe estar confirmada antes de procesarse"
                )

            logging.info(
                f"Reserva procesada para {self.cliente}"
            )

            print("Reserva procesada exitosamente")

        except Exception as error:

            logging.error(f"Error al procesar reserva: {error}")
            print("Error:", error)

    # --------------------------------------------------------
    # Cálculo simple del costo
    # --------------------------------------------------------

    def calcular_costo(self):

        return self.costo_base

    # --------------------------------------------------------
    # Cálculo con impuesto
    # --------------------------------------------------------

    def calcular_costo_impuesto(self, impuesto):

        total = self.costo_base + (self.costo_base * impuesto)

        return total

    # --------------------------------------------------------
    # Cálculo con impuesto y descuento
    # --------------------------------------------------------

    def calcular_costo_completo(self, impuesto=0, descuento=0):

        total = self.costo_base

        # Aplicar impuesto
        total += total * impuesto

        # Aplicar descuento
        total -= total * descuento

        return total

    # --------------------------------------------------------
    # Mostrar información completa
    # --------------------------------------------------------

    def mostrar_reserva(self):

        print("\n========== RESERVA ==========")
        print("Cliente:", self.cliente)
        print("Servicio:", self.servicio)
        print("Duración:", self.duracion, "horas")
        print("Costo base:", self.costo_base)
        print("Estado:", self.estado)
        print("=============================\n")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

try:

    # Crear objeto reserva
    reserva1 = Reserva(
        "Santiago Mateus",
        "Spa Premium",
        3,
        150000
    )

    # Mostrar información
    reserva1.mostrar_reserva()

    # Confirmar reserva
    reserva1.confirmar()

    # Procesar reserva
    reserva1.procesar()

    # ========================================================
    # PRUEBAS DE LOS MÉTODOS SOBRECARGADOS
    # ========================================================

    print("Costo normal:",
          reserva1.calcular_costo())

    print("Costo con impuesto:",
          reserva1.calcular_costo_impuesto(0.19))

    print("Costo con impuesto y descuento:",
          reserva1.calcular_costo_completo(
              impuesto=0.19,
              descuento=0.10
          ))

    # Cancelar reserva
    reserva1.cancelar()

except Exception as error_general:

    logging.critical(f"Error general del sistema: {error_general}")
    print("Error crítico:", error_general)    
