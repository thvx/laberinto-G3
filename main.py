from maze import Maze
from genetic_algorithm import GeneticAlgorithm

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
    ]
    
    maze = Maze(grid)
    ga = GeneticAlgorithm(maze)
    ga.run(generations=100)  # Ejecutar por 100 generaciones
    best_path = min(ga.population, key=ga.fitness)
    maze.display(best_path)  # Visualiza el mejor camino encontrado
    ga.plot_fitness()  # Muestra la gráfica de evolución de la aptitud