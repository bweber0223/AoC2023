class Universe:
    def __init__(self, config, stretch_constant):
        self.ROWS, self.COLS = len(config), len(config[0])
        self.galaxies = self.build_galaxies(config)
        self.empty_rows = self.build_empty_rows(config)
        self.empty_cols = self.build_empty_cols(config)
        self.stretch_constant = stretch_constant

    def build_galaxies(self, config):
        res = []
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if config[r][c] == "#":
                    res.append((r, c))
        return res
    
    def build_empty_rows(self, config):
        res = []
        for i, row in enumerate(config):
            if all(char == "." for char in row):
                res.append(i)
        return res
    
    def build_empty_cols(self, config):
        res = []
        for i in range(self.COLS):
            if all(row[i] == "." for row in config):
                res.append(i)
        return res
    
    def distance(self, galaxy1, galaxy2):
        g1_r, g1_c = galaxy1
        g2_r, g2_c = galaxy2
        max_r, min_r = max(g1_r, g2_r), min(g1_r, g2_r)
        max_c, min_c = max(g1_c, g2_c), min(g1_c, g2_c)
        empty_rows = [row for row in self.empty_rows if row in range(min_r, max_r)]
        empty_cols = [col for col in self.empty_cols if col in range(min_c, max_c)]
        return (max_r - min_r) + (max_c - min_c) + (self.stretch_constant - 1) * len(empty_rows) + (self.stretch_constant - 1) * len(empty_cols)