import numpy as np

class juego:
    def __init__(self, nombre, edad): #Constructor de la clase
        self.nombre = nombre #Nombre del jugador
        self.edad = edad #Edad del jugador
        self.puntos = 0 #Puntos de inicio para el juego
        self.posicion_aleatoria=np.NaN #Con esta variable se definirá una posición aleatoria para seleccionar la pregunta de cada ronda
        self.ronda=np.NaN #Esta variable contiene el número de la ronda actual durante el juego
        self.respuesta_ingresada=np.NaN #Almacena la respuesta ingresada por el jugador a través del teclado
        self.juego_habilitado=False  #Determina si el juego sigue activo, se deshabilita por ejemplo cuando el jugador se equivoca, esto inidcará que el juego deberá terminar
        self.literales=['a','b','c','d'] #Lista con los literales de las respuestas, está se iterará en algunos métodos de esta clase 
        self.preguntas = np.empty(shape=(5,5,6), dtype='U100') #Se crea un arreglo vacío de 3 dimensiones (5 rondas, 5 preguntas por ronda,6 elementos 
        #por fila: 1 pregunta, 4 respuestas y el literal que corresponde a la respuesta correcta)
        