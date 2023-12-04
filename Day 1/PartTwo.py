from DayOne import DayOne

class PartTwo(DayOne):
    def __init__(self):
        super().__init__()
        self.digit_strings = {
            "one" : 1,
            "two" : 2,
            "three" : 3,
            "four" : 4,
            "five" : 5,
            "six" : 6,
            "seven" : 7,
            "eight" : 8,
            "nine" : 9
        }

    def parse(self, line, i):
        if line[i].isdigit():
            return int(line[i])
        for key in self.digit_strings.keys():
            if line[i:].startswith(key):
                return self.digit_strings[key]
        return -1
            
part2 = PartTwo()
part2.main()