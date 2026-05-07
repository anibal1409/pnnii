# Unidad II - Enunciados de ejercicios propuestos

Este documento contiene los enunciados de todos los ejercicios desarrollados en `ejercicios-propuestos/`.

## Ejercicios adicionales

### Ejercicio adicional 1: Busqueda binaria en una matriz ordenada
Dada una matriz de tamano `m x n` donde cada fila esta ordenada de izquierda a derecha y cada columna de arriba hacia abajo, implementar un algoritmo basado en divide y conquista para determinar si un valor objetivo pertenece a la matriz.

### Ejercicio adicional 2: Contar inversiones en un arreglo con Merge Sort
Una inversion es un par `(i, j)` tal que `i < j` y `arr[i] > arr[j]`. Dado un arreglo de enteros, implementar una solucion eficiente para contar el total de inversiones usando la tecnica de merge sort.

### Ejercicio adicional 3: k-esimo elemento mas pequeno (Quickselect)
Dado un arreglo de enteros y un valor `k` (iniciando en 1), implementar Quickselect para devolver el k-esimo elemento mas pequeno sin ordenar completamente el arreglo.

## Ejercicios resueltos

### Ejercicio resuelto 1: Busqueda binaria en arreglo descendente
Adaptar la busqueda binaria para que funcione correctamente cuando la lista esta ordenada de mayor a menor, explicando el cambio en las condiciones de comparacion.

### Ejercicio resuelto 2: Posicion de insercion con busqueda binaria
Dada una lista ordenada ascendente y un valor objetivo, devolver el indice donde debe insertarse el valor para mantener el orden. Si el valor ya existe, devolver su indice.

### Ejercicio resuelto 3: Maximo y minimo con arreglo vacio o de un elemento
Modificar el algoritmo de maximo y minimo por divide y conquista para que maneje:
- arreglo vacio (retornar `None, None`);
- arreglo con un elemento (retornar ese valor como maximo y minimo).

### Ejercicio resuelto 4: Merge Sort en lista enlazada simple
Implementar merge sort para ordenar una lista enlazada simple, definiendo la estructura de nodo y las funciones necesarias para dividir, ordenar y fusionar.

### Ejercicio resuelto 5: Quicksort con particion tipo Hoare
Implementar quicksort usando particion de Hoare (dos indices moviendose desde extremos) y comentar sus diferencias generales frente al esquema de Lomuto.
