"""
Planteamiento:
Implementar Merge Sort para una lista enlazada simple sin usar arreglos.
Definir clase Nodo y funciones de division/fusion necesarias.

Solucion:
Se usa enfoque divide y conquista:
- Dividir la lista en dos mitades con punteros lento/rapido.
- Ordenar recursivamente cada mitad.
- Fusionar ambas listas ordenadas.
Complejidad temporal: O(n log n).
Complejidad espacial adicional: O(log n) por recursion.
"""


# Clase basica de nodo para lista enlazada simple.
class Nodo:
    # Constructor del nodo con dato y siguiente opcional.
    def __init__(self, valor: int, siguiente: "Nodo | None" = None) -> None:
        # Se guarda valor del nodo.
        self.valor = valor
        # Se guarda referencia al siguiente nodo.
        self.siguiente = siguiente


# Convierte lista Python a lista enlazada.
def construir_lista_enlazada(valores: list[int]) -> Nodo | None:
    # Si no hay valores, la lista enlazada queda vacia.
    if len(valores) == 0:
        return None
    # Se crea cabeza con primer valor.
    cabeza = Nodo(valores[0])
    # Puntero actual para ir enlazando.
    actual = cabeza
    # Se recorren valores restantes.
    for valor in valores[1:]:
        # Se crea nuevo nodo al final.
        actual.siguiente = Nodo(valor)
        # Se avanza puntero.
        actual = actual.siguiente
    # Se retorna cabeza de la lista construida.
    return cabeza


# Convierte lista enlazada a lista Python para mostrar resultados.
def lista_a_python(cabeza: Nodo | None) -> list[int]:
    # Se crea contenedor de salida.
    salida: list[int] = []
    # Se inicia recorrido desde cabeza.
    actual = cabeza
    # Se recorre hasta llegar a None.
    while actual is not None:
        # Se agrega valor actual.
        salida.append(actual.valor)
        # Se avanza al siguiente nodo.
        actual = actual.siguiente
    # Se retorna lista de valores.
    return salida


# Divide lista enlazada en dos mitades y retorna inicio de cada mitad.
def dividir_mitad(cabeza: Nodo) -> tuple[Nodo, Nodo]:
    # Puntero lento avanza de uno en uno.
    lento = cabeza
    # Puntero rapido avanza de dos en dos.
    rapido = cabeza
    # Puntero previo para cortar lista al dividir.
    previo: Nodo | None = None
    # Mientras rapido pueda avanzar dos pasos, seguimos.
    while rapido is not None and rapido.siguiente is not None:
        # Guardamos posicion de lento para corte final.
        previo = lento
        # Lento avanza un nodo.
        lento = lento.siguiente  # type: ignore[assignment]
        # Rapido avanza dos nodos.
        rapido = rapido.siguiente.siguiente
    # Se corta enlace para separar mitad izquierda.
    if previo is not None:
        previo.siguiente = None
    # Se retorna inicio de mitad izquierda (cabeza) y derecha (lento).
    return cabeza, lento


# Fusiona dos listas enlazadas ya ordenadas.
def fusionar_ordenadas(a: Nodo | None, b: Nodo | None) -> Nodo | None:
    # Si una lista es vacia, retorna la otra.
    if a is None:
        return b
    if b is None:
        return a
    # Se elige nodo menor para iniciar resultado.
    if a.valor <= b.valor:
        resultado = a
        resultado.siguiente = fusionar_ordenadas(a.siguiente, b)
    else:
        resultado = b
        resultado.siguiente = fusionar_ordenadas(a, b.siguiente)
    return resultado


# Merge sort recursivo para lista enlazada.
def merge_sort_lista(cabeza: Nodo | None) -> Nodo | None:
    # Caso base: lista vacia o de un nodo ya esta ordenada.
    if cabeza is None or cabeza.siguiente is None:
        return cabeza
    # Se divide en dos mitades.
    izquierda, derecha = dividir_mitad(cabeza)
    # Se ordena mitad izquierda recursivamente.
    izquierda_ordenada = merge_sort_lista(izquierda)
    # Se ordena mitad derecha recursivamente.
    derecha_ordenada = merge_sort_lista(derecha)
    # Se fusionan ambas mitades ordenadas.
    return fusionar_ordenadas(izquierda_ordenada, derecha_ordenada)


if __name__ == "__main__":
    print("Ejercicio resuelto 4 - Merge Sort en lista enlazada simple")
    datos = [4, 2, 1, 3, 7, 5]
    cabeza = construir_lista_enlazada(datos)
    print(f"Entrada: {lista_a_python(cabeza)}")
    ordenada = merge_sort_lista(cabeza)
    print(f"Salida ordenada: {lista_a_python(ordenada)}")
