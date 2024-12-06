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
    
    def look(self, line_ind: int, str_ind: int, dir: str):
        
        next_line_ind = line_ind
        next_str_ind = str_ind

        if dir == 'up':
            next_line_ind = line_ind + -1
        elif dir == 'down':
            next_line_ind = line_ind + 1
        elif dir == 'right':
            next_str_ind = str_ind + 1
        elif dir == 'left':
            next_str_ind = str_ind + -1

        return next_line_ind, next_str_ind
    
    def step(self, map: list, pos: tuple, dir: str, in_area = True):
        
    
    
    def solve1(self, map: list, pos: tuple, dir: str, in_area = True) -> list:

        line_ind, str_ind = pos

        map[line_ind] = map[line_ind][:str_ind] + 'X' + map[line_ind][str_ind+1:]


        try:
            next_line_ind, next_str_ind = self.look(line_ind, str_ind, dir)
            look_at_next_pos = map[next_line_ind][next_str_ind]

            while look_at_next_pos == '#':
                dir = self.turnRight[dir]
                next_line_ind, next_str_ind = self.look(line_ind, str_ind, dir)
                look_at_next_pos = map[next_line_ind][next_str_ind]

            while look_at_next_pos !

            line_ind = next_line_ind
            str_ind = next_str_ind

        except IndexError:
            in_area = False
            return map


        if in_area:

            return self.solve1(map, (line_ind, str_ind), dir, in_area)
            
        return map
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        for ind, line in enumerate(input):
            if line.find('^') > -1:
                pos = (ind, line.find('^'))
                dir = 'up'
                in_area = True
                break


        travelled_map = self.solve1(input, pos, dir, in_area)

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