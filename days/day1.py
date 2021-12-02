from utils.aoc_utils import AOCDay, day


@day(1)
class Day1(AOCDay):
    def common(self):
        return 0

    def part1(self):
        return self.checkIncrements(self.inputData)

    def part2(self):
        windowSums = []
        for index, _ in enumerate(self.inputData[:-1]):
            windowSums.append(
                int(self.inputData[index-1]) + int(self.inputData[index]) + int(self.inputData[index + 1]))

        return self.checkIncrements(windowSums)

    def checkIncrements(self, list):
        increases = 0

        for index, depth in enumerate(list):
            if int(list[index - 1]) < int(depth):
                increases += 1

        return increases
