"""
Planteamiento:
Implementar Quickselect para encontrar el k-esimo elemento mas pequeno
(k inicia en 1) sin ordenar completamente el arreglo.

Solucion:
Quickselect usa la misma idea de particion de Quicksort:
- El pivote queda en su posicion final.
- Si esa posicion es k, se termina.
- Si esta a la derecha, se busca solo en izquierda.
- Si esta a la izquierda, se busca solo en derecha.
Complejidad promedio: O(n).
Peor caso: O(n^2) con pivotes muy malos.
"""

# Particion tipo Lomuto para ubicar pivote y dividir el arreglo.
def particion_lomuto(arr: list[int], bajo: int, alto: int) -> int:
    # Se elige pivote como ultimo elemento del rango.
    pivote = arr[alto]
    # Se inicializa i para marcar zona de menores o iguales al pivote.
    i = bajo - 1
    # Se recorre j por todos los elementos antes del pivote.
    for j in range(bajo, alto):
        # Si el elemento actual es menor o igual al pivote, va a la zona izquierda.
        if arr[j] <= pivote:
            # Se amplia la zona izquierda.
            i += 1
            # Se intercambia para colocar elemento en zona correcta.
            arr[i], arr[j] = arr[j], arr[i]
    # Al final se coloca pivote inmediatamente despues de la zona izquierda.
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    # Se retorna indice final del pivote.
    return i + 1


# Quickselect recursivo para buscar indice objetivo.
def quickselect(arr: list[int], bajo: int, alto: int, indice_objetivo: int) -> int:
    # Caso base de rango invalido (no deberia ocurrir con entrada valida).
    if bajo > alto:
        # Se lanza error explicito para no devolver dato incorrecto.
        raise ValueError("Rango invalido durante quickselect.")
    # Se particiona el rango actual.
    pivote_idx = particion_lomuto(arr, bajo, alto)
    # Si pivote coincide con indice buscado, ya tenemos respuesta.
    if pivote_idx == indice_objetivo:
        # Se retorna valor exacto.
        return arr[pivote_idx]
    # Si indice buscado queda a la izquierda del pivote.
    if indice_objetivo < pivote_idx:
        # Se continua solo en subarreglo izquierdo.
        return quickselect(arr, bajo, pivote_idx - 1, indice_objetivo)
    # Si queda a la derecha, se continua solo en subarreglo derecho.
    return quickselect(arr, pivote_idx + 1, alto, indice_objetivo)


# Funcion de alto nivel para usuario, usando k en base 1.
def obtener_kesimo_menor(arr: list[int], k: int) -> int:
    # Se valida que el arreglo no este vacio.
    if len(arr) == 0:
        # Se informa error por entrada invalida.
        raise ValueError("El arreglo no puede estar vacio.")
    # Se valida rango de k para evitar indices fuera de limites.
    if k < 1 or k > len(arr):
        # Se informa error de parametro invalido.
        raise ValueError("k debe estar entre 1 y el tamano del arreglo.")
    # Se crea copia para no modificar arreglo original de entrada.
    copia = arr.copy()
    # Se convierte k (base 1) a indice de Python (base 0).
    indice_objetivo = k - 1
    # Se invoca quickselect en todo el arreglo.
    return quickselect(copia, 0, len(copia) - 1, indice_objetivo)


# Bloque de ejemplos de uso.
if __name__ == "__main__":
    # Se define arreglo de prueba.
    arreglo = [7, 10, 4, 3, 20, 15]
    # Se define k de ejemplo.
    k_1 = 3
    # Se define otro k de ejemplo.
    k_2 = 5
    # Se imprime encabezado.
    print("Ejercicio adicional 3 - Quickselect (k-esimo menor)")
    # Se imprime arreglo original.
    print(f"Arreglo: {arreglo}")
    # Se imprime resultado para k_1.
    print(f"k={k_1} -> {obtener_kesimo_menor(arreglo, k_1)}")
    # Se imprime resultado para k_2.
    print(f"k={k_2} -> {obtener_kesimo_menor(arreglo, k_2)}")
