"""
Planteamiento:
Dada una lista ordenada ascendente y un numero, devolver el indice donde
debe insertarse para mantener el orden; si ya existe, devolver su indice.

Solucion:
Se usa busqueda binaria iterativa, ajustando limites hasta que inicio
indique la posicion correcta de insercion.
Complejidad temporal: O(log n).
Complejidad espacial: O(1).
"""

# Convierte texto de lista en arreglo ordenado ascendente.
def parsear_ascendente(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay elementos vacios en la lista.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    if numeros != sorted(numeros):
        raise ValueError("La lista debe estar ordenada de menor a mayor.")
    return numeros


# Encuentra indice de insercion usando busqueda binaria.
def posicion_insercion(arr: list[int], objetivo: int) -> int:
    inicio = 0
    fin = len(arr) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arr[medio] == objetivo:
            return medio
        if objetivo < arr[medio]:
            fin = medio - 1
        else:
            inicio = medio + 1
    # Cuando termina, inicio queda en el punto de insercion.
    return inicio


if __name__ == "__main__":
    print("Ejercicio resuelto 2 - Posicion de insercion con busqueda binaria")
    try:
        arr = parsear_ascendente(input("Lista ascendente (ej: 1,3,5,6): "))
        objetivo = int(input("Numero objetivo: ").strip())
    except ValueError as error:
        print(f"Entrada invalida: {error}")
    else:
        pos = posicion_insercion(arr, objetivo)
        print(f"Indice de insercion/encontrado: {pos}")
