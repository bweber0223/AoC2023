from collections import Counter
from abc import ABC, abstractmethod

class Hand(ABC):
    def __init__(self, config):
        hand_config, bid_config = config.split()
        self.hand = [self.parse(c) for c in hand_config]
        self.bid = int(bid_config)

    def parse(self, card):
        face_cards = self.get_face_cards()
        if card in face_cards:
            return face_cards[card]
        return int(card)

    def __lt__(self, yours):
        my_key = self.get_type_key()
        your_key = yours.get_type_key()
        if my_key == your_key:
            return self.hand < yours.hand
        return my_key < your_key
    
    @abstractmethod
    def get_type_key(self):
        counts = self.get_counts()
        return sorted(list(counts.values()), reverse=True)

    @abstractmethod
    def get_face_cards(self):
        pass
    
class HandWithJacks(Hand):
    def get_face_cards(self):
        return {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10
        }
    
    def get_type_key(self):
        counts = Counter(self.hand)
        return sorted(list(counts.values()), reverse=True)
    
class HandWithJokers(Hand):
    def get_face_cards(self):
        return {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 0,
            "T": 10
        }
    
    def get_type_key(self):
        counts = Counter(self.hand)
        jokers = counts[0]
        if jokers == 5:
            return [jokers]
        values = [count for key, count in counts.items() if key != 0]
        values.sort(reverse=True)
        values[0] += jokers
        return values
