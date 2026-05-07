"""
Planteamiento:
Dada una matriz de tamano m x n donde cada fila esta ordenada de izquierda a
derecha y cada columna de arriba hacia abajo, determinar si un objetivo existe
en la matriz usando una estrategia de divide y conquista (sin recorrido lineal
completo de toda la matriz).

Solucion:
Se aplica una busqueda por "escalera" desde la esquina superior derecha.
En cada paso se descarta una fila o una columna completa:
- Si el valor actual es mayor que el objetivo, se mueve a la izquierda.
- Si el valor actual es menor que el objetivo, se mueve hacia abajo.
Esto reduce el espacio de busqueda de forma sistematica.
Complejidad temporal: O(m + n).
Complejidad espacial: O(1).
"""

# Esta funcion busca un objetivo en una matriz ordenada por filas y columnas.
def buscar_en_matriz_ordenada(matriz: list[list[int]], objetivo: int) -> bool:
    # Se valida si la matriz esta vacia para evitar errores de indices.
    if len(matriz) == 0:
        # Si no hay filas, no existe el objetivo.
        return False
    # Se valida si la primera fila esta vacia para cubrir matriz sin columnas.
    if len(matriz[0]) == 0:
        # Si no hay columnas, tampoco existe el objetivo.
        return False
    # Se obtiene cantidad de filas para limitar movimiento vertical.
    filas = len(matriz)
    # Se obtiene cantidad de columnas para limitar movimiento horizontal.
    columnas = len(matriz[0])
    # Se inicia en la fila superior, indice 0.
    fila = 0
    # Se inicia en la columna mas a la derecha.
    columna = columnas - 1
    # Se repite mientras el indice de fila y columna permanezcan en rango valido.
    while fila < filas and columna >= 0:
        # Se lee el valor actual de la celda en la posicion evaluada.
        valor_actual = matriz[fila][columna]
        # Si el valor actual coincide con el objetivo, ya se encontro.
        if valor_actual == objetivo:
            # Se retorna True para indicar exito.
            return True
        # Si el valor actual es mayor, la columna actual y derecha no sirven.
        if valor_actual > objetivo:
            # Se mueve una columna a la izquierda.
            columna -= 1
        else:
            # Si el valor actual es menor, la fila actual y superiores no sirven.
            fila += 1
    # Si se sale del ciclo, se agotaron opciones y no se encontro.
    return False


# Punto de entrada para probar el ejercicio con datos de ejemplo.
if __name__ == "__main__":
    # Se define matriz ordenada por filas y columnas.
    matriz_prueba = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17],
    ]
    # Se define primer objetivo existente.
    objetivo_1 = 9
    # Se define segundo objetivo no existente.
    objetivo_2 = 15
    # Se imprime encabezado didactico.
    print("Ejercicio adicional 1 - Busqueda en matriz ordenada")
    # Se muestra matriz usada.
    print(f"Matriz: {matriz_prueba}")
    # Se muestra resultado para objetivo existente.
    print(f"Buscar {objetivo_1}: {buscar_en_matriz_ordenada(matriz_prueba, objetivo_1)}")
    # Se muestra resultado para objetivo no existente.
    print(f"Buscar {objetivo_2}: {buscar_en_matriz_ordenada(matriz_prueba, objetivo_2)}")
