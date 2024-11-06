from ui.maze import Maze
from ui.genotype import Genotype
from ui.geneticAlgorithm import GeneticAlgorithm
import matplotlib.pyplot as plt

def main():
    # Creamos un laberinto de 10x10
    laberinto = Maze(10, 10, start=(1, 1), end=(10, 10))

    """
    #Laberinto fácil (menos obstáculos)
    laberinto_facil = Maze(10, 10, start=(1, 1), end=(10, 10))
    laberinto_facil.add_obstacle(3, 3)
    laberinto_facil.add_obstacle(4, 4)
    """
    
    #Laberinto medio
    laberinto.add_obstacle(3, 3)
    laberinto.add_obstacle(4, 4)
    laberinto.add_obstacle(6, 6)
    laberinto.add_obstacle(7, 7)
    laberinto.add_obstacle(8, 1)
    laberinto.add_obstacle(9, 2)
    """
    # Laberinto difícil (más obstáculos)
    for i in range(1, 9):
        for j in range(1, 9):
          if (i + j) % 2 == 0:
               laberinto.add_obstacle(i, j)
    """
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

    # Crear el algoritmo genético con la población de tamaño 400
    ga = GeneticAlgorithm(population_size=400, maze=laberinto, crossover_rate=0.9, mutation_rate=0.08)

    # Ejecutamos el algoritmo genético
    generations = 100  # Número de generaciones
    ga.evolve(generations)
    laberinto.display()

    # Retornamos los objetos configurados
    return laberinto, ga

def prueba_algoritmo(laberinto, ga, generations=50):
    # Variables para almacenar los resultados
    best_fitness_history = []
    success_routes = 0

    # Ejecutar el algoritmo a través de generaciones adicionales
    for generation in range(generations):
        ga.evolve(1)  # Evolucionar una generación adicional para pruebas
        
        # Almacenar el mejor resultado de la generación actual
        best_fitness = ga.population[0].fitness
        best_fitness_history.append(best_fitness)
        
        # Verificar si se encontró una ruta exitosa
        if ga.solution_found():
            success_routes += 1
    
    # Gráfica de la evolución de la aptitud
    plt.figure(figsize=(10, 5))
    plt.plot(best_fitness_history, label="Mejor aptitud")
    plt.xlabel("Generaciones")
    plt.ylabel("Aptitud")
    plt.title("Evolución de la aptitud a través de generaciones")
    plt.legend()
    plt.grid()
    plt.show()

    # Mostrar resultados finales
    print(f"Rutas exitosas encontradas: {success_routes}/{generations}")
    print(f"Aptitud máxima alcanzada: {best_fitness_history[-1]}")

if __name__ == '__main__':
    laberinto, ga = main()
    prueba_algoritmo(laberinto, ga)