import numpy as np
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, grid):
        self.grid = np.array(grid)
        self.start = (0, 0)  # posición de inicio
        self.end = (len(grid) - 1, len(grid[0]) - 1)  # posición de final

    def is_free(self, position):
        x, y = position
        return self.grid[x][y] == 0

    def display(self, path=None):
        plt.imshow(self.grid, cmap='binary')
        if path:
            for (x, y) in path:
                plt.plot(y, x, 'ro')  # Marcamos el camino encontrado
        plt.scatter(self.start[1], self.start[0], c='green', label='Start')
        plt.scatter(self.end[1], self.end[0], c='blue', label='End')
        plt.legend()
        plt.show()