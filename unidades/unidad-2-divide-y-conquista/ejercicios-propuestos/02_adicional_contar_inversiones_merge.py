"""
Planteamiento:
Una inversion es un par (i, j) tal que i < j y arr[i] > arr[j].
Dado un arreglo, contar cuantas inversiones existen usando la tecnica
de Merge Sort, para evitar el enfoque cuadratico de revisar todos los pares.

Solucion:
Se adapta merge sort para contar inversiones durante la fusion:
cuando un elemento de la mitad derecha pasa antes que uno de la izquierda,
eso implica inversiones con todos los elementos restantes de la izquierda.
Complejidad temporal: O(n log n).
Complejidad espacial: O(n).
"""

# Esta funcion fusiona dos mitades ordenadas y cuenta inversiones cruzadas.
def merge_y_contar(arr: list[int], inicio: int, medio: int, fin: int) -> int:
    # Se copia la mitad izquierda para poder intercalar sin perder datos.
    izquierda = arr[inicio:medio + 1]
    # Se copia la mitad derecha para intercalar de forma estable.
    derecha = arr[medio + 1:fin + 1]
    # Se inicializa indice de recorrido para izquierda.
    i = 0
    # Se inicializa indice de recorrido para derecha.
    j = 0
    # Se inicializa indice de escritura en arreglo original.
    k = inicio
    # Se inicia contador local de inversiones cruzadas.
    inversiones = 0
    # Se intercalan elementos mientras ambas mitades tengan elementos pendientes.
    while i < len(izquierda) and j < len(derecha):
        # Si izquierda es menor o igual, no crea inversion.
        if izquierda[i] <= derecha[j]:
            # Se escribe valor de izquierda en posicion actual.
            arr[k] = izquierda[i]
            # Se avanza indice izquierdo.
            i += 1
        else:
            # Si derecha es menor, se escribe primero y se cuentan inversiones.
            arr[k] = derecha[j]
            # Se suman todas las inversiones con elementos restantes de izquierda.
            inversiones += len(izquierda) - i
            # Se avanza indice derecho.
            j += 1
        # Se avanza posicion de escritura.
        k += 1
    # Se copian elementos faltantes de izquierda, si existen.
    while i < len(izquierda):
        # Se coloca siguiente valor pendiente de izquierda.
        arr[k] = izquierda[i]
        # Se avanza indice izquierdo.
        i += 1
        # Se avanza posicion de escritura.
        k += 1
    # Se copian elementos faltantes de derecha, si existen.
    while j < len(derecha):
        # Se coloca siguiente valor pendiente de derecha.
        arr[k] = derecha[j]
        # Se avanza indice derecho.
        j += 1
        # Se avanza posicion de escritura.
        k += 1
    # Se retorna cantidad de inversiones encontradas en esta fusion.
    return inversiones


# Esta funcion aplica merge sort y acumula conteo total de inversiones.
def contar_inversiones_dc(arr: list[int], inicio: int, fin: int) -> int:
    # Caso base: si hay 0 o 1 elemento, no hay inversiones.
    if inicio >= fin:
        # Se retorna cero porque no hay pares i < j.
        return 0
    # Se calcula punto medio para dividir el arreglo.
    medio = (inicio + fin) // 2
    # Se cuentan inversiones de la mitad izquierda recursivamente.
    inv_izquierda = contar_inversiones_dc(arr, inicio, medio)
    # Se cuentan inversiones de la mitad derecha recursivamente.
    inv_derecha = contar_inversiones_dc(arr, medio + 1, fin)
    # Se cuentan inversiones cruzadas durante la fusion.
    inv_cruzadas = merge_y_contar(arr, inicio, medio, fin)
    # Se retorna suma total de los tres componentes.
    return inv_izquierda + inv_derecha + inv_cruzadas


# Funcion auxiliar para no modificar el arreglo original recibido por usuario.
def contar_inversiones(arr: list[int]) -> int:
    # Se crea una copia para preservar entrada original.
    copia = arr.copy()
    # Se maneja caso de lista vacia de forma segura.
    if len(copia) == 0:
        # Lista vacia tiene cero inversiones.
        return 0
    # Se llama algoritmo sobre todo el rango de indices.
    return contar_inversiones_dc(copia, 0, len(copia) - 1)


# Bloque de prueba con ejemplos directos.
if __name__ == "__main__":
    # Arreglo de ejemplo con inversiones.
    arreglo_1 = [2, 4, 1, 3, 5]
    # Arreglo ya ordenado para contraste.
    arreglo_2 = [1, 2, 3, 4, 5]
    # Arreglo en orden inverso para mayor numero de inversiones.
    arreglo_3 = [5, 4, 3, 2, 1]
    # Se imprime encabezado.
    print("Ejercicio adicional 2 - Contar inversiones con Merge Sort")
    # Se imprime resultado del primer caso.
    print(f"{arreglo_1} -> inversiones: {contar_inversiones(arreglo_1)}")
    # Se imprime resultado del segundo caso.
    print(f"{arreglo_2} -> inversiones: {contar_inversiones(arreglo_2)}")
    # Se imprime resultado del tercer caso.
    print(f"{arreglo_3} -> inversiones: {contar_inversiones(arreglo_3)}")
