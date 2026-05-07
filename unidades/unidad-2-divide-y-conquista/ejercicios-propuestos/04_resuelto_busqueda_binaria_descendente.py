"""
Planteamiento:
Adaptar la busqueda binaria para una lista ordenada en forma descendente
(de mayor a menor), explicando que condicion de comparacion cambia.

Solucion:
La logica es igual a busqueda binaria normal, pero las decisiones de
izquierda/derecha se invierten por el orden descendente.
Complejidad temporal: O(log n).
Complejidad espacial: O(1) en version iterativa.
"""

# Funcion que valida y parsea una lista descendente.
def parsear_descendente(texto: str) -> list[int]:
    # Se separa entrada por comas.
    partes = texto.split(",")
    # Se crea lista de salida.
    numeros: list[int] = []
    # Se recorre cada parte para limpiarla.
    for parte in partes:
        # Se elimina espacios alrededor.
        token = parte.strip()
        # Se valida que el token no este vacio.
        if token == "":
            # Se lanza error si hay huecos.
            raise ValueError("Hay elementos vacios en la lista.")
        # Se convierte token a entero.
        numeros.append(int(token))
    # Se valida que lista no quede vacia.
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    # Se valida que realmente este en orden descendente.
    if numeros != sorted(numeros, reverse=True):
        raise ValueError("La lista debe estar ordenada de mayor a menor.")
    # Se retorna lista valida.
    return numeros


# Busqueda binaria iterativa para orden descendente.
def busqueda_binaria_desc(arr: list[int], objetivo: int) -> int:
    # Se inicializa extremo izquierdo.
    inicio = 0
    # Se inicializa extremo derecho.
    fin = len(arr) - 1
    # Se itera mientras exista rango valido.
    while inicio <= fin:
        # Se calcula posicion central.
        medio = (inicio + fin) // 2
        # Si coincide, se retorna indice.
        if arr[medio] == objetivo:
            return medio
        # En descendente: si objetivo es mayor, se mueve a la izquierda.
        if objetivo > arr[medio]:
            fin = medio - 1
        else:
            # Si objetivo es menor, se mueve a la derecha.
            inicio = medio + 1
    # Si termina el ciclo, no se encontro.
    return -1


# Bloque principal con ejemplo interactivo.
if __name__ == "__main__":
    print("Ejercicio resuelto 1 - Busqueda binaria descendente")
    try:
        arr = parsear_descendente(input("Lista descendente (ej: 9,7,5,2): "))
        objetivo = int(input("Objetivo a buscar: ").strip())
    except ValueError as error:
        print(f"Entrada invalida: {error}")
    else:
        indice = busqueda_binaria_desc(arr, objetivo)
        if indice != -1:
            print(f"Resultado: encontrado en indice {indice}.")
        else:
            print("Resultado: no encontrado.")
