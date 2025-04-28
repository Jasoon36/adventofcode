class Solution:
    '''
        Attempt at Day 16
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '16'
        self.prod           = self.read('input.txt')
        self.test0          = self.read('input_test0.txt')
        self.test1          = self.read('input_test1.txt')
        self.part1TestAns0  = 7036
        self.part1TestAns1  = 11048
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    def prettyPrint(self, warehouse: dict):

        real_vals = list({pos.real for pos in warehouse.keys()})
        real_vals.sort()

        imag_vals = list({pos.imag for pos in warehouse.keys()})
        imag_vals.sort()

        for r in real_vals:
            print(''.join([
                warehouse[r + i * 1j] 
                    for i 
                    in imag_vals
            ]))

        print('\n')
    
    
    def solve1(self, maze: dict) -> int:

        found = 0
        for pos, char in maze.items():
            if char == 'S':
                found += 1
                reindeer_pos = pos
                if found == 2:
                    break
            
            if char == 'E':
                found += 1
                exit_pos = pos
                if found == 2:
                    break

        dir = 1j

        nodes = {
            pos
                for pos in maze.items()
                if ''.join([maze[pos+1],maze[pos-1],maze[pos+1j],maze[pos-1j]]).count('.') > 2
        } | (reindeer_pos, exit_pos)

        # search

        edges = {}




        return something

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
    
    def part1(self, realAttempt = False, test = 0) -> int:

        if realAttempt:
            input = self.prod
        else:
            if test == 0:
                input = self.test0
            else:
                input = self.test1

        maze = {
            i + j * 1j : char
                for i, row in enumerate(input)
                for j, char in enumerate(row)
        }

        attempt = self.solve1(maze)

        return attempt
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1(False, 0)
            assert part1TestAttempt == self.part1TestAns0
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns0}')
            raise e

        try:
            part1TestAttempt = self.part1(False, 1)
            assert part1TestAttempt == self.part1TestAns1
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns1}')
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