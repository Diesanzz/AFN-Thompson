import tkinter as tk
from tkinter import messagebox

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
            width=25
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

    def ejecutar(self):
        self.ventana.mainloop()