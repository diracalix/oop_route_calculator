# Importamos las excepciones personalizadas desde el archivo exceptions.py.
from exceptions import CoordenadasInvalidas, ObstaculoEnInicioFin, TipoObstaculoInvalido

# Definimos la clase Mapa que maneja la creación y manipulación del mapa.
class Mapa:
    # Constantes para los diferentes tipos de celdas en el mapa.
    LIBRE = 0
    PERMANENTE = 1
    AGUA = 2
    TEMPORAL = 3

    # Inicializamos el mapa con filas, columnas y una estructura de datos que representa el mapa.
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.mapa = self.crear_mapa()
        self.inicio = None
        self.fin = None

    # Método para crear un mapa vacío con las dimensiones especificadas.
    def crear_mapa(self):
        return [[self.LIBRE for _ in range(self.columnas)] for _ in range(self.filas)]

    # Método para imprimir el mapa en la consola, incluyendo ruta, inicio y fin.
    def imprimir_mapa(self, ruta=[]):
        simbolos = {self.LIBRE: '.', self.PERMANENTE: 'X', self.AGUA: 'A', self.TEMPORAL: 'T'}
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                if (i, j) == self.inicio:
                    print("I", end=" ")  # Punto de inicio marcado con 'I'
                elif (i, j) == self.fin:
                    print("S", end=" ")  # Punto de fin marcado con 'S'
                elif (i, j) in ruta:
                    print("*", end=" ")  # Ruta encontrada marcada con '*'
                else:
                    print(simbolos.get(self.mapa[i][j], '?'), end=" ")  # Usar símbolos definidos o '?' por defecto
            print()
        print()

    # Método para ingresar coordenadas del usuario y validar que sean válidas.
    def ingresar_coordenadas(self):
        while True:
            try:
                x, y = map(int, input("Ingrese las coordenadas (X,Y): ").split(','))
                x -= 1  # Ajustamos la coordenada x
                y -= 1  # Ajustamos la coordenada y
                # Verifica si las coordenadas son válidas y el punto es transitable.
                if 0 <= x < len(self.mapa) and 0 <= y < len(self.mapa[0]) and self.mapa[x][y] == self.LIBRE:
                    return x, y
                else:
                    raise CoordenadasInvalidas()
            except ValueError:
                print("Entrada no válida. Asegúrese de ingresar dos números enteros separados por una coma.")
            except CoordenadasInvalidas as e:
                print(e)

    # Método para agregar un obstáculo en el mapa en las coordenadas dadas.
    def agregar_obstaculo(self, x, y, tipo):
        if (x, y) == self.inicio or (x, y) == self.fin:
            raise ObstaculoEnInicioFin()
        if tipo not in [self.PERMANENTE, self.AGUA, self.TEMPORAL]:
            raise TipoObstaculoInvalido()
        self.mapa[x][y] = tipo
