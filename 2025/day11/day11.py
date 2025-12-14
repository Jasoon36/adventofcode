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
        self.part2TestAns   = 2


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

            paths = 0

            for next_device in rack[device]:
                if next_device == 'out': 
                    paths += 1
                    continue
                elif next_device not in rack_paths:
                    rack_paths[next_device] = getPaths(next_device)

                paths += rack_paths[next_device]

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
            (key_value := line.split(': '))[0] : set(key_value[1].split(' '))
                for line
                in input
        }

        connections = {}

        def getConnections(device: str):

            set_of_all_connections = set(rack[device])
            
            for next_device in rack[device]:
                # print(device, next_device)
                if next_device == 'out':
                    set_of_all_connections |= {'out'}
                else:
                    if next_device not in connections:
                        connections[next_device] = getConnections(next_device)
                    set_of_all_connections |= connections[next_device]

            return set_of_all_connections

        connections['svr'] = getConnections('svr')

        dac_first = len({'fft'} & connections['dac']) > 0

        if dac_first:
            stops = ('svr', 'dac', 'fft', 'out')
        else:
            stops = ('svr', 'fft', 'dac', 'out')

        def getPaths2(device: str, base: str, allowed_devices: set) -> int:

            connections_to_search = rack[device] & (allowed_devices | {base})

            paths = 0

            for next_device in connections_to_search:
                if next_device == base: 
                    paths += 1
                    continue
                elif next_device == 'out':
                    continue
                elif next_device not in rack_paths:
                    rack_paths[next_device] = getPaths2(next_device, base, allowed_devices)

                paths += rack_paths[next_device]

            return paths

        attempt = 1

        for i in range(3):

            start = stops[i]
            end_i = i+1
            end = stops[end_i]
            needed_connections = set(stops[end_i:])
            required_length = len(needed_connections)

            allowed_devices = connections[start] | {
                device
                    for device, connected_devices
                    in connections.items()
                    if len(connected_devices & needed_connections) == required_length
            }

            rack_paths = {}
            attempt *= getPaths2(start, end, allowed_devices)

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