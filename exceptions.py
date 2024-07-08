# Definimos una clase base para todas las excepciones personalizadas relacionadas con el mapa.
class MapaException(Exception):
    pass

# Excepción para coordenadas no válidas.
class CoordenadasInvalidas(MapaException):
    def __init__(self, mensaje="Coordenadas no válidas o punto no transitable. Intente de nuevo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Excepción para intentar colocar un obstáculo en el punto de inicio o fin.
class ObstaculoEnInicioFin(MapaException):
    def __init__(self, mensaje="No se puede colocar un obstáculo en el punto de inicio o fin."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Excepción para tipo de obstáculo no válido.
class TipoObstaculoInvalido(MapaException):
    def __init__(self, mensaje="Tipo de obstáculo no válido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
