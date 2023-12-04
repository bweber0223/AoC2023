from DayThree import DayThree
from Board import Board

class PartOne(DayThree):
    def process (self, lines):
        board = Board(lines)
        return sum(int(entity.key) for entity in board.entities if entity.is_part == True)
    
part1 = PartOne()
part1.main()