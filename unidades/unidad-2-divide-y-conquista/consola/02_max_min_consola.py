"""
Objetivo del modulo:
Encontrar maximo y minimo simultaneamente con Divide y Conquista.

Enunciado:
Dado un arreglo no ordenado, encontrar maximo y minimo en una sola
estrategia de Divide y Conquista.

Explicacion breve:
Se divide la lista en mitades, se resuelve cada mitad recursivamente y
luego se combinan resultados parciales.

Desarrollo de la solucion propuesta:
- Caso base de 1 elemento: ese valor es maximo y minimo.
- Caso base de 2 elementos: comparar directamente.
- Caso general: dividir, conquistar y combinar.
"""

# Se importa random para poder generar listas aleatorias como opcion didactica.
import random


# Esta funcion parsea texto "1,2,3" a lista de enteros.
def parsear_lista(texto: str) -> list[int]:
    # Se separa por comas.
    partes = texto.split(",")
    # Se crea contenedor vacio.
    numeros: list[int] = []
    # Se recorre cada parte.
    for parte in partes:
        # Se limpia espacio.
        token = parte.strip()
        # Se valida no vacio.
        if token == "":
            # Se reporta error de formato.
            raise ValueError("Formato invalido: hay elementos vacios.")
        # Se agrega entero convertido.
        numeros.append(int(token))
    # Se valida lista no vacia.
    if len(numeros) == 0:
        # Se evita trabajar con entrada vacia.
        raise ValueError("La lista no puede estar vacia.")
    # Se retorna lista lista para proceso.
    return numeros


# Algoritmo Divide y Conquista para max/min.
def max_min_divide_conquista(arr: list[int], inicio: int, fin: int, pasos: list[str]) -> tuple[int, int]:
    # Big O temporal: O(n), pero usa cerca de 3n/2 - 2 comparaciones.
    # Caso base 1: solo un elemento.
    if inicio == fin:
        # Se registra paso base.
        pasos.append(f"Caso base 1 elemento en indice {inicio}: max=min={arr[inicio]}.")
        # Ese unico valor es maximo y minimo.
        return arr[inicio], arr[inicio]
    # Caso base 2: dos elementos.
    if fin == inicio + 1:
        # Se compara directamente para reducir comparaciones.
        if arr[inicio] > arr[fin]:
            # Se registra resultado de comparacion.
            pasos.append(f"Caso base 2 elementos [{arr[inicio]}, {arr[fin]}]: max={arr[inicio]}, min={arr[fin]}.")
            # Se retorna max y min.
            return arr[inicio], arr[fin]
        # Si no, el segundo es mayor o igual.
        pasos.append(f"Caso base 2 elementos [{arr[inicio]}, {arr[fin]}]: max={arr[fin]}, min={arr[inicio]}.")
        # Se retorna en orden max, min.
        return arr[fin], arr[inicio]
    # Paso divide: calcular punto medio.
    medio = (inicio + fin) // 2
    # Se registra como se divide el problema.
    pasos.append(f"Dividir rango [{inicio}, {fin}] en [{inicio}, {medio}] y [{medio+1}, {fin}].")
    # Conquistar izquierda recursivamente.
    max_izq, min_izq = max_min_divide_conquista(arr, inicio, medio, pasos)
    # Conquistar derecha recursivamente.
    max_der, min_der = max_min_divide_conquista(arr, medio + 1, fin, pasos)
    # Combinar maximos parciales.
    max_global = max(max_izq, max_der)
    # Combinar minimos parciales.
    min_global = min(min_izq, min_der)
    # Se registra combinacion final de este nivel.
    pasos.append(f"Combinar: max({max_izq},{max_der})={max_global}, min({min_izq},{min_der})={min_global}.")
    # Se retorna resultado del subproblema actual.
    return max_global, min_global


# Funcion principal de consola.
def main() -> None:
    # Titulo de la practica.
    print("=== Ejercicio 2.1 - Maximo/Minimo con Divide y Conquista ===")
    print("Enunciado: calcular maximo y minimo de una lista usando Divide y Conquista.")
    print("Explicacion breve: el algoritmo divide la lista y combina maximos/minimos parciales.")
    # Menu para elegir origen de datos.
    print("1) Ingresar lista manual")
    print("2) Generar lista aleatoria")
    # Captura opcion del usuario.
    opcion = input("Selecciona opcion: ").strip()
    try:
        # Si opcion manual.
        if opcion == "1":
            # Se pide lista de enteros separados por coma.
            arr = parsear_lista(input("Ingresa numeros separados por coma: "))
        elif opcion == "2":
            # Se pide cantidad para generar.
            cantidad = int(input("Cantidad de elementos (>0): ").strip())
            # Se valida cantidad positiva.
            if cantidad <= 0:
                # Se lanza error si no cumple.
                raise ValueError("La cantidad debe ser mayor que cero.")
            # Se genera lista aleatoria en rango didactico.
            arr = [random.randint(-99, 99) for _ in range(cantidad)]
        else:
            # Se corta por opcion invalida.
            print("Opcion invalida.")
            return
    except ValueError as error:
        # Se imprime mensaje amigable de error.
        print(f"Entrada invalida: {error}")
        return
    # Se muestra lista a procesar.
    print(f"Lista usada: {arr}")
    # Se crea acumulador de pasos.
    pasos: list[str] = []
    # Se ejecuta algoritmo recursivo sobre todo el rango.
    maximo, minimo = max_min_divide_conquista(arr, 0, len(arr) - 1, pasos)
    # Se imprime detalle de pasos.
    print("\n--- Pasos ---")
    for paso in pasos:
        print(f"- {paso}")
    # Se imprimen resultados finales.
    print(f"\nResultado final -> maximo: {maximo}, minimo: {minimo}")


# Bloque de ejecucion directa del archivo.
if __name__ == "__main__":
    # Llamada al flujo principal.
    main()
