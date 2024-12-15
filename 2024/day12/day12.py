class Solution:
    '''
        Attempt at Day 12
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '12'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        self.part1TestAns   = 1930
        self.test2Ans       = []
        self.part2TestAns   = 1206


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input

    def getRegions(self, pos_list: set) -> list:

        pos_assigned = set()
        regions = []

        while len(pos_assigned) < len(pos_list):

            for pos in pos_list:

                if pos in pos_assigned:
                    continue

                region = set()
                new_region = {pos}

                while len(new_region) != len(region):

                    region = new_region

                    scan = {
                        pos
                            for pos in region
                    } | {
                        pos + 1
                            for pos in region
                    } | {
                        pos - 1
                            for pos in region
                    } | {
                        pos + 1j
                            for pos in region
                    } | {
                        pos - 1j
                            for pos in region
                    }
                    
                    new_region = pos_list & scan

                pos_assigned |= region
                regions.append(list(region))

        return regions
    
    
    def solve1(self, garden_plot: dict) -> int:

        plot_locations = {}

        for pos, letter in garden_plot.items():

            plot_locations[letter] = plot_locations.get(letter, set()) | {pos}

        regions = {
            letter : self.getRegions(pos_list)
                for letter, pos_list
                in plot_locations.items()
        }

        region_fences = {
            letter : [
                [
                    4 - len(set(pos_list) & {pos+1,pos-1,pos+1j,pos-1j})
                        for pos in pos_list
                ]
                    for pos_list in region_list
            ]
                for letter, region_list in regions.items()
        }

        cost = {
            letter : sum([
                len(fences) * sum(fences)
                    for fences in fences_list
            ])
                for letter, fences_list
                in region_fences.items()
        }

        return sum(cost.values())
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        garden_plot = {
            i + j * 1j : plot
                for i, row_string in enumerate(input)
                for j, plot in enumerate(row_string)
        }

        attempt = self.solve1(garden_plot)

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


    def getSides(self, region: set) -> dict:

        fence_dir = {
            'up'    : set(),
            'down'  : set(),
            'left'  : set(),
            'right' : set(),
        }

        direction = {
            'up'    : -1,
            'down'  : 1,
            'left'  : -1j,
            'right' : 1j,
        }

        for pos in region:
            for dir, vec in direction.items():
                if pos + vec in region:
                    continue
                fence_dir[dir] |= {pos}

        sides = sum([
            len(self.getRegions(pos_set))
                for pos_set in fence_dir.values()
        ])

        return sides


    def solve2(self, garden_plot: dict) -> int:

        plot_locations = {}

        for pos, letter in garden_plot.items():

            plot_locations[letter] = plot_locations.get(letter, set()) | {pos}

        regions = {
            letter : self.getRegions(pos_list)
                for letter, pos_list
                in plot_locations.items()
        }

        cost = {
            letter : sum([
                len(region) * self.getSides(region)
                    for region in region_list
            ])
                for letter, region_list
                in regions.items()
        }

        return sum(cost.values())   
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        garden_plot = {
            i + j * 1j : plot
                for i, row_string in enumerate(input)
                for j, plot in enumerate(row_string)
        }

        attempt = self.solve2(garden_plot)

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