from DayFive import DayFive
from Almanac import Almanac

class PartOne(DayFive):
    def process(self, config):
        almanac = Almanac(config)
        return min(almanac.chain_number("seed", "location", seed) for seed in almanac.seeds)
    
part1 = PartOne()
part1.main()