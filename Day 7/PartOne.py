from DaySeven import DaySeven
from CamelCards import HandWithJacks

class PartOne(DaySeven):
    def process(self, lines):
        hands = [HandWithJacks(line) for line in lines]
        hands.sort()
        return sum((i + 1) * hand.bid for i, hand in enumerate(hands))
    
part1 = PartOne()
part1.main()