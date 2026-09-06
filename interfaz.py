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
        pass

    def ejecutar(self):
        self.ventana.mainloop()