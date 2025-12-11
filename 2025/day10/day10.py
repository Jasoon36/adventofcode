class Solution:
    '''
        Attempt at Day 10
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '10'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [2, 3, 2]
        self.test2Ans       = [10, 12, 11]
        self.part1TestAns   = 7
        self.part2TestAns   = 33


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, line: str) -> int:
        
        machine = line.split()

        lights = set()

        lights.add(
            sum(
                2 ** power
                    for power, light 
                    in enumerate(machine[0][1:-1])
                    if light == '#'
            )
        )

        buttons = [
            sum(
                1 * 2 ** power
                    for power 
                    in map(int, button[1:-1].split(','))
            )
                for button in machine[1:-1]
        ]

        button_presses = 0

        while 0 not in lights:
            press_button = set((
                light ^ b
                    for light in lights
                    for b in buttons
            ))

            lights |= press_button

            button_presses += 1

        return button_presses

    def testSolution1(self) -> bool:

        for line, ans in zip(self.test, self.test1Ans):
            try:
                attempt = self.solve1(line)
                assert attempt == ans
            except AssertionError as e:
                e.add_note(f'{attempt} is not {ans} for input\n{line}')
                raise e
        
        print('keep going')
        return True
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = sum(self.solve1(line) for line in input)

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



    def solve2(self, line: str) -> int:
        
        machine = line.split()

        joltage_counters = {tuple(
            joltage
                for joltage 
                in map(int, machine[-1][1:-1].split(','))
        )}


        buttons = tuple(
            set(map(int, button[1:-1].split(',')))
                for button 
                in machine[1:-1]
        )

        # print(joltage_counters, buttons)
        
        button_presses = 0

        while len(joltage_counters):
            
            button_presses += 1

            new_counters = set()

            for current_counter in joltage_counters:

                for button in buttons:
                    new_counter = tuple(
                        count - 1 if idx in button else count
                            for idx, count
                            in enumerate(current_counter)
                    )

                    if {-1} <= set(new_counter):
                        continue

                    if {0} == set(new_counter):
                        # print(current_counter, button, new_counter)
                        return button_presses

                    new_counters.add(new_counter)

            joltage_counters = new_counters

            # print(joltage_counters)

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

        attempt = sum(self.solve2(line) for line in input)

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
# a.testSolution1()
a.runPart1()
# a.testSolution2()
a.runPart2()