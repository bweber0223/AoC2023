from DayEleven import DayEleven
from Universe import Universe

class PartTwo(DayEleven):
    def process(self, config):
        universe = Universe(config.split("\n"), 1000000)
        res = 0
        for g1 in universe.galaxies:
            for g2 in universe.galaxies:
                res += universe.distance(g1, g2)
        return res // 2
    
part2 = PartTwo()
part2.main()