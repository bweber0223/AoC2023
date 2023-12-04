from DayFour import DayFour
from Card import CardDeck

class PartOne(DayFour):
    def process(self, lines):
        cards = CardDeck(lines)
        return sum(card.points for card in cards.deck)
    
part1 = PartOne()
part1.main()