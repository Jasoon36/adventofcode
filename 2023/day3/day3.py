class Solution:
    '''
        Attempt at Day 3
    '''
    def __init__(self):
        self.year           = '2023'
        self.day            = '3'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 4361
        self.part2TestAns   = 467835


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [el.strip('\n') for el in f]

        return input
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        # first get locations of symbol locations
        symbolLocations = [
            (el, c)
                for el, line in enumerate(input)
                for c, char in enumerate(line)
                if (char != '.') and (not char.isdigit())
        ]

        # get numbers and check they are next to a symbol

        numbers = []

        for el, line in enumerate(input):
            
            appending = False
            first_c = -1
            last_c = -1

            for c, char in enumerate(line):

                if char.isdigit():
                    last_c = c
                    if not appending:
                        first_c = c
                        appending = True

                elif appending:
                    # check if number is adjcacent
                    valid_part_number = False
                    for line_check in (el-1, el, el+1):
                        for char_check in range(first_c-1, last_c+2):
                            if (line_check, char_check) in symbolLocations:
                                valid_part_number = True

                    if valid_part_number:
                        numbers.append(int(line[first_c:last_c+1]))

                    appending = False
                    first_c = -1
                    last_c = -1

            # edge case number is on end of line
            if appending:
                # check if number is adjcacent
                valid_part_number = False
                for line_check in (el-1, el, el+1):
                    for char_check in range(first_c-1, last_c+2):
                        if (line_check, char_check) in symbolLocations:
                            valid_part_number = True

                if valid_part_number:
                    numbers.append(int(line[first_c:last_c+1]))

        return sum(numbers)

    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))
        
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        # first get locations of symbol locations
        symbolLocations = {
            (el, c): []
                for el, line in enumerate(input)
                for c, char in enumerate(line)
                if (char != '.') and (not char.isdigit())
        }

        # get numbers and check they are next to a symbol

        for el, line in enumerate(input):
            
            appending = False
            first_c = -1
            last_c = -1

            for c, char in enumerate(line):

                if char.isdigit():
                    last_c = c
                    if not appending:
                        first_c = c
                        appending = True

                elif appending:
                    # check if number is adjcacent
                    for line_check in (el-1, el, el+1):
                        for char_check in range(first_c-1, last_c+2):
                            if (line_check, char_check) in symbolLocations.keys():
                                symbolLocations[(line_check, char_check)].append(int(line[first_c:last_c+1]))

                    appending = False
                    first_c = -1
                    last_c = -1

            # edge case number is on end of line
            if appending:
                # check if number is adjcacent
                for line_check in (el-1, el, el+1):
                    for char_check in range(first_c-1, last_c+2):
                        if (line_check, char_check) in symbolLocations.keys():
                            symbolLocations[(line_check, char_check)].append(int(line[first_c:last_c+1]))

        gearRatios = []

        for symbolLoc, part_numbers in symbolLocations.items():

            if len(part_numbers) != 2:
                continue


            el, c = symbolLoc
            if input[el][c] != '*':
                continue
        
            # no power function again
            gearRatio = 1
            for partnum in part_numbers:
                gearRatio *= partnum
            
            gearRatios.append(gearRatio)

        return sum(gearRatios)

        
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