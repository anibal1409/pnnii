"""
Planteamiento:
Implementar Quicksort con particion de Hoare (dos indices desde extremos)
y comentar diferencias generales frente a Lomuto.

Solucion:
Se usan dos punteros:
- uno avanza desde izquierda buscando elemento fuera de lugar;
- otro retrocede desde derecha buscando elemento fuera de lugar.
Cuando ambos encuentran desorden relativo al pivote, se intercambian.
Complejidad promedio: O(n log n).
Peor caso: O(n^2) con pivotes desfavorables.
"""


# Funcion para parsear lista de entrada desde consola.
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


# Particion tipo Hoare usando pivote en posicion media.
def particion_hoare(arr: list[int], bajo: int, alto: int) -> int:
    # Se elige pivote como valor medio del rango.
    pivote = arr[(bajo + alto) // 2]
    # i inicia antes del rango para avanzar hacia la derecha.
    i = bajo - 1
    # j inicia despues del rango para retroceder hacia la izquierda.
    j = alto + 1
    # Se repite hasta que punteros se crucen.
    while True:
        # Avanzar i hasta encontrar valor >= pivote.
        i += 1
        while arr[i] < pivote:
            i += 1
        # Retroceder j hasta encontrar valor <= pivote.
        j -= 1
        while arr[j] > pivote:
            j -= 1
        # Si se cruzaron, j marca punto de corte.
        if i >= j:
            return j
        # Si no se cruzan, se intercambian elementos fuera de lugar.
        arr[i], arr[j] = arr[j], arr[i]


# Quicksort recursivo con particion Hoare.
def quicksort_hoare(arr: list[int], bajo: int, alto: int) -> None:
    # Caso recursivo cuando existe al menos dos elementos.
    if bajo < alto:
        # Se particiona y obtiene indice de separacion.
        p = particion_hoare(arr, bajo, alto)
        # Se ordena lado izquierdo incluyendo p.
        quicksort_hoare(arr, bajo, p)
        # Se ordena lado derecho desde p+1.
        quicksort_hoare(arr, p + 1, alto)


if __name__ == "__main__":
    print("Ejercicio resuelto 5 - Quicksort con particion tipo Hoare")
    try:
        arr = parsear_lista(input("Lista (ej: 9,4,8,3,1,2): "))
    except ValueError as error:
        print(f"Entrada invalida: {error}")
    else:
        print(f"Entrada original: {arr}")
        quicksort_hoare(arr, 0, len(arr) - 1)
        print(f"Salida ordenada: {arr}")
        print("Comentario: Hoare usa dos indices extremos; Lomuto usa un pivote final y un indice de frontera.")
