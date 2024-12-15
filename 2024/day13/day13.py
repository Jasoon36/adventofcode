class Solution:
    '''
        Attempt at Day 13
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '13'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 480


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [block.split('\n') for block in f.read().split('\n\n')]

        return input
    
    
    def solve1(self, a_1: int, b_1: int, c_1: int, a_2: int, b_2: int, c_2: int) -> int:

        # i have forgotten more mathematics than the average person will learn

        a = ( c_1 * b_2 - b_1 * c_2 ) / ( a_1 * b_2 - b_1 * a_2 )
        b = ( a_1 * c_2 - a_2 * c_1 ) / ( a_1 * b_2 - b_1 * a_2 )

        try:
            assert a > 0
            assert b > 0 
            assert a.is_integer()
            assert b.is_integer()
            assert int(a) * a_1 + int(b) * b_1 == c_1
            assert int(a) * a_2 + int(b) * b_2 == c_2
        except AssertionError:
            return 0

        tokens = int(a) * 3 + int(b) * 1

        return tokens
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        machines = []
        
        for block in input:

            a_1, a_2 = block[0].split(': ')[1].split(', ')
            b_1, b_2 = block[1].split(': ')[1].split(', ')
            c_1, c_2 = block[2].split(': ')[1].split(', ')

            a_1 = int(a_1.split('+')[1])
            a_2 = int(a_2.split('+')[1])
            b_1 = int(b_1.split('+')[1])
            b_2 = int(b_2.split('+')[1])

            c_1 = int(c_1.split('=')[1])
            c_2 = int(c_2.split('=')[1])

            machines.append((a_1, b_1, c_1, a_2, b_2, c_2))
            
        attempt = sum([
            self.solve1(*machine)
                for machine
                in machines 
        ])

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

        machines = []
        
        for block in input:

            a_1, a_2 = block[0].split(': ')[1].split(', ')
            b_1, b_2 = block[1].split(': ')[1].split(', ')
            c_1, c_2 = block[2].split(': ')[1].split(', ')

            a_1 = int(a_1.split('+')[1])
            a_2 = int(a_2.split('+')[1])
            b_1 = int(b_1.split('+')[1])
            b_2 = int(b_2.split('+')[1])

            c_1 = int(c_1.split('=')[1]) + 10000000000000
            c_2 = int(c_2.split('=')[1]) + 10000000000000

            machines.append((a_1, b_1, c_1, a_2, b_2, c_2))
            
        attempt = sum([
            self.solve1(*machine)
                for machine
                in machines 
        ])

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