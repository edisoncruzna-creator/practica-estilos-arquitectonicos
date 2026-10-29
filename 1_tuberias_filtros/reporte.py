"""SUMIDERO: convierte el flujo en un reporte legible."""
import json
import sys

print(f"{'Nombre':<20}{'Carrera':<12}{'Promedio':>9}")
print("-" * 41)
total = 0
for linea in sys.stdin:
    est = json.loads(linea)
    print(f"{est['nombre']:<20}{est['carrera']:<12}{est['promedio']:>9.2f}")
    total += 1
print("-" * 41)
print(f"Total: {total} estudiante(s)")
