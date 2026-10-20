#!/usr/bin/env python3

alumnos = {}  # Diccionario para almacenar los alumnos y sus notas


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
with open("notas.txt", "w") as archivo:
    for nombre, nota in alumnos.items():
        archivo.write(f"{nombre},{nota}\n")