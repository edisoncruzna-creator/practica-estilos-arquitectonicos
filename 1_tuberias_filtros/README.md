# Estilo 1: Tuberías y filtros

| Elemento | En este código |
| --- | --- |
| Fuente | `leer.py` |
| Filtros | `promedio.py`, `aprobados.py`, `ordenar.py` |
| Sumidero | `reporte.py` |
| Tubería | el operador `|` de la terminal |

## Ejecutar

```bash
cd 1_tuberias_filtros
python leer.py ../datos/estudiantes.csv | python promedio.py | python aprobados.py 7 | python ordenar.py | python reporte.py
```

Prueba también la versión en un solo programa:

```bash
python pipeline.py
```

## Ejercicios

1. Cambia la nota mínima a 6 sin tocar ningún archivo.
2. Quita `ordenar.py` de la tubería. ¿Qué cambia? ¿Se rompe algo?
3. Crea el filtro `por_carrera.py` que reciba una carrera como argumento
   (`python por_carrera.py Software`) y deje pasar solo a esos estudiantes.
   Insértalo en la tubería sin modificar los demás filtros.
4. Crea el sumidero `a_csv.py` que escriba el resultado como CSV y guárdalo con `> aprobados.csv`.
