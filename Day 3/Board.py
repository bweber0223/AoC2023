class Board:
    def __init__(self, lines):
        self.dirs = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        self.lines = lines
        self.entities = []
        self.coords_to_entities = {}
        self.initialize_entities()

    def initialize_entities(self):
        self.initialize_entity_keys()
        self.initialize_entity_is_part()

    def initialize_entity_keys(self):
        for i, line in enumerate(self.lines):
            for j, _ in enumerate(line):
                self.build_entity(i, j)

    def build_entity(self, row, col):
        key_piece = self.lines[row][col]
        if key_piece.isdigit():
            prev_coord = (row, col - 1)
            if prev_coord in self.coords_to_entities:
                entity = self.coords_to_entities[prev_coord]
                entity.key = entity.key + key_piece
                self.coords_to_entities[(row, col)] = entity
            else:
                entity = Entity(key = key_piece)
                self.entities.append(entity)
                self.coords_to_entities[(row, col)] = entity

    def initialize_entity_is_part(self):
        for i, line in enumerate(self.lines):
            for j, _ in enumerate(line):
                self.set_symbol_neighbors_as_parts(i, j)

    def set_symbol_neighbors_as_parts(self, row, col):
        for neighbor in self.get_symbol_neighbors(row, col):
            neighbor.is_part = True

    def calculate_all_gear_ratios(self):
        ratios = []
        for i, line in enumerate(self.lines):
            for j, _ in enumerate(line):
                ratios.append(self.get_gear_ratio(i, j))
        return ratios


    def get_gear_ratio(self, row, col):
        if self.lines[row][col] != "*":
            return 0
        match self.get_symbol_neighbors(row, col):
            case [gear1, gear2]:
                return int(gear1.key) * int(gear2.key)
            case _:
                return 0

    def get_symbol_neighbors(self, row, col):
        neighbors = set()
        symbol = self.lines[row][col]
        if symbol != "." and symbol != '\n' and not symbol.isdigit():
            for r_dir, c_dir in self.dirs:
                neighbor_coord = (row + r_dir, col + c_dir)
                if neighbor_coord in self.coords_to_entities:
                    neighbors.add(self.coords_to_entities[neighbor_coord])
        return list(neighbors)

class Entity:
    def __init__(self, key, is_part = False):
        self.key = key
        self.is_part = is_part