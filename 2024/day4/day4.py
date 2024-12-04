class Solution:
    '''
        Attempt at Day 4
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '4'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 18
        self.part2TestAns   = 9
        self.itssschristmas = {'XMAS','SAMX'}
        self.itsmasnotmaaas = {'MAS','SAM'}


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    def check_string1(self, substring: str) -> bool:

        return substring in self.itssschristmas
    
    def check_splat1(self, splat: list) -> int:

        found_xmas = 0

        # check right
        found_xmas += self.check_string1(splat[0])

        # set first string to one length (for diag right)
        splat[0] = splat[0][0]
    
        # check down
        found_xmas += self.check_string1(''.join([ string[ind] for ind, string in enumerate(splat)]))

        # check diag left
        found_xmas += self.check_string1(''.join([ string[0] for string in splat]))

        # check diag right
        found_xmas += self.check_string1(''.join([ string[-1] for string in splat]))

        return found_xmas
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        pad = 4

        line_length = len(input[0])
        empty_line = ''.join([' ' for _ in range(line_length + pad*2)])

        empty_lines = [empty_line for _ in range(pad)]

        pad_str = ''.join([' ' for _ in range(pad)])

        padded_input = empty_lines + [pad_str + line + pad_str for line in input] + empty_lines

        xmas_found = 0

        for line_ind in range(pad, len(padded_input)-pad):
            for str_ind in range(pad, line_length+pad):

                xmas_found += self.check_splat1([
                    padded_input[line_ind][str_ind:str_ind+pad],
                    padded_input[line_ind + 1][str_ind-1:str_ind+1+1],
                    padded_input[line_ind + 2][str_ind-2:str_ind+2+1],
                    padded_input[line_ind + 3][str_ind-3:str_ind+3+1],
                ])

        return xmas_found
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))


    
    def check_string2(self, substring: str) -> bool:

        return substring in self.itsmasnotmaaas
    
    def check_splat2(self, splat: list) -> int:

        # check diag down right
        if self.check_string2(''.join([ string[ind] for ind, string in enumerate(splat)])):

            # check diag up right
            if self.check_string2(''.join([ string[ind] for ind, string in enumerate(splat[::-1])])):
                return 1

        return 0
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        pad = 3

        line_length = len(input[0])
        empty_line = ''.join([' ' for _ in range(line_length + pad*2)])

        empty_lines = [empty_line for _ in range(pad)]

        pad_str = ''.join([' ' for _ in range(pad)])

        padded_input = empty_lines + [pad_str + line + pad_str for line in input] + empty_lines

        xmas_found = 0

        for line_ind in range(pad, len(padded_input)-pad):
            for str_ind in range(pad, line_length+pad):

                xmas_found += self.check_splat2([
                    padded_input[line_ind][str_ind:str_ind+pad],
                    padded_input[line_ind + 1][str_ind:str_ind+pad],
                    padded_input[line_ind + 2][str_ind:str_ind+pad],
                ])

        return xmas_found
        
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