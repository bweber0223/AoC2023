class HauntedWasteland:
    def __init__(self, config):
        self.instructions, graph_config = config.split("\n\n")
        self.graph = Graph(graph_config.split("\n"))

    def travel(self, node_name, end_condition):
        node = self.graph.node_dict[node_name]
        count = 0
        while not end_condition(node):
            direction = self.instructions[count % len(self.instructions)]
            node = node.get_neighbor(direction)
            count += 1
        return count

class Graph:
    def __init__(self, node_configs):
        self.node_dict = self.build_dict(node_configs)
        self.connect_nodes(node_configs)

    def build_dict(self, node_configs):
        res = {}
        for config in node_configs:
            name, _ = config.split(" = ")
            res[name] = Node(name)
        return res

    def connect_nodes(self, node_configs):
        for config in node_configs:
            name, connections = config.split(" = ")
            left, right = self.parse_connections(connections)
            node = self.node_dict[name]
            node.left, node.right = self.node_dict[left], self.node_dict[right]

    def parse_connections(self, connections):
        left, right = connections.split(",")
        left = left.replace("(", "").strip()
        right = right.replace(")", "").strip()
        return (left, right)

class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

    def get_neighbor(self, direction):
        match direction:
            case "L":
                return self.left
            case "R":
                return self.right
            case _:
                raise Exception(f"Invalid direction: {direction}")