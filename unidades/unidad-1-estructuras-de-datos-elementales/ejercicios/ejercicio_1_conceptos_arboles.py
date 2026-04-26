"""
UNIDAD I - Ejercicio 1
Tema: Conceptos basicos de arbol, altura, nivel y grado.

Enunciado:
Dado un arbol representado por relaciones padre -> hijos, determinar:
1) Altura del arbol.
2) Nivel de cada nodo.
3) Grado de cada nodo.

Resultado esperado:
- Altura: 2
- Niveles: A=0, B=1, C=1, D=2, E=2, F=2
- Grados: A=2, B=2, C=1, D=0, E=0, F=0

Explicacion general:
- Se modela un arbol con un diccionario (lista de adyacencia).
- Se calcula el nivel con recorrido en anchura (BFS).
- Se obtiene la altura como el maximo nivel.
- Se obtiene el grado contando hijos directos de cada nodo.

Explicacion breve:
En este ejercicio aprenderas a leer un arbol paso a paso: primero ubicamos
en que nivel esta cada nodo, luego hallamos la altura total y finalmente
contamos cuantos hijos tiene cada nodo (grado).

Desarrollo de la solucion propuesta:
- Se define un arbol con diccionario padre -> hijos.
- Se aplica BFS para calcular niveles.
- Se obtiene altura como maximo nivel.
- Se obtiene grado como cantidad de hijos por nodo.
"""

# Importa deque para manejar la cola de BFS eficientemente.
from collections import deque


# Define el arbol de ejemplo como padre -> lista de hijos.
TREE = {
    # Nodo raiz con dos hijos.
    "A": ["B", "C"],
    # Nodo interno con dos hijos.
    "B": ["D", "E"],
    # Nodo interno con un hijo.
    "C": ["F"],
    # Nodos hoja sin hijos.
    "D": [],
    # Nodos hoja sin hijos.
    "E": [],
    # Nodos hoja sin hijos.
    "F": [],
}


def calcular_niveles(raiz: str, estructura: dict[str, list[str]]) -> dict[str, int]:
    """Recorre en anchura para obtener el nivel de cada nodo."""
    # Inicializa niveles: la raiz siempre esta en nivel 0.
    niveles: dict[str, int] = {raiz: 0}
    # Inicializa cola BFS con la raiz.
    cola: deque[str] = deque([raiz])

    # Procesa nodos mientras haya elementos pendientes en la cola.
    while cola:
        # Extrae el nodo actual desde el frente de la cola.
        nodo = cola.popleft()
        # Recorre hijos directos del nodo actual.
        for hijo in estructura.get(nodo, []):
            # Asigna al hijo el nivel del padre + 1.
            niveles[hijo] = niveles[nodo] + 1
            # Encola el hijo para procesar sus descendientes.
            cola.append(hijo)
    # Devuelve el diccionario completo de niveles.
    return niveles


def calcular_altura(niveles: dict[str, int]) -> int:
    """La altura es el nivel maximo desde la raiz."""
    # Retorna el valor maximo de todos los niveles calculados.
    return max(niveles.values())


def calcular_grados(estructura: dict[str, list[str]]) -> dict[str, int]:
    """El grado es la cantidad de hijos directos."""
    # Construye un diccionario nodo -> cantidad de hijos.
    return {nodo: len(hijos) for nodo, hijos in estructura.items()}


def ejecutar_ejercicio_1() -> None:
    # Calcula niveles partiendo de la raiz A.
    niveles = calcular_niveles("A", TREE)
    # Calcula altura usando los niveles obtenidos.
    altura = calcular_altura(niveles)
    # Calcula grado por nodo usando la estructura del arbol.
    grados = calcular_grados(TREE)

    # Imprime encabezado del ejercicio.
    print("Ejercicio 1 - Conceptos basicos de arbol")
    # Imprime explicacion breve orientada a estudiantes principiantes.
    print(
        "Explicacion breve: analizamos niveles, altura y grado para entender "
        "como se describe la estructura basica de un arbol."
    )
    # Imprime el enunciado del ejercicio.
    print("Enunciado:")
    print("calcular altura, niveles y grados del arbol dado.")
    # Imprime titulo separado para el desarrollo de la solucion.
    print("Desarrollo de la solucion propuesta:")
    print("- aplicar BFS para niveles")
    print("- obtener altura como maximo nivel")
    print("- obtener grado por cantidad de hijos")
    # Imprime resultado de altura.
    print(f"Resultado -> Altura: {altura}")
    # Imprime resultado de niveles.
    print(f"Resultado -> Niveles: {niveles}")
    # Imprime resultado de grados.
    print(f"Resultado -> Grados: {grados}")
