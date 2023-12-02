class Game:
    def __init__(self, config):
        game_config, rounds_config = config.split(":")
        self.id = self.get_id(game_config)
        self.rounds = self.get_rounds(rounds_config)

    def get_id(self, game_config):
        _, id = game_config.split()
        return int(id)
    
    def get_rounds(self, rounds_config):
        single_round_configs = rounds_config.split(";")
        return [Round(round_config) for round_config in single_round_configs]

class Round:
    def __init__(self, round_config):
        self.red = 0
        self.blue = 0
        self.green = 0
        self.initialize_blocks(round_config)

    def initialize_blocks(self, round_config):
        block_configs = round_config.split(",")
        for block in block_configs:
            match block.split():
                case [count, "red"]:
                    self.red = int(count)
                case [count, "blue"]:
                    self.blue = int(count)
                case [count, "green"]:
                    self.green = int(count)
                case _:
                    raise Exception(f"Invalid round config: {round_config}")