class OASIS:
    def __init__(self, config):
        sand_configs = config.split("\n")
        self.sand_rows = [
            SandRow([int(location) for location in sand_config.split(" ")])
            for sand_config in sand_configs
        ]

class SandRow:
    def __init__(self, sand):
        self.sand = sand

    def get_next_location(self):
        if all(sand_location == 0 for sand_location in self.sand):
            return 0
        next_row = self.get_next_row()
        return next_row.get_next_location() + self.sand[-1]
    
    def get_previous_location(self):
        if all(sand_location == 0 for sand_location in self.sand):
            return 0
        next_row = self.get_next_row()
        return self.sand[0] - next_row.get_previous_location()
    
    def get_next_row(self):
        return SandRow([self.sand[i + 1] - self.sand[i] for i in range(len(self.sand) - 1)])