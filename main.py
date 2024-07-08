# Importamos las clases Mapa y CalculadoraRutas.
from mapa import Mapa
from calculadora_rutas import CalculadoraRutas
# Importamos las excepciones personalizadas.
from exceptions import ObstaculoEnInicioFin, TipoObstaculoInvalido

def main():
    # Solicitamos las dimensiones del mapa al usuario.
    filas = int(input("Ingrese el número de filas del laberinto: "))
    columnas = int(input("Ingrese el número de columnas del laberinto: "))
    
    # Creamos una instancia de Mapa.
    mapa = Mapa(filas, columnas)
    mapa.imprimir_mapa()  # Mostramos el mapa vacío.

    # Solicitamos y establecemos las coordenadas del punto de inicio.
    print("Ingrese las coordenadas del punto de inicio:")
    inicio = mapa.ingresar_coordenadas()
    mapa.inicio = inicio

    # Solicitamos y establecemos las coordenadas del punto de destino.
    print("Ingrese las coordenadas del punto de destino:")
    fin = mapa.ingresar_coordenadas()
    mapa.fin = fin

    # Proceso para agregar obstáculos en el mapa.
    print("Agregar obstáculos:")
    while True:
        agregar_obstaculo_opcion = input("¿Desea agregar un obstáculo? (s/n): ")
        if agregar_obstaculo_opcion.lower() != 's':
            break
        try:
            x, y = mapa.ingresar_coordenadas()  # Obtenemos las coordenadas del obstáculo.
            tipo = int(input("Ingrese el tipo de obstáculo (1: permanente, 2: agua, 3: temporal): "))
            mapa.agregar_obstaculo(x, y, tipo)  # Añadimos el obstáculo al mapa.
            mapa.imprimir_mapa()  # Mostramos el mapa actualizado.
        except (ObstaculoEnInicioFin, TipoObstaculoInvalido) as e:
            print(e)

    # Creamos una instancia de CalculadoraRutas y buscamos la ruta más corta.
    calculadora = CalculadoraRutas(mapa)
    ruta = calculadora.buscar_ruta(inicio, fin)
    
    # Mostramos el resultado de la búsqueda de la ruta.
    if ruta:
        print("Ruta más corta encontrada:")
        mapa.imprimir_mapa(ruta)  # Mostramos el mapa con la ruta.
    else:
        print("No se encontró una ruta válida.")  # Mensaje en caso de no encontrar ruta.

# Ejecutamos la función principal si el script se ejecuta directamente.
if __name__ == "__main__":
    main()
