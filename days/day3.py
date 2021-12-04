from utils.aoc_utils import AOCDay, day

@day(3)
class Day3(AOCDay):
    def common(self):
        return 0

    def part1(self):
        gammaRate = self.getBitOccurences(0, len(self.inputData[0]), self.inputData)
        epsilonRate = self.flipBits(gammaRate)
        return int(gammaRate, 2) * int(epsilonRate, 2)
    
    def part2(self):
        return self.getRating(True) * self.getRating(False)
    
    def getBitOccurences(self, startIndex, stopIndex, data):
        """Gets the most bit occurences for a specifin index column."""
        bitOccurence = ""
        for index in range(startIndex, stopIndex):
            binaryValue = ""
            for row in data:
                binaryValue += row[index]

            bitOccurence += '1' if binaryValue.count('1') >= binaryValue.count('0') else '0'
        return bitOccurence
    
    def flipBits(self, binaryString):
        """Flips all the bits of a string that contains only 0 and 1 values."""
        binaryFlipped = ""
        for char in binaryString:
            binaryFlipped += '0' if (char == '1') else '1'
        return binaryFlipped

    def getRating(self, forOxygen):
        """Gets the ratings for oxygen or carbon dioxyde as ints."""
        ratings = self.inputData.copy()
        for column in range(0, len(ratings[0])):
            updatedList = ratings.copy()
            if len(updatedList) == 1:
                break
            bitCriteria = self.getBitOccurences(column, column + 1, ratings)
            if forOxygen:
                bitCriteria = self.flipBits(bitCriteria)
            for row in updatedList:
                if row[column] != bitCriteria:
                    ratings.remove(row)

        return int(ratings[0], 2)