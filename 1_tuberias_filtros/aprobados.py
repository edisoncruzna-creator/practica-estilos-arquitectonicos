"""FILTRO: deja pasar solo a los estudiantes con promedio >= nota mínima.

Uso:  ... | python aprobados.py 7
"""
import json
import sys

minimo = float(sys.argv[1]) if len(sys.argv) > 1 else 7.0
for linea in sys.stdin:
    est = json.loads(linea)
    if est["promedio"] >= minimo:
        print(json.dumps(est, ensure_ascii=False))
