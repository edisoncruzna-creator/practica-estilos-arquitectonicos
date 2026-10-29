"""CONSUMIDOR: simula el envío de un correo al estudiante."""


def enviar_correo(evento):
    print(f"  [Notificaciones] Correo a {evento['estudiante']}: "
          f"tu nota de {evento['materia']} es {evento['nota']}")
