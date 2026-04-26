"""
Programa grafico principal de la Unidad I.

Explicacion general:
- Este modulo implementa una interfaz grafica completa para practicar los
  conceptos trabajados en la unidad (arboles, teoremas y heaps).
- El objetivo es que el estudiante manipule datos y observe resultados en vivo.
- Se usa Tkinter para mantener una ejecucion simple y local.
- El contexto didactico esta orientado a situaciones de vida laboral y cotidiana:
  organigrama de equipo, capacidad de estructura y prioridad de incidencias.
"""

# Importa copia profunda para reiniciar estructuras sin referencias compartidas.
from copy import deepcopy
# Importa tkinter como toolkit de interfaz.
import tkinter as tk
# Importa widgets ttk con estilo moderno.
from tkinter import ttk
# Importa caja de texto con scroll para salidas largas.
from tkinter.scrolledtext import ScrolledText

# Importa funciones reutilizables desde la interfaz base.
from interfaz_unidad_1 import (
    calcular_niveles,
    heapify_max,
    insertar_en_max_heap,
)

# Define arbol de ejemplo en contexto laboral (organigrama).
ORG_TREE = {
    "GERENCIA": ["OPERACIONES", "TECNOLOGIA"],
    "OPERACIONES": ["LOGISTICA", "ATENCION_CLIENTE"],
    "TECNOLOGIA": ["DESARROLLO"],
    "LOGISTICA": [],
    "ATENCION_CLIENTE": [],
    "DESARROLLO": [],
}
# Define raiz del organigrama.
ORG_ROOT = "GERENCIA"


class ProgramaGraficoUnidad1:
    """Interfaz grafica principal para practicar la Unidad I."""

    def __init__(self, root: tk.Tk) -> None:
        # Guarda referencia de ventana principal.
        self.root = root
        # Define titulo descriptivo de la app.
        self.root.title("Programa grafico - Unidad I")
        # Define tamano inicial.
        self.root.geometry("1180x780")
        # Define tamano minimo para mantener usabilidad.
        self.root.minsize(980, 680)
        # Configura estilos generales.
        self._configurar_estilos()
        # Inicializa estado del arbol editable en contexto laboral.
        self.tree = deepcopy(ORG_TREE)
        # Inicializa raiz del arbol.
        self.tree_root = ORG_ROOT
        # Crea notebook de modulos.
        self.tabs = ttk.Notebook(self.root)
        # Empaqueta notebook expandible.
        self.tabs.pack(fill="both", expand=True, padx=12, pady=12)
        # Crea modulo de arboles.
        self._crear_tab_arboles()
        # Crea modulo de teoremas.
        self._crear_tab_teoremas()
        # Crea modulo de heaps.
        self._crear_tab_heaps()

    def _configurar_estilos(self) -> None:
        """Configura look&feel profesional y limpio."""
        # Crea administrador de estilos.
        style = ttk.Style()
        # Selecciona tema moderno si existe.
        if "clam" in style.theme_names():
            style.theme_use("clam")
        # Configura fuente base de labels.
        style.configure("TLabel", font=("Segoe UI", 10))
        # Configura botones.
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        # Configura tabs.
        style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=(12, 8))
        # Configura secciones tipo card.
        style.configure("Card.TLabelframe", padding=12)
        # Configura titulo de cards.
        style.configure("Card.TLabelframe.Label", font=("Segoe UI", 10, "bold"))

    def _crear_tab_arboles(self) -> None:
        """Crea interfaz de practica para conceptos de arboles."""
        # Crea contenedor de la pestaña.
        frame = ttk.Frame(self.tabs, padding=16)
        # Agrega pestaña al notebook.
        self.tabs.add(frame, text="Organigrama")
        # Configura expansion en la grilla.
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(3, weight=1)
        # Muestra explicacion breve.
        ttk.Label(
            frame,
            text="Explicacion breve: simula un organigrama y observa nivel, grado y altura del equipo.",
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))
        # Crea card de controles.
        controls = ttk.LabelFrame(frame, text="Operacion sobre organigrama", style="Card.TLabelframe")
        # Posiciona card de controles.
        controls.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        # Variable del padre seleccionado.
        self.parent_var = tk.StringVar(value="GERENCIA")
        # Variable de nuevo nodo.
        self.new_node_var = tk.StringVar(value="")
        # Etiqueta de padre.
        ttk.Label(controls, text="Area padre:").grid(row=0, column=0, padx=(0, 6))
        # Combobox de padres disponibles.
        self.parent_combo = ttk.Combobox(controls, textvariable=self.parent_var, width=12, state="readonly")
        # Posiciona combo.
        self.parent_combo.grid(row=0, column=1, padx=(0, 10))
        # Etiqueta de nuevo nodo.
        ttk.Label(controls, text="Nueva area:").grid(row=0, column=2, padx=(0, 6))
        # Entrada de nombre del nodo.
        ttk.Entry(controls, textvariable=self.new_node_var, width=12).grid(row=0, column=3, padx=(0, 10))
        # Boton de agregar.
        self.add_btn = ttk.Button(controls, text="Agregar area", command=self._agregar_nodo)
        # Posiciona boton.
        self.add_btn.grid(row=0, column=4, padx=4)
        # Boton de limpiar.
        ttk.Button(controls, text="Limpiar organigrama", command=self._limpiar_arbol).grid(row=0, column=5, padx=4)
        # Boton de restaurar.
        ttk.Button(controls, text="Restaurar organigrama", command=self._restaurar_arbol).grid(row=0, column=6, padx=4)
        # Variable de estado de arbol.
        self.tree_status = tk.StringVar(value="Estado: organigrama inicial cargado.")
        # Muestra estado.
        ttk.Label(frame, textvariable=self.tree_status).grid(row=2, column=0, sticky="w", pady=(0, 8))
        # Crea card de visualizacion.
        visual_card = ttk.LabelFrame(frame, text="Visualizacion del organigrama", style="Card.TLabelframe")
        # Posiciona card.
        visual_card.grid(row=3, column=0, sticky="nsew")
        # Configura expansion interna.
        visual_card.columnconfigure(0, weight=1)
        visual_card.rowconfigure(0, weight=1)
        # Crea canvas de dibujo.
        self.tree_canvas = tk.Canvas(visual_card, bg="white", highlightthickness=0)
        # Posiciona canvas.
        self.tree_canvas.grid(row=0, column=0, sticky="nsew")
        # Redibuja al redimensionar.
        self.tree_canvas.bind("<Configure>", self._redibujar_arbol)
        # Etiqueta de altura.
        self.height_label = ttk.Label(frame, text="Altura jerarquica total: 0")
        # Posiciona altura.
        self.height_label.grid(row=4, column=0, sticky="w", pady=(8, 0))
        # Inicializa combobox y dibujo.
        self._actualizar_padres_disponibles()
        self._redibujar_arbol()

    def _actualizar_padres_disponibles(self) -> None:
        """Actualiza select de nodos padres permitidos."""
        # Filtra nodos con menos de 2 hijos.
        disponibles = sorted([n for n, hijos in self.tree.items() if len(hijos) < 2])
        # Asigna lista al combo.
        self.parent_combo["values"] = disponibles
        # Maneja caso sin opciones.
        if not disponibles:
            self.parent_var.set("")
            self.parent_combo.configure(state="disabled")
            self.add_btn.configure(state="disabled")
            return
        # Habilita controles.
        self.parent_combo.configure(state="readonly")
        self.add_btn.configure(state="normal")
        # Asegura valor valido en combo.
        if self.parent_var.get() not in disponibles:
            self.parent_var.set(disponibles[0])

    def _redibujar_arbol(self, _event: tk.Event | None = None) -> None:
        """Redibuja arbol en canvas con posiciones por nivel."""
        # Limpia dibujo anterior.
        self.tree_canvas.delete("all")
        # Obtiene dimensiones actuales.
        width = max(560, self.tree_canvas.winfo_width())
        height = max(300, self.tree_canvas.winfo_height())
        # Calcula niveles del arbol.
        niveles = calcular_niveles(self.tree_root, self.tree)
        # Agrupa nodos por nivel.
        por_nivel: dict[int, list[str]] = {}
        for nodo, nivel in niveles.items():
            por_nivel.setdefault(nivel, []).append(nodo)
        # Calcula coordenadas por nodo.
        pos: dict[str, tuple[float, float]] = {}
        nivel_max = max(por_nivel) if por_nivel else 0
        for nivel, nodos in por_nivel.items():
            nodos = sorted(nodos)
            step_x = width / (len(nodos) + 1)
            y = 40 + (nivel * (height - 80) / max(1, nivel_max))
            for i, nodo in enumerate(nodos, start=1):
                pos[nodo] = (step_x * i, y)
        # Dibuja aristas.
        for padre, hijos in self.tree.items():
            for hijo in hijos:
                x1, y1 = pos[padre]
                x2, y2 = pos[hijo]
                self.tree_canvas.create_line(x1, y1, x2, y2, width=2, fill="#6b7280")
        # Dibuja nodos.
        for nodo, (x, y) in pos.items():
            grado = len(self.tree[nodo])
            self.tree_canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#dbeafe", outline="#1d4ed8", width=2)
            self.tree_canvas.create_text(x, y, text=nodo, font=("Segoe UI", 10, "bold"))
            self.tree_canvas.create_text(x, y + 28, text=f"n={niveles[nodo]} g={grado}", font=("Segoe UI", 9))
        # Actualiza altura.
        self.height_label.config(text=f"Altura total: {max(niveles.values()) if niveles else 0}")

    def _agregar_nodo(self) -> None:
        """Agrega nodo hijo al padre seleccionado."""
        padre = self.parent_var.get().strip().upper()
        nuevo = self.new_node_var.get().strip().upper()
        if not nuevo:
            self.tree_status.set("Estado: ingrese nombre de la nueva area.")
            return
        if padre not in self.tree:
            self.tree_status.set("Estado: seleccione un padre valido.")
            return
        if nuevo in self.tree:
            self.tree_status.set(f"Estado: el area '{nuevo}' ya existe.")
            return
        if len(self.tree[padre]) >= 2:
            self.tree_status.set(f"Estado: el padre '{padre}' ya tiene dos hijos.")
            return
        self.tree[nuevo] = []
        self.tree[padre].append(nuevo)
        self.new_node_var.set("")
        self.tree_status.set(f"Estado: agregada area '{nuevo}' bajo '{padre}'.")
        self._actualizar_padres_disponibles()
        self._redibujar_arbol()

    def _limpiar_arbol(self) -> None:
        """Reinicia arbol dejando solo la raiz."""
        self.tree = {self.tree_root: []}
        self.tree_status.set("Estado: organigrama limpiado.")
        self._actualizar_padres_disponibles()
        self._redibujar_arbol()

    def _restaurar_arbol(self) -> None:
        """Restaura arbol inicial por defecto."""
        self.tree = deepcopy(ORG_TREE)
        self.tree_root = ORG_ROOT
        self.tree_status.set("Estado: organigrama restaurado.")
        self._actualizar_padres_disponibles()
        self._redibujar_arbol()

    def _crear_tab_teoremas(self) -> None:
        """Crea modulo interactivo para teoremas de arbol binario."""
        frame = ttk.Frame(self.tabs, padding=16)
        self.tabs.add(frame, text="Capacidad")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        ttk.Label(frame, text="Explicacion breve: estima capacidad de estructura usando teoremas binarios.").grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )
        form = ttk.LabelFrame(frame, text="Entradas", style="Card.TLabelframe")
        form.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        self.h_var = tk.StringVar(value="3")
        self.i_var = tk.StringVar(value="7")
        ttk.Label(form, text="Niveles de supervision (h):").grid(row=0, column=0, sticky="w", padx=(0, 6), pady=(0, 8))
        ttk.Entry(form, textvariable=self.h_var, width=16).grid(row=0, column=1, sticky="w", pady=(0, 8))
        ttk.Label(form, text="Responsables internos (I):").grid(row=1, column=0, sticky="w", padx=(0, 6))
        ttk.Entry(form, textvariable=self.i_var, width=16).grid(row=1, column=1, sticky="w")
        ttk.Button(form, text="Calcular", command=self._calcular_teoremas).grid(row=0, column=2, rowspan=2, padx=(12, 0))
        result = ttk.LabelFrame(frame, text="Resultado", style="Card.TLabelframe")
        result.grid(row=2, column=0, sticky="nsew")
        result.columnconfigure(0, weight=1)
        result.rowconfigure(0, weight=1)
        self.theory_output = ScrolledText(result, wrap="word", height=10, font=("Consolas", 10))
        self.theory_output.grid(row=0, column=0, sticky="nsew")
        self._calcular_teoremas()

    def _calcular_teoremas(self) -> None:
        """Calcula y muestra resultados de teoremas."""
        self.theory_output.delete("1.0", tk.END)
        try:
            h = int(self.h_var.get())
            i = int(self.i_var.get())
            nmax = (2 ** (h + 1)) - 1
            hojas = i + 1
            msg = (
                f"Enunciado: estimar capacidad del equipo para h={h}, I={i}\n"
                "Desarrollo: puestos maximos=2^(h+1)-1, equipos hoja=I+1\n"
                f"Resultado -> puestos maximos posibles: {nmax}\n"
                f"Resultado -> equipos finales (hojas): {hojas}\n"
            )
            self.theory_output.insert(tk.END, msg)
        except ValueError:
            self.theory_output.insert(tk.END, "Ingrese valores enteros validos.")

    def _crear_tab_heaps(self) -> None:
        """Crea modulo interactivo para INSERTAR y HEAPIFY."""
        frame = ttk.Frame(self.tabs, padding=16)
        self.tabs.add(frame, text="Prioridades")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        ttk.Label(frame, text="Explicacion breve: prioriza incidencias operativas con un max-heap.").grid(
            row=0, column=0, sticky="w", pady=(0, 10)
        )
        controls = ttk.LabelFrame(frame, text="Operaciones de prioridad", style="Card.TLabelframe")
        controls.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        self.heap_base = [90, 70, 60, 20, 40, 10, 30]
        self.heap_insert_var = tk.StringVar(value="45")
        ttk.Label(controls, text=f"Cola de prioridad base: {self.heap_base}").grid(row=0, column=0, columnspan=3, sticky="w")
        ttk.Label(controls, text="Nueva prioridad:").grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(controls, textvariable=self.heap_insert_var, width=16).grid(row=1, column=1, sticky="w", pady=(8, 0))
        ttk.Button(controls, text="INSERTAR", command=self._heap_insertar).grid(row=2, column=0, pady=(10, 0), sticky="w")
        ttk.Button(controls, text="HEAPIFY", command=self._heap_heapify).grid(row=2, column=1, pady=(10, 0), padx=(10, 0), sticky="w")
        result = ttk.LabelFrame(frame, text="Resultado y pasos", style="Card.TLabelframe")
        result.grid(row=2, column=0, sticky="nsew")
        result.columnconfigure(0, weight=1)
        result.rowconfigure(0, weight=1)
        self.heap_output = ScrolledText(result, wrap="word", height=16, font=("Consolas", 10))
        self.heap_output.grid(row=0, column=0, sticky="nsew")

    def _heap_insertar(self) -> None:
        """Ejecuta operacion INSERTAR y muestra pasos."""
        self.heap_output.delete("1.0", tk.END)
        try:
            valor = int(self.heap_insert_var.get())
            resultado, pasos = insertar_en_max_heap(self.heap_base, valor)
            self.heap_output.insert(tk.END, "Enunciado: registrar incidencia y actualizar cola de prioridad\n")
            self.heap_output.insert(tk.END, "Desarrollo:\n")
            for paso in pasos:
                self.heap_output.insert(tk.END, f"- {paso}\n")
            self.heap_output.insert(tk.END, f"Resultado -> cola de prioridad final: {resultado}\n")
        except ValueError:
            self.heap_output.insert(tk.END, "Ingrese un numero entero valido.")

    def _heap_heapify(self) -> None:
        """Ejecuta operacion HEAPIFY y muestra pasos."""
        self.heap_output.delete("1.0", tk.END)
        arreglo = [35, 80, 60, 20, 40, 10, 30]
        resultado, pasos = heapify_max(arreglo, 0)
        self.heap_output.insert(tk.END, "Enunciado: reordenar prioridades despues de un cambio en la raiz\n")
        self.heap_output.insert(tk.END, "Desarrollo:\n")
        for paso in pasos:
            self.heap_output.insert(tk.END, f"- {paso}\n")
        self.heap_output.insert(tk.END, f"Resultado -> cola de prioridad final: {resultado}\n")


def main() -> None:
    """Punto de entrada del programa grafico de la unidad."""
    root = tk.Tk()
    ProgramaGraficoUnidad1(root)
    root.mainloop()


if __name__ == "__main__":
    main()
