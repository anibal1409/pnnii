"""
Lanzador de ejercicios de la Unidad II.
Ejecuta los ejercicios principales de consola en orden.

Explicacion general:
- Este modulo centraliza la ejecucion de los ejercicios base de la unidad.
- Cada ejercicio de consola se ejecuta como script independiente.
- Se mantiene un flujo secuencial para trabajar la unidad como guia de clase.
"""

# Se importa subprocess para ejecutar scripts Python externos en orden.
import subprocess
# Se importa Path para construir rutas de archivos de forma segura.
from pathlib import Path


# Define funcion auxiliar para ejecutar un script de consola de la unidad.
def ejecutar_script(ruta_script: Path) -> None:
    # Ejecuta el script con python3 y permite interaccion en terminal.
    subprocess.run(["python3", str(ruta_script)], check=False)


# Define funcion del ejercicio 1 para mantener estilo similar a unidad 1.
def ejecutar_ejercicio_1() -> None:
    # Construye ruta absoluta al script de busqueda binaria en consola.
    ruta = Path(__file__).parent / "consola" / "01_busqueda_binaria_consola.py"
    # Ejecuta script del ejercicio 1.
    ejecutar_script(ruta)


# Define funcion del ejercicio 2 para mantener estructura uniforme.
def ejecutar_ejercicio_2() -> None:
    # Construye ruta al script de maximo y minimo por divide y conquista.
    ruta = Path(__file__).parent / "consola" / "02_max_min_consola.py"
    # Ejecuta script del ejercicio 2.
    ejecutar_script(ruta)


# Define funcion del ejercicio 3 para merge sort recursivo.
def ejecutar_ejercicio_3() -> None:
    # Construye ruta al script de merge sort recursivo.
    ruta = Path(__file__).parent / "consola" / "03_merge_sort_recursivo_consola.py"
    # Ejecuta script del ejercicio 3.
    ejecutar_script(ruta)


# Define funcion del ejercicio 4 para merge sort iterativo.
def ejecutar_ejercicio_4() -> None:
    # Construye ruta al script de merge sort iterativo.
    ruta = Path(__file__).parent / "consola" / "04_merge_sort_iterativo_consola.py"
    # Ejecuta script del ejercicio 4.
    ejecutar_script(ruta)


# Define funcion del ejercicio 5 para quicksort.
def ejecutar_ejercicio_5() -> None:
    # Construye ruta al script de quicksort en consola.
    ruta = Path(__file__).parent / "consola" / "05_quicksort_consola.py"
    # Ejecuta script del ejercicio 5.
    ejecutar_script(ruta)


# Funcion principal que organiza la ejecucion completa de la unidad.
def main() -> None:
    # Imprime titulo principal de la unidad.
    print("UNIDAD II - DIVIDE Y CONQUISTA")
    # Imprime linea decorativa.
    print("=" * 54)
    # Ejecuta ejercicio 1.
    ejecutar_ejercicio_1()
    # Imprime separador.
    print("-" * 54)
    # Ejecuta ejercicio 2.
    ejecutar_ejercicio_2()
    # Imprime separador.
    print("-" * 54)
    # Ejecuta ejercicio 3.
    ejecutar_ejercicio_3()
    # Imprime separador.
    print("-" * 54)
    # Ejecuta ejercicio 4.
    ejecutar_ejercicio_4()
    # Imprime separador.
    print("-" * 54)
    # Ejecuta ejercicio 5.
    ejecutar_ejercicio_5()


# Punto de entrada cuando se ejecuta este archivo directamente.
if __name__ == "__main__":
    # Llama a la funcion principal.
    main()
