from DayEight import DayEight
from HauntedWasteland import HauntedWasteland

class PartOne(DayEight):
    def process(self, config):
        hw = HauntedWasteland(config)
        return hw.travel("AAA", lambda node: node.name == "ZZZ")
    
part1 = PartOne()
part1.main()