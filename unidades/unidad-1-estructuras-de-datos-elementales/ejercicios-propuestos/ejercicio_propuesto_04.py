"""
Ejercicio propuesto 4 - Solucion independiente.

Enunciado:
En arreglo secuencial ['A','B','C','D','E','F','G','H'], hallar padre e hijos de indices 1 y 2.

Desarrollo de la solucion propuesta:
- padre(i)=(i-1)//2
- hijo_izq(i)=2*i+1
- hijo_der(i)=2*i+2
"""

# Define arreglo secuencial del arbol.
arr = ["A", "B", "C", "D", "E", "F", "G", "H"]
# Define indices solicitados.
indices = [1, 2]

# Imprime encabezado.
print("Ejercicio propuesto 4")
print("Enunciado: hallar padre e hijos para indices 1 y 2.")
print("Desarrollo de la solucion propuesta: usar formulas de indice en arbol secuencial.")

# Recorre indices de interes.
for i in indices:
    # Calcula indice de padre.
    padre_i = (i - 1) // 2 if i > 0 else None
    # Calcula indices de hijos.
    izq_i = 2 * i + 1
    der_i = 2 * i + 2
    # Recupera valores o None si no existen.
    padre = arr[padre_i] if padre_i is not None else None
    izq = arr[izq_i] if izq_i < len(arr) else None
    der = arr[der_i] if der_i < len(arr) else None
    # Imprime resultado para el indice.
    print(f"Resultado -> indice {i} ({arr[i]}): padre={padre}, hijo_izq={izq}, hijo_der={der}")
