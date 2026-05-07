"""
Objetivo del modulo:
Interfaz Tkinter para Quicksort con Lomuto y mediana de tres opcional.

Enunciado:
Ingresar una lista y ordenarla con Quicksort, pudiendo elegir mediana
de tres para seleccionar mejor pivote.

Explicacion breve:
La interfaz permite observar las particiones y comparar cantidad de
comparaciones realizadas durante el ordenamiento.

Desarrollo de la solucion propuesta:
- Capturar lista desde Entry.
- Ejecutar Quicksort con o sin mediana de tres.
- Mostrar pasos de particion y resultado final.
"""

import tkinter as tk
from tkinter import scrolledtext


def parsear_lista(texto: str) -> list[int]:
    partes = texto.split(",")
    numeros: list[int] = []
    for parte in partes:
        token = parte.strip()
        if token == "":
            raise ValueError("Hay elementos vacios.")
        numeros.append(int(token))
    if len(numeros) == 0:
        raise ValueError("La lista no puede estar vacia.")
    return numeros


def elegir_pivote_mediana_tres(arr: list[int], bajo: int, alto: int) -> int:
    medio = (bajo + alto) // 2
    candidatos = [(arr[bajo], bajo), (arr[medio], medio), (arr[alto], alto)]
    candidatos.sort(key=lambda x: x[0])
    return candidatos[1][1]


def particion_lomuto(arr: list[int], bajo: int, alto: int, pasos: list[str], comparaciones: list[int]) -> int:
    pivote = arr[alto]
    i = bajo - 1
    pasos.append(f"Particion [{bajo},{alto}] con pivote={pivote}.")
    for j in range(bajo, alto):
        comparaciones[0] += 1
        if arr[j] <= pivote:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            pasos.append(f"Swap interno: {arr}")
    arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
    pasos.append(f"Pivote fijado: {arr}")
    return i + 1


def quicksort(arr: list[int], bajo: int, alto: int, pasos: list[str], comparaciones: list[int], mediana: bool) -> None:
    # Big O: promedio O(n log n), peor O(n^2) si pivote divide mal.
    if bajo < alto:
        if mediana:
            idx = elegir_pivote_mediana_tres(arr, bajo, alto)
            arr[idx], arr[alto] = arr[alto], arr[idx]
            pasos.append(f"Mediana de tres elegida; pivote actual={arr[alto]}.")
        p = particion_lomuto(arr, bajo, alto, pasos, comparaciones)
        quicksort(arr, bajo, p - 1, pasos, comparaciones, mediana)
        quicksort(arr, p + 1, alto, pasos, comparaciones, mediana)


class AppQuick:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Ejercicio 5.2 - Quicksort (Tkinter)")
        self.root.geometry("780x560")
        tk.Label(
            root,
            text="Enunciado: ordenar la lista con Quicksort (Lomuto) y opcion de mediana de tres.",
        ).pack(anchor="w", padx=10, pady=(10, 0))
        tk.Label(root, text="Lista (ej: 9,4,6,2,8,1):").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry = tk.Entry(root, width=90)
        self.entry.pack(padx=10, pady=4)
        self.usar_mediana = tk.BooleanVar(value=False)
        tk.Checkbutton(root, text="Usar mediana de tres", variable=self.usar_mediana).pack(anchor="w", padx=10, pady=4)
        tk.Button(root, text="Ordenar", command=self.ordenar).pack(anchor="w", padx=10, pady=6)
        self.label = tk.Label(root, text="Resultado: pendiente", fg="blue")
        self.label.pack(anchor="w", padx=10)
        self.salida = scrolledtext.ScrolledText(root, width=90, height=23)
        self.salida.pack(padx=10, pady=8, fill="both", expand=True)

    def ordenar(self) -> None:
        self.salida.delete("1.0", tk.END)
        try:
            arr = parsear_lista(self.entry.get())
        except ValueError as error:
            self.label.config(text=f"Error: {error}", fg="red")
            return
        pasos: list[str] = []
        comparaciones = [0]
        quicksort(arr, 0, len(arr) - 1, pasos, comparaciones, self.usar_mediana.get())
        for paso in pasos:
            self.salida.insert(tk.END, f"- {paso}\n")
        self.label.config(text=f"Resultado: {arr} | Comparaciones: {comparaciones[0]}", fg="green")


if __name__ == "__main__":
    raiz = tk.Tk()
    AppQuick(raiz)
    raiz.mainloop()
