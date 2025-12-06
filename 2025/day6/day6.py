class Solution:
    '''
        Attempt at Day 6
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '6'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [33210, 490, 4243455, 401]
        self.test2Ans       = [1058, 3253600, 625, 8544]
        self.part1TestAns   = 4277556
        self.part2TestAns   = 3263827


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, line: str) -> int:

        if line[-1] == '+':
            return sum(map(int, line[:-1]))
        else:
            product = 1
            for num in map(int, line[:-1]):
                product *= num
            return product
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        transpose_input = list(map(list, zip(*map(str.split, input))))

        attempt = sum([self.solve1(line) for line in transpose_input])

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



    def solve2(self, line, operation) -> int:

        if operation == '+':
            return sum(line)
        else:
            product = 1
            for num in line:
                product *= num
            return product
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        starts = [
            i
                for i, char
                in enumerate(input[-1])
                if char != ' '
        ]

        starts.append(len(input[-1])+1)

        number_strings = [
            [
                line[start:end-1]
                    for line
                    in input[:-1]
            ]
                for start, end
                in zip(starts[:-1],starts[1:])
        ]

        vertical_numbers = [
            [
                int(''.join([horizontal_number[idx] for horizontal_number in horizontal_numbers]))
                    for idx
                    in range(len(horizontal_numbers[0]))
            ]
                for horizontal_numbers
                in number_strings
        ]

        attempt = sum(
            self.solve2(line, operation) 
                for line, operation 
                in zip(vertical_numbers, input[-1].split())
        )

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