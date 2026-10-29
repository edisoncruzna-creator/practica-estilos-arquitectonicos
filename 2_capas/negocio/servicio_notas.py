"""CAPA DE NEGOCIO: contiene las REGLAS del dominio académico.

- El promedio es la media de las tres notas.
- Se aprueba con promedio >= 7.
- Una nota válida está entre 0 y 10.

Solo conoce a la capa inmediatamente inferior (datos) y a través de un
repositorio que recibe en el constructor. No sabe si los datos vienen de un
CSV, de SQLite o de internet.
"""
NOTA_APROBACION = 7.0


class ServicioNotas:
    def __init__(self, repositorio):
        self.repo = repositorio

    @staticmethod
    def promedio(est):
        return round((est["nota1"] + est["nota2"] + est["nota3"]) / 3, 2)

    def estado(self, est):
        return "APROBADO" if self.promedio(est) >= NOTA_APROBACION else "REPROBADO"

    def resumen(self):
        filas = []
        for est in self.repo.listar():
            filas.append({**est, "promedio": self.promedio(est), "estado": self.estado(est)})
        return filas

    def registrar_nota(self, id_est, numero, valor):
        if not 0 <= valor <= 10:
            raise ValueError("La nota debe estar entre 0 y 10")
        if numero not in (1, 2, 3):
            raise ValueError("El número de nota debe ser 1, 2 o 3")
        est = self.repo.buscar(id_est)
        if est is None:
            raise LookupError(f"No existe el estudiante {id_est}")
        est[f"nota{numero}"] = valor
        self.repo.guardar(est)
        return est
