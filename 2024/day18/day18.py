class Solution:
    '''
        Attempt at Day 
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '18'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 22
        self.part2TestAns   = '6,1'


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, input: list[str], num_bytes: int) -> int:

        fallen_bytes = []
        max_grid = 0
        for i, byt in enumerate(input):
            if i == num_bytes: 
                break

            x_str, y_str = byt.split(',')
            fallen_bytes.append((y := int(y_str)) + (x := int(x_str)) * 1j)
            max_grid = max(max_grid, x, y)

        # walk
        current_positions = set([0])
        visited_positions = set([0])

        steps = 0

        endpoint = max_grid + max_grid * 1j

        while True:
            

            # grid = [
            #     [
            #         '#' if i + j * 1j in fallen_bytes else 'X' if i + j * 1j in current_positions else'.'
            #         for j in range(max_grid + 1)
            #     ]
            #     for i in range(max_grid + 1)
            # ]

            # print(steps)
            # for l in grid: print(l)
            # print('\n')

            for current_pos in current_positions:
                if current_pos == endpoint:
                    return steps


            move = set()
            for current_pos in current_positions:
                move |= set(
                    new_pos
                        for move in [1, -1, 1j, -1j]
                        if (new_pos := current_pos + move) not in fallen_bytes and new_pos not in visited_positions and new_pos.real <= max_grid and new_pos.imag <= max_grid and new_pos.real >= 0 and new_pos.imag >= 0
                )


            current_positions = move - visited_positions
            visited_positions |= move
                
            steps += 1

    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
            num_bytes = 1024
        else:
            input = self.test
            num_bytes = 12

        attempt = self.solve1(input, num_bytes)

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



    def solve2(self, input: list[str], num_bytes: int) -> list[int]:

        fallen_bytes = set()
        max_grid = 0
        for i, byt in enumerate(input):
            if i == num_bytes: 
                break

            x_str, y_str = byt.split(',')
            fallen_bytes.add((y := int(y_str)) + (x := int(x_str)) * 1j)
            max_grid = max(max_grid, x, y)



        for byt in input[num_bytes:]:

            x_str, y_str = byt.split(',')
            fallen_bytes.add((y := int(y_str)) + (x := int(x_str)) * 1j)
            max_grid = max(max_grid, x, y)

            # walk
            current_positions = set([0])
            visited_positions = set([0])

            endpoint = max_grid + max_grid * 1j

            while len(current_positions) + len(fallen_bytes) < (max_grid + 1) ** 2:

                if current_positions:

                    if endpoint in current_positions:
                        break

                    move = set()
                    for current_pos in current_positions:
                        move |= set(
                            new_pos
                                for move in [1, -1, 1j, -1j]
                                if (new_pos := current_pos + move) not in fallen_bytes and new_pos not in visited_positions and new_pos.real <= max_grid and new_pos.imag <= max_grid and new_pos.real >= 0 and new_pos.imag >= 0
                        )

                    current_positions = move - visited_positions
                    visited_positions |= move
                
                else:
                    return byt

    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
            num_bytes = 1024
        else:
            input = self.test
            num_bytes = 12

        attempt = self.solve2(input, num_bytes)

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