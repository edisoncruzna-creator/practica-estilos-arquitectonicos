"""CONTROLADOR: recibe las peticiones del usuario, usa el MODELO y elige la VISTA.

Las vistas son las plantillas HTML de la carpeta templates/.
Ejecutar:  python app.py   (puerto 5001)
"""
from flask import Flask, abort, redirect, render_template, request, url_for

from modelo import ModeloEstudiantes

app = Flask(__name__)
modelo = ModeloEstudiantes()
historial = []                      # observador sencillo del modelo
modelo.suscribir(historial.append)


@app.get("/")
def lista():
    # Vista 1: tabla
    return render_template("lista.html", estudiantes=modelo.todos(), historial=historial)


@app.get("/tarjetas")
def tarjetas():
    # Vista 2: los MISMOS datos del modelo, presentados de otra forma
    return render_template("tarjetas.html", estudiantes=modelo.todos())


@app.get("/estudiante/<int:id_est>")
def detalle(id_est):
    est = modelo.buscar(id_est) or abort(404)
    return render_template("detalle.html", est=est, error=request.args.get("error"))


@app.post("/estudiante/<int:id_est>/nota")
def guardar_nota(id_est):
    if modelo.buscar(id_est) is None:
        abort(404)
    try:
        numero = int(request.form["numero"])
        valor = float(request.form["valor"])
        modelo.actualizar_nota(id_est, numero, valor)
    except (KeyError, ValueError) as error:
        return redirect(url_for("detalle", id_est=id_est, error=str(error)))
    return redirect(url_for("lista"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
