"""CAPA DE PRESENTACIÓN: muestra información y recibe órdenes del usuario.

Solo habla con la capa de negocio. NUNCA abre el CSV directamente.
"""


class Consola:
    def __init__(self, servicio):
        self.servicio = servicio

    def mostrar_resumen(self):
        print(f"\n{'ID':<4}{'Nombre':<20}{'Prom.':>6}  Estado")
        print("-" * 42)
        for f in self.servicio.resumen():
            print(f"{f['id']:<4}{f['nombre']:<20}{f['promedio']:>6.2f}  {f['estado']}")

    def menu(self):
        while True:
            print("\n1) Ver resumen   2) Registrar nota   0) Salir")
            opcion = input("Opción: ").strip()
            if opcion == "1":
                self.mostrar_resumen()
            elif opcion == "2":
                try:
                    id_est = int(input("ID del estudiante: "))
                    numero = int(input("Número de nota (1-3): "))
                    valor = float(input("Valor (0-10): "))
                    est = self.servicio.registrar_nota(id_est, numero, valor)
                    print(f"Nota registrada para {est['nombre']}")
                except (ValueError, LookupError) as error:
                    print(f"Error: {error}")
            elif opcion == "0":
                break
