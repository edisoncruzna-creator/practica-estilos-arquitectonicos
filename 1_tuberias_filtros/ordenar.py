"""FILTRO: ordena a los estudiantes por promedio, de mayor a menor.

Nota: este filtro NO es incremental; necesita leer toda la entrada antes de
producir salida. Es una limitación del estilo que se discute en clase.
"""
import json
import sys

estudiantes = [json.loads(linea) for linea in sys.stdin]
for est in sorted(estudiantes, key=lambda e: e["promedio"], reverse=True):
    print(json.dumps(est, ensure_ascii=False))
