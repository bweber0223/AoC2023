from DayTwo import DayTwo
from Game import Game

class PartOne(DayTwo):
    def __init__(self):
        self.max_red = 12
        self.max_green = 13
        self.max_blue = 14

    def process(self, lines):
        games = [Game(line) for line in lines]
        return sum(game.id for game in games if self.is_game_valid(game))
    
    def is_game_valid(self, game):
        for round in game.rounds:
            if round.red > self.max_red \
            or round.green > self.max_green \
            or round.blue > self.max_blue:
                return False
        return True
    
part1 = PartOne()
part1.main()