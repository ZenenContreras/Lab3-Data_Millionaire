import tkinter as tk
from tkinter import font as tkFont
from datos import lista_preguntas
from logica import verificar_respuesta

class JuegoMillonario:
    
    #Clase para la interfaz del juego "Quién Quiere Ser Millonario".
    
    def __init__(self, master):
        self.master = master
        master.title("Quién Quiere Ser Millonario")

        # Configuraciones de estilo y fuente
        pregunta_fuente = tkFont.Font(family="Helvetica", size=14)
        opciones_fuente = tkFont.Font(family="Helvetica", size=12)
        master.configure(bg='light blue')

        # Área de la pregunta
        self.label_pregunta = tk.Label(master, text="", font=pregunta_fuente, wraplength=400, bg='light blue')
        self.label_pregunta.pack(pady=20)

        # Botones de opciones de respuesta
        self.botones_opcion = []
        for i in range(4):
            boton = tk.Button(master, text="", font=opciones_fuente, command=lambda i=i: self.seleccionar_respuesta(i))
            boton.pack(pady=5, fill=tk.X)
            self.botones_opcion.append(boton)
        
        # Área de puntaje
        self.label_puntaje = tk.Label(master, text="Puntaje: 0", font=opciones_fuente, bg='light blue')
        self.label_puntaje.pack(pady=10)

        # Inicialización de variables y primera pregunta
        self.puntaje = 0
        self.iterador_preguntas = lista_preguntas.iterar()
        self.cargar_siguiente_pregunta()

    def seleccionar_respuesta(self, indice):
        
        # Método para manejar la selección de una respuesta.
        
        es_correcta = verificar_respuesta(self.pregunta_actual, self.pregunta_actual["opciones"][indice])
        if es_correcta:
            self.puntaje += 1
            self.label_puntaje.config(text=f"Puntaje: {self.puntaje}")
            self.cargar_siguiente_pregunta()
        else:
            self.label_pregunta.config(text="Incorrecto. Fin del juego.")

    def cargar_siguiente_pregunta(self):
        
        # Método para cargar la siguiente pregunta del juego.
        
        self.pregunta_actual = next(self.iterador_preguntas, None)
        if self.pregunta_actual:
            self.label_pregunta.config(text=self.pregunta_actual["texto"])
            for i, opcion in enumerate(self.pregunta_actual["opciones"]):
                self.botones_opcion[i].config(text=opcion)
        else:
            self.label_pregunta.config(text="¡Has completado el juego!")

#  métodos adicionales
