class Solution:
    '''
        Attempt at Day 7
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '7'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 21
        self.part2TestAns   = 40


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        manifold = {
            i + j * 1j : char
                for i, line in enumerate(input)
                for j, char in enumerate(line)
        }

        beams = set()

        for pos, char in manifold.items():
            if char == 'S':
                beams.add(pos)
                break
            
        split_count  = 0
        
        while beams:

            new_beams = set()

            for beam_pos in beams:
                new_beam_pos = beam_pos + 1

                match manifold.get(new_beam_pos, 'x'):
                    case '.':
                        new_beams.add(new_beam_pos)
                    case '^':
                        new_beams.update((new_beam_pos - 1j, new_beam_pos + 1j))
                        split_count += 1

            beams = new_beams

        return split_count
        
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

        manifold = {
            i + j * 1j : char
                for i, line in enumerate(input)
                for j, char in enumerate(line)
        }

        many_worlds = {
            pos : 1
                for pos, char 
                in manifold.items()
                if char == 'S'
        }


        while many_worlds:
            
            total_timelines = sum(many_worlds.values())
            new_many_worlds = {}

            for beam_pos, timelines in many_worlds.items():
                new_beam_pos = beam_pos + 1

                match manifold.get(new_beam_pos, 'x'):
                    case '.':
                        new_many_worlds[new_beam_pos] = timelines + new_many_worlds.get(new_beam_pos, 0)
                    case '^':
                        new_many_worlds[new_beam_pos - 1j] = timelines + new_many_worlds.get(new_beam_pos - 1j, 0)
                        new_many_worlds[new_beam_pos + 1j] = timelines + new_many_worlds.get(new_beam_pos + 1j, 0)

            many_worlds = new_many_worlds

        return total_timelines
        
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