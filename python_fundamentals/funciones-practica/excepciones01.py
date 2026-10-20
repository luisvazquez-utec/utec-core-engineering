#!/usr/bin/env python3

from pathlib import Path

from lecturanotas import leer_notas

alumnos = {}  # Diccionario para almacenar los alumnos y sus notas
archivo_notas = Path(__file__).with_name("notas.txt")
alumnos_cargados = leer_notas(archivo_notas)
formato_valido = alumnos_cargados is not None
if alumnos_cargados is not None:
    alumnos.update(alumnos_cargados)


alumno = input("Ingrese el nombre del alumno: ")
while alumno != "":  # Mientras el nombre del alumno no esté vacío
    while True:
        try:
            nota = int(input("Ingrese la nota del alumno: "))
            if nota < 0 or nota > 10:
                raise ValueError("La nota debe estar entre 0 y 10.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    alumnos[alumno] = nota
    alumno = input("Ingrese el nombre del alumno: ")


print("Alumnos y sus notas:")
for nombre, nota in alumnos.items():
    print(f"Alumno: {nombre}, Nota: {nota}")

# Persistencia de datos: Guardar los datos en un archivo
if formato_valido:
    with open(archivo_notas, "w", encoding="utf-8") as archivo:
        for nombre, nota in alumnos.items():
            archivo.write(f"{nombre},{nota}\n")
else:
    print("No se guardaron los cambios para conservar el archivo original.")
