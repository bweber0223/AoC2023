class CardDeck:
    def __init__(self, lines):
        self.deck = [Card(line) for line in lines]
        self.duplicate_cards()

    def duplicate_cards(self):
        for i, card in enumerate(self.deck):
            matches = card.calculate_matches()
            for j in range(i + 1, i + matches + 1):
                self.deck[j].count += card.count
                
class Card:
    def __init__(self, line):
        _, lotto_config = line.split(":")
        winning_config, card_config = lotto_config.split("|")
        self.winning_values = self.config_to_numbers(winning_config)
        self.card_values = self.config_to_numbers(card_config)
        self.points = self.calculate_points()
        self.count = 1

    def config_to_numbers(self, config):
        return [int(num) for num in config.split()]
    
    def calculate_points(self):
        matches = self.calculate_matches()
        if matches == 0:
            return 0
        return 2 ** (matches - 1)

    def calculate_matches(self):
        count = 0
        for winning_val in self.winning_values:
            for card_val in self.card_values:
                if winning_val == card_val:
                    count += 1
        return count