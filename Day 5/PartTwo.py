from DayFive import DayFive
from Almanac import Almanac

class PartTwo(DayFive):
    def process(self, config):
        almanac = Almanac(config)
        return min(interval.start for interval in almanac.chain_intervals("seed", "location", almanac.seed_intervals))
    
part2 = PartTwo()
part2.main()