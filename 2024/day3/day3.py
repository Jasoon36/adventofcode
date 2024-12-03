class Solution:
    '''
        Attempt at Day 3
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '3'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns  = 322
        self.part2TestAns  = 209

    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = ''.join([line.strip('\n') for line in f])

        return input
    
    
    def solve1(self, line: str) -> int:

        lineAns = 0
        
        for mul_start in line.split('mul(')[1:]:
            instruction = mul_start.split(')')[0]

            try:
                first_number, second_number = instruction.split(',', maxsplit = 1)
            except:
                continue

            if all([char.isdigit() for char in first_number] + [char.isdigit() for char in second_number]):
                lineAns += int(first_number) * int(second_number)

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

        for sub_line in line.split('do()'):
            lineAns += self.solve1(sub_line.split("don't()")[0])

        return lineAns
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = self.solve2(input)

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
# a.testSolution1()
a.runPart1()
a.runPart2()
