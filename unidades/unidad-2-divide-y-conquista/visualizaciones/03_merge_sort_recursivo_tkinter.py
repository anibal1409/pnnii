"""
Objetivo del modulo:
Interfaz Tkinter para ordenar listas con Merge Sort recursivo.

Enunciado:
Ingresar una lista y ordenarla con Merge Sort recursivo, visualizando
los pasos de division y fusion.

Explicacion breve:
El algoritmo separa el problema en sublistas mas pequenas y despues
las fusiona conservando orden ascendente.

Desarrollo de la solucion propuesta:
- Leer lista desde Entry.
- Ejecutar merge sort top-down.
- Mostrar pasos intermedios y salida ordenada.
"""

import tkinter as tk
from tkinter import scrolledtext


def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay elementos vacios en la lista.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


def merge(arr: list[int], inicio: int, medio: int, fin: int, pasos: list[str]) -> None:
    izquierda = arr[inicio:medio + 1]
    derecha = arr[medio + 1:fin + 1]
    pasos.append(f"Fusiono {izquierda} con {derecha}.")
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
    pasos.append(f"Subarreglo ordenado: {arr[inicio:fin+1]}")


def merge_sort(arr: list[int], inicio: int, fin: int, pasos: list[str]) -> None:
    # Big O: O(n log n) y uso de memoria extra O(n).
    if inicio >= fin:
        return
    medio = (inicio + fin) // 2
    pasos.append(f"Dividir [{inicio},{fin}] en [{inicio},{medio}] y [{medio+1},{fin}].")
    merge_sort(arr, inicio, medio, pasos)
    merge_sort(arr, medio + 1, fin, pasos)
    merge(arr, inicio, medio, fin, pasos)


class AppMergeRec:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ejercicio 3.2 - Merge Sort Recursivo (Tkinter)")
        self.root.geometry("780x540")
        tk.Label(
            root,
            text="Enunciado: ordenar la lista ingresada con Merge Sort recursivo (top-down).",
        ).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(root, text="Lista (ej: 9,1,8,3,2):").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry = tk.Entry(root, width=90)
        self.entry.pack(padx=10, pady=4)
        tk.Button(root, text="Ordenar", command=self.ordenar).pack(anchor="w", padx=10, pady=6)
        self.resultado = tk.Label(root, text="Resultado: pendiente", fg="blue")
        self.resultado.pack(anchor="w", padx=10)
        self.texto = scrolledtext.ScrolledText(root, width=90, height=22)
        self.texto.pack(padx=10, pady=8, fill="both", expand=True)

    def ordenar(self) -> None:
        self.texto.delete("1.0", tk.END)
        try:
            arr = parsear_lista(self.entry.get())
        except ValueError as error:
            self.resultado.config(text=f"Error: {error}", fg="red")
            return
        pasos: list[str] = []
        merge_sort(arr, 0, len(arr) - 1, pasos)
        for paso in pasos:
            self.texto.insert(tk.END, f"- {paso}\n")
        self.resultado.config(text=f"Resultado: {arr}", fg="green")


if __name__ == "__main__":
    raiz = tk.Tk()
    AppMergeRec(raiz)
    raiz.mainloop()
