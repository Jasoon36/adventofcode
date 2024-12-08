class Solution:
    '''
        Attempt at Day 8
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '8'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 14
        self.part2TestAns   = 34


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, city: dict) -> int:

        antenna_pos = {}

        for pos, freq in city.items():
            if freq != '.':
                antenna_pos[freq] = antenna_pos.get(freq, []) + [pos]

        antinodes = set()

        for freq, pos_list in antenna_pos.items():

            for ind, pos in enumerate(pos_list[:-1]):
                for pair_pos in pos_list[ind+1:]:
                    distance = pos - pair_pos
                    new_antinodes = {pos + distance, pair_pos - distance}
                    antinodes |= new_antinodes

        number_of_antinodes = len(antinodes & set(city.keys()))

        return number_of_antinodes
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        city = {
            i + j * 1j : char
                for i, line in enumerate(input)
                for j, char in enumerate(line)
        }

        attempt = self.solve1(city)

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



    def solve2(self, city: dict) -> int:

        antenna_pos = {}

        for pos, freq in city.items():
            if freq != '.':
                antenna_pos[freq] = antenna_pos.get(freq, []) + [pos]

        antinodes = set()

        for freq, pos_list in antenna_pos.items():

            for ind, pos in enumerate(pos_list[:-1]):
                for pair_pos in pos_list[ind+1:]:
                    distance = pos - pair_pos

                    new_antinodes = set()

                    from_pos = pos + distance
                    while from_pos in city.keys():
                        new_antinodes |= {from_pos}
                        from_pos += distance
                    
                    from_pair_pos = pair_pos - distance
                    while from_pair_pos in city.keys():
                        new_antinodes |= {from_pair_pos}
                        from_pair_pos -= distance

                    antinodes |= new_antinodes

            if len(pos_list) > 1:
                antinodes |= set(pos_list)

        number_of_antinodes = len(antinodes & set(city.keys()))

        return number_of_antinodes
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test
        
        city = {
            i + j * 1j : char
                for i, line in enumerate(input)
                for j, char in enumerate(line)
        }

        attempt = self.solve2(city)

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