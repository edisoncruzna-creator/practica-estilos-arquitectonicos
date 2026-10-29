# Estilo 4: Modelo-Vista-Controlador (MVC)

| Parte | Archivo | Responsabilidad |
| --- | --- | --- |
| Modelo | `modelo.py` | Datos, promedio, aprobación, validación, notificación de cambios |
| Vistas | `templates/*.html` | Mostrar los datos (tabla, tarjetas, detalle) |
| Controlador | `app.py` | Recibir la petición, llamar al modelo y elegir la vista |

## Ejecutar

```bash
cd 4_mvc
python app.py
```

Abre la pestaña **PORTS** y pulsa el globo del puerto **5001**.

## Ejercicios

1. Cambia la nota de un estudiante desde la página. Observa el aviso del Observer.
2. Compara `/` y `/tarjetas`: ¿qué cambió en el modelo para tener dos vistas? (respuesta: nada).
3. Crea una tercera vista `/estadisticas` con `templates/estadisticas.html` que use
   `modelo.estadisticas()`. Solo debes tocar el controlador y crear la plantilla.
4. Cambia la nota de aprobación a 6 en el modelo. ¿Qué vistas se actualizan?
