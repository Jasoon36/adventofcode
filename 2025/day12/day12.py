class Solution:
    '''
        Attempt at Day 12
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '12'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = [True, True, False]
        self.test2Ans       = []
        # self.part1TestAns   = 2
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [chunk.strip('\n').split('\n') for chunk in f.read().split('\n\n')]

        return input
    
    
    def solve1(self, line: str) -> bool:

        region_size, gifts = line.split(': ')
        
        gifts_to_place = 9 * sum(quantity for quantity in map(int, gifts.split(' ')) if quantity)

        x, y = map(int, region_size.split('x'))

        return x * y >= gifts_to_place
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = sum(
            1 
                for line 
                in input[-1]
                if self.solve1(line)
        )

        return attempt
        
    def runPart1(self):

        # try:
        #     part1TestAttempt = self.part1()
        #     assert part1TestAttempt == self.part1TestAns
        # except AssertionError as e:
        #     e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
        #     raise e
        
        realAttempt = True
        print(self.part1(realAttempt))

    def plotPart1(self):
        import matplotlib.pyplot as plt
        
        tiles_per_present = {
            idx : sum(
                1
                    for line in present
                    for tile in line
                    if tile == '#'
            )
                for idx, present in enumerate(self.prod[:-1])
        }

        available_tiles = []
        max_tiles_required = []
        min_tiles_required = []

        for line in self.prod[-1]:

            region_size, gifts = line.split(': ')

            x, y = map(int, region_size.split('x'))
            available_tiles.append(x*y)
            
            max_tiles_required.append(9 * sum(quantity for quantity in map(int, gifts.split(' ')) if quantity))

            min_tiles_required.append(sum(tiles_per_present[idx] *quantity for idx, quantity in enumerate(map(int, gifts.split(' '))) if quantity))

        plt.scatter(available_tiles, max_tiles_required, color='blue', marker='o')
        plt.scatter(available_tiles, min_tiles_required, color='green', marker='x', label='Min Tiles Required')

        max_val = max(max(available_tiles), max(max_tiles_required))
        plt.plot([0, max_val], [0, max_val], color='red', linestyle='--', label='y = x')

        plt.xlabel("Available Tiles")
        plt.ylabel("Tiles Required")
        plt.title("Tiles vs Required Tiles")
        plt.grid(True)
        plt.show()


    def solve2(self, line: str) -> int:

        lineAns = 0

        return lineAns

    def testSolution2(self) -> bool:

        for line, ans in zip(self.test, self.test2Ans):
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
a.plotPart1()