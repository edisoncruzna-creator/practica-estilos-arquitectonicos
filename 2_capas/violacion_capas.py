"""EJEMPLO DE LO QUE NO SE DEBE HACER.

Esta "pantalla" se salta la capa de negocio y lee el CSV directamente.
Funciona, pero:
  - duplica la regla del promedio (si cambia, hay que cambiarla en dos sitios);
  - si mañana los datos pasan a SQLite, esta pantalla se rompe.
Ejercicio: encuentra las dos violaciones y corrígelas usando ServicioNotas.
"""
import csv

with open("../datos/estudiantes.csv", encoding="utf-8") as archivo:
    for fila in csv.DictReader(archivo):
        prom = (float(fila["nota1"]) + float(fila["nota2"]) + float(fila["nota3"])) / 3
        estado = "APROBADO" if prom >= 7 else "REPROBADO"
        print(f"{fila['nombre']:<20}{prom:>6.2f}  {estado}")
