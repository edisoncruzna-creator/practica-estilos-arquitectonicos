"""CAPA DE DATOS: sabe CÓMO y DÓNDE se guardan los estudiantes (un archivo CSV).

No sabe nada de reglas de negocio ni de la interfaz de usuario.
"""
import csv
from pathlib import Path

RUTA = Path(__file__).resolve().parents[2] / "datos" / "estudiantes.csv"
CAMPOS = ["id", "nombre", "carrera", "nota1", "nota2", "nota3"]


class RepositorioCSV:
    def __init__(self, ruta=RUTA):
        self.ruta = Path(ruta)

    def listar(self):
        with open(self.ruta, encoding="utf-8") as archivo:
            return [self._convertir(f) for f in csv.DictReader(archivo)]

    def buscar(self, id_est):
        return next((e for e in self.listar() if e["id"] == id_est), None)

    def guardar(self, estudiante):
        estudiantes = [e for e in self.listar() if e["id"] != estudiante["id"]]
        estudiantes.append(estudiante)
        estudiantes.sort(key=lambda e: e["id"])
        with open(self.ruta, "w", encoding="utf-8", newline="", ) as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=CAMPOS, lineterminator="\n")
            escritor.writeheader()
            for e in estudiantes:
                escritor.writerow({c: e[c] for c in CAMPOS})

    @staticmethod
    def _convertir(fila):
        return {
            "id": int(fila["id"]),
            "nombre": fila["nombre"],
            "carrera": fila["carrera"],
            "nota1": float(fila["nota1"]),
            "nota2": float(fila["nota2"]),
            "nota3": float(fila["nota3"]),
        }
