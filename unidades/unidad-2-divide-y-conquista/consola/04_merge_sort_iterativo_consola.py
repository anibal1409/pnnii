"""
Objetivo del modulo:
Aplicar Merge Sort iterativo (bottom-up) y mostrar pasadas por tamano.

Enunciado:
Ordenar una lista con Merge Sort iterativo bottom-up, iniciando con
subarreglos de tamano 1 y fusionando en tamanos 2, 4, 8, etc.

Explicacion breve:
Esta version evita recursion y por eso no usa pila de llamadas.
La complejidad temporal sigue siendo O(n log n).

Desarrollo de la solucion propuesta:
- Recorrer tamanos de bloque con size = 1, 2, 4, ...
- Fusionar pares de bloques contiguos en cada pasada.
- Mostrar estado parcial luego de cada fusion.
"""


def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay elementos vacios en la lista.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


def merge(arr: list[int], inicio: int, medio: int, fin: int) -> None:
    izquierda = arr[inicio:medio + 1]
    derecha = arr[medio + 1:fin + 1]
    i = 0
    j = 0
    k = inicio
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            arr[k] = izquierda[i]
            i += 1
        else:
            arr[k] = derecha[j]
            j += 1
        k += 1
    while i < len(izquierda):
        arr[k] = izquierda[i]
        i += 1
        k += 1
    while j < len(derecha):
        arr[k] = derecha[j]
        j += 1
        k += 1


def merge_sort_iterativo(arr: list[int], pasos: list[str]) -> None:
    # Big O temporal: O(n log n). Big O espacial: O(n).
    # Ventaja didactica: no usa recursion ni pila de llamadas.
    n = len(arr)
    size = 1
    while size < n:
        pasos.append(f"Pasada con size={size}.")
        inicio = 0
        while inicio < n - 1:
            medio = min(inicio + size - 1, n - 1)
            fin = min(inicio + 2 * size - 1, n - 1)
            if medio < fin:
                pasos.append(f"Fusionar bloques [{inicio},{medio}] y [{medio+1},{fin}].")
                merge(arr, inicio, medio, fin)
                pasos.append(f"Estado parcial: {arr}")
            inicio += 2 * size
        size *= 2


def main() -> None:
    print("=== Ejercicio 4.1 - Merge Sort Iterativo (Consola) ===")
    print("Enunciado: ordenar una lista con Merge Sort iterativo (bottom-up).")
    print("Explicacion breve: fusionar bloques crecientes sin usar recursion.")
    entrada = input("Ingresa numeros separados por coma: ")
    try:
        arr = parsear_lista(entrada)
    except ValueError as error:
        print(f"Entrada invalida: {error}")
        return
    pasos: list[str] = []
    merge_sort_iterativo(arr, pasos)
    print("\n--- Pasadas ---")
    for paso in pasos:
        print(f"- {paso}")
    print(f"\nResultado ordenado: {arr}")


if __name__ == "__main__":
    main()
