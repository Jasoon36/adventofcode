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
        self.part1TestAns   = '4,6,3,5,6,3,5,2,1,0'
        self.part2TestAns   = 117440


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, a, b, c, program: list[int]) -> int:

        operating = True
        out = []

        pointer = 0

        while operating:

            # get opcode, literal operand, and combo operand
            try:
                opcode = program[pointer]
                operand = program[pointer + 1]
            except IndexError as e:
                break

            if operand < 4:
                comboOperand = operand
            elif operand == 4:
                comboOperand = a
            elif operand == 5:
                comboOperand = b
            elif operand == 6:
                comboOperand = c

            
            # perform instruction    
            if opcode == 0:
                a = a // (2**comboOperand)
            elif opcode == 1:
                b = b ^ operand
            elif opcode == 2:
                b = comboOperand % 8
            elif opcode == 3:
                if a != 0:
                    pointer = operand
                    continue
            elif opcode == 4:
                b = b ^ c
            elif opcode == 5:
                out.append(comboOperand % 8)
            elif opcode == 6:
                b = a // (2**comboOperand)
            elif opcode == 7:
                c = a // (2**comboOperand)
            
            pointer += 2
            

        return out
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        a = int(input[0].split(': ')[1])
        b = int(input[1].split(': ')[1])
        c = int(input[2].split(': ')[1])


        program = [int(s) for s in input[-1].split(': ')[1].split(',')]

        attempt = self.solve1(a, b, c, program)

        return ','.join(map(str, attempt))
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))



    def solve2(self, a, b, c, program: list[int]) -> int:

        # figured out what it did, half helped
        # while simA != 0:
        #     out.append(
        #         (
        #             simA // (
        #                 2 ** (
        #                     (simAmod8bitxor1 := (simA % 8) ^ 1)
        #                 )
        #             ) 
        #         ) ^ ( simAmod8bitxor1 ^ 4)
        #     )
        #     simA = simA // 8
        
        # each output could have potential 8 different correct values of A
        # so multiply each potential value by 8 and check it works
        # start from right to left
        # because the A is // by 8 each time, the first value should be between 0 and 7

        # a += 8

        def check_part(a, b, c, index, program):

            # call recursively, find the correct values of A for each part of the program from the right

            # end case
            if (output := self.solve1(a, b, c, program)) == program:
                return a
            
            # doesn't match whole program, check it matches so far
            if output == program[-index:] or not index:
                # multiply by 8 add and possible remainders
                for j in range(8):
                    if (ans := check_part(a * 8 + j, b, c, index + 1, program)):
                        return ans

        return check_part(0, 0, 0, 0, program)

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

        a = int(input[0].split(': ')[1])
        b = int(input[1].split(': ')[1])
        c = int(input[2].split(': ')[1])

        program = [int(s) for s in input[-1].split(': ')[1].split(',')]

        attempt = self.solve2(a, b, c, program)

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
# a.runPart1()
a.runPart2()