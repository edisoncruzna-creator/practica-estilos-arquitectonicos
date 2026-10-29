"""Punto de arranque: ensambla las capas de abajo hacia arriba.

    Presentación  ->  Negocio  ->  Datos
"""
from datos.repositorio_csv import RepositorioCSV
from negocio.servicio_notas import ServicioNotas
from presentacion.consola import Consola

if __name__ == "__main__":
    repositorio = RepositorioCSV()
    servicio = ServicioNotas(repositorio)
    Consola(servicio).menu()
