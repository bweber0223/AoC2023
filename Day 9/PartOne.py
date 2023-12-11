from DayNine import DayNine
from OASIS import OASIS

class PartOne(DayNine):
    def process(self, config):
        oasis = OASIS(config)
        return sum(sand_row.get_next_location() for sand_row in oasis.sand_rows)
    
part1 = PartOne()
part1.main()