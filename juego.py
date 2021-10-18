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

        def info(self): #método que despliega información referente al jugador
            print(f'Nombre del jugador: {self.nombre}\n') #Imprimir en pantalla el nombre del jugador
            print(f'Edad del jugador: {self.edad}\n') #Imprime en pantalla la edad del juigador

    def configurar_juego(self): #método para configurar el juego, acá se ingresan todas las preguntas y respuestas. Se va recorriendo el arreglo
        #y se va rellenando con las preguntas y respuestas
        for ronda in range(0,5): #Itera cada ronda del juego (5 rondas)
            print(f'Preguntas de la ronda {ronda+1}\n')
            for pregunta in range(0,5): #Itera todas las preguntas de una ronda (5 preguntas por ronda)
                self.preguntas[ronda,pregunta,0]=input(f'Ingrese la pregunta # {pregunta+1} (Máximo 100 caracteres):\n')
                for respuesta in range(0,4): #Itera todas las respuestas de una pregunta (4 respuestas por pregunta)
                    self.preguntas[ronda,pregunta,respuesta+1]=input(f'Ingrese la respuesta {self.literales[respuesta]} (Máximo 100 caracteres):\n')
                self.preguntas[ronda,pregunta,5] = input('Ingrese el literal de respuesta correcta (a,b,c,d):\n') #Para cada pregunta, se debe ingresar
                #el literal de la respuesta correcta
        print(self.preguntas)       # Al final de la configuración, se imprime en pantalla el arreglo de 3 dimensiones con todas las preguntas 
        #y respuestas configuradas.  