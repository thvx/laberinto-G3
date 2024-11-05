from ui.maze import Maze


def main():
    # Creamos un laberinto de 10x10
    laberinto = Maze(10, 10, start=(1, 1), end=(10, 10))

    # Agregamos obstáculos en ciertas posiciones
    laberinto.add_obstacle(3, 3)
    laberinto.add_obstacle(3, 4)
    laberinto.add_obstacle(4, 4)
    laberinto.add_obstacle(5, 5)

    # Verificamos si una posición está libre
    print(laberinto.is_free(1, 1))
    print(laberinto.is_free(3, 3))

    # Obtener la posición de inicio y fin
    print(laberinto.get_start_position())
    print(laberinto.get_end_position())

    # Visualizar el laberinto
    laberinto.display()


if __name__ == '__main__':
    main()