class Solution:
    '''
        Attempt at Day 3
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '3'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [98, 89, 78, 92]
        self.test2Ans       = [987654321111, 811111111119, 434234234278, 888911112111]
        self.part1TestAns   = 357
        self.part2TestAns   = 3121910778619


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, line: str) -> int:

        bank = [int(digit) for digit in line]

        first_digit = max(bank[:-1])
        second_digit = max(bank[bank.index(first_digit)+1:])

        lineAns = first_digit * 10 + second_digit

        return lineAns

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
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))



    def solve2(self, line: str) -> int:

        bank = [int(digit) for digit in line]

        digits = [max(bank[:-11])]
        cut = bank.index(digits[-1]) + 1

        for pad in range(10, 0, -1):
            digits.append(max(bank[cut:-pad]))
            cut += bank[cut:].index(digits[-1]) + 1

        digits.append(max(bank[cut:]))

        lineAns = int(''.join(map(str,digits)))

        return lineAns

    def testSolution2(self) -> bool:

        for line, ans in zip(self.test, self.test2Ans):
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
# a.testSolution1()
a.runPart1()
# a.testSolution2()
a.runPart2()