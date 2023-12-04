from abc import ABC, abstractmethod

class DayFour(ABC):
    def main(self):
        filename = input("Input file: ")
        lines = self.get_lines(filename)
        print(f"Answer: {self.process(lines)}")

    def get_lines(self, filename):
        with open(filename, "r") as f:
            return f.readlines()
        
    @abstractmethod
    def process(self, lines):
        pass
