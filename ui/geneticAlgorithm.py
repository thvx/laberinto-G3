import random
from ui.genotype import Genotype

class GeneticAlgorithm:
    def __init__(self, population_size, maze, crossover_rate=0.7, mutation_rate=0.1):
        self.population_size = population_size
        self.maze = maze
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.population = [Genotype(maze) for _ in range(population_size)]

    def selection(self):
        tournament_size = 3
        return [max(random.sample(self.population, tournament_size), key=lambda g: g.fitness) for _ in range(self.population_size)]

    def crossover(self, parent1, parent2):
        return parent1.crossover(parent2) if random.random() < self.crossover_rate else parent1

    def mutate(self, genotype):
        genotype.mutate(mutation_rate=self.mutation_rate)

    def evolve(self, generations):
        for generation in range(generations):
            for genotype in self.population:
                genotype.calculate_fitness()
            selected_population = self.selection()
            new_population = []
            for i in range(0, len(selected_population), 2):
                offspring = self.crossover(selected_population[i], selected_population[(i + 1) % len(selected_population)])
                self.mutate(offspring)
                offspring.calculate_fitness()
                new_population.append(offspring)
            self.population = sorted(new_population, key=lambda g: g.fitness, reverse=True)
            print(f"Generación {generation}: Mejor aptitud = {self.population[0].fitness}")

    def solution_found(self):
        return self.population[0].fitness > 0 #and self.population[0].no_of_obstacles == 0