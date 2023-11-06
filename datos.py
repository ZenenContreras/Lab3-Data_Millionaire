class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        if not self.primero:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            nuevo.anterior = self.ultimo
            self.ultimo = nuevo

    def iterar(self):
        actual = self.primero
        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

lista_preguntas = ListaDoble()
lista_preguntas.agregar({
    "texto": "¿Cuál es la capital de Francia?",
    "opciones": ["Madrid", "Berlín", "París", "Londres"],
    "respuesta": "París"
})

lista_preguntas.agregar({
    "texto": "¿Cuál es el símbolo químico del oro?",
    "opciones": ["Ag", "Au", "Fe", "O"],
    "respuesta": "Au"
})

lista_preguntas.agregar({
    "texto": "¿Cuál es el océano más grande del mundo?",
    "opciones": ["Océano Pacífico", "Océano Índico", "Océano Antártico", "Océano Atlántico"],
    "respuesta": "Océano Pacífico"
})

lista_preguntas.agregar({
    "texto": "¿Como se llama el libro sagrado de la cultura Islámica?",
    "opciones": ["Talmud", "Torá", "Corán", "Kojiki"],
    "respuesta": "Corán"
})

lista_preguntas.agregar({
    "texto": "¿Cuál de estos planetas está más cercano al sol?",
    "opciones": ["Neptuno", "Mercurio", "Saturno", "Tierra"],
    "respuesta": "Mercurio"
})

lista_preguntas.agregar({
    "texto": "¿Quién es conocido como el padre de la teoría de la relatividad?",
    "opciones": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Stephen Hawking"],
    "respuesta": "Albert Einstein"
})

lista_preguntas.agregar({
    "texto": "¿Qué trilogía de las películas basadas en los cómics de Marvel recaudó más dinero en taquilla?",
    "opciones": ["Thor", "Capitán América", "Iron Man", "Wolverine"],
    "respuesta": "Capitán América"
})

lista_preguntas.agregar({
    "texto": "¿Cuál es el órgano más grande del cuerpo humano?",
    "opciones": ["Corazón", "Hígado", "Piel", "Cerebro"],
    "respuesta": "Piel"
})

lista_preguntas.agregar({
    "texto": "¿Qué filósofo escribió 'La República'?",
    "opciones": ["Aristóteles", "Sócrates", "Platón", "Descartes"],
    "respuesta": "Platón"
})

lista_preguntas.agregar({
    "texto": "¿Qué lenguaje de programación es conocido por su eficiencia y uso en sistemas operativos y videojuegos?",
    "opciones": ["Python", "Java", "C++", "JavaScript"],
    "respuesta": "C++"
})

lista_preguntas.agregar({
    "texto": "¿Cuál fue el primer país en industrializarse?",
    "opciones": ["Estados Unidos", "Alemania", "Reino Unido", "Francia"],
    "respuesta": "Reino Unido"
})

lista_preguntas.agregar({
    "texto": "La vara que suele llevar como cetro el Dios de la mitología romana Baco se llama:",
    "opciones": ["Tirso", "Talión", "Vareta", "Mástil"],
    "respuesta": "Tirso"
})

lista_preguntas.agregar({
    "texto": "¿Cuál es el número primo más grande conocido hasta la fecha?",
    "opciones": ["2^74207281 - 1", "2^77232917 - 1", "2^82589933 - 1", "2^43112609 - 1"],
    "respuesta": "2^82589933 - 1"
})

lista_preguntas.agregar({
    "texto": "¿Cuál es el nombre de la hipótesis que sugiere que el universo podría tener más de tres dimensiones espaciales?",
    "opciones": ["Teoría de la Relatividad", "Hipótesis del Multiverso", "Teoría de Cuerdas", "Principio Cosmológico"],
    "respuesta": "Teoría de Cuerdas"
})

lista_preguntas.agregar({
    "texto": "¿Qué enfermedad tenía el legendario astrofísico Stephen Hawking?",
    "opciones": ["Enfermedad de Addison", "Progeria de Hutchinson-Gilford", "Esclerosis Lateral Amiotrófica", "Síndrome de Marfan"],
    "respuesta": "Esclerosis Lateral Amiotrófica"
})



