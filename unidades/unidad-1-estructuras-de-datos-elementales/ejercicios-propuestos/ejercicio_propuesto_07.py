"""
Ejercicio propuesto 7 - Solucion independiente.

Enunciado:
En max-heap [85,70,60,20,50,40,10], insertar 75 y mostrar pasos.

Desarrollo de la solucion propuesta:
- Se inserta al final.
- Se aplica bubble-up comparando con padre.
- Se registran intercambios.
"""

# Define heap inicial.
heap = [85, 70, 60, 20, 50, 40, 10]
# Define valor a insertar.
valor = 75

# Imprime encabezado.
print("Ejercicio propuesto 7")
print("Enunciado: insertar 75 en max-heap y mostrar pasos.")
print("Desarrollo de la solucion propuesta: insercion al final + bubble-up.")
print(f"Paso -> heap inicial: {heap}")

# Inserta valor al final.
heap.append(valor)
print(f"Paso -> insertar {valor} al final: {heap}")

# Inicializa indice del nuevo elemento.
i = len(heap) - 1
# Recorre mientras pueda subir.
while i > 0:
    # Calcula indice del padre.
    padre = (i - 1) // 2
    # Si propiedad max-heap se cumple, termina.
    if heap[padre] >= heap[i]:
        print("Paso -> propiedad max-heap cumplida. Fin.")
        break
    # Imprime intercambio.
    print(f"Paso -> intercambiar {heap[i]} con {heap[padre]}")
    # Intercambia valores.
    heap[padre], heap[i] = heap[i], heap[padre]
    # Sube al padre.
    i = padre
    # Imprime estado actual.
    print(f"Paso -> estado actual: {heap}")

# Imprime resultado final.
print(f"Resultado -> heap final: {heap}")
