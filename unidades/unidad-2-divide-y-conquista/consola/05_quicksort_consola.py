"""
Objetivo del modulo:
Practicar Quicksort con particion de Lomuto y opcion mediana de tres.

Enunciado:
Ordenar una lista de enteros con Quicksort usando particion de Lomuto,
y opcionalmente mejorar eleccion de pivote con mediana de tres.

Explicacion breve:
Quicksort organiza elementos menores o iguales a la izquierda del pivote
y mayores a la derecha, repitiendo recursivamente.

Desarrollo de la solucion propuesta:
- Elegir pivote (ultimo o mediana de tres).
- Particionar con esquema de Lomuto.
- Ordenar subrangos izquierdo y derecho.
"""


def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay elementos vacios.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


def elegir_pivote_mediana_tres(arr: list[int], bajo: int, alto: int) -> int:
    medio = (bajo + alto) // 2
    candidatos = [(arr[bajo], bajo), (arr[medio], medio), (arr[alto], alto)]
    candidatos.sort(key=lambda x: x[0])
    return candidatos[1][1]


def particion_lomuto(arr: list[int], bajo: int, alto: int, pasos: list[str], comparaciones: list[int]) -> int:
    pivote = arr[alto]
    i = bajo - 1
    pasos.append(f"Particion Lomuto en [{bajo},{alto}], pivote={pivote}.")
    for j in range(bajo, alto):
        comparaciones[0] += 1
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            pasos.append(f"Intercambio <= pivote: {arr}")
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    pasos.append(f"Pivote a posicion final: {arr}")
    return i + 1


def quicksort(arr: list[int], bajo: int, alto: int, pasos: list[str], comparaciones: list[int], mediana: bool) -> None:
    # Big O: promedio/mejor O(n log n), peor O(n^2) con pivotes malos.
    if bajo < alto:
        if mediana:
            idx = elegir_pivote_mediana_tres(arr, bajo, alto)
            arr[idx], arr[alto] = arr[alto], arr[idx]
            pasos.append(f"Mediana de tres elegida, pivote movido al final: {arr[alto]}.")
        p = particion_lomuto(arr, bajo, alto, pasos, comparaciones)
        quicksort(arr, bajo, p - 1, pasos, comparaciones, mediana)
        quicksort(arr, p + 1, alto, pasos, comparaciones, mediana)


def main() -> None:
    print("=== Ejercicio 5.1 - Quicksort (Consola) ===")
    print("Enunciado: ordenar una lista con Quicksort (Lomuto) y opcion mediana de tres.")
    print("Explicacion breve: cada particion deja el pivote en su posicion final.")
    entrada = input("Ingresa numeros separados por coma: ")
    try:
        arr = parsear_lista(entrada)
    except ValueError as error:
        print(f"Entrada invalida: {error}")
        return
    print("Elige variante: 1) Lomuto basico  2) Lomuto + mediana de tres")
    opcion = input("Opcion: ").strip()
    usar_mediana = opcion == "2"
    pasos: list[str] = []
    comparaciones = [0]
    quicksort(arr, 0, len(arr) - 1, pasos, comparaciones, usar_mediana)
    print("\n--- Particiones ---")
    for paso in pasos:
        print(f"- {paso}")
    print(f"\nResultado ordenado: {arr}")
    print(f"Comparaciones registradas: {comparaciones[0]}")


if __name__ == "__main__":
    main()
