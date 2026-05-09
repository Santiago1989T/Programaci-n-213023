# comment
nombre = "hola"
print("hola")

import logging
from abc import ABC, abstractmethod
from datetime import datetime

# Configuración de Logs
logging.basicConfig(
    filename='software_fj_errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SoftwareFJError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando una reserva no cumple los requisitos."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando el servicio solicitado está agotado o fuera de horario."""
    pass
class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Encapsulamiento protegido

    @abstractmethod
    def mostrar_detalle(self):
        pass

class Servicio(EntidadBase):
    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

    def mostrar_detalle(self):
        return f"Servicio: {self.nombre} (ID: {self._id_entidad})"

# Clases Derivadas
class SalaReunion(Servicio):
    def calcular_costo(self, horas):
        # Aplicamos un recargo si son más de 5 horas (Lógica de negocio)
        if horas > 5:
            return (self.precio_base * horas) * 0.9  # Descuento 10%
        return self.precio_base * horas

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias):
        return self.precio_base * dias
class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, email):
        super().__init__(id_cliente)
        self.__nombre = nombre
        self.__email = self.__validar_email(email)

    def __validar_email(self, email):
        if "@" not in email:
            raise ValueError(f"Email inválido: {email}")
        return email

    @property
    def nombre(self):
        return self.__nombre

    def mostrar_detalle(self):
        return f"Cliente: {self.__nombre} | Contacto: {self.__email}"
if __name__ == "__main__":
    sistema = sistema_reserva() 

    try:
        # 1. Creación de datos
        cliente1 = Cliente("C001", "Abraham Corredor", "abraham@ejemplo.com")
        sala_vips = SalaReunion("S101", "Sala Ejecutiva", 50.0)
        laptop = AlquilerEquipo("E201", "Laptop Gaming", 30.0)

        # 2. Operación Normal
        sistema.registrar_reserva(cliente1, sala_vips, 6) # Con descuento

        # 3. Operación con Error de Lógica (Cantidad negativa)
        sistema.registrar_reserva(cliente1, laptop, -1)

        # 4. Operación con Error de Tipo (Simulación de caída controlada)
        # Intentar calcular costo con un string en lugar de número
        sistema.registrar_reserva(cliente1, sala_vips, "ocho")

    except ValueError as e:
        print(f"Error crítico al crear entidades: {e}")
    
    # El sistema sigue vivo y puede mostrar resultados
    sistema.listar_reservas()