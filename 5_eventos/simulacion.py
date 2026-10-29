"""Publica varios eventos seguidos para ver el sistema sin escribir datos a mano."""
from main import registro

for nombre, nota in [("Ana Torres", 9.5), ("Luis Mendoza", 4.0), ("Valeria Bravo", 6.5)]:
    registro.registrar(nombre, "Arquitectura", nota)
