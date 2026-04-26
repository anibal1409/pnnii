"""
Interfaz interactiva de la Unidad I (Tkinter).

Explicacion general:
- Este programa crea una interfaz para practicar conceptos de la unidad.
- Incluye tres modulos interactivos: arboles, teoremas y heaps.
- Esta pensado para estudiantes principiantes que necesitan ver el
  funcionamiento paso a paso de cada concepto.
"""

# Importa deque para recorrer el arbol por niveles.
from collections import deque
# Importa deepcopy para restaurar estructuras sin referencias compartidas.
from copy import deepcopy
# Importa tkinter como libreria base para GUI.
import tkinter as tk
# Importa ttk para widgets modernos (pestanas, botones, labels).
from tkinter import ttk
# Importa caja de texto con scroll para resultados largos.
from tkinter.scrolledtext import ScrolledText


# Define la estructura del arbol base usado en la interfaz.
DEFAULT_TREE = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": [],
}
# Define raiz inicial para el arbol.
DEFAULT_ROOT = "A"


def calcular_niveles(raiz: str, estructura: dict[str, list[str]]) -> dict[str, int]:
    """Calcula nivel de cada nodo con recorrido BFS."""
    # Inicializa el diccionario de niveles con la raiz en 0.
    niveles = {raiz: 0}
    # Crea la cola para procesar nodos pendientes.
    cola = deque([raiz])
    # Recorre el arbol hasta vaciar la cola.
    while cola:
        # Saca el nodo del frente.
        nodo = cola.popleft()
        # Recorre hijos del nodo actual.
        for hijo in estructura.get(nodo, []):
            # El nivel del hijo es el nivel del padre + 1.
            niveles[hijo] = niveles[nodo] + 1
            # Encola el hijo para seguir el recorrido.
            cola.append(hijo)
    # Retorna niveles completos.
    return niveles


def construir_posiciones_y_aristas(
    raiz: str, estructura: dict[str, list[str]], ancho: int, alto: int
) -> tuple[dict[str, tuple[float, float]], list[tuple[str, str]]]:
    """Construye posiciones dinamicas por nivel y lista de aristas."""
    # Calcula niveles para distribuir nodos verticalmente.
    niveles = calcular_niveles(raiz, estructura)
    # Agrupa nodos por nivel para distribuirlos horizontalmente.
    nodos_por_nivel: dict[int, list[str]] = {}
    # Recorre todos los nodos con su nivel.
    for nodo, nivel in niveles.items():
        # Crea lista del nivel si no existe.
        nodos_por_nivel.setdefault(nivel, [])
        # Agrega nodo al nivel correspondiente.
        nodos_por_nivel[nivel].append(nodo)
    # Define diccionario final de posiciones.
    posiciones: dict[str, tuple[float, float]] = {}
    # Calcula el nivel maximo para espaciar en vertical.
    nivel_max = max(nodos_por_nivel) if nodos_por_nivel else 0
    # Recorre niveles para asignar coordenadas.
    for nivel, nodos in nodos_por_nivel.items():
        # Ordena para mantener estabilidad visual.
        nodos_ordenados = sorted(nodos)
        # Calcula separacion horizontal en este nivel.
        separacion_x = ancho / (len(nodos_ordenados) + 1)
        # Calcula coordenada Y para el nivel.
        y = 40 + (nivel * (alto - 80) / max(1, nivel_max))
        # Asigna coordenadas a cada nodo.
        for i, nodo in enumerate(nodos_ordenados, start=1):
            x = separacion_x * i
            posiciones[nodo] = (x, y)
    # Construye lista de aristas desde la estructura actual.
    aristas: list[tuple[str, str]] = []
    # Recorre cada padre del arbol.
    for padre, hijos in estructura.items():
        # Recorre hijos del padre.
        for hijo in hijos:
            # Agrega arista padre -> hijo.
            aristas.append((padre, hijo))
    # Retorna posiciones y aristas para dibujar.
    return posiciones, aristas


def insertar_en_max_heap(heap: list[int], valor: int) -> tuple[list[int], list[str]]:
    """Inserta un valor en max-heap y devuelve pasos explicativos."""
    # Copia el heap para no mutar el original.
    salida = heap.copy()
    # Crea lista de mensajes para explicar cada paso.
    pasos = [f"Heap inicial: {salida}", f"Insertar valor {valor} al final."]
    # Inserta el nuevo valor al final.
    salida.append(valor)
    # Apunta al indice del elemento insertado.
    i = len(salida) - 1
    # Aplica bubble-up mientras no llegue a la raiz.
    while i > 0:
        # Calcula indice del padre.
        padre = (i - 1) // 2
        # Si padre ya es mayor o igual, la propiedad se mantiene.
        if salida[padre] >= salida[i]:
            pasos.append("No hay intercambio adicional: propiedad max-heap cumplida.")
            break
        # Registra intercambio didactico.
        pasos.append(
            f"Intercambiar {salida[i]} (hijo) con {salida[padre]} (padre)."
        )
        # Realiza intercambio.
        salida[padre], salida[i] = salida[i], salida[padre]
        # Sube al padre para seguir validando.
        i = padre
    # Agrega estado final del heap.
    pasos.append(f"Heap final: {salida}")
    # Devuelve heap resultante y explicaciones.
    return salida, pasos


def heapify_max(heap: list[int], idx: int) -> tuple[list[int], list[str]]:
    """Aplica heapify descendente y devuelve pasos explicativos."""
    # Copia heap de entrada para conservar original.
    salida = heap.copy()
    # Crea lista de mensajes para explicacion paso a paso.
    pasos = [f"Heap inicial: {salida}", f"Aplicar HEAPIFY desde indice {idx}."]

    # Define funcion interna recursiva de heapify.
    def _heapify(arr: list[int], i: int) -> None:
        # Marca mayor con el nodo actual.
        mayor = i
        # Calcula indice de hijo izquierdo.
        izq = 2 * i + 1
        # Calcula indice de hijo derecho.
        der = 2 * i + 2
        # Compara con hijo izquierdo.
        if izq < len(arr) and arr[izq] > arr[mayor]:
            mayor = izq
        # Compara con hijo derecho.
        if der < len(arr) and arr[der] > arr[mayor]:
            mayor = der
        # Si el mayor no es el actual, intercambia y continua.
        if mayor != i:
            pasos.append(f"Intercambiar arr[{i}]={arr[i]} con arr[{mayor}]={arr[mayor]}.")
            arr[i], arr[mayor] = arr[mayor], arr[i]
            _heapify(arr, mayor)

    # Ejecuta heapify desde indice inicial.
    _heapify(salida, idx)
    # Agrega estado final del heap.
    pasos.append(f"Heap final: {salida}")
    # Devuelve salida y pasos didacticos.
    return salida, pasos


class InterfazUnidad1:
    """Ventana principal para trabajar conceptos de la unidad."""

    def __init__(self, root: tk.Tk) -> None:
        # Guarda referencia de la ventana raiz.
        self.root = root
        # Configura titulo de la ventana.
        self.root.title("Unidad I - Interfaz interactiva")
        # Configura tamano inicial de la ventana.
        self.root.geometry("1100x760")
        # Define un tamano minimo para mantener buena legibilidad.
        self.root.minsize(920, 640)
        # Configura estilo visual profesional de la interfaz.
        self._configurar_estilos()
        # Inicializa arbol editable copiando estructura por defecto.
        self.tree = deepcopy(DEFAULT_TREE)
        # Define raiz activa del arbol editable.
        self.tree_root = DEFAULT_ROOT
        # Crea contenedor de pestanas.
        self.tabs = ttk.Notebook(self.root)
        # Expande el contenedor en toda la ventana.
        self.tabs.pack(fill="both", expand=True, padx=10, pady=10)
        # Crea cada pestana interactiva.
        self._crear_tab_arboles()
        self._crear_tab_teoremas()
        self._crear_tab_heaps()

    def _configurar_estilos(self) -> None:
        """Configura estilos para una interfaz mas pulcra y profesional."""
        # Crea objeto de estilos ttk.
        style = ttk.Style()
        # Selecciona un tema moderno disponible.
        if "clam" in style.theme_names():
            style.theme_use("clam")
        # Configura tipografia base para labels.
        style.configure("TLabel", font=("Segoe UI", 10))
        # Configura estilo de botones.
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        # Configura estilo de entradas.
        style.configure("TEntry", padding=4)
        # Configura estilo de pestañas.
        style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=(12, 8))
        # Configura estilo de secciones tipo card.
        style.configure("Card.TLabelframe", padding=12)
        # Configura estilo de titulo en secciones.
        style.configure("Card.TLabelframe.Label", font=("Segoe UI", 10, "bold"))

    def _crear_tab_arboles(self) -> None:
        # Crea frame de pestana para conceptos de arboles.
        frame = ttk.Frame(self.tabs, padding=16)
        # Agrega pestana al notebook.
        self.tabs.add(frame, text="Arboles")
        # Permite que el contenido se adapte al tamaño de ventana.
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(3, weight=1)
        # Agrega explicacion breve.
        ttk.Label(
            frame,
            text="Explicacion breve: observa niveles, altura y grado en un arbol binario.",
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))
        # Crea contenedor horizontal para controles del arbol.
        controles = ttk.LabelFrame(frame, text="Controles del arbol", style="Card.TLabelframe")
        # Muestra contenedor de controles.
        controles.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        # Crea variable para padre donde insertar nuevo nodo.
        self.parent_var = tk.StringVar(value="A")
        # Crea variable para nombre del nuevo nodo.
        self.node_var = tk.StringVar(value="")
        # Etiqueta para entrada de nodo padre.
        ttk.Label(controles, text="Nodo padre:").grid(row=0, column=0, padx=(0, 4))
        # Crea selector de padres disponibles (nodos con menos de 2 hijos).
        self.parent_combo = ttk.Combobox(
            controles, textvariable=self.parent_var, width=10, state="readonly"
        )
        # Muestra selector de padres.
        self.parent_combo.grid(row=0, column=1, padx=(0, 10))
        # Etiqueta para entrada de nuevo nodo.
        ttk.Label(controles, text="Nuevo nodo:").grid(row=0, column=2, padx=(0, 4))
        # Campo para escribir nuevo nodo.
        ttk.Entry(controles, textvariable=self.node_var, width=8).grid(row=0, column=3, padx=(0, 10))
        # Boton para agregar nuevo nodo.
        self.agregar_nodo_btn = ttk.Button(
            controles, text="Agregar nodo", command=self._agregar_nodo_arbol
        )
        self.agregar_nodo_btn.grid(row=0, column=4, padx=4)
        # Boton para limpiar arbol.
        ttk.Button(controles, text="Limpiar arbol", command=self._limpiar_arbol).grid(row=0, column=5, padx=4)
        # Boton para restaurar arbol inicial.
        ttk.Button(controles, text="Restaurar arbol", command=self._restaurar_arbol).grid(row=0, column=6, padx=4)
        # Crea etiqueta de estado para mensajes al usuario.
        self.arbol_estado = tk.StringVar(value="Estado: arbol inicial cargado.")
        # Muestra etiqueta de estado.
        ttk.Label(frame, textvariable=self.arbol_estado).grid(row=2, column=0, sticky="w", pady=(0, 8))
        # Crea contenedor visual tipo card para el canvas.
        canvas_card = ttk.LabelFrame(frame, text="Vista del arbol", style="Card.TLabelframe")
        # Muestra card del canvas y permite expandir.
        canvas_card.grid(row=3, column=0, sticky="nsew", pady=(0, 8))
        # Configura expansion interna de la card.
        canvas_card.columnconfigure(0, weight=1)
        canvas_card.rowconfigure(0, weight=1)
        # Crea canvas para dibujo del arbol editable.
        self.arbol_canvas = tk.Canvas(canvas_card, bg="white", highlightthickness=0)
        # Muestra canvas en pantalla con expansion completa.
        self.arbol_canvas.grid(row=0, column=0, sticky="nsew")
        # Redibuja automaticamente cuando cambia el tamaño del canvas.
        self.arbol_canvas.bind("<Configure>", self._on_canvas_resize)
        # Crea etiqueta para mostrar altura actual.
        self.altura_label = ttk.Label(frame, text="Altura total del arbol: 0")
        # Muestra etiqueta de altura.
        self.altura_label.grid(row=4, column=0, sticky="w", pady=6)
        # Dibuja el arbol por primera vez.
        self._redibujar_arbol()
        # Carga opciones iniciales del selector de padres.
        self._actualizar_padres_disponibles()

    def _actualizar_padres_disponibles(self) -> None:
        """Actualiza select con nodos que pueden recibir nuevos hijos."""
        # Calcula padres disponibles segun restriccion binaria.
        padres_disponibles = sorted(
            [nodo for nodo, hijos in self.tree.items() if len(hijos) < 2]
        )
        # Actualiza opciones del combobox.
        self.parent_combo["values"] = padres_disponibles
        # Si no hay padres disponibles, deshabilita agregar.
        if not padres_disponibles:
            self.parent_var.set("")
            self.parent_combo.configure(state="disabled")
            self.agregar_nodo_btn.configure(state="disabled")
            self.arbol_estado.set(
                "Estado: no hay nodos padre disponibles (todos tienen 2 hijos)."
            )
            return
        # Si hay opciones, habilita controles de agregado.
        self.parent_combo.configure(state="readonly")
        self.agregar_nodo_btn.configure(state="normal")
        # Conserva seleccion si sigue siendo valida.
        if self.parent_var.get() not in padres_disponibles:
            self.parent_var.set(padres_disponibles[0])

    def _on_canvas_resize(self, _event: tk.Event) -> None:
        """Redibuja el arbol al redimensionar para mantener responsividad."""
        # Llama redibujo completo al cambiar tamaño.
        self._redibujar_arbol()

    def _redibujar_arbol(self) -> None:
        """Redibuja el arbol actual en el canvas."""
        # Limpia todo lo dibujado previamente.
        self.arbol_canvas.delete("all")
        # Obtiene ancho actual del canvas.
        ancho = max(520, self.arbol_canvas.winfo_width())
        # Obtiene alto actual del canvas.
        alto = max(260, self.arbol_canvas.winfo_height())
        # Si no hay nodos, muestra mensaje y sale.
        if not self.tree:
            self.arbol_canvas.create_text(ancho / 2, alto / 2, text="Arbol vacio", font=("Arial", 14, "bold"))
            self.altura_label.config(text="Altura total del arbol: N/A")
            return
        # Ajusta raiz si no existe en la estructura actual.
        if self.tree_root not in self.tree:
            self.tree_root = next(iter(self.tree))
        # Construye posiciones y aristas dinamicas para el arbol actual.
        posiciones, aristas = construir_posiciones_y_aristas(
            self.tree_root, self.tree, ancho=ancho, alto=alto
        )
        # Calcula niveles para mostrar nivel y grado por nodo.
        niveles = calcular_niveles(self.tree_root, self.tree)
        # Dibuja aristas.
        for padre, hijo in aristas:
            x1, y1 = posiciones[padre]
            x2, y2 = posiciones[hijo]
            self.arbol_canvas.create_line(x1, y1, x2, y2, width=2, fill="#6b7280")
        # Dibuja nodos y etiquetas.
        for nodo, (x, y) in posiciones.items():
            grado = len(self.tree.get(nodo, []))
            self.arbol_canvas.create_oval(
                x - 20, y - 20, x + 20, y + 20, fill="#dbeafe", outline="#1d4ed8", width=2
            )
            self.arbol_canvas.create_text(x, y, text=nodo, font=("Arial", 11, "bold"))
            self.arbol_canvas.create_text(
                x, y + 28, text=f"nivel={niveles.get(nodo, 0)} grado={grado}", font=("Arial", 9)
            )
        # Calcula altura y actualiza etiqueta.
        altura = max(niveles.values()) if niveles else 0
        self.altura_label.config(text=f"Altura total del arbol: {altura}")
        # Actualiza select de padres en cada cambio visual.
        self._actualizar_padres_disponibles()

    def _agregar_nodo_arbol(self) -> None:
        """Agrega un nodo nuevo como hijo del padre indicado."""
        # Lee y normaliza nombre del padre.
        padre = self.parent_var.get().strip().upper()
        # Lee y normaliza nombre del nuevo nodo.
        nuevo = self.node_var.get().strip().upper()
        # Valida que padre no este vacio.
        if not padre:
            self.arbol_estado.set("Estado: ingrese un nodo padre valido.")
            return
        # Valida que nuevo nodo no este vacio.
        if not nuevo:
            self.arbol_estado.set("Estado: ingrese el nombre del nuevo nodo.")
            return
        # Valida existencia del padre en el arbol.
        if padre not in self.tree:
            self.arbol_estado.set(f"Estado: el nodo padre '{padre}' no existe.")
            return
        # Valida que el nuevo nodo no exista.
        if nuevo in self.tree:
            self.arbol_estado.set(f"Estado: el nodo '{nuevo}' ya existe.")
            return
        # Valida que el padre no tenga mas de dos hijos (arbol binario).
        if len(self.tree[padre]) >= 2:
            self.arbol_estado.set(f"Estado: '{padre}' ya tiene 2 hijos.")
            return
        # Crea entrada del nuevo nodo sin hijos.
        self.tree[nuevo] = []
        # Agrega nuevo nodo como hijo del padre.
        self.tree[padre].append(nuevo)
        # Limpia campo del nuevo nodo para siguiente insercion.
        self.node_var.set("")
        # Informa exito en barra de estado.
        self.arbol_estado.set(f"Estado: nodo '{nuevo}' agregado como hijo de '{padre}'.")
        # Redibuja el arbol actualizado.
        self._redibujar_arbol()

    def _limpiar_arbol(self) -> None:
        """Limpia el arbol y deja solo la raiz."""
        # Conserva solo la raiz para reiniciar estructura minima.
        self.tree = {self.tree_root: []}
        # Informa accion de limpieza.
        self.arbol_estado.set("Estado: arbol limpiado (solo raiz).")
        # Redibuja arbol limpio.
        self._redibujar_arbol()

    def _restaurar_arbol(self) -> None:
        """Restaura el arbol al estado inicial de la unidad."""
        # Restaura estructura por defecto sin compartir referencias.
        self.tree = deepcopy(DEFAULT_TREE)
        # Restaura raiz por defecto.
        self.tree_root = DEFAULT_ROOT
        # Informa restauracion.
        self.arbol_estado.set("Estado: arbol restaurado a su estado inicial.")
        # Redibuja arbol restaurado.
        self._redibujar_arbol()

    def _crear_tab_teoremas(self) -> None:
        # Crea frame de pestana para teoremas.
        frame = ttk.Frame(self.tabs, padding=16)
        # Agrega pestana al notebook.
        self.tabs.add(frame, text="Teoremas")
        # Configura expansión responsive del contenido.
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        # Agrega explicacion breve.
        ttk.Label(
            frame,
            text="Explicacion breve: calcula nodos maximos y hojas con formulas basicas.",
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))
        # Crea card para formulario de entrada.
        form = ttk.LabelFrame(frame, text="Datos de entrada", style="Card.TLabelframe")
        # Muestra formulario expandible en ancho.
        form.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        # Crea variables de entrada.
        self.altura_var = tk.StringVar(value="3")
        self.internos_var = tk.StringVar(value="7")
        # Crea formulario para altura.
        ttk.Label(form, text="Altura h:").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 8))
        ttk.Entry(form, textvariable=self.altura_var, width=20).grid(row=0, column=1, sticky="w", pady=(0, 8))
        # Crea formulario para nodos internos.
        ttk.Label(form, text="Nodos internos I:").grid(row=1, column=0, sticky="w", padx=(0, 8))
        ttk.Entry(form, textvariable=self.internos_var, width=20).grid(row=1, column=1, sticky="w")
        # Crea boton de calculo.
        ttk.Button(form, text="Calcular teoremas", command=self._calcular_teoremas).grid(
            row=0, column=2, rowspan=2, padx=(12, 0)
        )
        # Crea card de resultados.
        resultado_card = ttk.LabelFrame(frame, text="Resultado", style="Card.TLabelframe")
        # Muestra card de resultados con expansion completa.
        resultado_card.grid(row=2, column=0, sticky="nsew")
        resultado_card.columnconfigure(0, weight=1)
        resultado_card.rowconfigure(0, weight=1)
        # Crea salida de texto con scroll.
        self.teoremas_resultado = ScrolledText(resultado_card, wrap="word", height=10, font=("Consolas", 10))
        self.teoremas_resultado.grid(row=0, column=0, sticky="nsew")
        # Crea boton de calculo.
        self._calcular_teoremas()

    def _calcular_teoremas(self) -> None:
        # Limpia salida previa.
        self.teoremas_resultado.delete("1.0", tk.END)
        try:
            # Convierte altura a entero.
            h = int(self.altura_var.get())
            # Convierte internos a entero.
            i = int(self.internos_var.get())
            # Aplica teorema I.
            nmax = (2 ** (h + 1)) - 1
            # Aplica teorema II.
            hojas = i + 1
            # Construye mensaje didactico.
            mensaje = (
                f"Resultado Teorema I: para h={h}, Nmax = 2^(h+1)-1 = {nmax}\n"
                f"Resultado Teorema II: para I={i}, hojas = I+1 = {hojas}\n"
                "Representacion secuencial base 0: hijo_izq=2*i+1, hijo_der=2*i+2"
            )
            # Muestra resultados.
            self.teoremas_resultado.insert(tk.END, mensaje)
        except ValueError:
            # Muestra error de validacion amigable.
            self.teoremas_resultado.insert(tk.END, "Ingrese valores enteros validos.")

    def _crear_tab_heaps(self) -> None:
        # Crea frame de pestana para heaps.
        frame = ttk.Frame(self.tabs, padding=16)
        # Agrega pestana al notebook.
        self.tabs.add(frame, text="Heaps")
        # Configura expansión responsive.
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(2, weight=1)
        # Agrega explicacion breve.
        ttk.Label(
            frame,
            text="Explicacion breve: prueba INSERTAR y HEAPIFY para mantener un max-heap.",
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))
        # Crea card para controles de heap.
        controles = ttk.LabelFrame(frame, text="Controles de heap", style="Card.TLabelframe")
        # Muestra card de controles expandible en ancho.
        controles.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        # Define heap base mostrado al inicio.
        self.heap_base = [90, 70, 60, 20, 40, 10, 30]
        # Campo para valor de insercion.
        self.insertar_var = tk.StringVar(value="45")
        # Etiqueta con heap base.
        ttk.Label(controles, text=f"Heap base: {self.heap_base}").grid(row=0, column=0, columnspan=3, sticky="w")
        # Campo para escribir valor a insertar.
        ttk.Label(controles, text="Valor a insertar:").grid(row=1, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(controles, textvariable=self.insertar_var, width=20).grid(row=1, column=1, sticky="w", pady=(8, 0))
        # Boton para ejecutar insercion.
        ttk.Button(controles, text="Ejecutar INSERTAR", command=self._ejecutar_insertar).grid(
            row=2, column=0, pady=(10, 0), sticky="w"
        )
        # Boton para ejecutar heapify.
        ttk.Button(controles, text="Ejecutar HEAPIFY", command=self._ejecutar_heapify).grid(
            row=2, column=1, pady=(10, 0), padx=(10, 0), sticky="w"
        )
        # Crea card de resultados para heaps.
        resultado_card = ttk.LabelFrame(frame, text="Resultado y pasos", style="Card.TLabelframe")
        # Muestra card de resultado expandible.
        resultado_card.grid(row=2, column=0, sticky="nsew")
        resultado_card.columnconfigure(0, weight=1)
        resultado_card.rowconfigure(0, weight=1)
        # Area de texto con scroll para mostrar pasos.
        self.heaps_resultado = ScrolledText(resultado_card, wrap="word", height=18, font=("Consolas", 10))
        self.heaps_resultado.grid(row=0, column=0, sticky="nsew")

    def _ejecutar_insertar(self) -> None:
        # Limpia resultados previos.
        self.heaps_resultado.delete("1.0", tk.END)
        try:
            # Convierte valor ingresado a entero.
            valor = int(self.insertar_var.get())
            # Ejecuta insercion con pasos.
            resultado, pasos = insertar_en_max_heap(self.heap_base, valor)
            # Muestra titulo del bloque.
            self.heaps_resultado.insert(tk.END, "INSERTAR en max-heap\n")
            # Muestra pasos uno a uno.
            for paso in pasos:
                self.heaps_resultado.insert(tk.END, f"- {paso}\n")
            # Muestra resultado final.
            self.heaps_resultado.insert(tk.END, f"Resultado final: {resultado}\n")
        except ValueError:
            # Muestra error de validacion amigable.
            self.heaps_resultado.insert(tk.END, "Ingrese un numero entero para insertar.")

    def _ejecutar_heapify(self) -> None:
        # Limpia resultados previos.
        self.heaps_resultado.delete("1.0", tk.END)
        # Define arreglo ejemplo para heapify.
        arreglo = [35, 80, 60, 20, 40, 10, 30]
        # Ejecuta heapify desde raiz.
        resultado, pasos = heapify_max(arreglo, 0)
        # Muestra titulo del bloque.
        self.heaps_resultado.insert(tk.END, "HEAPIFY desde indice 0\n")
        # Muestra pasos uno a uno.
        for paso in pasos:
            self.heaps_resultado.insert(tk.END, f"- {paso}\n")
        # Muestra resultado final.
        self.heaps_resultado.insert(tk.END, f"Resultado final: {resultado}\n")


def main() -> None:
    # Crea ventana principal de Tkinter.
    root = tk.Tk()
    # Instancia la interfaz completa de la unidad.
    InterfazUnidad1(root)
    # Inicia el bucle de eventos de la GUI.
    root.mainloop()


if __name__ == "__main__":
    # Ejecuta la aplicacion al correr este archivo.
    main()
