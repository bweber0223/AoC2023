from abc import ABC, abstractmethod

class DayOne(ABC):
    def __init__(self):
        self.lines = []

    def main(self):
        filename = input("Input file: ")
        self.get_lines(filename)
        print(f"Answer: {self.process()}")

    def process(self):
        digits_per_line = self.get_digits_per_line()
        calibrations = self.get_calibrations(digits_per_line)
        return sum(calibrations)
    
    def get_digits_per_line(self):
        return [
            [
                self.parse(line, i)
                for i, _ in enumerate(line)
                if self.parse(line, i) != -1
            ]
            for line in self.lines
        ]
    
    #ABSTRACT METHOD
    #Returns digit corresponding to char at i in line
    #Returns -1 if char does not correspond to digit
    @abstractmethod
    def parse(self, line, i):
        pass

    def get_calibrations(self, digit_lines):
        return [digit_line[0] * 10 + digit_line[-1] for digit_line in digit_lines]

    def get_lines(self, filename):
        with open(filename, "r") as f:
            self.lines = f.readlines()