from DayNine import DayNine
from OASIS import OASIS

class PartTwo(DayNine):
    def process(self, config):
        oasis = OASIS(config)
        return sum(sand_row.get_previous_location() for sand_row in oasis.sand_rows)
    
part2 = PartTwo()
part2.main()