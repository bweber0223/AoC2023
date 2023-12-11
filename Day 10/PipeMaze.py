class PipeMaze:
    def __init__(self, config):
        self.define_constants()
        self.pipes = self.build_pipes(config)
        self.pipe_locations = {pipe.location: pipe for pipe in self.pipes}
        self.uf = UnionFind([pipe for pipe in self.pipes])
        self.connect_pipes()
        self.loop = self.get_loop()

    def get_loop(self):
        return set(self.uf.get_group(self.get_start()))

    def build_pipes(self, config):
        res = []
        for i, row in enumerate(config):
            for j, type in enumerate(row):
                res.append(Pipe(type, (i, j)))
        return res
    
    def connect_pipes(self):
        for pipe in self.pipes:
            for neighbor in self.get_neighbors(pipe):
                if self.is_connected(pipe, neighbor):
                    self.uf.union(pipe, neighbor)

    def get_start(self):
        return self.get_pipes_of_type("S")[0]

    def get_pipes_of_type(self, type):
        return [pipe for pipe in self.pipes if pipe.type == type]

    def get_neighbors(self, pipe):
        r, c = pipe.location
        neighbor_locations = []
        for dir in self.pipe_types[pipe.type]:
            dr, dc = self.directions[dir]
            neighbor_locations.append((r + dr, c + dc))
        return [self.pipe_locations[location] for location in neighbor_locations if location in self.pipe_locations]
    
    def is_connected(self, pipe1, pipe2):
        return pipe1 in self.get_neighbors(pipe2) and pipe2 in self.get_neighbors(pipe1)
    
    def resolve_start(self):
        start = self.get_start()
        r, c = start.location
        locations = [n.location for n in self.get_neighbors(start) if self.is_connected(n, start)]
        directions = [(neighbor_r - r, neighbor_c - c) for neighbor_r, neighbor_c in locations]
        return self.resolve_directions(directions)
    
    def resolve_directions(self, directions):
        cardinals = set(key for key, value in self.directions.items() if value in directions)
        pipe_type = [key for key, value in self.pipe_types.items() if len(value) == 2 and cardinals.issubset(value)]
        return pipe_type[0]
    
    def define_constants(self):
        self.directions = {
            "N": (-1, 0),
            "S": (1, 0),
            "E": (0, 1),
            "W": (0, -1)
        }

        self.pipe_types = {
            "|": ("N", "S"),
            "-": ("E", "W"),
            "L": ("N", "E"),
            "J": ("N", "W"),
            "7": ("S", "W"),
            "F": ("S", "E"),
            "S": ("N", "S", "E", "W"),
            ".": ()
        }

class Pipe:
    def __init__(self, type, location):
        self.location = location
        self.type = type

class UnionFind:
    def __init__(self, elements):
        self.parents = {element: element for element in elements}
        self.rank = {element: 0 for element in elements}

    def union(self, element1, element2):
        parent1, parent2 = self.find(element1), self.find(element2)
        if parent1 == parent2:
            return
        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = self.parents[parent1]
            self.rank[parent1] += 1
        else:
            self.parents[parent1] = self.parents[parent2]
            self.rank[parent2] += 1

    def find(self, element):
        if element not in self.parents:
            raise Exception(f"{element} not included in UnionFind")
        parent = self.parents[element]
        while parent != self.parents[parent]:
            self.parents[parent] = self.parents[self.parents[parent]]
            parent = self.parents[parent]
        return parent
    
    def get_group(self, element):
        p = self.find(element)
        return [e for e in self.parents if self.find(e) == p]