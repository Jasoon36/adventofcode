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
        self.test2          = self.read('input_test2.txt')
        self.part1TestAns0  = 2028
        self.part1TestAns1  = 10092
        self.vector         = {
            '^' : -1    ,
            'v' :  1    ,
            '<' : -1j   ,
            '>' :  1j   ,
        }
        self.part2TestAns1  = 9021
        self.part2TestAns2  = 9021


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



    def solve2(self, warehouse: dict, movements: str) -> int:

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

            # if left or right same again
            if move in ('<','>'):
                box_positions = {}
                while warehouse[next_pos] in ('[',']'):
                    box_positions[next_pos] = warehouse[next_pos]
                    next_pos += vec

                # boxes are blocked
                if warehouse[next_pos] == '#':
                    continue

                # boxes can move
                if warehouse[next_pos] == '.':

                    for box_pos, char in box_positions.items():
                        warehouse[box_pos + vec] = char
                    
                    warehouse[robot_pos + vec] = '@'
                    warehouse[robot_pos] = '.'
                    robot_pos = robot_pos + vec
                    continue
            
            # up and down, annoying
            else:
                box_positions = {}

                # search in direction of vec for new boxes
                new_box_positions = {next_pos : warehouse[next_pos]}
                
                # check you haven't got half a box after search up
                new_box_positions |= {
                    pos - 1j : warehouse[pos - 1j]
                        for pos, char
                        in new_box_positions.items()
                        if char == ']'
                } | {
                    pos + 1j : warehouse[pos + 1j]
                        for pos, char
                        in new_box_positions.items()
                        if char == '['
                }

                box_positions |= new_box_positions

                blocked = False

                while len(new_box_positions.keys()) > 0:
                    # search in direction of vec for new boxes
                    new_box_positions = {
                        pos + vec : char
                            for pos in new_box_positions
                            if (char := warehouse[pos + vec]) != '.'
                    }

                    if len(set(new_box_positions.values()) & {'#'}) > 0:
                        blocked = True
                        break
                    
                    # cool so no walls
                    # check you haven't got half a box after searching up
                    new_box_positions |= {
                        pos - 1j : warehouse[pos - 1j]
                            for pos, char
                            in new_box_positions.items()
                            if char == ']'
                    } | {
                        pos + 1j : warehouse[pos + 1j]
                            for pos, char
                            in new_box_positions.items()
                            if char == '['
                    }
                
                    box_positions |= new_box_positions

                if blocked:
                    continue

                # now move boxes
                
                pos_moved_to = []
                for box_pos, char in box_positions.items():
                    warehouse[box_pos + vec] = char
                    pos_moved_to.append(box_pos + vec)

                for box_pos in box_positions.keys():
                    if box_pos not in pos_moved_to:
                        warehouse[box_pos] = '.'

                # and move robot
                warehouse[robot_pos + vec] = '@'
                warehouse[robot_pos] = '.'
                robot_pos = robot_pos + vec


        # self.prettyPrint(warehouse)

        gps_coordinates = [
            100 * pos.real + pos.imag
                for pos, char
                in warehouse.items()
                if char == '['
        ]

        return sum(gps_coordinates)
    
    def part2(self, realAttempt = False, test = 2) -> int:

        if realAttempt:
            input = self.prod
        else:
            if test == 2:
                input = self.test2
            else:
                input = self.test1
        
        warehouse_map, movements = input.split('\n\n')

        char_map = {
            '#' : '##',
            '.' : '..',
            '@' : '@.',
            'O' : '[]',
        }

        warehouse_2 = [
            ''.join([
                char_map[char]
                    for char in row
            ])
                for row in warehouse_map.split('\n')
        ]

        warehouse = {
            i + j * 1j : char
                for i, row in enumerate(warehouse_2) 
                for j, char in enumerate(row) 
        }

        movements = ''.join(movements.split('\n'))

        # self.prettyPrint(warehouse)

        attempt = self.solve2(warehouse, movements)

        return attempt
        
    def runPart2(self):

        # try:
        #     part2TestAttempt = self.part2(False, 2)
        #     assert part2TestAttempt == self.part2TestAns2
        # except AssertionError as e:
        #     e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns2}')
        #     raise e

        try:
            part2TestAttempt = self.part2(False, 1)
            assert part2TestAttempt == self.part2TestAns1
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns1}')
            raise e
        
        realAttempt = True
        print(self.part2(realAttempt))


a = Solution()
a.runPart1()
a.runPart2()