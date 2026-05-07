"""
Objetivo del modulo:
Crear una interfaz grafica con Tkinter para practicar busqueda binaria
en una lista ordenada, mostrando pasos del algoritmo y resultado.

Enunciado:
Ingresar una lista ordenada y un valor objetivo para aplicar busqueda
binaria y determinar si el valor aparece dentro de la lista.

Explicacion breve:
El algoritmo compara contra el elemento central y descarta media lista
en cada iteracion, por eso su complejidad es O(log n).

Desarrollo de la solucion propuesta:
- Validar precondicion de lista ordenada.
- Ejecutar busqueda binaria iterativa.
- Mostrar trazas y resultado en la ventana.
"""

# Se importa tkinter para construir la ventana y controles.
import tkinter as tk
# Se importa scrolledtext para mostrar pasos largos con barra de desplazamiento.
from tkinter import scrolledtext


# Esta funcion convierte texto en lista de enteros y valida que este ordenada.
def parsear_lista_ordenada(texto: str) -> list[int]:
    # Se divide el texto por comas para separar cada posible numero.
    partes = texto.split(",")
    # Se define lista vacia para guardar enteros.
    numeros: list[int] = []
    # Se recorre cada parte para limpiarla y convertirla.
    for parte in partes:
        # Se quitan espacios extras.
        token = parte.strip()
        # Se valida que no quede vacio.
        if token == "":
            # Se corta con error si hay formato incorrecto.
            raise ValueError("Hay elementos vacios en la lista.")
        # Se convierte a entero.
        numeros.append(int(token))
    # Se valida que la lista no quede vacia.
    if len(numeros) == 0:
        # Se informa error didactico.
        raise ValueError("La lista no puede estar vacia.")
    # Se valida precondicion de busqueda binaria.
    if numeros != sorted(numeros):
        # Se informa que el arreglo debe estar ordenado.
        raise ValueError("La lista debe estar ordenada ascendentemente.")
    # Se retorna la lista lista para buscar.
    return numeros


# Version iterativa para usar en la interfaz.
def busqueda_binaria_iterativa(arr: list[int], objetivo: int, pasos: list[str]) -> int:
    # Big O: O(log n) porque se reduce el rango aproximadamente a la mitad en cada iteracion.
    # Se define el inicio del rango.
    inicio = 0
    # Se define el final del rango.
    fin = len(arr) - 1
    # Se itera mientras el rango sea valido.
    while inicio <= fin:
        # Se calcula posicion central con division entera.
        medio = (inicio + fin) // 2
        # Se guarda traza explicativa.
        pasos.append(f"Comparo objetivo={objetivo} con arr[{medio}]={arr[medio]}.")
        # Si coincide, se encontro y termina.
        if arr[medio] == objetivo:
            # Se deja constancia del hallazgo.
            pasos.append("Coincidencia: encontrado.")
            # Se retorna indice encontrado.
            return medio
        # Si el objetivo es menor, se descarta derecha.
        if objetivo < arr[medio]:
            # Se mueve fin a la izquierda del medio.
            fin = medio - 1
            # Se registra movimiento de limites.
            pasos.append("Objetivo menor: actualizar fin = medio - 1.")
        else:
            # Si es mayor, se descarta izquierda.
            inicio = medio + 1
            # Se registra movimiento de limites.
            pasos.append("Objetivo mayor: actualizar inicio = medio + 1.")
    # Si se sale del while, no se encontro.
    pasos.append("No se encontro el objetivo en la lista.")
    # Se retorna -1 para indicar ausencia.
    return -1


# Clase principal de la interfaz para organizar widgets y logica.
class AppBusquedaBinaria:
    # Constructor que recibe la ventana raiz.
    def __init__(self, root: tk.Tk) -> None:
        # Se guarda referencia a la ventana.
        self.root = root
        # Se define titulo de la aplicacion.
        self.root.title("Ejercicio 1.2 - Busqueda Binaria (Tkinter)")
        # Se fija tamano inicial de ventana.
        self.root.geometry("760x540")
        # Etiqueta de instruccion para lista.
        tk.Label(
            root,
            text="Enunciado: dado un arreglo ordenado y un objetivo, encontrar su posicion con busqueda binaria.",
        ).pack(anchor="w", padx=10, pady=(10, 0))
        # Etiqueta de instruccion para lista.
        tk.Label(root, text="Lista ordenada (ej: 2,5,9,12):").pack(anchor="w", padx=10, pady=(10, 0))
        # Entrada de texto para lista.
        self.entrada_lista = tk.Entry(root, width=80)
        # Se muestra el campo de lista.
        self.entrada_lista.pack(padx=10, pady=4)
        # Etiqueta de instruccion para objetivo.
        tk.Label(root, text="Valor objetivo:").pack(anchor="w", padx=10, pady=(8, 0))
        # Entrada de texto para objetivo.
        self.entrada_objetivo = tk.Entry(root, width=20)
        # Se muestra campo objetivo.
        self.entrada_objetivo.pack(padx=10, pady=4, anchor="w")
        # Boton para ejecutar busqueda.
        tk.Button(root, text="Buscar", command=self.ejecutar_busqueda).pack(padx=10, pady=8, anchor="w")
        # Etiqueta para resultado corto.
        self.label_resultado = tk.Label(root, text="Resultado: pendiente", fg="blue")
        # Se muestra etiqueta de resultado.
        self.label_resultado.pack(anchor="w", padx=10, pady=(0, 8))
        # Area de texto con scroll para pasos detallados.
        self.salida_pasos = scrolledtext.ScrolledText(root, width=90, height=20)
        # Se muestra area de salida.
        self.salida_pasos.pack(padx=10, pady=6, fill="both", expand=True)

    # Metodo que toma datos de la UI y ejecuta el algoritmo.
    def ejecutar_busqueda(self) -> None:
        # Se limpia texto previo en la salida.
        self.salida_pasos.delete("1.0", tk.END)
        try:
            # Se parsea lista con validaciones.
            arr = parsear_lista_ordenada(self.entrada_lista.get())
            # Se parsea objetivo a entero.
            objetivo = int(self.entrada_objetivo.get().strip())
        except ValueError as error:
            # Se informa error de entrada en etiqueta.
            self.label_resultado.config(text=f"Error: {error}", fg="red")
            # Se termina para evitar continuar con datos invalidos.
            return
        # Se crea lista para guardar pasos didacticos.
        pasos: list[str] = []
        # Se ejecuta algoritmo iterativo.
        indice = busqueda_binaria_iterativa(arr, objetivo, pasos)
        # Se imprime todos los pasos en el cuadro de texto.
        for paso in pasos:
            # Se inserta cada linea con guion.
            self.salida_pasos.insert(tk.END, f"- {paso}\n")
        # Si se encontro posicion valida.
        if indice != -1:
            # Se actualiza etiqueta con exito.
            self.label_resultado.config(text=f"Resultado: encontrado en indice {indice}.", fg="green")
        else:
            # Se actualiza etiqueta con no encontrado.
            self.label_resultado.config(text="Resultado: no encontrado.", fg="orange")


# Punto de entrada del script para abrir la ventana.
if __name__ == "__main__":
    # Se crea ventana principal de Tkinter.
    raiz = tk.Tk()
    # Se crea instancia de la app con esa ventana.
    AppBusquedaBinaria(raiz)
    # Se inicia bucle de eventos de la interfaz.
    raiz.mainloop()
