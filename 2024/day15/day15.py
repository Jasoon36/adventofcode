class Solution:
    '''
        Attempt at Day 15
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '15'
        self.prod           = self.read('input.txt')
        self.test0          = self.read('input_test0.txt')
        self.test1          = self.read('input_test1.txt')
        self.part1TestAns0  = 2028
        self.part1TestAns1  = 10092
        self.vector         = {
            '^' : -1    ,
            'v' :  1    ,
            '<' : -1j   ,
            '>' :  1j   ,
        }
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = f.read()

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
    
    
    def solve1(self, warehouse: dict, movements: str) -> int:

        for pos, char in warehouse.items():
            if char == '@':
                robot_pos = pos
                break

        for move in movements:

            # self.prettyPrint(warehouse)
            
            vec = self.vector[move]
            next_pos = robot_pos + vec

            # robot is blocked
            if warehouse[next_pos] == '#':
                continue

            # robot can move
            if warehouse[next_pos] == '.':
                warehouse[next_pos] = '@'
                warehouse[robot_pos] = '.'
                robot_pos = next_pos
                continue

            # find out how many boxes are in direction
            box_positions = []
            while warehouse[next_pos] == 'O':
                box_positions.append(next_pos)
                next_pos += vec

            # boxes are blocked
            if warehouse[next_pos] == '#':
                continue

            # boxes can move
            if warehouse[next_pos] == '.':

                for box_pos in box_positions:
                    warehouse[box_pos + vec] = 'O'
                
                warehouse[robot_pos + vec] = '@'
                warehouse[robot_pos] = '.'
                robot_pos = robot_pos + vec
                continue

        # self.prettyPrint(warehouse)

        gps_coordinates = [
            100 * pos.real + pos.imag
                for pos, char
                in warehouse.items()
                if char == 'O'
        ]

        return sum(gps_coordinates)
    
    def part1(self, realAttempt = False, test = 0) -> int:

        if realAttempt:
            input = self.prod
        else:
            if test == 0:
                input = self.test0
            else:
                input = self.test1
        
        warehouse_map, movements = input.split('\n\n')

        warehouse = {
            i + j * 1j : char
                for i, row in enumerate(warehouse_map.split('\n')) 
                for j, char in enumerate(row) 
        }

        movements = ''.join(movements.split('\n'))

        attempt = self.solve1(warehouse, movements)

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
a.runPart1()