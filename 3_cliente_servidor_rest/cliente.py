"""CLIENTE: consume la API REST. No conoce el CSV ni el código del servidor;
solo conoce las URI y el formato JSON (el contrato).

Ejecutar en una SEGUNDA terminal, con el servidor encendido:
    python cliente.py
"""
import json
import urllib.error
import urllib.request

BASE = "http://localhost:5000/api/estudiantes"


def peticion(metodo, url, datos=None):
    cuerpo = json.dumps(datos).encode() if datos is not None else None
    req = urllib.request.Request(url, data=cuerpo, method=metodo,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            texto = resp.read().decode()
            return resp.status, json.loads(texto) if texto else None
    except urllib.error.HTTPError as error:
        return error.code, json.loads(error.read().decode())


if __name__ == "__main__":
    estado, lista = peticion("GET", BASE)
    print(f"GET  /api/estudiantes        -> {estado}, {len(lista)} estudiantes")

    estado, est = peticion("GET", f"{BASE}/1")
    print(f"GET  /api/estudiantes/1      -> {estado}, {est['nombre']} (promedio {est['promedio']})")

    nuevo = {"nombre": "Paula Reyes", "carrera": "Software", "notas": [8, 9, 7.5]}
    estado, creado = peticion("POST", BASE, nuevo)
    print(f"POST /api/estudiantes        -> {estado}, creado con id {creado['id']}")

    estado, error = peticion("GET", f"{BASE}/999")
    print(f"GET  /api/estudiantes/999    -> {estado}, {error['error']}")

    estado, _ = peticion("DELETE", f"{BASE}/{creado['id']}")
    print(f"DELETE /api/estudiantes/{creado['id']}   -> {estado}")
