class Solution:
    '''
        Attempt at Day 
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '6'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 41
        self.part2TestAns   = 0
        self.turnRight      = {
            'up'    : 'right',
            'right' : 'down',
            'down'  : 'left',
            'left'  : 'up',
        }


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    

    
    def getStep(self, next_line_ind: int, next_str_ind: int, dir: str) -> tuple: 

            if dir == 'up':
                next_line_ind = next_line_ind + -1
            elif dir == 'down':
                next_line_ind = next_line_ind + 1
            elif dir == 'right':
                next_str_ind = next_str_ind + 1
            elif dir == 'left':
                next_str_ind = next_str_ind + -1

            return next_line_ind, next_str_ind
    
    def getAction(self, map: list, line_ind: int, str_ind: int, dir: str):

        next_line_ind, next_str_ind = self.getStep(line_ind, str_ind, dir)
        try:
            look_at_next_pos = map[next_line_ind][next_str_ind]
        except IndexError:
            # out of map
            return next_line_ind, next_str_ind, dir, False

        # only turns if going forward is NG
        # and will turn twice if right is blocked too - maybe it shouldn't
        while look_at_next_pos == '#':
            dir = self.turnRight[dir]
            next_line_ind, next_str_ind = self.getStep(line_ind, str_ind, dir)
            try:
                look_at_next_pos = map[next_line_ind][next_str_ind]
            except IndexError:
                # out of map
                return next_line_ind, next_str_ind, dir, False

        return next_line_ind, next_str_ind, dir, True
    
    def takeAction(self, map: list, line_ind: int, str_ind: int, dir: str):
        
        # set current position to X
        map[line_ind] = map[line_ind][:str_ind] + 'X' + map[line_ind][str_ind+1:]

        next_line_ind, next_str_ind, dir, in_bounds = self.getAction(map, line_ind, str_ind, dir)

        return map, next_line_ind, next_str_ind, dir, in_bounds
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        for ind, line in enumerate(input):
            if line.find('^') > -1:
                line_ind = ind
                str_ind = line.find('^')
                dir = 'up'
                global in_area # except changes the scope why dear santa why
                in_area = True
                break

        


        while in_area:

            prev_line_ind = line_ind
            prev_str_ind = str_ind
            
            # take action and return new state
            input, line_ind, str_ind, dir, in_area = self.takeAction(input, line_ind, str_ind, dir)

            print(line_ind, str_ind, in_area)

            if (prev_line_ind == line_ind) and (prev_str_ind == str_ind):
                break
            elif line_ind < 0:
                break



        travelled_map = input

        visited_positions = sum([
            sum([
                1 
                    for char 
                    in line 
                    if char == 'X'
            ]) 
                for line 
                in travelled_map
        ])


        return visited_positions
        
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
a.runPart1()