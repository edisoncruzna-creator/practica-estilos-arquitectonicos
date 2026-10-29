"""MODELO: datos y reglas del dominio. No sabe nada de HTML ni de rutas web.

Implementa el patrón Observer: cuando cambia un estudiante, avisa a quien
se haya suscrito (por ejemplo, un registro de cambios).
"""
import csv
from pathlib import Path

RUTA = Path(__file__).resolve().parents[1] / "datos" / "estudiantes.csv"
NOTA_APROBACION = 7.0


class Estudiante:
    def __init__(self, id_est, nombre, carrera, notas):
        self.id = id_est
        self.nombre = nombre
        self.carrera = carrera
        self.notas = notas

    @property
    def promedio(self):
        return round(sum(self.notas) / len(self.notas), 2)

    @property
    def aprobado(self):
        return self.promedio >= NOTA_APROBACION


class ModeloEstudiantes:
    def __init__(self):
        self._estudiantes = {}
        self._observadores = []
        with open(RUTA, encoding="utf-8") as archivo:
            for f in csv.DictReader(archivo):
                e = Estudiante(int(f["id"]), f["nombre"], f["carrera"],
                               [float(f["nota1"]), float(f["nota2"]), float(f["nota3"])])
                self._estudiantes[e.id] = e

    # --- consultas ---
    def todos(self):
        return sorted(self._estudiantes.values(), key=lambda e: e.id)

    def buscar(self, id_est):
        return self._estudiantes.get(id_est)

    def estadisticas(self):
        lista = self.todos()
        aprobados = sum(e.aprobado for e in lista)
        return {
            "total": len(lista),
            "aprobados": aprobados,
            "reprobados": len(lista) - aprobados,
            "promedio_general": round(sum(e.promedio for e in lista) / len(lista), 2),
        }

    # --- comandos ---
    def actualizar_nota(self, id_est, numero, valor):
        if not 0 <= valor <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        est = self._estudiantes[id_est]
        anterior = est.notas[numero - 1]
        est.notas[numero - 1] = valor
        self._notificar(f"{est.nombre}: nota {numero} cambió de {anterior} a {valor}")

    # --- Observer ---
    def suscribir(self, funcion):
        self._observadores.append(funcion)

    def _notificar(self, mensaje):
        for funcion in self._observadores:
            funcion(mensaje)
