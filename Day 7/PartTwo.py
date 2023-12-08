from DaySeven import DaySeven
from CamelCards import HandWithJokers

class PartTwo(DaySeven):
    def process(self, lines):
        hands = [HandWithJokers(line) for line in lines]
        hands.sort()
        return sum((i + 1) * hand.bid for i, hand in enumerate(hands))
    
part2 = PartTwo()
part2.main()