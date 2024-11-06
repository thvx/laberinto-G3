from pyamaze import maze, agent, COLOR


class Maze:
    def __init__(self, rows, cols, start=(1, 1), end=None):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.end = end if end else (rows, cols)
        self.maze_grid = maze(rows, cols)
        self.maze_grid.CreateMaze(x=self.end[0], y=self.end[1])

    def get_start_position(self):
        return self.start

    def get_end_position(self):
        return self.end

    def add_obstacle(self, row, col):
        self.maze_grid.maze_map[(row, col)]['N'] = 0
        self.maze_grid.maze_map[(row, col)]['S'] = 0
        self.maze_grid.maze_map[(row, col)]['E'] = 0
        self.maze_grid.maze_map[(row, col)]['W'] = 0
        agent(self.maze_grid, x=row, y=col, color=COLOR.red, shape='square')

    def is_free(self, row, col):
        if (row, col) not in self.maze_grid.maze_map:
            return False
        directions = self.maze_grid.maze_map[(row, col)]
        return directions['N'] == 1 or directions['S'] == 1 or directions['E'] == 1 or directions['W'] == 1

    def display(self):
        robot_agent = agent(self.maze_grid, x=self.start[0], y=self.start[1], goal=(self.end[0], self.end[1]),
                            footprints=True, color=COLOR.blue)
        self.maze_grid.tracePath({robot_agent: [(self.end[0], self.end[1])]}, delay=100)
        self.maze_grid.run()
