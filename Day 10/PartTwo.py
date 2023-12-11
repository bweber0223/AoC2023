from DayTen import DayTen
from PipeMaze import PipeMaze

class PartTwo(DayTen):
    def process(self, config):
        calculator = InternalLoopCalculator(config.split("\n"))
        return calculator.calculate()

class InternalLoopCalculator:
    def __init__(self, config):
        self.pipe_rows = config
        self.maze = PipeMaze(config)

    def calculate(self):
        return sum(self.calculate_row(i, row) for i, row in enumerate(self.pipe_rows))
    
    def calculate_row(self, i, row):
        count = 0
        is_internal = False
        boundary_pipe = None
        for j, char in enumerate(row):
            if self.maze.pipe_locations[(i, j)] not in self.maze.loop:
                count += 1 if is_internal else 0
            elif self.crossed_boundary(boundary_pipe, (i, j)):
                is_internal = not is_internal
                boundary_pipe = self.maze.pipe_locations[(i, j)]
        return count
    
    def crossed_boundary(self, last_boundary, location):
        if not last_boundary:
            return True
        pipe = self.maze.pipe_locations[location]
        type = pipe.type if pipe.type != "S" else self.maze.resolve_start()
        last_type = last_boundary.type if last_boundary.type != "S" else self.maze.resolve_start()
        if type == "-":
            return False
        if type == "|" or type == "F" or type == "L":
            return True
        if type == "J":
            if last_type == "F":
                return False
            if last_type == "L":
                return True
        if type == "7":
            if last_type == "F":
                return True
            if last_type == "L":
                return False
        return False        
    
part2 = PartTwo()
part2.main()