"""
Planteamiento:
Modificar maximo/minimo por Divide y Conquista para manejar:
- arreglo vacio -> (None, None)
- arreglo de un elemento -> (valor, valor)

Solucion:
Se agrega una validacion inicial para lista vacia y se conserva la logica
de casos base de 1 y 2 elementos para recursion.
Complejidad temporal: O(n).
"""

# Esta funcion resuelve caso general, suponiendo rango valido.
def max_min_dc(arr: list[int], inicio: int, fin: int) -> tuple[int, int]:
    if inicio == fin:
        return arr[inicio], arr[inicio]
    if fin == inicio + 1:
        if arr[inicio] > arr[fin]:
            return arr[inicio], arr[fin]
        return arr[fin], arr[inicio]
    medio = (inicio + fin) // 2
    max_i, min_i = max_min_dc(arr, inicio, medio)
    max_d, min_d = max_min_dc(arr, medio + 1, fin)
    return max(max_i, max_d), min(min_i, min_d)


# Esta funcion envuelve el algoritmo para incluir casos vacios.
def max_min_seguro(arr: list[int]) -> tuple[int | None, int | None]:
    # Si arreglo vacio, se devuelve par de None.
    if len(arr) == 0:
        return None, None
    # Si arreglo no vacio, se aplica algoritmo normal.
    return max_min_dc(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    print("Ejercicio resuelto 3 - Maximo/minimo con vacio y un elemento")
    caso_vacio: list[int] = []
    caso_uno = [42]
    caso_varios = [8, 3, 17, -2, 10]
    print(f"{caso_vacio} -> {max_min_seguro(caso_vacio)}")
    print(f"{caso_uno} -> {max_min_seguro(caso_uno)}")
    print(f"{caso_varios} -> {max_min_seguro(caso_varios)}")
