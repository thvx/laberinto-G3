import random

class Genotype:
    def __init__(self, maze, path=None, direction_bits=None):
        self.maze = maze 
        self.start = self.maze.get_start_position()
        self.end = self.maze.get_end_position()
        self.path = path if path else self.generate_random_path()
        self.direction_bits = direction_bits if direction_bits else self.generate_random_directions()
        self.fitness = None 

    def generate_random_path(self, length=10):
        # Generamos una lista de segmentos de longitud aleatoria
        segments = []
        for _ in range(length):
            end_row = random.randint(1, self.maze.rows)
            end_col = random.randint(1, self.maze.cols)
            segments.append((end_row, end_col))
        return segments

    def generate_random_directions(self):
        # Lista de bits de dirección aleatoria
        return [random.choice([0, 1]) for _ in range(len(self.path))]

    def calculate_fitness(self, weight_feasibility=3, weight_length=2, weight_turns=2):
        # Calculamos la aptitud del genotipo basado en la distancia a la meta y sus colisiones
        position = self.start
        total_distance = 0
        valid_moves = True
        num_turns = 0

        for idx, (target, direction_bit) in enumerate(zip(self.path, self.direction_bits)):
            if not valid_moves:
                break

            # Calculamos el movimiento basado en el bit de dirección
            if direction_bit == 0:
                # Movimiento vertical seguido de movimiento horizontal
                new_position = self.move_vertically(position, target[0])
                if self.maze.is_free(*new_position):
                    position = new_position
                    new_position = self.move_horizontally(position, target[1])
                    if not self.maze.is_free(*new_position):
                        valid_moves = False
                else:
                    valid_moves = False
            else:
                # Movimiento horizontal seguido de movimiento vertical
                new_position = self.move_horizontally(position, target[1])
                if self.maze.is_free(*new_position):
                    position = new_position
                    new_position = self.move_vertically(position, target[0])
                    if not self.maze.is_free(*new_position):
                        valid_moves = False
                else:
                    valid_moves = False

            if valid_moves:
                total_distance += abs(self.end[0] - position[0]) + abs(self.end[1] - position[1])
                if idx > 0 and self.direction_bits[idx] != self.direction_bits[idx - 1]:
                    num_turns += 1

        feasibility_factor = 1 if valid_moves else 0
        length_factor = 1 / (total_distance + 1)
        turns_factor = 1 / (num_turns + 1)

        # Calculamos funcion fitness
        self.fitness = (weight_feasibility * feasibility_factor +
                        weight_length * length_factor +
                        weight_turns * turns_factor)

    def move_vertically(self, position, target_row):
        # Movemos el robot en la dirección vertical hacia la fila objetivo
        row, col = position
        if row < target_row:
            return (row + 1, col)
        elif row > target_row:
            return (row - 1, col)
        return (row, col)

    def move_horizontally(self, position, target_col):
        # Movemos el robot en la dirección horizontal hacia la columna objetivo
        row, col = position
        if col < target_col:
            return (row, col + 1)
        elif col > target_col:
            return (row, col - 1)
        return (row, col)

    def mutate(self, mutation_rate=0.1):
        # Mutamos el camino y los bits de dirección con una tasa de mutación
        for i in range(len(self.path)):
            if random.random() < mutation_rate:
                # Mutar la posición objetivo en el camino
                self.path[i] = (random.randint(1, self.maze.rows), random.randint(1, self.maze.cols))
            if random.random() < mutation_rate:
                # Mutar el bit de dirección
                self.direction_bits[i] = 1 - self.direction_bits[i]  # Cambia de 0 a 1 o de 1 a 0

    def crossover(self, other):
        # Cruzamos dos genotipos para crear un nuevo camino y bit de dirección
        cut_point = random.randint(1, len(self.path) - 2)
        new_path = self.path[:cut_point] + other.path[cut_point:]
        new_direction_bits = self.direction_bits[:cut_point] + other.direction_bits[cut_point:]
        return Genotype(self.maze, new_path, new_direction_bits)

    def __repr__(self):
        return f"Genotype(path={self.path}, direction_bits={self.direction_bits}, fitness={self.fitness})"
