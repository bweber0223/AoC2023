from collections import defaultdict
from DayTwo import DayTwo
from Game import Game
from math import prod

class PartTwo(DayTwo):
    def process(self, lines):
        games = [Game(line) for line in lines]
        return sum(self.calculate_power(game) for game in games)
    
    def calculate_power(self, game):
        partitions = self.partition_by_color(game)
        return prod(max(color_value) for color_value in partitions.values())
    
    def partition_by_color(self, game):
        partition = defaultdict(list)
        for round in game.rounds:
            if round.red != 0:
                partition["red"].append(round.red)
            if round.blue != 0:
                partition["blue"].append(round.blue)
            if round.green != 0:
                partition["green"].append(round.green)
        return partition
    
part2 = PartTwo()
part2.main()