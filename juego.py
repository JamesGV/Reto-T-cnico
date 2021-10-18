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

    def iniciar_juego(self): #método con el que se inicia el juego, con esto empieza una interacción con el jugador.
        self.juego_habilitado = True
        self.info()
        print('Bienvenido al juego!!!!!!\n')
        for i in range(1,6): #Se iteran 5 rondas
            if i > 1: #Para cada ronda, se le da la opción al jugador de continuar o retirarse
                if not(self.continuar_juego()):
                    break
            self.desplegar_pregunta(i) #Se invoca el método para desplegar pregunta en pantalla
            if not(self.juego_habilitado): #si el jugador se equivoca en alguna respuesta, se finaliza el juego
                break
        self.fin_juego() #se invoca el método con el que se finaliza el juego 

    def desplegar_pregunta(self,ronda): # método que despliega en cada ronda, una pregunta aleatoria de las 5 posibles
        self.ronda=ronda
        print(f'Pregunta #{self.ronda}:\n') # informa acerca de en qué ronda se encuentra el jugador
        self.posicion_aleatoria=np.random.randint(5) #Se selecciona aleatoriamente un número entre 0 y 4
        print(f'Por {100*self.ronda + self.puntos} puntos\n') #Para cada ronda los puntos posibles a ganar es: 100*número de ronda
        print(f'{self.preguntas[ronda-1,self.posicion_aleatoria,0]}\n') #Imprime en pantalla la pregunta seleccionada aleatoriamente
        for i in range(1,5): #Itera todas las respuestas de la pregunta seleccionada y las imprime en pantalla
            print(f'{self.literales[i-1]}. {self.preguntas[self.ronda-1,self.posicion_aleatoria,i]}\n')
        self.respuesta_ingresada = input('Seleccione la respuesta correcta (a, b, c, d)\n') #Recibe la respuesta ingresada por el jugador
        self.evaluar_pregunta() #Invoca este método para evaluar si la respuesta es correcta o no

    def evaluar_pregunta(self): # método que evalua si la respuesta ingresada por el jugador es correcta o no
        if self.respuesta_ingresada == self.preguntas[self.ronda-1,self.posicion_aleatoria,5]:
            print('Respuesta correcta\n')
            self.puntaje(True) #Se invoa el método donde se suma el puntaje ganado en la ronda
        else:
            print('Respuesta incorrecta\n')
            self.juego_habilitado = False
            self.puntaje(False) #Se invoca el método para asignar un puntaje de 0, debido a que el jugador se equivocó

    def puntaje(self,sumar_puntaje): #método para acumular puntos en cada ronda
        if sumar_puntaje:
            self.puntos += 100*self.ronda #si la respuesta es correcta, se suman los puntos correspondientes a cada nivel (100*número de ronda)
        else:
            self.puntos = 0 #si la respuesta es incorrecta, el puntaje final será de 0 y el juego finalizará
        print(f'Puntaje actual: {self.puntos}\n') #Imprime en pantalla el puntaje

    def fin_juego(self): #método que imprime en pantalla el final del juego, ya sea porque el jugador completó las 5 rondas, se retiró o perdió.
        print(f'Fin del juego \nSu puntaje final ha sido: {self.puntos}') #Imprime el total de puntos ganados en el juego.

    def continuar_juego(self): # método que se invoca cada vez que el jugador pasa de ronda, se le da la oportunidad de continuar o de retirarse. 
        #Si se retira, obtiene los puntos acumulados hasta el momento.
        continuar = np.NaN
        while True:
            continuar_entrada = input('Desea continuar el juego? \nIngrese "sí" para continuar. \nIngrese "no" para retirarse.\n')
            if continuar_entrada == 'sí':
                continuar = True
                break
            elif continuar_entrada == 'no':
                continuar = False
                break
        return continuar

#################### CÓDIGO DE PRUEBA ################################################################

jugador_1=juego("James García", 30) #Se instancia la clase y se crea el objeto "jugador_1".
jugador_1.configurar_juego() #Se invoca este método para configurar el juego, es decir, para ingresar todas las preguntas y respuestas.
jugador_1.iniciar_juego() #Se invoca este método para dar inicio al juego, los demás métodos de la clase se invocan internamente.
######################################################################################################
