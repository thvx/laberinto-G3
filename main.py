from ui.maze import Maze
from ui.genotype import Genotype


def main():
    # Creamos un laberinto de 10x10
    laberinto = Maze(10, 10, start=(1, 1), end=(10, 10))

    # Agregamos obstáculos en ciertas posiciones
    laberinto.add_obstacle(3, 3)
    laberinto.add_obstacle(3, 4)
    laberinto.add_obstacle(4, 4)
    laberinto.add_obstacle(5, 5)

    # Crear un genotipo con el laberinto
    gen = Genotype(laberinto)
    gen.calculate_fitness()
    print("Genotipo:", gen)

    # Aplicar mutación
    gen.mutate(mutation_rate=0.1)
    print("Genotipo después de mutación:", gen)

    # Crear otro genotipo y hacer cruce
    gen2 = Genotype(laberinto)
    gen3 = gen.crossover(gen2)
    gen3.calculate_fitness()
    print("Genotipo resultado de cruce:", gen3)


if __name__ == '__main__':
    main()