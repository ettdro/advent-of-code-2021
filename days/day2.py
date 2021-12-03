from utils.aoc_utils import AOCDay, day

@day(2)
class Day2(AOCDay):
    def common(self):
        return 0

    def part1(self):
        # answer: 1 947 824
        horizontal, depth = self.executeCommands(False)
        return horizontal * depth

    def part2(self):
        # answer: 1 813 062 561
        horizontal, depth = self.executeCommands()
        return horizontal * depth

    def executeCommands(self, withAim = True):
        horizontal = depth = aim = 0
        commands = [elem.split(" ") for elem in self.inputData]

        for command in commands:
            value = int(command[1])
            if command[0] == 'forward':
                if (withAim):
                    depth += value * aim
                else:
                    horizontal += value
            elif command[0] == 'down':
                if (withAim):
                    aim += value
                else:
                    depth += value
            elif command[0] == 'up':
                if (withAim):
                    aim -= value
                else:
                    depth -= value

        return horizontal, depth