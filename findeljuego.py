import tkinter as tk
from tkinter import font as tkFont


class FinDelJuego:
    def __init__(self, master, puntaje, regresar_menu_principal, salir_aplicacion):
        self.master = master
        self.regresar_menu_principal = regresar_menu_principal
        self.salir_aplicacion = salir_aplicacion
        master.title("Fin del Juego")
        master.geometry("600x400")
        self.centrar_ventana(600, 400)  # Llamas a la función para centrar la ventana
        master.resizable(False, False)
        master.configure(bg='light blue')

        resultado_fuente = tkFont.Font(family="Helvetica", size=14)
        botones_fuente = tkFont.Font(family="Helvetica", size=12)

        self.label_resultado = tk.Label(master, text=f"Puntaje obtenido: {puntaje}", font=resultado_fuente, bg='light blue')
        self.label_resultado.pack(pady=20)

        self.boton_menu_principal = tk.Button(master, text="Menú Principal", font=botones_fuente, command=self.volver_al_menu)
        self.boton_menu_principal.pack(pady=5, fill=tk.X)

        self.boton_salir = tk.Button(master, text="Salir", font=botones_fuente, command=self.salir)
        self.boton_salir.pack(pady=5, fill=tk.X)

    def volver_al_menu(self):
        self.master.destroy()
        self.regresar_menu_principal()

    def centrar_ventana(self, ancho, alto):
        # Calcula las coordenadas x e y para posicionar la ventana en el centro
        posicion_x = (self.master.winfo_screenwidth() // 2) - (ancho // 2)
        posicion_y = (self.master.winfo_screenheight() // 2) - (alto // 2)
        self.master.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

    def salir(self):
        self.master.destroy()
        self.salir_aplicacion()
