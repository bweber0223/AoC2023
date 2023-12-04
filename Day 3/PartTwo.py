from DayThree import DayThree
from Board import Board

class PartTwo(DayThree):
    def process (self, lines):
        board = Board(lines)
        return sum(board.calculate_all_gear_ratios())
    
part2 = PartTwo()
part2.main()