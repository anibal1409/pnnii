"""
Objetivo del modulo:
Practicar busqueda binaria recursiva e iterativa sobre una lista ordenada.

Enunciado:
Dada una lista ORDENADA y un valor objetivo, aplicar busqueda binaria
con dos enfoques (recursivo e iterativo) para indicar si el valor existe
y en que indice se encuentra.

Explicacion breve:
Este ejercicio entrena como reducir el problema a la mitad en cada paso.
Si el objetivo es menor que el centro, se revisa la izquierda; si es mayor,
se revisa la derecha.

Desarrollo de la solucion propuesta:
- Validar que la lista este ordenada (precondicion).
- Ejecutar version recursiva o iterativa segun menu.
- Mostrar pasos de comparacion y resultado final.
"""

# Esta funcion transforma un texto tipo "1,2,3" en una lista de enteros.
def parsear_lista_ordenada(texto: str) -> list[int]:
    # Se separa por comas para tomar cada numero por separado.
    partes = texto.split(",")
    # Se prepara una lista vacia para almacenar los enteros convertidos.
    numeros: list[int] = []
    # Se recorre cada parte para limpiarla y validarla.
    for parte in partes:
        # Se elimina espacio en blanco alrededor de cada valor.
        token = parte.strip()
        # Se valida que no exista un fragmento vacio.
        if token == "":
            # Se lanza error amigable si hay valores faltantes.
            raise ValueError("Hay elementos vacios en la lista.")
        # Se convierte el texto a entero y se agrega a la lista.
        numeros.append(int(token))
    # Se valida que haya al menos un numero.
    if len(numeros) == 0:
        # Se lanza error porque no se puede buscar en lista vacia.
        raise ValueError("La lista no puede estar vacia.")
    # Se valida precondicion: lista ordenada ascendente.
    if numeros != sorted(numeros):
        # Se informa al usuario que debe ordenar primero.
        raise ValueError("La busqueda binaria requiere lista ordenada.")
    # Se retorna lista valida para ejecutar el algoritmo.
    return numeros


# Version recursiva de busqueda binaria.
def busqueda_binaria_recursiva(arr: list[int], objetivo: int, inicio: int, fin: int, pasos: list[str]) -> int:
    # Big O: O(log n) en promedio/peor; mejor caso O(1) si el centro coincide.
    # Caso base: rango invalido significa que no se encontro el objetivo.
    if inicio > fin:
        # Se guarda explicacion para la salida didactica.
        pasos.append("Caso base: inicio > fin, objetivo no encontrado.")
        # Se retorna -1 como codigo de "no encontrado".
        return -1
    # Se calcula indice central con division entera.
    medio = (inicio + fin) // 2
    # Se registra el estado actual de comparacion.
    pasos.append(f"Comparo objetivo={objetivo} con arr[{medio}]={arr[medio]}.")
    # Caso base de exito: el elemento central es el objetivo.
    if arr[medio] == objetivo:
        # Se registra traza de exito.
        pasos.append("Caso base: arr[medio] == objetivo.")
        # Se retorna indice encontrado.
        return medio
    # Si el objetivo es menor que el centro, se busca a la izquierda.
    if objetivo < arr[medio]:
        # Se registra por que se toma la mitad izquierda.
        pasos.append("Objetivo menor al centro, ir a mitad izquierda.")
        # Llamada recursiva reduciendo fin.
        return busqueda_binaria_recursiva(arr, objetivo, inicio, medio - 1, pasos)
    # Si no fue menor ni igual, entonces es mayor y se va a la derecha.
    pasos.append("Objetivo mayor al centro, ir a mitad derecha.")
    # Llamada recursiva reduciendo inicio.
    return busqueda_binaria_recursiva(arr, objetivo, medio + 1, fin, pasos)


# Version iterativa de busqueda binaria.
def busqueda_binaria_iterativa(arr: list[int], objetivo: int, pasos: list[str]) -> int:
    # Big O: O(log n) en promedio/peor; O(1) en mejor caso.
    # Se define limite izquierdo inicial.
    inicio = 0
    # Se define limite derecho inicial.
    fin = len(arr) - 1
    # El ciclo se mantiene mientras exista un rango valido.
    while inicio <= fin:
        # Se calcula indice central del rango actual.
        medio = (inicio + fin) // 2
        # Se registra paso de comparacion.
        pasos.append(f"Comparo objetivo={objetivo} con arr[{medio}]={arr[medio]}.")
        # Si coincide, se encontro y se retorna indice.
        if arr[medio] == objetivo:
            # Se registra exito.
            pasos.append("Coincidencia exacta encontrada.")
            # Se retorna posicion.
            return medio
        # Si el objetivo es menor, se descarta mitad derecha.
        if objetivo < arr[medio]:
            # Se actualiza fin para quedar solo con izquierda.
            fin = medio - 1
            # Se registra decision.
            pasos.append("Objetivo menor, nuevo fin = medio - 1.")
        else:
            # Si es mayor, se descarta mitad izquierda.
            inicio = medio + 1
            # Se registra decision.
            pasos.append("Objetivo mayor, nuevo inicio = medio + 1.")
    # Si termina el ciclo, no se encontro el objetivo.
    pasos.append("Fin del while: no encontrado.")
    # Se retorna -1 para indicar ausencia.
    return -1


# Funcion principal con menu para practicar ambas versiones.
def main() -> None:
    # Se imprime introduccion para orientar al estudiante.
    print("=== Ejercicio 1.1 - Busqueda Binaria (Consola) ===")
    print("Enunciado: buscar un valor objetivo en una lista ordenada con busqueda binaria.")
    print("Explicacion breve: en cada paso se elimina la mitad del rango de busqueda.")
    # Se explica brevemente la precondicion principal.
    print("Recuerda: debes ingresar una lista ORDENADA de enteros.")
    # Se solicita lista al usuario.
    entrada_lista = input("Ingresa numeros separados por coma (ejemplo 1,3,5,7): ")
    # Se solicita objetivo a buscar.
    entrada_objetivo = input("Ingresa el valor objetivo: ")
    try:
        # Se parsea y valida la lista.
        arr = parsear_lista_ordenada(entrada_lista)
        # Se convierte objetivo a entero.
        objetivo = int(entrada_objetivo.strip())
    except ValueError as error:
        # Se muestra error amigable en caso de entrada invalida.
        print(f"Entrada invalida: {error}")
        # Se sale de la funcion para evitar continuar con datos rotos.
        return
    # Se pide elegir algoritmo para comparar enfoques.
    print("Elige metodo: 1) Recursivo  2) Iterativo")
    # Se captura seleccion como texto.
    opcion = input("Opcion: ").strip()
    # Se crea lista de pasos para mostrar trazas del proceso.
    pasos: list[str] = []
    # Si el usuario eligio opcion recursiva.
    if opcion == "1":
        # Se ejecuta busqueda recursiva con extremos iniciales.
        indice = busqueda_binaria_recursiva(arr, objetivo, 0, len(arr) - 1, pasos)
    elif opcion == "2":
        # Se ejecuta busqueda iterativa.
        indice = busqueda_binaria_iterativa(arr, objetivo, pasos)
    else:
        # Se avisa opcion invalida.
        print("Opcion no valida.")
        # Se termina ejecucion.
        return
    # Se imprime separador visual.
    print("\n--- Pasos del algoritmo ---")
    # Se recorre cada paso para visualizar el proceso.
    for paso in pasos:
        # Se imprime paso individual.
        print(f"- {paso}")
    # Si el indice es distinto de -1, se encontro el elemento.
    if indice != -1:
        # Se informa posicion encontrada.
        print(f"Resultado: encontrado en indice {indice}.")
    else:
        # Se informa que no existe en la lista.
        print("Resultado: no encontrado.")


# Este bloque permite ejecutar ejemplos solo cuando el archivo se corre directamente.
if __name__ == "__main__":
    # Se llama a la funcion principal para iniciar la practica.
    main()
