from abc import ABC, abstractmethod
from Race import Race
import re

class DaySix(ABC):
    def main(self):
        filename = input("Input file: ")
        time_config, distance_config = self.get_lines(filename)
        races = self.parse_races(time_config, distance_config)
        print(f"Answer: {self.process(races)}")

    def get_lines(self, filename):
        with open(filename, "r") as f:
            return f.readlines()
        
    @abstractmethod
    def parse_races(self, time_config, distance_config):
        pass
        
    @abstractmethod
    def process(self, lines):
        pass