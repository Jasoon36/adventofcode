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
            input = [list(line.strip('\n')) for line in f]

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
    
    def checkInBounds(self, area: int, next_line_ind: int, next_str_ind: int) -> bool:

        if next_line_ind < 0:
            return False
        
        if next_line_ind == len(area):
            return False
        
        if next_str_ind < 0:
            return False
        
        if next_str_ind == len(area[0]):
            return False

        return True
    
    def look(self, area: list, next_line_ind: int, next_str_ind: int) -> str:
        
        return area[next_line_ind][next_str_ind]


    def getAction1(self, area: list, line_ind: int, str_ind: int, dir: str):

        next_line_ind, next_str_ind = self.getStep(line_ind, str_ind, dir)
        in_bounds = self.checkInBounds(area, next_line_ind, next_str_ind)

        # early return if we step out
        if not in_bounds:
            return next_line_ind, next_str_ind, dir, in_bounds
        
        # only turns if going forward is NG
        look_at_next_pos = self.look(area, next_line_ind, next_str_ind)
        if look_at_next_pos == '#':
            dir = self.turnRight[dir]
            next_line_ind, next_str_ind = self.getStep(line_ind, str_ind, dir)
            
        return next_line_ind, next_str_ind, dir, in_bounds
    
    def takeAction1(self, area: list, line_ind: int, str_ind: int, dir: str, vectors: False):
        
        looped = False
        
        # set current position to X
        area[line_ind][str_ind] = 'X'

        # get new position, direction, and if in bounds
        next_line_ind, next_str_ind, dir, in_bounds = self.getAction1(area, line_ind, str_ind, dir)

        if (next_line_ind, next_str_ind, dir) in vectors:
            looped = True

        return area, next_line_ind, next_str_ind, dir, in_bounds, looped
    
    def solve1(self, area: list, line_ind: int, str_ind: int, dir: str, vectors: list):

       
        in_area = True

        while in_area:

            # take action and return new state
            area, line_ind, str_ind, dir, in_area, looped = self.takeAction1(area, line_ind, str_ind, dir, vectors)

            # print(line_ind, str_ind, dir)
            if looped:
                break
            
            vectors.append((line_ind, str_ind, dir))

            print(line_ind, str_ind, dir, in_area, looped)

        return area, looped

    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        for line_ind, line in enumerate(input):
            for str_ind, char in enumerate(line):
                if char == '^':
                    break
            if char == '^':
                break

        dir = 'up'
        vectors = []

        travelled_map, _ = self.solve1(input, line_ind, str_ind, dir, vectors)

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


    
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        for line_ind, line in enumerate(input):
            for str_ind, char in enumerate(line):
                if char == '^':
                    break
            if char == '^':
                break

        dir = 'up'
        vectors = []

        ## okay now brute force this

        in_area = True

        new_obstacles_looping = 0

        no_added_obstacle_map = input

        while in_area:

            # add an obstacle only if next step is in bounds
            next_line_ind, next_str_ind = self.getStep(line_ind, str_ind, dir)
            in_bounds = self.checkInBounds(no_added_obstacle_map, next_line_ind, next_str_ind)

            if in_bounds:
                look_at_next_pos = self.look(no_added_obstacle_map, next_line_ind, next_str_ind)

                # add obstacle and check if it loops
                if look_at_next_pos != '#':
                    new_map = no_added_obstacle_map
                    new_map[next_line_ind][next_str_ind] = '#'
                    new_vectors = vectors

                    new_map_travelled, new_map_looped = self.solve1(new_map, line_ind, str_ind, dir, new_vectors)

                    new_obstacles_looping += new_map_looped


                no_added_obstacle_map, line_ind, str_ind, dir, in_area, looped = self.takeAction1(no_added_obstacle_map, line_ind, str_ind, dir, vectors)
                
                vectors.append((line_ind, str_ind, dir))


            # next step is out of bounds so we stop adding obstacles
            else:
                break
            print(new_obstacles_looping)

        return new_obstacles_looping
        
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
# a.runPart2()