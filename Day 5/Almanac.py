from collections import deque

class Almanac:
    def __init__(self, config):
        seed_config, *map_configs = config.split("\n\n")
        self.seeds = self.initialize_seeds(seed_config)
        self.seed_intervals = self.initialize_seed_intervals()
        self.maps = {}
        self.populate_maps(map_configs)

    def initialize_seeds(self, seed_config):
        _, seeds = seed_config.split(":")
        return [int(seed) for seed in seeds.split()]
    
    def initialize_seed_intervals(self):
        return [Interval(self.seeds[i], self.seeds[i] + self.seeds[i+1]) for i in range(0, len(self.seeds), 2)]

    def populate_maps(self, map_configs):
        for config in map_configs:
            map_node = MapNode(config)
            self.maps[map_node.source] = map_node

    def chain_number(self, source, destination, number):
        node = source
        res = number
        while node != destination:
            mapper = self.maps[node]
            res = mapper.transform_number(res)
            node = mapper.destination
        return res
    
    def chain_intervals(self, source, destination, intervals):
        node = source
        res = intervals
        while node != destination:
            mapper = self.maps[node]
            res = mapper.transform_intervals(res)
            node = mapper.destination
        return res

class MapNode:
    def __init__(self, config):
        name_config, *range_config = config.split("\n")
        self.source, self.destination = self.get_source_and_destination(name_config)
        self.map_ranges = self.get_map_ranges(range_config)

    def get_source_and_destination(self, name_config):
        key, _ = name_config.split()
        return key.split("-to-")
    
    def get_map_ranges(self, range_config):
        return [MapRange(map_range) for map_range in range_config]
    
    def transform_number(self, number):
        map_range = self.get_map_range_for_number(number)
        if map_range:
            return map_range.transform(number)
        return number
    
    def transform_intervals(self, intervals):
        res = []
        intervals_to_process = deque(intervals)
        while intervals_to_process:
            head = intervals_to_process.popleft()
            remainder = self.process(res, head)
            if remainder is not None:
                intervals_to_process.append(remainder)
        return res
    
    def process(self, result, interval):
        start_range = self.get_map_range_for_number(interval.start)
        end_range = self.get_map_range_for_number(interval.end - 1)
        if not start_range and not end_range:
            result.append(interval)
            return None
        if start_range == end_range:
            mapped_interval = Interval(start_range.transform(interval.start), start_range.transform(interval.end))
            result.append(mapped_interval)
            return None
        if start_range:
            mapped_interval = Interval(start_range.transform(interval.start), start_range.destination.end)
            result.append(mapped_interval)
            return Interval(start_range.source.end, interval.end)
        if end_range:
            mapped_interval = Interval(end_range.destination.start, end_range.transform(interval.end))
            result.append(mapped_interval)
            return Interval(interval.start, end_range.source.start)
        return None

    def get_map_range_for_number(self, number):
        for map_range in self.map_ranges:
            if map_range.source.is_in_range(number):
                return map_range
        return None
    
class MapRange:
    def __init__(self, range_config):
        destination_start, source_start, range_length = [
            int(num) for num in range_config.split()
        ]
        self.source = Interval(source_start, source_start + range_length)
        self.destination = Interval(destination_start, destination_start + range_length)

    def transform(self, number):
        return self.destination.start + (number - self.source.start)
    
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def is_in_range(self, number):
        return number >= self.start and number < self.end