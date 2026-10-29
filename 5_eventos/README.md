# Estilo 5: Dirigido por eventos

```
EMISOR                 CANAL                   CONSUMIDORES
registro_notas.py ───► bus_eventos.py ───┬───► notificaciones.py
                    «NotaRegistrada»     ├───► estadisticas.py
                                         └───► auditoria.py
```

## Ejecutar

```bash
cd 5_eventos
python simulacion.py     # eventos automáticos
python main.py           # registrar notas a mano
```

## Ejercicios

1. Comenta en `main.py` la suscripción de `estadisticas`. ¿El emisor falló? ¿Por qué no?
2. **Reto principal:** crea `consumidores/alerta_riesgo.py` que imprima una alerta
   cuando la nota sea menor que 5. Suscríbelo en `main.py`.
   No modifiques `registro_notas.py` ni los otros consumidores.
3. Haz que `alerta_riesgo` falle a propósito (`1/0`). ¿Los otros consumidores siguen funcionando?
4. Agrega un segundo tipo de evento, «EstudianteMatriculado», con su propio consumidor.
