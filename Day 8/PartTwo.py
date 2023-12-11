from DayEight import DayEight
from HauntedWasteland import HauntedWasteland
from math import lcm

class PartTwo(DayEight):
    def process(self, config):
        hw = HauntedWasteland(config)
        node_names = [key for key in hw.graph.node_dict.keys() if key[-1] == "A"]
        loop_lengths = [hw.travel(name, lambda node: node.name[-1] == "Z") for name in node_names]
        return lcm(*loop_lengths)

    
part2 = PartTwo()
part2.main()