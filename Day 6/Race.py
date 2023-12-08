from math import floor, ceil, sqrt

class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def ways_to_win(self):
        small, large = self.calculate_roots()
        return self.count_integers_between(small, large)
    
    def calculate_roots(self):
        center = self.get_center()
        offset = self.get_offset()
        return [center - offset, center + offset]
    
    def get_center(self):
        return self.time / 2.0
    
    def get_offset(self):
        disc = (self.time ** 2) - (4 * self.distance)
        return sqrt(disc) / 2.0
    
    def count_integers_between(self, small, large):
        smallest_included = max(ceil(small), floor(small + 1))
        largest_included = min(floor(large), ceil(large - 1))
        return largest_included - max(smallest_included, 0) + 1