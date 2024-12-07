class Solution:
    '''
        Attempt at Day 7
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '7'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [
            190,
            3267,
            0,
            0,
            0,
            0,
            0,
            0,
            292,
        ]
        self.part1TestAns   = 3749
        self.test2Ans       = [
            190,
            3267,
            0,
            156,
            7290,
            0,
            192,
            0,
            292,
        ]
        self.part2TestAns   = 11387


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, line: str) -> int:

        answer, _ = line.split(': ')
        numbers = [int(num) for num in _.split()]

        answer = int(answer)
        mult_or_add = [numbers[0]]

        for num in numbers[1:]:
            mult_or_add = [
                x 
                    for calc 
                    in mult_or_add
                    if (x := calc + num) <= answer
            ] + [
                x 
                    for calc 
                    in mult_or_add
                    if (x := calc * num) <= answer
            ]


        if answer in mult_or_add:
            return answer

        return 0

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

        answer, _ = line.split(': ')
        numbers = [int(num) for num in _.split()]

        answer = int(answer)

        mult_or_add_or_conc = [numbers[0]]

        for num in numbers[1:]:
            mult_or_add_or_conc = [
                x 
                    for calc 
                    in mult_or_add_or_conc
                    if (x := calc + num) <= answer
            ] + [
                x 
                    for calc 
                    in mult_or_add_or_conc 
                    if (x := calc * num) <= answer
            ] + [
                x 
                    for calc 
                    in mult_or_add_or_conc 
                    if (x := int(str(calc) + str(num))) <= answer
            ]


        if answer in mult_or_add_or_conc:
            return answer

        return 0

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
a.runPart1()
a.runPart2()