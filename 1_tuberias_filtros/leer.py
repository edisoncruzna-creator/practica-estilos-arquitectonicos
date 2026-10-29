"""FUENTE: lee el CSV y emite un estudiante por línea en formato JSON.

Uso:  python leer.py ../datos/estudiantes.csv
"""
import csv
import json
import sys

ruta = sys.argv[1] if len(sys.argv) > 1 else "../datos/estudiantes.csv"
with open(ruta, encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):
        print(json.dumps(fila, ensure_ascii=False))
