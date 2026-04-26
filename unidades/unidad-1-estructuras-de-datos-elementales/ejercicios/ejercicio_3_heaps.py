"""
UNIDAD I - Ejercicio 3
Tema: Algoritmos INSERTAR y HEAPIFY en max-heap.

Enunciado 1:
Insertar 45 en el heap [90, 70, 60, 20, 40, 10, 30]
y reordenar para mantener propiedad max-heap.

Resultado esperado:
[90, 70, 60, 45, 40, 10, 30, 20]

Enunciado 2:
Aplicar heapify en indice 0 sobre [35, 80, 60, 20, 40, 10, 30].

Resultado esperado:
[80, 40, 60, 20, 35, 10, 30]

Explicacion general:
- Se implementa INSERTAR sobre max-heap con bubble-up.
- Se implementa HEAPIFY descendente desde un indice.
- Se muestran resultados para los dos enunciados de clase.

Explicacion breve:
En este ejercicio veras como mantener el orden de un max-heap al insertar
un nuevo valor y como corregir un heap usando heapify desde la raiz.

Desarrollo de la solucion propuesta:
- Se implementa INSERTAR con bubble-up.
- Se implementa HEAPIFY descendente desde un indice.
- Se ejecutan ambos algoritmos sobre arreglos de ejemplo.
"""


def insertar_en_max_heap(heap: list[int], valor: int) -> list[int]:
    """Inserta un valor y realiza bubble-up para conservar max-heap."""
    # Copia el heap para no mutar la lista original.
    salida = heap.copy()
    # Inserta el nuevo valor al final del arreglo.
    salida.append(valor)

    # Inicia en la posicion del nuevo elemento.
    i = len(salida) - 1
    # Repite mientras no se llegue a la raiz.
    while i > 0:
        # Calcula indice del padre.
        padre = (i - 1) // 2
        # Si se cumple propiedad max-heap, termina el proceso.
        if salida[padre] >= salida[i]:
            break
        # Si no se cumple, intercambia padre e hijo.
        salida[padre], salida[i] = salida[i], salida[padre]
        # Sube al indice del padre para continuar bubble-up.
        i = padre
    # Retorna el heap resultante tras insertar.
    return salida


def heapify_max(heap: list[int], i: int) -> list[int]:
    """Aplica heapify descendente desde un indice."""
    # Copia el heap para no modificar el arreglo de entrada.
    salida = heap.copy()

    def _heapify(arr: list[int], idx: int) -> None:
        # Inicializa mayor como indice actual.
        mayor = idx
        # Calcula indice de hijo izquierdo.
        izq = 2 * idx + 1
        # Calcula indice de hijo derecho.
        der = 2 * idx + 2

        # Evalua si el hijo izquierdo existe y es mayor.
        if izq < len(arr) and arr[izq] > arr[mayor]:
            mayor = izq
        # Evalua si el hijo derecho existe y es mayor.
        if der < len(arr) and arr[der] > arr[mayor]:
            mayor = der

        # Si el mayor no es el nodo actual, se intercambia y continua.
        if mayor != idx:
            arr[idx], arr[mayor] = arr[mayor], arr[idx]
            _heapify(arr, mayor)

    # Llama heapify comenzando desde el indice indicado.
    _heapify(salida, i)
    # Retorna el heap tras reordenamiento.
    return salida


def ejecutar_ejercicio_3() -> None:
    # Define heap valido para demostrar INSERTAR.
    heap_inicial = [90, 70, 60, 20, 40, 10, 30]
    # Define heap desordenado para aplicar HEAPIFY.
    heap_desordenado = [35, 80, 60, 20, 40, 10, 30]

    # Ejecuta insercion de 45 en max-heap.
    resultado_insertar = insertar_en_max_heap(heap_inicial, 45)
    # Ejecuta heapify desde la raiz (indice 0).
    resultado_heapify = heapify_max(heap_desordenado, 0)

    # Imprime encabezado del ejercicio.
    print("Ejercicio 3 - Heaps")
    # Imprime explicacion breve orientada a estudiantes principiantes.
    print(
        "Explicacion breve: practicamos dos operaciones basicas de heaps para "
        "mantener la propiedad de maximo en la raiz."
    )
    # Imprime bloque separado para desarrollo.
    print("Desarrollo de la solucion propuesta:")
    print("- INSERTAR: insertar al final y subir mientras sea mayor que el padre")
    print("- HEAPIFY: bajar intercambiando con el mayor hijo")
    # Imprime enunciado de insercion.
    print("Enunciado 1: insertar 45 en max-heap.")
    # Imprime resultado de insercion.
    print(f"Resultado -> {resultado_insertar}")
    # Imprime enunciado de heapify.
    print("Enunciado 2: aplicar heapify desde indice 0.")
    # Imprime resultado de heapify.
    print(f"Resultado -> {resultado_heapify}")
