"""Ensambla el sistema: crea el bus, conecta los consumidores y arranca el emisor.

Para agregar un comportamiento nuevo basta con suscribir un consumidor nuevo.
El emisor (RegistroNotas) no se modifica.
"""
from bus_eventos import BusEventos
from consumidores import auditoria, estadisticas, notificaciones
from registro_notas import RegistroNotas

bus = BusEventos()
bus.suscribir("NotaRegistrada", notificaciones.enviar_correo)
bus.suscribir("NotaRegistrada", estadisticas.actualizar)
bus.suscribir("NotaRegistrada", auditoria.registrar)

registro = RegistroNotas(bus)

if __name__ == "__main__":
    print("Registro de notas dirigido por eventos (Enter vacío para salir)")
    while True:
        nombre = input("\nEstudiante: ").strip()
        if not nombre:
            break
        materia = input("Materia: ").strip() or "Arquitectura"
        try:
            registro.registrar(nombre, materia, float(input("Nota (0-10): ")))
        except ValueError as error:
            print(f"Error: {error}")
