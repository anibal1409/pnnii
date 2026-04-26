"""
Ejercicio propuesto 2 - Solucion independiente.

Enunciado:
Dado el arbol: M->[N,O], N->[P], O->[Q,R], determinar hojas, altura y nodo de mayor grado.

Desarrollo de la solucion propuesta:
- Se calcula nivel de cada nodo con BFS.
- Se identifican hojas como nodos sin hijos.
- Se busca el nodo con mayor grado.
"""

# Importa deque para recorrido por niveles.
from collections import deque

# Define estructura del arbol.
tree = {
    "M": ["N", "O"],
    "N": ["P"],
    "O": ["Q", "R"],
    "P": [],
    "Q": [],
    "R": [],
}

# Inicializa niveles.
niveles = {"M": 0}
# Crea cola BFS.
cola = deque(["M"])
# Recorre arbol.
while cola:
    # Saca nodo.
    nodo = cola.popleft()
    # Recorre hijos.
    for hijo in tree[nodo]:
        # Guarda nivel.
        niveles[hijo] = niveles[nodo] + 1
        # Encola hijo.
        cola.append(hijo)

# Calcula hojas.
hojas = [nodo for nodo, hijos in tree.items() if len(hijos) == 0]
# Calcula altura.
altura = max(niveles.values())
# Calcula grados.
grados = {nodo: len(hijos) for nodo, hijos in tree.items()}
# Obtiene nodo con mayor grado.
nodo_mayor_grado = max(grados, key=grados.get)

# Imprime resultados.
print("Ejercicio propuesto 2")
print("Enunciado: hojas, altura y nodo de mayor grado.")
print("Desarrollo de la solucion propuesta: BFS + filtro de hojas + maximo grado.")
print(f"Resultado -> hojas: {hojas}")
print(f"Resultado -> altura: {altura}")
print(f"Resultado -> nodo con mayor grado: {nodo_mayor_grado} (grado={grados[nodo_mayor_grado]})")
