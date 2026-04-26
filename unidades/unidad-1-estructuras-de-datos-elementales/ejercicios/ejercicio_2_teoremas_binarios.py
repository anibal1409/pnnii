"""
UNIDAD I - Ejercicio 2
Tema: Teoremas para arboles binarios.

Enunciado 1 (Teorema I):
Si un arbol binario tiene altura h (raiz en nivel 0),
calcular el maximo de nodos: Nmax = 2^(h+1) - 1.

Resultado del ejemplo:
- Para h=3 -> Nmax=15

Enunciado 2 (Teorema II):
En un arbol binario lleno, si hay I nodos internos,
calcular hojas: L = I + 1.

Resultado del ejemplo:
- Para I=7 -> L=8

Explicacion general:
- Se implementan funciones directas para aplicar teoremas de arboles binarios.
- Se agrega una funcion para indices de hijos en representacion secuencial.
- El bloque final imprime enunciados y resultados para uso didactico.

Explicacion breve:
Este ejercicio muestra formulas rapidas para calcular propiedades de arboles
binarios y entender como se representan en un arreglo usando indices.

Desarrollo de la solucion propuesta:
- Se implementa Teorema I con Nmax = 2^(h+1)-1.
- Se implementa Teorema II con hojas = internos + 1.
- Se aplica formula de hijos en arreglo secuencial.
"""


def max_nodos_por_altura(altura: int) -> int:
    """Aplica Teorema I."""
    # Formula del Teorema I: Nmax = 2^(h+1) - 1.
    return (2 ** (altura + 1)) - 1


def hojas_por_nodos_internos(nodos_internos: int) -> int:
    """Aplica Teorema II para arbol binario lleno."""
    # Formula del Teorema II: hojas = internos + 1.
    return nodos_internos + 1


def hijos_en_arreglo(i: int) -> tuple[int, int]:
    """Indices de hijos en representacion secuencial base 0."""
    # Retorna indice del hijo izquierdo y derecho.
    return (2 * i + 1, 2 * i + 2)


def ejecutar_ejercicio_2() -> None:
    # Define altura de ejemplo para Teorema I.
    altura = 3
    # Define cantidad de nodos internos para Teorema II.
    internos = 7
    # Define representacion secuencial de un arbol binario completo.
    arbol_secuencial = ["A", "B", "C", "D", "E", "F", "G"]
    # Selecciona el indice del nodo B.
    indice = 1  # Nodo B

    # Calcula maximo de nodos para la altura dada.
    nmax = max_nodos_por_altura(altura)
    # Calcula hojas para nodos internos dados.
    hojas = hojas_por_nodos_internos(internos)
    # Obtiene indices de hijos en arreglo secuencial.
    i_izq, i_der = hijos_en_arreglo(indice)

    # Imprime encabezado del ejercicio.
    print("Ejercicio 2 - Teoremas para arboles binarios")
    # Imprime explicacion breve orientada a estudiantes principiantes.
    print(
        "Explicacion breve: aplicamos dos teoremas para calcular nodos y hojas, "
        "y reforzamos como ubicar hijos en una representacion secuencial."
    )
    # Imprime separacion entre enunciado y desarrollo.
    print("Desarrollo de la solucion propuesta:")
    print("- aplicar formula de Nmax")
    print("- aplicar formula de hojas")
    print("- aplicar indices de hijos en arreglo")
    # Imprime enunciado del Teorema I.
    print("Enunciado 1: hallar Nmax para h=3.")
    # Imprime resultado del Teorema I.
    print(f"Resultado -> Nmax: {nmax}")
    # Imprime enunciado del Teorema II.
    print("Enunciado 2: hallar hojas para I=7.")
    # Imprime resultado del Teorema II.
    print(f"Resultado -> Hojas: {hojas}")
    # Imprime enunciado de representacion en arreglo.
    print("Enunciado 3: en arreglo secuencial, hallar hijos de indice 1 (B).")
    # Imprime resultado de hijos izquierdo y derecho para el indice seleccionado.
    print(
        "Indices de los hijos -> "
        f"hijo izquierdo: {i_izq}, hijo derecho: {i_der}"
    )
    print(
        "Resultado -> "
        f"hijo izquierdo: {arbol_secuencial[i_izq]}, hijo derecho: {arbol_secuencial[i_der]}"
    )
