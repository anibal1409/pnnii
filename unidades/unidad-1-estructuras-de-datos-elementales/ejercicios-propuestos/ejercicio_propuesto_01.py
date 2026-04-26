"""
Ejercicio propuesto 1 - Solucion independiente.

Enunciado:
Dado el arbol: A->[B,C], B->[D,E], C->[F,G], calcular nivel, altura y grado.

Desarrollo de la solucion propuesta:
- Se modela el arbol con diccionario padre->hijos.
- Se aplica BFS para niveles.
- Se calcula altura como maximo nivel.
- Se calcula grado contando hijos por nodo.
"""

# Importa deque para recorrido por niveles.
from collections import deque

# Define el arbol de entrada del ejercicio.
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

# Inicializa niveles con la raiz.
niveles = {"A": 0}
# Crea cola para BFS.
cola = deque(["A"])
# Recorre mientras existan nodos pendientes.
while cola:
    # Extrae nodo actual.
    nodo = cola.popleft()
    # Recorre hijos directos del nodo.
    for hijo in tree[nodo]:
        # Asigna nivel del hijo.
        niveles[hijo] = niveles[nodo] + 1
        # Encola hijo.
        cola.append(hijo)

# Calcula altura del arbol.
altura = max(niveles.values())
# Calcula grado de cada nodo.
grados = {nodo: len(hijos) for nodo, hijos in tree.items()}

# Imprime resultados.
print("Ejercicio propuesto 1")
print("Enunciado: calcular nivel, altura y grado.")
print("Desarrollo de la solucion propuesta: BFS + max nivel + conteo de hijos.")
print(f"Resultado -> niveles: {niveles}")
print(f"Resultado -> altura: {altura}")
print(f"Resultado -> grados: {grados}")
