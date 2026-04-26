"""
Ejercicio propuesto 8 - Solucion independiente.

Enunciado:
Aplicar HEAPIFY desde indice 0 a [35,90,80,20,40,10,60], mostrando intercambios.

Desarrollo de la solucion propuesta:
- Se compara nodo con sus hijos.
- Se intercambia con el mayor.
- Se continua recursivamente hasta restaurar max-heap.
"""

# Define arreglo inicial.
heap = [35, 90, 80, 20, 40, 10, 60]

# Imprime encabezado.
print("Ejercicio propuesto 8")
print("Enunciado: aplicar HEAPIFY desde indice 0 y mostrar pasos.")
print("Desarrollo de la solucion propuesta: comparar hijos y bajar el nodo.")
print(f"Paso -> heap inicial: {heap}")

# Define funcion heapify con trazas.
def heapify(arr: list[int], idx: int) -> None:
    # Inicializa mayor.
    mayor = idx
    # Calcula hijo izquierdo.
    izq = 2 * idx + 1
    # Calcula hijo derecho.
    der = 2 * idx + 2
    # Compara hijo izquierdo.
    if izq < len(arr) and arr[izq] > arr[mayor]:
        mayor = izq
    # Compara hijo derecho.
    if der < len(arr) and arr[der] > arr[mayor]:
        mayor = der
    # Si cambia el mayor, intercambia y continua.
    if mayor != idx:
        print(f"Paso -> intercambiar arr[{idx}]={arr[idx]} con arr[{mayor}]={arr[mayor]}")
        arr[idx], arr[mayor] = arr[mayor], arr[idx]
        print(f"Paso -> estado actual: {arr}")
        heapify(arr, mayor)

# Aplica heapify desde la raiz.
heapify(heap, 0)

# Imprime resultado final.
print(f"Resultado -> heap final: {heap}")
