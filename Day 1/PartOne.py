from DayOne import DayOne

class PartOne(DayOne):
    def parse(self, line, i):
        if line[i].isdigit():
            return int(line[i])
        return -1
    
part1 = PartOne()
part1.main()