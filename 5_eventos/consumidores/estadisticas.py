"""CONSUMIDOR: mantiene estadísticas en tiempo real (estado propio)."""

_notas = []


def actualizar(evento):
    _notas.append(evento["nota"])
    promedio = sum(_notas) / len(_notas)
    print(f"  [Estadísticas] {len(_notas)} nota(s) registradas, promedio del curso: {promedio:.2f}")
