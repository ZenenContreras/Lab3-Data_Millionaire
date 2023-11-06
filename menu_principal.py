import tkinter as tk
from tkinter import font as tkFont
from juego_millonario import JuegoMillonario
from instrucciones import Instrucciones

class MenuPrincipal:
    def __init__(self, master):
        self.master = master
        master.title("Menú Principal - Quién Quiere Ser Millonario")
        master.geometry("600x400")
        self.centrar_ventana(600, 400)  # Llamas a la función para centrar la ventana
        master.resizable(False, False)
        master.configure(bg='light blue')

        titulo_fuente = tkFont.Font(family="Helvetica", size=16, weight="bold")
        opciones_fuente = tkFont.Font(family="Helvetica", size=12)

        self.label_titulo = tk.Label(master, text="Quién Quiere Ser Millonario", font=titulo_fuente, bg='light blue')
        self.label_titulo.pack(pady=50)

        self.boton_iniciar = tk.Button(master, text="Iniciar Juego", font=opciones_fuente, command=self.iniciar_juego)
        self.boton_iniciar.pack(pady=10, fill=tk.X)

        self.boton_instrucciones = tk.Button(master, text="Instrucciones", font=opciones_fuente, command=self.mostrar_instrucciones)
        self.boton_instrucciones.pack(pady=10, fill=tk.X)

        self.boton_salir = tk.Button(master, text="Salir", font=opciones_fuente, command=self.salir)
        self.boton_salir.pack(pady=10, fill=tk.X)

    def iniciar_juego(self):
        self.master.withdraw()
        ventana_juego = tk.Toplevel(self.master)
        juego = JuegoMillonario(ventana_juego, self.regresar_al_menu, self.salir)
        ventana_juego.mainloop()

    def mostrar_instrucciones(self):
        self.master.withdraw()
        ventana_instrucciones = tk.Toplevel(self.master)
        Instrucciones(ventana_instrucciones, self.regresar_al_menu)
        
    def centrar_ventana(self, ancho, alto):
        # Calcula las coordenadas x e y para posicionar la ventana en el centro
        posicion_x = (self.master.winfo_screenwidth() // 2) - (ancho // 2)
        posicion_y = (self.master.winfo_screenheight() // 2) - (alto // 2)
        self.master.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

    def regresar_al_menu(self):
        self.master.deiconify()

    def salir(self):
        self.master.quit()


