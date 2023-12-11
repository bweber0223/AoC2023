from abc import ABC, abstractmethod

class DayNine(ABC):
    def main(self):
        filename = input("Input file: ")
        config = self.get_lines(filename)
        print(f"Answer: {self.process(config)}")

    def get_lines(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
    @abstractmethod
    def process(self, lines):
        pass