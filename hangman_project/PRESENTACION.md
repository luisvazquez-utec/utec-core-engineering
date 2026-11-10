# Presentacion final: Hangman

Repositorio: <https://github.com/luisvazquez-utec/utec-core-engineering>

## Guion de cinco minutos

### 0:00-0:35 | Introduccion

**Integrante 1:** Presentamos Hangman, un juego de consola en el que se
adivinan las letras de una palabra elegida al azar. El jugador puede cometer
hasta seis errores. El proyecto aplica funciones, clases, módulos, validación
de entradas y lectura de archivos.

### 0:35-1:25 | Componentes

**Integrante 1:** `main.py` es el punto de entrada y controla la ronda
interactiva. `game.py` define `HangmanGame` y mantiene la palabra, las letras
adivinadas, el límite de errores y el estado de la partida. `utils.py` carga
una palabra aleatoria y reúne funciones para validar y presentar información.
`wordlist.txt` almacena una palabra candidata por línea.

```text
main.py ── usa ──> HangmanGame (game.py)
   │                    │
   └── usa ──> utils.py ── lee ──> wordlist.txt
```

### 1:25-2:20 | Decisiones técnicas

**Integrante 2:** Separamos el flujo de consola del estado y las reglas para
que cada módulo tenga una responsabilidad clara. `guessed_letters` es una
lista, tal como requiere el ejercicio, y `errors` solo aumenta ante una letra
incorrecta. `is_won()` comprueba que todas las letras estén descubiertas;
`is_lost()` compara los errores con `max_errors`.

**Integrante 2:** Para admitir palabras compuestas, `display_progress()`
revela espacios y signos automáticamente. Esos caracteres no se tienen que
adivinar para ganar.

### 2:20-4:20 | Demostracion en vivo

**Integrante 3:** Desde la carpeta `hangman_project`, iniciamos:

```sh
python main.py
```

Durante la ronda:

1. Introducimos una entrada vacía, un número o varias letras y mostramos que
   se rechaza sin consumir intentos.
2. Adivinamos una letra y observamos el patrón, las letras intentadas y los
   intentos restantes.
3. Repetimos una letra, incluyendo una que haya sido incorrecta, para mostrar
   que se vuelve a solicitar sin alterar el estado.
4. Mostramos el final de la ronda: al revelar todas las letras aparece el
   mensaje de victoria; al alcanzar seis errores aparece el mensaje de fin.

La palabra se elige aleatoriamente, así que las letras acertadas dependen de
la selección de esa ronda. Si la demo requiere pasos totalmente repetibles,
se puede elegir temporalmente una sola palabra de prueba en `wordlist.txt` y
restaurar después el archivo original.

### 4:20-5:00 | Cierre

**Integrante 1:** El juego cumple el objetivo de mantener el estado de una
ronda y procesar entradas en consola con validación y un límite de errores.
La separación en módulos permite cambiar la lista o extender las reglas sin
mezclar esas tareas con el punto de entrada.

**Integrante 2:** Como mejoras opcionales se podrían añadir dificultad,
gráfico ASCII, puntuaciones persistentes o una opción para jugar otra ronda.
No forman parte de la implementación actual.

## Participacion del equipo

El guion propone tres turnos. Si el equipo tiene más integrantes, pueden
repartir la explicación de los módulos, las decisiones, la demo y las
preguntas; si tiene menos, una persona puede cubrir más de un turno. Reemplacen
los números por los nombres de quienes presentan.

## Preparacion de la demo

- Abrir una terminal en `hangman_project/`.
- Ejecutar `python main.py`.
- Tener a mano una palabra de prueba de `wordlist.txt` para poder planear
  letras antes de la demo; no mostrar la palabra objetivo hasta el final.
- Probar de antemano entradas inválidas, una letra repetida y ambos finales
  posibles (victoria y derrota).

## Preguntas probables

**¿Por qué separar el código en módulos?**

Para distinguir el punto de entrada, las reglas y el estado del juego, las
funciones auxiliares y los datos.

**¿Cómo se evita gastar intentos con una entrada inválida o repetida?**

`main.py` valida que haya exactamente una letra y comprueba la lista de letras
ya intentadas antes de llamar a `process_guess()`.

**¿Qué ocurre con espacios y signos de puntuación?**

`display_progress()` los revela en su posición original y `is_won()` solo
requiere adivinar los caracteres alfabéticos.

**¿Cómo se determina la derrota?**

Cada letra nueva que no aparece en la palabra aumenta `errors`; hay derrota
cuando llega a `max_errors`, que vale seis.

**¿Qué cambiarían para permitir otra ronda?**

Se puede envolver la creación y ejecución de `HangmanGame` en un ciclo exterior
y pedir confirmación al jugador al terminar cada partida.

## Enlace de entrega

Código y documentación: <https://github.com/luisvazquez-utec/utec-core-engineering/tree/main/hangman_project>
