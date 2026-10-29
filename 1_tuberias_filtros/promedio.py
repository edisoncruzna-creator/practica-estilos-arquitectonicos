"""FILTRO: agrega el campo 'promedio' a cada estudiante.

Lee de la entrada estándar (stdin) y escribe en la salida estándar (stdout).
No sabe quién le envía los datos ni a quién se los pasa.
"""
import json
import sys

for linea in sys.stdin:
    est = json.loads(linea)
    notas = [float(est["nota1"]), float(est["nota2"]), float(est["nota3"])]
    est["promedio"] = round(sum(notas) / len(notas), 2)
    print(json.dumps(est, ensure_ascii=False))
