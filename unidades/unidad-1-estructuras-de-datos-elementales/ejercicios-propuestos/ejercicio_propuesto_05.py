"""
Ejercicio propuesto 5 - Solucion independiente.

Enunciado:
Aplicar Teorema I para h=2, h=4 y h=5, usando Nmax = 2^(h+1)-1.

Desarrollo de la solucion propuesta:
- Se itera por cada altura.
- Se aplica formula directa del teorema.
"""

# Define alturas del enunciado.
alturas = [2, 4, 5]

# Imprime encabezado.
print("Ejercicio propuesto 5")
print("Enunciado: calcular Nmax para h=2, h=4, h=5.")
print("Desarrollo de la solucion propuesta: Nmax = 2^(h+1)-1.")

# Recorre alturas.
for h in alturas:
    # Aplica formula del teorema I.
    nmax = (2 ** (h + 1)) - 1
    # Imprime resultado.
    print(f"Resultado -> h={h}: Nmax={nmax}")
