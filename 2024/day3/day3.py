class Solution:
    '''
        Attempt at Day 3
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '3'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [161, 161]
        self.part1TestAns   = 322
        self.test2Ans       = [161, 48]
        self.part2TestAns   = 209


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, line: str) -> int:

        lineAns = 0
        pos = 0
        line_length = len(line)

        while pos < line_length:
            if line[pos:pos+4] == 'mul(':
                pos += 4
                first_number = ''
                second_number = ''
                first_valid = True

                while pos < line_length:
                    if line[pos].isdigit():
                        first_number += line[pos]
                        pos += 1
                    elif line[pos] == ',':
                        pos += 1
                        break
                    else:
                        pos += 1
                        first_valid = False
                        break
                
                if first_valid:

                    second_valid = True

                    while pos < line_length:
                        if line[pos].isdigit():
                            second_number += line[pos]
                            pos += 1
                        elif line[pos] == ')':
                            pos += 1
                            break
                        else:
                            pos += 1
                            second_valid = False
                            break
                
                    if second_valid:

                        lineAns += int(first_number) * int(second_number)

            else:
                pos += 1


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

        lineAns = 0
        pos = 0
        line_length = len(line)
        do = True

        while pos < line_length:

            if do:

                if (line[pos:pos+7] == "don\'t()"):
                    pos += 7
                    do = False


                elif (line[pos:pos+4] == 'mul('):
                    pos += 4
                    first_number = ''
                    second_number = ''
                    first_valid = True

                    while pos < line_length:
                        if line[pos].isdigit():
                            first_number += line[pos]
                            pos += 1
                        elif line[pos] == ',':
                            pos += 1
                            break
                        else:
                            pos += 1
                            first_valid = False
                            break
                    
                    if first_valid:

                        second_valid = True

                        while pos < line_length:
                            if line[pos].isdigit():
                                second_number += line[pos]
                                pos += 1
                            elif line[pos] == ')':
                                pos += 1
                                break
                            else:
                                pos += 1
                                second_valid = False
                                break
                    
                        if second_valid:

                            print(first_number, second_number)

                            lineAns += int(first_number) * int(second_number)

                else:
                    pos += 1
            
            elif (line[pos:pos+4] == 'do()'):
                pos += 4
                do = True

            else:
                pos += 1


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