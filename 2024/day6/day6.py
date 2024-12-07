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
        self.part2TestAns   = 6
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
        while look_at_next_pos == '#':
            dir = self.turnRight[dir]
            next_line_ind, next_str_ind = self.getStep(line_ind, str_ind, dir)
            look_at_next_pos = self.look(area, next_line_ind, next_str_ind)
            
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
            vectors.append((line_ind, str_ind, dir))

            # take action and return new state
            area, line_ind, str_ind, dir, in_area, looped = self.takeAction1(area, line_ind, str_ind, dir, vectors)
            
            if looped:
                break
            

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



    
    def solve2(self, area: list, line_ind: int, str_ind: int, dir: str, vectors: list):

        in_area = True
        new_obstacle_positions = [] # it took me forever to realise I was checking the same new obstacle more than once
        new_obstacles_looping = 0

        step_count = 0

        while in_area:

            # take action and return new state
            vectors.append((line_ind, str_ind, dir))

            area_copy = [[_ for _ in first_layer] for first_layer in area]
            line_ind_copy = line_ind
            str_ind_copy = str_ind
            dir_copy = dir
            vectors_copy = vectors.copy()

            area, line_ind, str_ind, dir, in_area, _ = self.takeAction1(area, line_ind, str_ind, dir, vectors)

            if not in_area:
                break

            if (line_ind, str_ind) not in new_obstacle_positions:

                new_obstacle_positions.append((line_ind, str_ind))

                area_copy[line_ind][str_ind] = '#'

                _, looped2 = self.solve1(area_copy, line_ind_copy, str_ind_copy, dir_copy, vectors_copy)
                new_obstacles_looping += looped2

            if step_count % 100 == 0:
                print(step_count, new_obstacles_looping) 
            
            step_count += 1
            

        return area, new_obstacles_looping
    
    
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

        _, new_obstacles_looping = self.solve2(input, line_ind, str_ind, dir, vectors)

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
# a.runPart1()
a.runPart2()