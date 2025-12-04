class Solution:
    '''
        Attempt at Day 4
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '4'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 13
        self.part2TestAns   = 43


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
        

    def checkAdjacentPositions(self, grid: dict, origin) -> bool:

        return sum([
            grid.get(origin + jitter, '.') == '@'
                for jitter
                in [1,-1, 1j, -1j, 1+1j, 1-1j, -1+1j, -1-1j]
        ]) < 4
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        
        grid = {
            i + j * 1j : char
                for i, line in enumerate(input)
                for j, char in enumerate(line)
        }

        attempt = sum(
            self.checkAdjacentPositions(grid, position)
                for position, val
                in grid.items()
                if val == '@'
        )

        return attempt
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))

    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        
        grid = {
            i + j * 1j : char
                for i, line in enumerate(input)
                for j, char in enumerate(line)
        }

        paper_to_remove = {
            position : 'x'
                for position, val
                in grid.items()
                if val == '@' and self.checkAdjacentPositions(grid, position)
        }

        grid |= paper_to_remove

        removed_rolls = len(paper_to_remove.keys())

        while paper_to_remove.keys():

            paper_to_remove = {
                position : 'x'
                    for position, val
                    in grid.items()
                    if val == '@' and self.checkAdjacentPositions(grid, position)
            }

            grid |= paper_to_remove
            removed_rolls += len(paper_to_remove.keys())

        return removed_rolls
        
    def runPart2(self):

        try:
            part2TestAttempt = self.part2()
            assert part2TestAttempt == self.part2TestAns
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns}')
            raise e
        
        realAttempt = True
        print(self.part2(realAttempt))


a = Solution()
a.runPart1()
a.runPart2()