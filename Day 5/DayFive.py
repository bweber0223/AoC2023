from abc import ABC, abstractmethod

class DayFive(ABC):
    def main(self):
        filename = input("Input file: ")
        config = self.read_file(filename)
        print(f"Answer: {self.process(config)}")

    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()
        
    @abstractmethod
    def process(self, config):
        pass