"""
Objetivo del modulo:
Ordenar una lista con Merge Sort recursivo (top-down) y mostrar pasos.

Enunciado:
Ordenar una lista de enteros aplicando Merge Sort recursivo top-down:
dividir en mitades, ordenar cada mitad y fusionar en orden.

Explicacion breve:
Merge Sort divide hasta listas de un elemento (caso base) y luego
combina de forma ordenada. Su complejidad temporal es O(n log n).

Desarrollo de la solucion propuesta:
- Dividir recursivamente por medio.
- Aplicar merge para intercalar dos mitades ordenadas.
- Mostrar pasos y resultado final.
"""


# Convierte un texto en lista de enteros.
def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Formato invalido: hay elementos vacios.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


# Funcion merge segun teoria: combina dos mitades ordenadas dentro de arr.
def merge(arr: list[int], inicio: int, medio: int, fin: int, pasos: list[str]) -> None:
    # Se crean copias de mitades para fusionar sin perder datos.
    izquierda = arr[inicio:medio + 1]
    derecha = arr[medio + 1:fin + 1]
    pasos.append(f"Merge de {izquierda} y {derecha}.")
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
    pasos.append(f"Resultado parcial: {arr[inicio:fin+1]}")


# Merge Sort top-down recursivo.
def merge_sort_recursivo(arr: list[int], inicio: int, fin: int, pasos: list[str]) -> None:
    # Big O temporal: O(n log n) en mejor, promedio y peor caso.
    # Big O espacial: O(n) por copias auxiliares en merge.
    if inicio >= fin:
        return
    medio = (inicio + fin) // 2
    pasos.append(f"Dividir rango [{inicio},{fin}] en [{inicio},{medio}] y [{medio+1},{fin}].")
    merge_sort_recursivo(arr, inicio, medio, pasos)
    merge_sort_recursivo(arr, medio + 1, fin, pasos)
    merge(arr, inicio, medio, fin, pasos)


def main() -> None:
    print("=== Ejercicio 3.1 - Merge Sort Recursivo (Consola) ===")
    print("Enunciado: ordenar una lista usando Merge Sort recursivo (top-down).")
    print("Explicacion breve: dividir, conquistar y combinar con merge.")
    entrada = input("Ingresa numeros separados por coma: ")
    try:
        arr = parsear_lista(entrada)
    except ValueError as error:
        print(f"Entrada invalida: {error}")
        return
    mostrar = input("Deseas ver pasos? (s/n): ").strip().lower() == "s"
    pasos: list[str] = []
    merge_sort_recursivo(arr, 0, len(arr) - 1, pasos)
    if mostrar:
        print("\n--- Pasos ---")
        for paso in pasos:
            print(f"- {paso}")
    print(f"\nResultado ordenado: {arr}")


if __name__ == "__main__":
    main()
