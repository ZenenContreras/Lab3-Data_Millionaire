import random
import tkinter as tk
from tkinter import Image, PhotoImage, font as tkFont
from datos import lista_preguntas, pila_preguntas
from findeljuego import FinDelJuego
from ganador import Ganaste
from logica import verificar_respuesta

class JuegoMillonario:
    
    def __init__(self, master, regresar_menu_principal, salir_aplicacion):
        
        self.master = master
        self.regresar_menu_principal = regresar_menu_principal
        self.salir_aplicacion = salir_aplicacion
        master.title("Quién Quiere Ser Millonario")
        master.geometry("600x500")
        self.centrar_ventana(600, 500)
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

        # Inicializar el temporizador y crear el label para mostrarlo
        self.tiempo_restante = 30
        self.label_temporizador = tk.Label(master, text="Tiempo restante: 30", font=opciones_fuente, bg='light blue')
        self.label_temporizador.pack(pady=10)

        self.puntaje = 0
        self.comodin_usado = False
        self.usar_pila = not pila_preguntas.esta_vacia()
        self.iterador_lista_preguntas = lista_preguntas.iterar()
        self.cargar_siguiente_pregunta()

        self.imagen_comodin = PhotoImage(file="imagenes/50.png")  # Usamos la imagen proporcionada por el usuario
        self.boton_comodin_50_50 = tk.Button(master, image=self.imagen_comodin, command=self.comodin_50_50)
        self.boton_comodin_50_50.pack(side=tk.TOP, anchor="center", pady=30)

        # Atributo para rastrear si el comodín ha sido usado
        self.comodin_usado = False

    def comodin_50_50(self):
        if self.comodin_usado:
            # Si el comodín ya se ha usado, no hacer nada
            return
        else:
            # Encuentra índices de respuestas incorrectas
            indices_incorrectos = [i for i, opcion in enumerate(self.pregunta_actual["opciones"])
                                   if opcion != self.pregunta_actual["respuesta"]]
            
            # Selecciona dos índices al azar para eliminar
            indices_a_eliminar = random.sample(indices_incorrectos, 2)

            # Oculta los botones de las respuestas incorrectas
            for indice in indices_a_eliminar:
                self.botones_opcion[indice].pack_forget()

            # Desactiva el botón del comodín para que no se pueda usar de nuevo
            self.boton_comodin_50_50.config(state=tk.DISABLED)
            self.comodin_usado = True

    def centrar_ventana(self, ancho, alto):
        posicion_x = (self.master.winfo_screenwidth() // 2) - (ancho // 2)
        posicion_y = (self.master.winfo_screenheight() // 2) - (alto // 2)
        self.master.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

    def seleccionar_respuesta(self, indice):
        es_correcta = verificar_respuesta(self.pregunta_actual, self.pregunta_actual["opciones"][indice])
        if es_correcta:
            self.puntaje += 100000
            self.label_puntaje.config(text=f"Puntaje: {self.puntaje}")
            self.cargar_siguiente_pregunta()
        else:
            self.mostrar_ventana_final("Respuesta Incorrecta!")

    def cargar_siguiente_pregunta(self):
        # Cancelar el temporizador existente si hay uno
        if hasattr(self, 'temporizador_id'):
            self.master.after_cancel(self.temporizador_id)
        self.temporizador_id = None
        # Obtener la siguiente pregunta de la pila o de la lista, dependiendo del estado de 'self.usar_pila'
        if self.usar_pila:
            self.pregunta_actual = pila_preguntas.desapilar()
            if self.pregunta_actual is None:
                self.usar_pila = False
                self.pregunta_actual = next(self.iterador_lista_preguntas, None)
        else:
            self.pregunta_actual = next(self.iterador_lista_preguntas, None)

        # Restablecer todos los botones de opciones en caso de que hayan sido ocultados por el comodín 50/50
        for boton in self.botones_opcion:
            boton.pack()
            boton.config(state=tk.NORMAL)

        # Restablecer el botón del comodín 50/50 si se había usado
        if self.comodin_usado:
            self.boton_comodin_50_50.config(state=tk.NORMAL)
            self.boton_comodin_50_50.config(state=tk.DISABLED)
            self.comodin_usado = True
        # Si hay una pregunta actual, actualiza la interfaz con la nueva pregunta y opciones
        if self.pregunta_actual:
            self.label_pregunta.config(text=self.pregunta_actual["texto"])
            for i, opcion in enumerate(self.pregunta_actual["opciones"]):
                self.botones_opcion[i].config(text=opcion)
            self.tiempo_restante = 30
            self.actualizar_temporizador()
        else:
            self.finalizar_juego("¡Has ganado el premio mayor!")

    def actualizar_temporizador(self):
        if self.tiempo_restante > 0:
            self.label_temporizador.config(text=f"Tiempo restante: {self.tiempo_restante}")
            self.tiempo_restante -= 1
            self.temporizador_id = self.master.after(1000, self.actualizar_temporizador)
        else:
            self.mostrar_ventana_final("¡Tiempo agotado!")

    def mostrar_ventana_final(self, mensaje):
        if hasattr(self, 'temporizador_id'):
            self.master.after_cancel(self.temporizador_id)
        self.master.withdraw()
        ventana_final = tk.Toplevel(self.master)
        FinDelJuego(ventana_final, self.puntaje, self.regresar_menu_principal, self.salir_aplicacion, mensaje)

    def finalizar_juego(self, mensaje):
        if hasattr(self, 'temporizador_id'):
            self.master.after_cancel(self.temporizador_id)
        self.master.withdraw()
        ventana_final = tk.Toplevel(self.master)
        Ganaste(ventana_final, self.puntaje, self.regresar_menu_principal, self.salir_aplicacion, mensaje)

