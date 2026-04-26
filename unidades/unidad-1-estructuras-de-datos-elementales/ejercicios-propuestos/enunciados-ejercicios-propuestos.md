# Unidad I - Enunciados de ejercicios propuestos

Este documento contiene los enunciados para que el estudiante practique.

## Contenido 1: Conceptos basicos de arbol, altura, nivel y grado

### Ejercicio propuesto 1
Dado el arbol: `A -> [B, C]`, `B -> [D, E]`, `C -> [F, G]`, calcule:
1. Nivel de cada nodo.
2. Altura del arbol.
3. Grado de cada nodo.

### Ejercicio propuesto 2
Dado el arbol: `M -> [N, O]`, `N -> [P]`, `O -> [Q, R]`, determine:
1. Cuales nodos son hojas.
2. Altura total del arbol.
3. Nodo con mayor grado.

## Contenido 2: Tipos de arboles (Binarios y Heap)

### Ejercicio propuesto 3
Dadas las estructuras siguientes, indique si cada una es:
- Arbol binario valido.
- Max-heap valido.
- Min-heap valido.

Estructura A: `[90, 70, 60, 40, 20, 10, 30]`
Estructura B: `[10, 20, 15, 30, 40, 18, 22]`
Estructura C: `[50, 40, 60, 20, 45]`

### Ejercicio propuesto 4
A partir de un arreglo secuencial de arbol binario completo `['A','B','C','D','E','F','G','H']`, para los indices `1` y `2` calcule:
1. Padre.
2. Hijo izquierdo.
3. Hijo derecho.

## Contenido 3: Teoremas I y II para arboles binarios

### Ejercicio propuesto 5
Aplique el Teorema I para alturas `h=2`, `h=4` y `h=5`, calculando `Nmax = 2^(h+1)-1`.

### Ejercicio propuesto 6
Aplique el Teorema II para nodos internos `I=3`, `I=8` y `I=12`, calculando hojas `L=I+1`.

## Contenido 4: Algoritmos INSERTAR y HEAPIFY

### Ejercicio propuesto 7
En el max-heap `[85, 70, 60, 20, 50, 40, 10]`, inserte `75` y muestre los pasos de bubble-up.

### Ejercicio propuesto 8
Aplique `HEAPIFY` desde indice `0` al arreglo `[35, 90, 80, 20, 40, 10, 60]` y muestre cada intercambio hasta restaurar max-heap.
