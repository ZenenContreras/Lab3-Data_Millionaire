import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
from datos import lista_preguntas
from findeljuego import FinDelJuego
from logica import verificar_respuesta

class JuegoMillonario:
    
    def __init__(self, master, regresar_menu_principal, salir_aplicacion):
        self.master = master
        self.regresar_menu_principal = regresar_menu_principal
        self.salir_aplicacion = salir_aplicacion
        master.title("Quién Quiere Ser Millonario")
        master.geometry("600x400")
        self.centrar_ventana(600, 400)  # Llamas a la función para centrar la ventana
        master.resizable(False, False)
        master.configure(bg='light blue')

        pregunta_fuente = tkFont.Font(family="Helvetica", size=14)
        opciones_fuente = tkFont.Font(family="Helvetica", size=12)

        self.label_pregunta = tk.Label(master, text="", font=pregunta_fuente, wraplength=400, bg='light blue')
        self.label_pregunta.pack(pady=20)

        self.botones_opcion = []
        for i in range(4):
            boton = tk.Button(master, text="", font=opciones_fuente, command=lambda i=i: self.seleccionar_respuesta(i))
            boton.pack(pady=5, fill=tk.X)
            self.botones_opcion.append(boton)

        self.label_puntaje = tk.Label(master, text="Puntaje: 0", font=opciones_fuente, bg='light blue')
        self.label_puntaje.pack(pady=10)
    
        self.puntaje = 0
        self.iterador_preguntas = lista_preguntas.iterar()
        self.cargar_siguiente_pregunta()

        self.tiempo_restante = 30
        self.label_temporizador = tk.Label(master, text=f"Tiempo restante: {self.tiempo_restante}", font=("Helvetica", 12), bg='light blue')
        self.label_temporizador.pack(pady=10)
        self.temporizador_id = None
        self.iniciar_temporizador()

    def centrar_ventana(self, ancho, alto):
        # Calcula las coordenadas x e y para posicionar la ventana en el centro
        posicion_x = (self.master.winfo_screenwidth() // 2) - (ancho // 2)
        posicion_y = (self.master.winfo_screenheight() // 2) - (alto // 2)
        self.master.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

    def iniciar_temporizador(self):
        self.tiempo_restante = 30
        self.actualizar_temporizador()

    def actualizar_temporizador(self):
        if self.tiempo_restante > 0:
            self.label_temporizador.config(text=f"Tiempo restante: {self.tiempo_restante} segundos")
            self.tiempo_restante -= 1
            self.temporizador_id = self.master.after(1000, self.actualizar_temporizador)
        else:
            self.mostrar_ventana_final()

    def seleccionar_respuesta(self, indice):
        es_correcta = verificar_respuesta(self.pregunta_actual, self.pregunta_actual["opciones"][indice])
        if es_correcta:
            self.puntaje += 1
            self.label_puntaje.config(text=f"Puntaje: {self.puntaje}")
            self.cargar_siguiente_pregunta()
        else:
            self.mostrar_ventana_final()
    

    def finalizar_juego(self):
        if self.temporizador_id is not None:
            self.master.after_cancel(self.temporizador_id)
            self.temporizador_id = None
        # Llamamos directamente a mostrar la ventana final sin mostrar mensaje de tiempo agotado
        self.mostrar_ventana_final()

    def mostrar_ventana_final(self, mensaje):
        self.master.withdraw()
        ventana_final = tk.Toplevel(self.master)
        FinDelJuego(ventana_final, self.puntaje, self.regresar_menu_principal, self.salir_aplicacion)

    def cargar_siguiente_pregunta(self):
        self.pregunta_actual = next(self.iterador_preguntas, None)
        if self.pregunta_actual:
            self.label_pregunta.config(text=self.pregunta_actual["texto"])
            for i, opcion in enumerate(self.pregunta_actual["opciones"]):
                self.botones_opcion[i].config(text=opcion)
            self.iniciar_temporizador()
        else:
            self.finalizar_juego()
