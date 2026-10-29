"""SERVIDOR REST: expone los estudiantes como recursos HTTP.

Restricciones REST que se ven aquí:
  - Cliente-servidor: este programa no tiene interfaz; solo responde peticiones.
  - Sin estado: cada petición trae todo lo necesario; el servidor no guarda sesiones.
  - Interfaz uniforme: recursos con URI (/api/estudiantes/3) y verbos HTTP.
  - Cacheable: las respuestas GET indican cuánto tiempo pueden guardarse.

Ejecutar:  python servidor.py   (puerto 5000)
"""
import csv
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)
app.json.ensure_ascii = False
RUTA = Path(__file__).resolve().parents[1] / "datos" / "estudiantes.csv"


def cargar():
    with open(RUTA, encoding="utf-8") as archivo:
        return {
            int(f["id"]): {
                "id": int(f["id"]),
                "nombre": f["nombre"],
                "carrera": f["carrera"],
                "notas": [float(f["nota1"]), float(f["nota2"]), float(f["nota3"])],
            }
            for f in csv.DictReader(archivo)
        }


ESTUDIANTES = cargar()  # los datos viven en memoria mientras corre el servidor


def con_promedio(est):
    return {**est, "promedio": round(sum(est["notas"]) / len(est["notas"]), 2)}


def validar(datos):
    if not datos or not datos.get("nombre") or not datos.get("carrera"):
        return "Se requieren 'nombre' y 'carrera'"
    notas = datos.get("notas", [0, 0, 0])
    if len(notas) != 3 or any(not 0 <= n <= 10 for n in notas):
        return "'notas' debe tener 3 valores entre 0 y 10"
    return None


@app.get("/api/estudiantes")
def listar():
    carrera = request.args.get("carrera")  # filtro opcional: ?carrera=Redes
    datos = [con_promedio(e) for e in ESTUDIANTES.values()
             if carrera is None or e["carrera"].lower() == carrera.lower()]
    respuesta = jsonify(datos)
    respuesta.headers["Cache-Control"] = "max-age=30"
    return respuesta


@app.get("/api/estudiantes/<int:id_est>")
def obtener(id_est):
    est = ESTUDIANTES.get(id_est)
    if est is None:
        return jsonify(error="Estudiante no encontrado"), 404
    return jsonify(con_promedio(est))


@app.post("/api/estudiantes")
def crear():
    datos = request.get_json(silent=True)
    error = validar(datos)
    if error:
        return jsonify(error=error), 400
    nuevo_id = max(ESTUDIANTES, default=0) + 1
    ESTUDIANTES[nuevo_id] = {"id": nuevo_id, "nombre": datos["nombre"],
                             "carrera": datos["carrera"], "notas": datos.get("notas", [0, 0, 0])}
    return jsonify(con_promedio(ESTUDIANTES[nuevo_id])), 201


@app.put("/api/estudiantes/<int:id_est>")
def reemplazar(id_est):
    if id_est not in ESTUDIANTES:
        return jsonify(error="Estudiante no encontrado"), 404
    datos = request.get_json(silent=True)
    error = validar(datos)
    if error:
        return jsonify(error=error), 400
    ESTUDIANTES[id_est] = {"id": id_est, "nombre": datos["nombre"],
                           "carrera": datos["carrera"], "notas": datos.get("notas", [0, 0, 0])}
    return jsonify(con_promedio(ESTUDIANTES[id_est]))


@app.delete("/api/estudiantes/<int:id_est>")
def eliminar(id_est):
    if ESTUDIANTES.pop(id_est, None) is None:
        return jsonify(error="Estudiante no encontrado"), 404
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
