import tkinter as tk
from tkinter import messagebox, ttk
import math

from afn import AFN

class InterfazThompson:

    def __init__(self):
        self.ventana = tk.Tk()

        self.ventana.title("Metodo de Thompson")
        self.ventana.geometry("500x500")

        self.crear_menu_principal()

    def crear_menu_principal(self):

        titulo = tk.Label(
            self.ventana,
            text="Metodo de Thompson",
            font=("Arial", 20, "bold")
        )

        titulo.pack(pady=25)

        boton_basico = tk.Button(
            self.ventana,
            text="Crear AFN basico",
            width=25,
            command=self.ventana_crear_basico
        )

        boton_basico.pack(pady=5)

        boton_union = tk.Button(
            self.ventana,
            text="Unir AFN",
            width=25,
            command=self.ventana_unir_afn
        )

        boton_union.pack(pady=5)

        boton_concatenar = tk.Button(
            self.ventana,
            text="Concatenar AFN",
            width=25,
            command=self.ventana_concatenar_afn
        )

        boton_concatenar.pack(pady=5)

        boton_pos = tk.Button(
            self.ventana,
            text="Cerradura positiva (+)",
            width=25,
            command=self.ventana_cerradura_pos
        )

        boton_pos.pack(pady=5)

        boton_kleene = tk.Button(
            self.ventana,
            text="Cerradura de Kleene (*)",
            width=25,
            command=self.ventana_cerradura_kleene
        )

        boton_kleene.pack(pady=5)

        boton_opcional = tk.Button(
            self.ventana,
            text="opcional (?)",
            width=25,
            command=self.ventana_opcional
        )

        boton_opcional.pack(pady=5)

        boton_ver = tk.Button(
            self.ventana,
            text="Ver AFN",
            width=25,
            command=self.ventana_ver_afn
        )

        boton_ver.pack(pady=5)

    def ventana_crear_basico(self):

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Crear AFN basico")
        ventana.geometry("350x300")

        titulo = tk.Label(
            ventana,
            text="Crear AFN basico",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        tk.Label(
            ventana,
            text="Simbolo inferior:"
        ).pack()

        entrada_simb1 = tk.Entry(ventana)
        entrada_simb1.pack(pady=5)

        tk.Label(
            ventana,
            text="Simbolo superior"
        ).pack()

        entrada_simb2 = tk.Entry(ventana)
        entrada_simb2.pack(pady=5)

        tk.Label(
            ventana,
            text="ID del AFN:"
        ).pack()

        entrada_id = tk.Entry(ventana)
        entrada_id.pack(pady=5)

        def crear():

            simb1 = entrada_simb1.get()
            simb2 = entrada_simb2.get()
            id_afn = entrada_id.get()

            try:

                if id_afn == "":
                    raise ValueError(
                        "Debes introducir un ID para el AFN."
                    )

                if simb2 == "":

                    AFN().crear_basico(
                        simb1,
                        id_afn=id_afn
                    )

                else:

                    AFN().crear_basico(
                        simb1,
                        simb2,
                        id_afn
                    )

                messagebox.showinfo(
                    "AFN creado",
                    f"El AFN `{id_afn}` fue creado correctamente."
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        boton_crear = tk.Button(
            ventana,
            text="Crear",
            width=15,
            command=crear
        )

        boton_crear.pack(pady=5)

    def ventana_unir_afn(self):

        ids = AFN.obtener_ids()

        if len(ids) < 2:
            messagebox.showwarning(
                "AFN insuficientes",
                "Debes crear al menos dos AFN para realizar una union."
            )
            return

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Unir AFN")
        ventana.geometry("350x300")

        titulo = tk.Label(
            ventana,
            text="Unir AFN",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        # Primer AFN

        tk.Label(
            ventana,
            text="Primer AFN:"
        ).pack()

        selector_afn1 = ttk.Combobox(
            ventana,
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn1.pack(pady=5)
        selector_afn1.current(0)

        # Segundo AFN

        tk.Label(
            ventana,
            text="Segundo AFN:"
        ).pack()

        selector_afn2 = ttk.Combobox(
            ventana, 
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn2.pack(pady=5)

        if len(ids) > 1:
            selector_afn2.current(1)

        # ID del resultado

        tk.Label(
            ventana, 
            text="ID del nuevo AFN:"
        ).pack()

        entrada_id = tk.Entry(
            ventana,
            width=28
        )

        entrada_id.pack(pady=5)

        #Accion

        def unir():

            id1 = selector_afn1.get()
            id2 = selector_afn2.get()
            nuevo_id = entrada_id.get().strip()

            try:

                if id1 == id2:
                    raise ValueError(
                        "Debes seleccionar dos AFN diferentes."
                    )

                if nuevo_id == "":
                    raise ValueError(
                        "Debes introducir un ID para el AFN resultante." 
                    )

                afn1 = AFN.obtener_afn(id1)
                afn2 = AFN.obtener_afn(id2)

                afn1.unir(
                    afn2,
                    nuevo_id
                )

                messagebox.showinfo(
                    "Union realizada",
                    f"El AFN `{nuevo_id}` fue creado correctamente."
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        boton_unir = tk.Button(
            ventana,
            text="Unir",
            width=15,
            command=unir
        )

        boton_unir.pack(pady=15)

    def ventana_concatenar_afn(self):

        ids = AFN.obtener_ids()

        if len(ids) < 2:

            messagebox.showwarning(
                "AFN insuficientes",
                "Necesitas al menos dos AFN para concatenar."
            )
            return

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Concatenar AFN")
        ventana.geometry("350x300")

        titulo = tk.Label(
            ventana,
            text="Concatenar AFN",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        tk.Label(
            ventana,
            text="Primer AFN:"
        ).pack()

        selector_afn1 = ttk.Combobox(
            ventana,
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn1.pack(pady=5)
        selector_afn1.current(0)

        tk.Label(
            ventana,
            text="Segundo AFN:"
        ).pack()

        selector_afn2 = ttk.Combobox(
            ventana,
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn2.pack(pady=5)
        selector_afn2.current(1)

        tk.Label(
            ventana,
            text="ID del nuevo AFN:"
        ).pack()

        entrada_id = tk.Entry(
            ventana,
            width=28
        )

        entrada_id.pack(pady=5)

        def concatenar():

            id1 = selector_afn1.get()
            id2 = selector_afn2.get()
            nuevo_id = entrada_id.get().strip()

            try:

                if id1 == id2:
                    raise ValueError(
                        "Debes seleccionar dos AFN diferentes."
                    )

                if nuevo_id == "":
                    raise ValueError(
                        "Debes seleccionar un ID para el AFN resultante."
                    )

                afn1 = AFN.obtener_afn(id1)
                afn2 = AFN.obtener_afn(id2)

                afn1.concatenar(
                    afn2,
                    nuevo_id
                )

                messagebox.showinfo(
                    "Concatenacion realizada",
                    f"El AFN `{nuevo_id}` fue creado correctamente."
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        boton_concatenar = tk.Button(
            ventana, 
            text="Concatenar",
            width=15,
            command=concatenar
        )

        boton_concatenar.pack(pady=15)

    def ventana_cerradura_pos(self):

        ids = AFN.obtener_ids()

        if not ids:
            messagebox.showwarning(
                "AFN faltante",
                "Debes crear al menos un AFN"
            )
            return

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Cerradura positiva")
        ventana.geometry("350x250")

        titulo = tk.Label(
            ventana,
            text="Cerradura Positiva (+)",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        tk.Label(
            ventana,
            text="AFN:"
        ).pack()

        selector_afn = ttk.Combobox(
            ventana,
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn.pack(pady=5)
        selector_afn.current(0)

        # Donde mete el nuevo ID del AFN

        tk.Label(
            ventana,
            text="ID del nuevo AFN:"
        ).pack()

        entrada_id = tk.Entry(
            ventana,
            width=28
        )

        entrada_id.pack(pady=5)

        # Cerradura

        def aplicar():

            id_afn = selector_afn.get()
            nuevo_id = entrada_id.get().strip()

            try:

                if nuevo_id == "":
                    raise ValueError(
                        "Debes introducir un ID para el AFN resultante"
                    )

                afn = AFN.obtener_afn(id_afn)

                afn.cerradura_pos(
                    nuevo_id
                )

                messagebox.showinfo(
                    "Cerradura realizada",
                    f"El afn `{nuevo_id}` fue creado correctamente."
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        boton_aplicar = tk.Button(
            ventana,
            text="Aplicar",
            width=15,
            command=aplicar
        )

        boton_aplicar.pack(pady=15)

    def ventana_cerradura_kleene(self):

        ids = AFN.obtener_ids()

        if not ids:
            messagebox.showwarning(
                "AFN faltante",
                "Debes crear al menos un AFN."
            )
            return

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Cerradura de Kleene")
        ventana.geometry("350x250")

        titulo = tk.Label(
            ventana,
            text="Cerradura de Kleene (*)",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        # Aqui viene el selector del AFN

        tk.Label(
            ventana,
            text="AFN:"
        ).pack()

        selector_afn = ttk.Combobox(
            ventana, 
            values=ids,
            state="onlyread",
            width=25
        )

        selector_afn.pack(pady=5)
        selector_afn.current(0)

        #Lo de siempreeee, el ID del nuevo afn

        tk.Label(
            ventana,
            text="ID del nuevo AFN:"
        ).pack()

        entrada_id = tk.Entry(
            ventana,
            width=28
        )

        entrada_id.pack(pady=5)

        # Lo mismo x2, aplicar la cerradura

        def aplicar():

            id_afn = selector_afn.get()
            nuevo_id = entrada_id.get().strip()

            try:

                if nuevo_id == "":
                    raise ValueError(
                        "Debes introducir un ID para el AFN resultante."
                    )

                afn = AFN.obtener_afn(id_afn)

                afn.cerradura_kleene(
                    nuevo_id
                )

                messagebox.showinfo(
                    "Cerradura realizada",
                    f"El AFN `{nuevo_id}` fue creado correctamente."
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        boton_aplicar = tk.Button(
            ventana,
            text="Aplicar",
            width=15,   
            command=aplicar
        )

        boton_aplicar.pack(pady=15)

    def ventana_opcional(self):

        ids = AFN.obtener_ids()

        if not ids:
            messagebox.showwarning(
                "AFN faltante",
                "Debes crear un AFN."
            )
            return

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Opcional")
        ventana.geometry("350x250")

        titulo = tk.Label(
            ventana,
            text="AFN opcional",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        tk.Label(
            ventana,
            text="AFN:"
        ).pack()

        selector_afn = ttk.Combobox(
            ventana,
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn.pack(pady=5)
        selector_afn.current(0)

        tk.Label(
            ventana,
            text="ID del nuevo AFN:"
        ).pack()

        entrada_id = tk.Entry(
            ventana,
            width=28
        )

        entrada_id.pack(pady=5)

        def aplicar():

            id_afn = selector_afn.get()
            nuevo_id = entrada_id.get().strip()

            try:

                if nuevo_id == "":
                    raise ValueError(
                        "Debe introducir un ID para el AFN resultante."
                    )

                afn = AFN.obtener_afn(id_afn)

                afn.opcional(
                    nuevo_id
                )

                messagebox.showinfo(
                    "Operacion realizada",
                    f"El AFN `{nuevo_id}` fue creado correctamente."
                )

                ventana.destroy()

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error)
                )

        boton_aplicar = tk.Button(
            ventana,
            text="Aplicar",
            width=15,
            command=aplicar
        )

        boton_aplicar.pack(pady=15)












        












        

    def ventana_ver_afn(self):

        # Verificamos que existe al menos un AFN
        ids = AFN.obtener_ids()

        if not ids:
            messagebox.showwarning(
                "Sin AFN",
                "Primero debes crear al menos un AFN"
            )
            return

        ventana = tk.Toplevel(self.ventana)

        ventana.title("Ver AFN")
        ventana.geometry("900x800")

        titulo = tk.Label(
            ventana,
            text="Ver AFN",
            font=("Arial", 16, "bold")
        )

        titulo.pack(pady=15)

        #Aqui implementamos un selector de AFN

        frame_selector = tk.Frame(ventana)
        frame_selector.pack(pady=10)

        tk.Label(
            frame_selector,
            text="AFN:"
        ).pack(side="left", padx=5)

        selector_afn = ttk.Combobox(
            frame_selector,
            values=ids,
            state="readonly",
            width=25
        )

        selector_afn.pack(side="left", padx=5)

        selector_afn.current(0)

        # Diagrama del AFN

        frame_grafo = tk.LabelFrame(
            ventana,
            text="Diagrama del AFN"
        )

        frame_grafo.pack(
            padx=15,
            pady=10,
            fill="both"
        )

        canvas = tk.Canvas(
            frame_grafo,
            width=850,
            height=400
        )

        canvas.pack(
            padx=10,
            pady=10
        )

        # Mostramos la info general

        frame_info = tk.Frame(ventana)
        frame_info.pack(pady=10)

        label_inicial = tk.Label(frame_info, text="")
        label_inicial.pack()

        label_estados = tk.Label(frame_info, text="")
        label_estados.pack()

        label_aceptacion = tk.Label(frame_info, text="")
        label_aceptacion.pack()

        label_alfabeto = tk.Label(frame_info, text="")
        label_alfabeto.pack()


        tabla = ttk.Treeview(
            ventana,
            columns=("origen", "simbolo", "destino"),
            show="headings",
            height=12
        )

        tabla.heading("origen", text="Estado origen")
        tabla.heading("simbolo", text="Simbolo")
        tabla.heading("destino", text="Estado destino")

        tabla.column(
            "origen",
            width=150,
            anchor="center"
        )

        tabla.column(
            "simbolo",
            width=150,
            anchor="center"
        )

        tabla.column(
            "destino",
            width=150,
            anchor="center"
        )

        tabla.pack(pady=15)

        # Con esta funcion mostraremos el AFN

        def mostrar_afn(event=None):

            id_afn = selector_afn.get()

            afn = AFN.obtener_afn(id_afn)

            if afn is None:
                return
            
            self.dibujar_afn(
                canvas,
                afn
            )

            estados = sorted(
                afn.edos_afn,
                key=lambda e: e.id_edo
            )

            aceptacion = sorted(
                afn.edos_acept,
                key=lambda e: e.id_edo
            )

            label_inicial.config(
                text=f"Estado inicial: {afn.edo_ini.id_edo} "
            )

            label_estados.config(
                text="Estados: " +
                str([e.id_edo for e in estados])
            )

            label_aceptacion.config(
                text="Estados de aceptacion: " +
                str([e.id_edo for e in aceptacion])
            )

            label_alfabeto.config(
                text="Alfabeto: " +
                str(sorted(afn.alfabeto))
            )

            # Este pa limpiar la tabla anterior
            for fila in tabla.get_children():
                tabla.delete(fila)

            for origen, simbolo, destino in afn.obtener_transiciones():

                tabla.insert(
                    "",
                    "end",
                    values=(
                        origen,
                        simbolo,
                        destino
                    )
                )

            # Con este selector se cambia 
            # automaticamente al cambiar de AFN

        selector_afn.bind(
            "<<ComboboxSelected>>",
            mostrar_afn
        )

        mostrar_afn()

    def dibujar_afn(self, canvas, afn):

        canvas.delete("all")

        estados = sorted(
            afn.edos_afn,
            key=lambda e: e.id_edo
        )

        if not estados:
            return

        ancho = 850
        alto = 400

        centro_x = ancho / 2
        centro_y = alto / 2

        radio_x = 300
        radio_y = 130

        radio_estado = 25

        posiciones = {}

        cantidad = len(estados)

        # Aqui vamos a calcular la posicion de cada estado

        if cantidad == 1:

            posiciones[estados[0].id_edo] = (
                centro_x,
                centro_y
            )

        else:

            for i, estado in  enumerate(estados):

                angulo = (
                    -math.pi / 2
                    + (2 * math.pi * i / cantidad)
                )

                x = centro_x + radio_x * math.cos(angulo)
                y = centro_y + radio_y * math.sin(angulo)

                posiciones[estado.id_edo] = (x, y)

        # Obtenemos las transiciones 
        transiciones = afn.obtener_transiciones()

        pares = (
            (origen, destino)
            for origen, simbolo, destino in transiciones
        )

        # Dibujaremos las transiciones

        for origen, simbolo, destino in transiciones:

            x1, y1 = posiciones[origen]
            x2, y2 = posiciones[destino]

            #transicion a si mismo

            if origen == destino:

                canvas.create_line(
                    x1, 
                    y1 - radio_estado,
                    x1 + 35,
                    y1 - 60,
                    x1 - 35,
                    y1 - 60,
                    x1, 
                    y1 - radio_estado,
                    smooth=True,
                    arrow=tk.LAST
                )

                canvas.create_text(
                    x1 + 5,
                    y1 - 75,
                    text = simbolo,
                    font=("Arial", 11, "bold")
                )

                continue

            # Distancia entre estados
            dx = x2 - x1
            dy = y2 - y1

            distancia = math.sqrt(
                dx ** 2 + dy ** 2
            )

            if distancia == 0:
                continue

            ux = dx / distancia
            uy = dy / distancia

            # Con esto impedimos que la linea entre al circulo
            inicio_x = x1 + ux * radio_estado
            inicio_y = y1 + uy * radio_estado

            fin_x = x2 - ux * radio_estado
            fin_y = y2 - uy * radio_estado

            # Curvamos las flechas en caso de 
            # transiciones en sentido contrario

            if (destino, origen) in pares:

                perpendicular_x = -uy
                perpendicular_y = ux

                desplazamiento = 30

                medio_x = (
                    (inicio_x + fin_x) / 2
                    + perpendicular_y * desplazamiento
                )

                medio_y = (
                    (inicio_y + fin_y) / 2
                    + perpendicular_y * desplazamiento
                )

                canvas.create_line(
                    inicio_x,
                    inicio_y,
                    medio_x,
                    medio_y,
                    fin_x,
                    fin_y,
                    smooth=True,
                    arrow=tk.LAST,
                    width=2
                )

                canvas.create_text(
                    (medio_x + perpendicular_x * 10) + 5,
                    medio_y + perpendicular_y * 10,
                    text=simbolo,
                    font=("Arial", 11, "bold")
                )

            else:

                canvas.create_line(
                    inicio_x,
                    inicio_y,
                    fin_x,
                    fin_y,
                    arrow=tk.LAST,
                    width=2
                )

                medio_x = (inicio_x + fin_x) / 2
                medio_y = (inicio_y + fin_y) / 2

                canvas.create_text(
                    medio_x + 5,
                    medio_y - 12,
                    text=simbolo,
                    font=("Arial", 11, "bold")
                )

            # Dibujar estados

            for estado in estados:
                x, y = posiciones[estado.id_edo]

                canvas.create_oval(
                    x - radio_estado,
                    y - radio_estado,
                    x + radio_estado,
                    y + radio_estado,
                    width = 2
                )

                # Ponemos doble circulo para los edos 
                # de aceptacion
                if estado in afn.edos_acept:

                    canvas.create_oval(
                        x - radio_estado + 5,
                        y - radio_estado + 5, 
                        x + radio_estado - 5, 
                        y + radio_estado - 5,
                        width=2
                    )

                canvas.create_text(
                    x + 5, 
                    y, 
                    text=str(estado.id_edo),
                    font=("Arial", 11, "bold")
                )

            # Flecha de estado incial

            inicial = afn.edo_ini

            x, y = posiciones[inicial.id_edo]

            canvas.create_line(
                x - radio_estado - 50,
                y,
                x - radio_estado - 3,
                y,
                arrow=tk.LAST,
                width=2
            )


    def ejecutar(self):
        self.ventana.mainloop()