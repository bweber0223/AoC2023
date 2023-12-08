from DaySix import DaySix
from Race import Race
import re

class PartOne(DaySix):
    def process(self, races):
        race = races[0]
        return race.ways_to_win()
    
    def parse_races(self, time_config, distance_config):
        _, *times = re.split(r'\s+', time_config)
        _, *distances = re.split(r'\s+', distance_config)
        return [Race(float("".join(times)), float("".join(distances)))]
    
part1 = PartOne()
part1.main()