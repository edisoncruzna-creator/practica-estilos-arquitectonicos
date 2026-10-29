"""EMISOR (productor): registra notas y publica el evento «NotaRegistrada».

Fíjate: este módulo NO importa a ningún consumidor. No sabe si existen
notificaciones, estadísticas o auditoría. Solo conoce el bus.
"""


class RegistroNotas:
    def __init__(self, bus):
        self.bus = bus

    def registrar(self, estudiante, materia, nota):
        if not 0 <= nota <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        # ... aquí se guardaría en una base de datos ...
        self.bus.publicar("NotaRegistrada", {"estudiante": estudiante, "materia": materia, "nota": nota})
