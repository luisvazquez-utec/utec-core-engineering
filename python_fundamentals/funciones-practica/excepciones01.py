#!/usr/bin/env python3

alumnos = {}  # Diccionario para almacenar los alumnos y sus notas


alumno = input("Ingrese el nombre del alumno: ")
while alumno != "":  # Mientras el nombre del alumno no esté vacío
    try:
        nota = int(input("Ingrese la nota del alumno: "))
        if nota < 0 or nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")
        alumnos[alumno] = nota
    except ValueError as e:
        print(f"Error: {e}")
    alumno = input("Ingrese el nombre del alumno: ")

print("Alumnos y sus notas:")
for nombre, nota in alumnos.items():
    print(f"Alumno: {nombre}, Nota: {nota}")

