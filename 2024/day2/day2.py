class Solution:
    '''
        Attempt at Day 2
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '2'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [
            True,
            False,
            False,
            False,
            False,
            True,
        ]
        self.part1TestAns   = 2
        self.test2Ans       = [
            True,
            False,
            False,
            True,
            True,
            True,
        ]
        self.part2TestAns   = 4


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n').split() for line in f]

        return input
    
    
    def solve1(self, line: str) -> int:

        deltas = [
            int(i) - int(j)   
                for i, j 
                in zip(line[1:], line[:-1])
        ]

        return set(deltas) <= {1,2,3} or set(deltas) <= {-3,-2,-1}

    def testSolution1(self) -> bool:

        for line, ans in zip(self.test, self.test1Ans):
            try:
                attempt = self.solve1(line)
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

        attempt = sum([self.solve1(line) for line in input])

        return attempt
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))



    def solve2(self, line: str) -> int:

        deltas = [
            int(i) - int(j)   
                for i, j 
                in zip(line[1:], line[:-1])
        ]

        abs_delta = [abs(delta) for delta in deltas]

        lineAns = (
            (max(abs_delta) <= 3)
            and (min(abs_delta) >= 1)
            and (abs(sum(deltas)) == sum(abs_delta))
        )

        if not lineAns:

            for ind in range(len(line)):

                minus_one_level = [
                    level
                        for position, level
                        in enumerate(line)
                        if position != ind
                    
                ]

                if self.solve1(minus_one_level):
                    lineAns = True
                    break

        return lineAns

    def testSolution2(self) -> bool:

        for line, ans in zip(self.test, self.test1Ans):
            try:
                attempt = self.solve2(line)
                assert attempt == ans
            except AssertionError as e:
                e.add_note(f'{attempt} is not {ans} for input\n{line}')
                raise e
        
        print('keep going')
        return True
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = sum([self.solve2(line) for line in input])

        return attempt
        
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