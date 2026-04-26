"""
Lanzador de ejercicios de la Unidad I.
Ejecuta los tres ejercicios en orden para mostrar enunciados y resultados.

Explicacion general:
- Este modulo centraliza la ejecucion de los ejercicios de la unidad.
- Importa cada ejercicio como una funcion independiente.
- Ejecuta los ejercicios en secuencia para mantener un guion de clase.
"""

# Importa la funcion del ejercicio 1 (conceptos de arboles).
from ejercicios.ejercicio_1_conceptos_arboles import ejecutar_ejercicio_1
# Importa la funcion del ejercicio 2 (teoremas binarios).
from ejercicios.ejercicio_2_teoremas_binarios import ejecutar_ejercicio_2
# Importa la funcion del ejercicio 3 (operaciones con heaps).
from ejercicios.ejercicio_3_heaps import ejecutar_ejercicio_3


def main() -> None:
    # Imprime el titulo principal de la unidad.
    print("UNIDAD I - ESTRUCTURAS DE DATOS ELEMENTALES")
    # Imprime una linea decorativa para separar visualmente el bloque.
    print("=" * 54)
    # Ejecuta el primer ejercicio de la unidad.
    ejecutar_ejercicio_1()
    # Imprime un separador entre ejercicios.
    print("-" * 54)
    # Ejecuta el segundo ejercicio de la unidad.
    ejecutar_ejercicio_2()
    # Imprime otro separador para mantener legibilidad.
    print("-" * 54)
    # Ejecuta el tercer ejercicio de la unidad.
    ejecutar_ejercicio_3()


if __name__ == "__main__":
    # Punto de entrada al ejecutar el archivo directamente.
    main()
