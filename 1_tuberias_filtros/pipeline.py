"""El mismo estilo dentro de un solo programa, usando generadores de Python.

Cada función es un filtro: recibe un flujo, lo transforma y lo entrega.
Los generadores procesan un estudiante a la vez (procesamiento incremental).
"""
import csv


def leer(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        yield from csv.DictReader(archivo)


def calcular_promedio(flujo):
    for est in flujo:
        notas = [float(est["nota1"]), float(est["nota2"]), float(est["nota3"])]
        est["promedio"] = round(sum(notas) / 3, 2)
        yield est


def filtrar_aprobados(flujo, minimo=7.0):
    for est in flujo:
        if est["promedio"] >= minimo:
            yield est


def imprimir(flujo):
    for est in flujo:
        print(f"{est['nombre']:<20}{est['promedio']:>6.2f}")


if __name__ == "__main__":
    # La "tubería" es la composición de funciones
    imprimir(filtrar_aprobados(calcular_promedio(leer("../datos/estudiantes.csv"))))
