class Solution:
    '''
        Attempt at Day 10
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '10'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 36
        self.part2TestAns   = 81


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, topo_map: dict) -> int:

        height_pos = {}

        for pos, height in topo_map.items():
            height_pos[height] = height_pos.get(height, []) + [pos]

        trail_head = {
            pos : []
                for pos in height_pos[0]
        }

        for starting_pos in trail_head:
            walks = [starting_pos]
            height = 0
            while height < 9:
                
                height += 1

                scans = [
                    [pos+1, pos-1, pos+1j, pos-1j]
                        for pos 
                        in walks
                ]

                walks = [
                    pos
                        for scan in scans
                        for pos in scan
                        if pos in height_pos[height]
                ]
            
            trail_head[starting_pos] = walks

        trail_head_scores = sum([len(set(ending_positions)) for ending_positions in trail_head.values()])

        return trail_head_scores
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        topo_map = {
            i + j * 1j : int(char)
                for i, line_string in enumerate(input)
                for j, char in enumerate(line_string)
        }

        attempt = self.solve1(topo_map)

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



    def solve2(self, topo_map: dict) -> int:

        height_pos = {}

        for pos, height in topo_map.items():
            height_pos[height] = height_pos.get(height, []) + [pos]

        trail_head = {
            pos : []
                for pos in height_pos[0]
        }

        for starting_pos in trail_head:
            walks = [starting_pos]
            height = 0
            while height < 9:
                
                height += 1

                scans = [
                    [pos+1, pos-1, pos+1j, pos-1j]
                        for pos 
                        in walks
                ]

                walks = [
                    pos
                        for scan in scans
                        for pos in scan
                        if pos in height_pos[height]
                ]
            
            trail_head[starting_pos] = walks

        trail_head_rating = sum([len(ending_positions) for ending_positions in trail_head.values()])

        return trail_head_rating
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        topo_map = {
            i + j * 1j : int(char)
                for i, line_string in enumerate(input)
                for j, char in enumerate(line_string)
        }

        attempt = self.solve2(topo_map)

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