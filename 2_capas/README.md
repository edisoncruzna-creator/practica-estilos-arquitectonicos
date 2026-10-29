# Estilo 2: Por capas

```
presentacion/consola.py      ← interfaz (menú en consola)
        │ usa
negocio/servicio_notas.py    ← reglas: promedio, aprobación, validaciones
        │ usa
datos/repositorio_csv.py     ← lee y escribe el archivo CSV
```

Regla del estilo: cada capa solo llama a la capa inmediatamente inferior.

## Ejecutar

```bash
cd 2_capas
python main.py
```

## Ejercicios

1. Abre `violacion_capas.py`. Explica por qué viola el estilo y corrígelo.
2. Cambia la nota de aprobación a 6.5. ¿Cuántos archivos tuviste que tocar?
3. **Reto principal:** crea `datos/repositorio_sqlite.py` con los mismos métodos
   (`listar`, `buscar`, `guardar`) usando el módulo `sqlite3` de Python.
   Luego cambia SOLO la línea del repositorio en `main.py`.
   Las capas de negocio y presentación no deben modificarse.
