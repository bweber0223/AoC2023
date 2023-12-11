from DayTen import DayTen
from PipeMaze import PipeMaze

class PartOne(DayTen):
    def process(self, config):
        maze = PipeMaze(config.split("\n"))
        print(maze.resolve_start())
        return len(maze.loop) // 2
    
part1 = PartOne()
part1.main()