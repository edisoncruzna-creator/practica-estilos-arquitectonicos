"""CANAL / GESTOR DE EVENTOS (un "broker" mínimo, como una versión de juguete de Kafka o RabbitMQ).

- suscribir(tipo, funcion): un consumidor declara qué eventos le interesan.
- publicar(tipo, datos): un emisor anuncia que algo ocurrió. No sabe quién escucha.
"""
from collections import defaultdict
from datetime import datetime


class BusEventos:
    def __init__(self):
        self._suscriptores = defaultdict(list)

    def suscribir(self, tipo_evento, funcion):
        self._suscriptores[tipo_evento].append(funcion)

    def publicar(self, tipo_evento, datos):
        evento = {"tipo": tipo_evento, "fecha": datetime.now().strftime("%H:%M:%S"), **datos}
        print(f"\n[BUS] {evento['fecha']} publicado «{tipo_evento}» -> "
              f"{len(self._suscriptores[tipo_evento])} consumidor(es)")
        for funcion in self._suscriptores[tipo_evento]:
            try:
                funcion(evento)
            except Exception as error:  # un consumidor que falla no detiene a los demás
                print(f"[BUS] error en {funcion.__name__}: {error}")
