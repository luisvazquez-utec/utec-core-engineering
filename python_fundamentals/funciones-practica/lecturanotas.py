from pathlib import Path


def leer_notas(ruta):
    """Lee notas con formato nombre,nota y devuelve un diccionario."""
    try:
        contenido = Path(ruta).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: no se encontró el archivo '{Path(ruta).name}'.")
        return {}
    except UnicodeDecodeError as error:
        print(f"Error al leer el archivo de notas: {error}")
        return None

    if not contenido.strip():
        print("Error: el archivo de notas está vacío.")
        return {}

    alumnos = {}
    try:
        for numero_linea, linea in enumerate(contenido.splitlines(), start=1):
            partes = linea.split(",")
            if len(partes) != 2:
                raise ValueError(
                    f"la línea {numero_linea} debe tener el formato nombre,nota."
                )

            nombre = partes[0].strip()
            if not nombre:
                raise ValueError(f"falta el nombre en la línea {numero_linea}.")

            try:
                nota = int(partes[1].strip())
            except ValueError as error:
                raise ValueError(
                    f"la nota de la línea {numero_linea} debe ser un número entero."
                ) from error

            if nota < 0 or nota > 10:
                raise ValueError(
                    f"la nota de la línea {numero_linea} debe estar entre 0 y 10."
                )

            alumnos[nombre] = nota
    except ValueError as error:
        print(f"Error al leer el archivo de notas: {error}")
        return None

    return alumnos
