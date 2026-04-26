"""
Ejercicio propuesto 3 - Solucion independiente.

Enunciado:
Clasificar estructuras como arbol binario valido, max-heap o min-heap.

Desarrollo de la solucion propuesta:
- Todo arreglo secuencial puede representar arbol binario completo por indice.
- Se verifica propiedad max-heap y min-heap comparando padres e hijos.
"""

# Define estructuras a evaluar.
estructuras = {
    "A": [90, 70, 60, 40, 20, 10, 30],
    "B": [10, 20, 15, 30, 40, 18, 22],
    "C": [50, 40, 60, 20, 45],
}

# Funcion para validar max-heap.
def es_max_heap(arr: list[int]) -> bool:
    # Recorre nodos internos.
    for i in range(len(arr) // 2):
        # Calcula hijos.
        izq = 2 * i + 1
        der = 2 * i + 2
        # Valida hijo izquierdo.
        if izq < len(arr) and arr[i] < arr[izq]:
            return False
        # Valida hijo derecho.
        if der < len(arr) and arr[i] < arr[der]:
            return False
    return True

# Funcion para validar min-heap.
def es_min_heap(arr: list[int]) -> bool:
    # Recorre nodos internos.
    for i in range(len(arr) // 2):
        # Calcula hijos.
        izq = 2 * i + 1
        der = 2 * i + 2
        # Valida hijo izquierdo.
        if izq < len(arr) and arr[i] > arr[izq]:
            return False
        # Valida hijo derecho.
        if der < len(arr) and arr[i] > arr[der]:
            return False
    return True

# Imprime resultados de clasificacion.
print("Ejercicio propuesto 3")
print("Enunciado: clasificar A, B y C como max-heap/min-heap.")
print("Desarrollo de la solucion propuesta: verificar padres vs hijos.")
for nombre, arr in estructuras.items():
    # Evalua propiedades.
    maxh = es_max_heap(arr)
    minh = es_min_heap(arr)
    print(f"Resultado -> estructura {nombre}: binario=si, max_heap={maxh}, min_heap={minh}")
