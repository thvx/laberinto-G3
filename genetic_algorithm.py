# genetic_algorithm.py
import random
import matplotlib.pyplot as plt

class GeneticAlgorithm:
    def __init__(self, maze, population_size=100, mutation_rate=0.02):
        self.maze = maze
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.population = self.initialize_population()
        self.best_fitness_history = []  # Para almacenar la mejor aptitud en cada generación

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            path = self.generate_random_path()
            population.append(path)
        return population

    def generate_random_path(self):
        path = [self.maze.start]
        while path[-1] != self.maze.end:
            x, y = path[-1]
            next_moves = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
            next_moves = [
                move for move in next_moves 
                if (0 <= move[0] < self.maze.grid.shape[0] and 
                    0 <= move[1] < self.maze.grid.shape[1] and 
                    self.maze.is_free(move) and 
                    move not in path)
            ]
            if not next_moves:
                break  # No se puede mover más
            path.append(random.choice(next_moves))
        return path

    def fitness(self, path):
        if not path or path[-1] != self.maze.end:
            return float('inf')  # Penaliza caminos que no llegan al final
        length = len(path)
        turns = sum(1 for i in range(1, len(path) - 1) if path[i - 1][0] != path[i][0] and path[i][1] != path[i][1])
        return length + turns  # Penaliza por longitud y giros

    def select(self):
        weighted_population = [(self.fitness(path), path) for path in self.population]
        weighted_population.sort(key=lambda x: x[0])
        return [path for _, path in weighted_population[:self.population_size // 2]]

    def crossover(self, parent1, parent2):
        split = random.randint(1, min(len(parent1), len(parent2)) - 1)
        child = parent1[:split] + parent2[split:]
        return child

    def mutate(self, path):
        if random.random() < self.mutation_rate:
            index = random.randint(0, len(path) - 1)
            new_move = self.generate_random_path()  # Generar un nuevo camino
            if new_move:
                path[index] = new_move[0]  # Reemplazar un movimiento
        return path

    def evolve(self):
        selected = self.select()
        next_generation = []
        while len(next_generation) < self.population_size:
            parent1, parent2 = random.sample(selected, 2)
            child = self.crossover(parent1, parent2)
            child = self.mutate(child)
            next_generation.append(child)
        self.population = next_generation

    def run(self, generations=500):
        for generation in range(generations):
            self.evolve()
            best_path = min(self.population, key=self.fitness)
            best_fitness = self.fitness(best_path)
            self.best_fitness_history.append(best_fitness)

            # Imprimir la generación y la mejor aptitud
            print(f'Generación {generation}: Mejor Aptitud = {best_fitness}')
            
            # Imprimir la aptitud de la población
            population_fitness = [self.fitness(path) for path in self.population]
            print(f'Aptitud de la población: {population_fitness}')

            # Imprimir estadísticas adicionales
            print(f'Media de aptitud: {sum(population_fitness)/len(population_fitness)}')
            print(f'Máxima aptitud: {max(population_fitness)}')
            print(f'Mínima aptitud: {min(population_fitness)}')

            x = 18 
            z = 16 
            y = float('inf') 

            count_x = population_fitness.count(x)
            count_z = population_fitness.count(z)
            count_y = population_fitness.count(y)

            print(f'Cantidad de aptitudes con valor {x} o {z}: {count_x} y {count_z}')
            print(f'Cantidad de aptitudes con valor {y}: {count_y}')
    
    def plot_fitness(self):
        plt.plot(self.best_fitness_history)
        plt.title('Evolución de la Aptitud a través de Generaciones')
        plt.xlabel('Generaciones')
        plt.ylabel('Aptitud')
        plt.grid()
        plt.show()