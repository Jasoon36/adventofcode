class Solution:
    '''
        Attempt at Day 17
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '17'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [4,6,3,5,6,3,5,2,1,0]
        self.test2Ans       = []
        self.part1TestAns   = '4635635210'
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, input: list[str]) -> int:

        register = {
            k : int(input[i].split(': ')[1])
                for i, k in enumerate('ABC')
        }

        program = [int(s) for s in input[-1].split(': ')[1].split(',')]

        

        return lineAns
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = self.solve1(input)

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



    def solve2(self, line: str) -> int:

        lineAns = 0

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

        attempt = sum([1 for line in input])

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