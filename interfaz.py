import tkinter as tk
import afn as AFN
from tkinter import messagebox, ttk

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
            width=25
        )

        boton_union.pack(pady=5)

        boton_concatenar = tk.Button(
            self.ventana,
            text="Concatenar AFN",
            width=25
        )

        boton_concatenar.pack(pady=5)

        boton_pos = tk.Button(
            self.ventana,
            text="Cerradura positiva (+)",
            width=25
        )

        boton_pos.pack(pady=5)

        boton_kleene = tk.Button(
            self.ventana,
            text="Cerradura de Kleene (*)",
            width=25
        )

        boton_kleene.pack(pady=5)

        boton_opcional = tk.Button(
            self.ventana,
            text="opcional (?)",
            width=25
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
        ventana.geometry("650x650")

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



    def ejecutar(self):
        self.ventana.mainloop()