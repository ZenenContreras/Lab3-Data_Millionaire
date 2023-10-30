import tkinter as tk
from tkinter import font as tkFont
from juego_millonario import JuegoMillonario

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Menú Principal - Quién Quiere Ser Millonario")

        # Estilos y fuentes
        titulo_fuente = tkFont.Font(family="Helvetica", size=16, weight="bold")
        opciones_fuente = tkFont.Font(family="Helvetica", size=12)
        master.configure(bg='light blue')

        # Título del menú
        self.label_titulo = tk.Label(master, text="Bienvenido a Quién Quiere Ser Millonario", font=titulo_fuente, bg='navy', fg='white')
        self.label_titulo.pack(pady=20, fill=tk.X)

        # Botones del menú
        self.boton_jugar = tk.Button(master, text="Jugar", font=opciones_fuente, command=self.iniciar_juego)
        self.boton_jugar.pack(pady=10, fill=tk.X)

        self.boton_instrucciones = tk.Button(master, text="Instrucciones", font=opciones_fuente, command=self.ver_instrucciones)
        self.boton_instrucciones.pack(pady=10, fill=tk.X)

        self.boton_salir = tk.Button(master, text="Salir", font=opciones_fuente, command=master.quit)
        self.boton_salir.pack(pady=10, fill=tk.X)

    def iniciar_juego(self):
        
        # Método para iniciar el juego.
        
        self.master.withdraw()
        ventana_juego = tk.Toplevel(self.master)
        juego = JuegoMillonario(ventana_juego)

    def ver_instrucciones(self):
        
        # Método para mostrar las instrucciones del juego.
        
        pass  # la lógica para mostrar las instrucciones
