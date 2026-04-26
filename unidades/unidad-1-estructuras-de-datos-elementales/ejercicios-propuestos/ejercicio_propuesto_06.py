"""
Ejercicio propuesto 6 - Solucion independiente.

Enunciado:
Aplicar Teorema II para I=3, I=8 e I=12, usando L = I + 1.

Desarrollo de la solucion propuesta:
- Se recorre cada valor de nodos internos.
- Se calcula hojas con formula directa.
"""

# Define nodos internos solicitados.
internos = [3, 8, 12]

# Imprime encabezado.
print("Ejercicio propuesto 6")
print("Enunciado: calcular hojas para I=3, I=8 e I=12.")
print("Desarrollo de la solucion propuesta: L = I + 1.")

# Recorre cada valor interno.
for i in internos:
    # Aplica Teorema II.
    hojas = i + 1
    # Imprime resultado.
    print(f"Resultado -> I={i}: hojas={hojas}")
