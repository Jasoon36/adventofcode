class Solution:
    '''
        Attempt at Day 11
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '11'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test2          = self.read('input_test2.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 5
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        rack = {
            (key_value := line.split(': '))[0] : key_value[1].split(' ')
                for line
                in input
        }

        rack_paths = {}

        def getPaths(device: str) -> int:
            
            paths = sum(
                1 if next_device == 'out' else rack_paths.setdefault(next_device, getPaths(next_device))
                    for next_device
                    in rack[device]
            )

            return paths

        return getPaths('you')
        
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
            input = self.test2

        rack = {
            (key_value := line.split(': '))[0] : key_value[1].split(' ')
                for line
                in input
        }

        rack_paths = {}

        def getPaths2(device: str):

            paths = [
                [0,0,0,1] if next_device == 'out' else rack_paths.setdefault(next_device, getPaths2(next_device))
                    for next_device
                    in rack[device]
            ]

            combine_paths = [
                sum(paths_via)
                   for paths_via
                   in map(list, zip(*paths)) # transpose
            ]

            match device: 
                case 'fft':
                    combine_paths[0] += combine_paths[2]
                    combine_paths[2] = 0
                    combine_paths[1] = combine_paths[3]
                    combine_paths[3] = 0

                case 'dac':
                    combine_paths[0] += combine_paths[1]
                    combine_paths[1] = 0
                    combine_paths[2] = combine_paths[3]
                    combine_paths[3] = 0
            
            return combine_paths

        return getPaths2('svr')[0]
        
    def runPart2(self):

        try:
            part2TestAttempt = self.part2()
            assert part2TestAttempt == self.part2TestAns
            print('yay')
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns}')
            raise e
        
        realAttempt = True
        print(self.part2(realAttempt))


a = Solution()
a.runPart1()
a.runPart2()