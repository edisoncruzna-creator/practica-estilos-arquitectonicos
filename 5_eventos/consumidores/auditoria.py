"""CONSUMIDOR: deja constancia de cada evento en un archivo de log."""
from pathlib import Path

LOG = Path(__file__).resolve().parents[1] / "auditoria.log"


def registrar(evento):
    with open(LOG, "a", encoding="utf-8") as archivo:
        archivo.write(f"{evento['fecha']} {evento['tipo']} {evento['estudiante']} "
                      f"{evento['materia']} {evento['nota']}\n")
    print(f"  [Auditoría] evento guardado en {LOG.name}")
