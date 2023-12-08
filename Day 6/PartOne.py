from DaySix import DaySix
from Race import Race
from math import prod
import re

class PartOne(DaySix):
    def process(self, races):
        return prod(race.ways_to_win() for race in races)
    
    def parse_races(self, time_config, distance_config):
        _, *times = re.split(r'\s+', time_config)
        _, *distances = re.split(r'\s+', distance_config)
        return [Race(float(time), float(distance)) for time, distance in zip(times, distances)]
    
part1 = PartOne()
part1.main()