from functools import cache

class Solution:
    '''
        Attempt at Day 19
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '19'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [True,True,True,True,False,True,True,False,]
        self.test2Ans       = [2,1,4,6,0,1,2,0]
        self.part1TestAns   = 6
        self.part2TestAns   = 16


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, patterns: list[str], design: str) -> bool:

        towels = set(patterns)
        remaining_designs = set()
        remaining_designs.add(design)

        while remaining_designs:

            des = remaining_designs.pop()

            if not des:
                return True

            remaining_designs |= set(
                des.removeprefix(towel)
                    for towel in towels
                    if des.startswith(towel)
            )

        return False

    def testSolution1(self) -> bool:

        patterns = self.test[0].split(', ')
        for line, ans in zip(self.test[2:], self.test1Ans):
            try:
                attempt = self.solve1(patterns, line)
                assert attempt == ans
            except AssertionError as e:
                e.add_note(f'{attempt} is not {ans} for input\n{line}')
                raise e
        
        print('keep going')
        return True
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        patterns = input[0].split(', ')
        designs = input[2:]

        attempt = sum(1 for design in designs if self.solve1(patterns, design))

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


    @cache
    def count(self, design):

        if not design:
            return 1
        
        return sum(
            # self.seenPatterns.setdefault(design.removeprefix(towel), self.count(design.removeprefix(towel)))
            self.count(design.removeprefix(towel))
                for towel in self.patterns
                if design.startswith(towel)
        )


    def solve2(self, patterns: list[str], designs: list[str]) -> int:

        self.patterns = patterns

        return sum(self.count(design) for design in designs)

    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        patterns = input[0].split(', ')
        designs = input[2:]

        # self.seenPatterns  = {}

        attempt = self.solve2(patterns, designs)

        return attempt
        
    def runPart2(self):

        # try:
        #     part2TestAttempt = self.part2()
        #     assert part2TestAttempt == self.part2TestAns
        # except AssertionError as e:
        #     e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns}')
        #     raise e
        
        realAttempt = True
        print(self.part2(realAttempt))


a = Solution()
a.runPart1()
a.runPart2()