"""
Objetivo del modulo:
Visualizar fusiones de Merge Sort iterativo en una interfaz Tkinter.

Enunciado:
Ingresar una lista y ordenarla con Merge Sort iterativo, observando
las fusiones por tamanos de subarreglo.

Explicacion breve:
La aplicacion muestra el crecimiento de bloques (1, 2, 4, ...) y
como cada pasada acerca la lista al orden final.

Desarrollo de la solucion propuesta:
- Leer lista desde Entry.
- Aplicar merge sort bottom-up.
- Mostrar trazas de cada fusion en el cuadro de salida.
"""

import tkinter as tk
from tkinter import scrolledtext


def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay valores vacios.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


def merge(arr: list[int], inicio: int, medio: int, fin: int) -> None:
    izquierda = arr[inicio:medio + 1]
    derecha = arr[medio + 1:fin + 1]
    i = 0
    j = 0
    k = inicio
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            arr[k] = izquierda[i]
            i += 1
        else:
            arr[k] = derecha[j]
            j += 1
        k += 1
    while i < len(izquierda):
        arr[k] = izquierda[i]
        i += 1
        k += 1
    while j < len(derecha):
        arr[k] = derecha[j]
        j += 1
        k += 1


def merge_sort_bottom_up(arr: list[int], pasos: list[str]) -> None:
    # Big O: O(n log n), memoria O(n), sin recursion.
    n = len(arr)
    size = 1
    while size < n:
        pasos.append(f"== size={size} ==")
        inicio = 0
        while inicio < n - 1:
            medio = min(inicio + size - 1, n - 1)
            fin = min(inicio + 2 * size - 1, n - 1)
            if medio < fin:
                pasos.append(f"Merge [{inicio},{medio}] + [{medio+1},{fin}]")
                merge(arr, inicio, medio, fin)
                pasos.append(f"Lista parcial: {arr}")
            inicio += 2 * size
        size *= 2


class AppMergeIter:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ejercicio 4.2 - Merge Sort Iterativo (Tkinter)")
        self.root.geometry("780x540")
        tk.Label(
            root,
            text="Enunciado: ordenar la lista con Merge Sort iterativo (bottom-up).",
        ).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(root, text="Lista (ej: 7,4,9,1,5):").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry = tk.Entry(root, width=90)
        self.entry.pack(padx=10, pady=4)
        tk.Button(root, text="Ordenar (Bottom-up)", command=self.ordenar).pack(anchor="w", padx=10, pady=6)
        self.label_resultado = tk.Label(root, text="Resultado: pendiente", fg="blue")
        self.label_resultado.pack(anchor="w", padx=10)
        self.salida = scrolledtext.ScrolledText(root, width=90, height=22)
        self.salida.pack(padx=10, pady=8, fill="both", expand=True)

    def ordenar(self) -> None:
        self.salida.delete("1.0", tk.END)
        try:
            arr = parsear_lista(self.entry.get())
        except ValueError as error:
            self.label_resultado.config(text=f"Error: {error}", fg="red")
            return
        pasos: list[str] = []
        merge_sort_bottom_up(arr, pasos)
        for paso in pasos:
            self.salida.insert(tk.END, f"{paso}\n")
        self.label_resultado.config(text=f"Resultado: {arr}", fg="green")


if __name__ == "__main__":
    raiz = tk.Tk()
    AppMergeIter(raiz)
    raiz.mainloop()
