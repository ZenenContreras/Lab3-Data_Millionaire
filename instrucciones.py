import tkinter as tk
from tkinter import font as tkFont

class Instrucciones:
    def __init__(self, master, regresar_menu_principal):
        self.master = master
        self.regresar_menu_principal = regresar_menu_principal
        master.title("Instrucciones")
        master.geometry("600x600")
        self.centrar_ventana(600, 600)  # Llamas a la función para centrar la ventana
        master.resizable(False, False)
        master.configure(bg='light blue')

        # Fuentes
        titulo_fuente = tkFont.Font(family="Helvetica", size=20, weight="bold")
        instrucciones_fuente = tkFont.Font(family="Helvetica", size=12)
        negrita_fuente = tkFont.Font(family="Helvetica", size=12, weight="bold")
        botones_fuente = tkFont.Font(family="Helvetica", size=12)

        # Widget de texto para las instrucciones
        self.texto_instrucciones = tk.Text(master, font=instrucciones_fuente, bg='light blue', wrap=tk.WORD, borderwidth=0)
        self.texto_instrucciones.tag_configure("centrado", justify='center')
        self.texto_instrucciones.tag_configure("negrita", font=negrita_fuente)
        self.texto_instrucciones.tag_configure("titulo", font=titulo_fuente)

        # Insertar título y aplicar formato centrado
        self.texto_instrucciones.insert(tk.END, "Instrucciones de ¿Quién quiere ser Millonario?\n\n", "titulo")
        self.texto_instrucciones.tag_add("centrado", "1.0", "end")

        # Instrucciones con formato centrado y negritas en los números
        instrucciones = [
            ("1. Inicio del Juego:\n", "negrita"),
            ("Comienza con preguntas fáciles que aumentan en dificultad y valor monetario.\n\n", ""),
            ("2. Preguntas:\n", "negrita"),
            ("Se presenta una pregunta con cuatro opciones de respuesta; solo una es correcta.\n", ""),
            ("Debes responder correctamente para avanzar a la siguiente pregunta.\n\n", ""),
            ("3. Comodines:\n", "negrita"),
            ("Utiliza comodines (50:50 y Pregunta al público) para ayudarte con respuestas difíciles.\n\n", ""),
            ("4. Respuesta Incorrecta:\n", "negrita"),
            ("Si respondes incorrectamente, el Juego termina y te llevas el dinero del último punto de seguridad alcanzado.\n\n", ""),
            ("5. Ganar el Juego:\n", "negrita"),
            ("Responde todas las preguntas correctamente para ganar el premio máximo.\n", "")
        ]

        # Insertar instrucciones con negritas en los números y centrar todo el texto
        for texto, tag in instrucciones:
            self.texto_instrucciones.insert(tk.END, texto, tag)
        self.texto_instrucciones.tag_add("centrado", "1.0", "end")

        # Configurar y deshabilitar edición
        self.texto_instrucciones.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        self.texto_instrucciones.config(state="disabled")

        # Botón de regreso al menú principal
        self.boton_menu_principal = tk.Button(master, text="Menú Principal", font=botones_fuente, command=self.volver_al_menu)
        self.boton_menu_principal.pack(pady=10, fill=tk.X)

    def centrar_ventana(self, ancho, alto):
        # Calcula las coordenadas x e y para posicionar la ventana en el centro
        posicion_x = (self.master.winfo_screenwidth() // 2) - (ancho // 2)
        posicion_y = (self.master.winfo_screenheight() // 2) - (alto // 2)
        self.master.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

    def volver_al_menu(self):
        self.master.destroy()
        self.regresar_menu_principal()




