"""
Objetivo del modulo:
Interfaz Tkinter para calcular maximo y minimo por Divide y Conquista.

Enunciado:
Ingresar o generar una lista para encontrar su maximo y minimo usando
la estrategia Divide y Conquista.

Explicacion breve:
La interfaz permite observar como el algoritmo divide en subproblemas
y luego combina resultados en cada retorno recursivo.

Desarrollo de la solucion propuesta:
- Capturar lista manual o aleatoria.
- Aplicar casos base y recursion por mitades.
- Mostrar pasos y resultado final en la ventana.
"""

# Se importa tkinter para interfaz grafica.
import tkinter as tk
# Se importa random para generar ejemplos aleatorios.
import random


# Parsea entrada de lista de texto a enteros.
def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay valores vacios en la lista.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


# Divide y Conquista para max/min.
def max_min_dc(arr: list[int], inicio: int, fin: int, pasos: list[str]) -> tuple[int, int]:
    # Big O: O(n), con menos comparaciones que el enfoque ingenuo.
    if inicio == fin:
        pasos.append(f"Caso base 1 elemento: {arr[inicio]}.")
        return arr[inicio], arr[inicio]
    if fin == inicio + 1:
        if arr[inicio] > arr[fin]:
            pasos.append(f"Caso base 2 elementos -> max={arr[inicio]}, min={arr[fin]}.")
            return arr[inicio], arr[fin]
        pasos.append(f"Caso base 2 elementos -> max={arr[fin]}, min={arr[inicio]}.")
        return arr[fin], arr[inicio]
    medio = (inicio + fin) // 2
    pasos.append(f"Dividir [{inicio},{fin}] en [{inicio},{medio}] y [{medio+1},{fin}].")
    max_i, min_i = max_min_dc(arr, inicio, medio, pasos)
    max_d, min_d = max_min_dc(arr, medio + 1, fin, pasos)
    max_g = max(max_i, max_d)
    min_g = min(min_i, min_d)
    pasos.append(f"Combinar -> max={max_g}, min={min_g}.")
    return max_g, min_g


# Clase de interfaz.
class AppMaxMin:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ejercicio 2.2 - Maximo y Minimo (Tkinter)")
        self.root.geometry("760x520")
        tk.Label(
            root,
            text="Enunciado: encontrar maximo y minimo de una lista no ordenada con Divide y Conquista.",
        ).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(root, text="Lista (ej: 8,2,14,-1,7):").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_lista = tk.Entry(root, width=80)
        self.entry_lista.pack(padx=10, pady=4)
        tk.Button(root, text="Generar lista aleatoria", command=self.generar_lista).pack(anchor="w", padx=10, pady=4)
        tk.Button(root, text="Calcular max/min", command=self.calcular).pack(anchor="w", padx=10, pady=4)
        self.label_resultado = tk.Label(root, text="Resultado: pendiente", fg="blue")
        self.label_resultado.pack(anchor="w", padx=10, pady=6)
        self.texto = tk.Text(root, width=90, height=20)
        self.texto.pack(padx=10, pady=8, fill="both", expand=True)

    def generar_lista(self) -> None:
        datos = [random.randint(-50, 50) for _ in range(10)]
        self.entry_lista.delete(0, tk.END)
        self.entry_lista.insert(0, ",".join(str(x) for x in datos))

    def calcular(self) -> None:
        self.texto.delete("1.0", tk.END)
        try:
            arr = parsear_lista(self.entry_lista.get())
        except ValueError as error:
            self.label_resultado.config(text=f"Error: {error}", fg="red")
            return
        pasos: list[str] = []
        maximo, minimo = max_min_dc(arr, 0, len(arr) - 1, pasos)
        for paso in pasos:
            self.texto.insert(tk.END, f"- {paso}\n")
        self.label_resultado.config(text=f"Resultado: maximo={maximo}, minimo={minimo}", fg="green")


if __name__ == "__main__":
    raiz = tk.Tk()
    AppMaxMin(raiz)
    raiz.mainloop()
