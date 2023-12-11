from DayEleven import DayEleven
from Universe import Universe

class PartOne(DayEleven):
    def process(self, config):
        universe = Universe(config.split("\n"), 2)
        res = 0
        for g1 in universe.galaxies:
            for g2 in universe.galaxies:
                res += universe.distance(g1, g2)
        return res // 2
    
part1 = PartOne()
part1.main()