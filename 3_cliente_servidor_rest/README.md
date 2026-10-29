# Estilo 3: Cliente-servidor y REST

| Elemento | En este código |
| --- | --- |
| Servidor | `servidor.py` (Flask, puerto 5000) |
| Clientes | `cliente.py`, el navegador, `pruebas.http` |
| Conector | HTTP con JSON |

## Ejecutar

Terminal 1:

```bash
cd 3_cliente_servidor_rest
python servidor.py
```

Terminal 2 (botón **+** del panel de terminales):

```bash
cd 3_cliente_servidor_rest
python cliente.py
```

También puedes abrir la pestaña **PORTS**, pulsar el globo del puerto 5000 y
agregar `/api/estudiantes` a la URL. O abrir `pruebas.http` y pulsar **Send Request**.

## Ejercicios

1. Prueba cada petición de `pruebas.http` y anota el código de estado de cada una.
2. Agrega el endpoint `GET /api/estudiantes/<id>/estado` que responda
   `{"id": 1, "estado": "APROBADO"}` (aprueba con promedio >= 7).
3. Agrega `PATCH /api/estudiantes/<id>` para cambiar solo una nota:
   `{"numero": 2, "valor": 9.5}`.
4. Reinicia el servidor. ¿Qué pasó con los estudiantes que creaste? ¿Por qué?
