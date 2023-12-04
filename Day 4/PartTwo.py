from DayFour import DayFour
from Card import CardDeck

class PartTwo(DayFour):
    def process(self, lines):
        cards = CardDeck(lines)
        return sum(card.count for card in cards.deck)
    
part2 = PartTwo()
part2.main()