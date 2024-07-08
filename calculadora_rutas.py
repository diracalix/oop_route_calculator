# Importamos heapq para utilizar una cola de prioridad en el algoritmo A*.
import heapq

# Definimos la clase CalculadoraRutas que contiene los métodos para calcular la ruta más corta.
class CalculadoraRutas:
    def __init__(self, mapa):
        self.mapa = mapa

    # Método heurístico para estimar la distancia entre dos puntos (distancia de Manhattan).
    def heuristica(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Método para obtener los vecinos de un nodo, validando que sean celdas transitables.
    def vecinos(self, nodo):
        fila, columna = nodo
        posibles_vecinos = [
            (fila - 1, columna), (fila + 1, columna),
            (fila, columna - 1), (fila, columna + 1)
        ]
        validos = []
        for f, c in posibles_vecinos:
            if 0 <= f < self.mapa.filas and 0 <= c < self.mapa.columnas:
                if self.mapa.mapa[f][c] in {self.mapa.LIBRE, self.mapa.AGUA, self.mapa.TEMPORAL}:
                    validos.append((f, c))
        return validos

    # Método que implementa el algoritmo A* para encontrar la ruta más corta desde el inicio hasta el fin.
    def buscar_ruta(self, inicio, fin):
        # Cola de prioridad para nodos abiertos.
        abierta = []
        heapq.heappush(abierta, (0, inicio))
        de_donde = {inicio: None}
        g_puntaje = {inicio: 0}
        f_puntaje = {inicio: self.heuristica(inicio, fin)}

        while abierta:
            _, actual = heapq.heappop(abierta)

            if actual == fin:
                ruta = []
                while actual:
                    ruta.append(actual)
                    actual = de_donde[actual]
                ruta.reverse()
                return ruta

            for vecino in self.vecinos(actual):
                puntaje_tentativo_g = g_puntaje[actual] + 1

                if vecino in g_puntaje and puntaje_tentativo_g >= g_puntaje[vecino]:
                    continue

                de_donde[vecino] = actual
                g_puntaje[vecino] = puntaje_tentativo_g
                f_puntaje[vecino] = g_puntaje[vecino] + self.heuristica(vecino, fin)
                heapq.heappush(abierta, (f_puntaje[vecino], vecino))

        return None  # Si no se encuentra una ruta, devolvemos None.
