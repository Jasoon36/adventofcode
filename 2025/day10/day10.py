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

        # yeah part 1 was a hint duh
        # the joltage requirements obviously still affects the lights
        # and we start with zero voltage and all lights off (all even, yes zero is even fight me)
        # and will need the lights to end as e.g. odd, even, even, etc.

        # pressing a button twice keeps the lights the same as before
        # so first find all combinations of buttons that will generate the lights we need
        # we only need to press each button once in the combinations, as twice will just reverse the first press

        # with the valid combinations subtract total joltage

        # i was closish, now all the lights are off, we can just half the joltages, as they're even, 
        # and there exists a combination of button presses to get exactly half the joltage required
        # and we repeat from the start
        # so need recursion and dfs
        # then we can iterate through pressing each button twice until the joltage is the same

        # yeah super easy right? no past jase is a melon

        
        machine = line.split()

        joltage_target = tuple(
            joltage
                for joltage 
                in map(int, machine[-1][1:-1].split(','))
        )

        buttons = {
            tuple(map(int, button[1:-1].split(','))) : sum(
                1 * 2 ** power
                    for power 
                    in map(int, button[1:-1].split(','))
            )
                for button 
                in machine[1:-1]
        }


        total_counters = len(joltage_target)

        def getJoltageFromCombo(button_combo):

            joltage_count = [0 for _ in range(total_counters)]

            for button in button_combo:
                for counter in button:
                    joltage_count[counter] += 1

            joltage = tuple(j for j in joltage_count)
            # tuples are better for comparison

            return joltage

        presses_required_for_joltage = {[0 for _ in range(total_counters)] : 0}

        def turnOffLights(joltage):

            lights = {
                sum(
                    (jolt % 2) * 2 ** power
                        for power, jolt 
                        in enumerate(joltage)
                ) : joltage
            }

            button_presses = 0

            while 0 not in lights:

                press_button = set((
                    light ^ b
                        for light in lights
                        for b in buttons
                ))

                lights |= press_button

                button_presses += 1

            return 

        def findMinimumPresses(joltage) -> int:

            # already seen
            if joltage in presses_required_for_joltage:
                return presses_required_for_joltage[joltage]

            # can I half
            if sum(jolt % 2 for jolt in joltage) == 0:
                if (new_joltage_to_find := [jolt // 2 for jolt in joltage]) not in presses_required_for_joltage:
                    presses_required_for_joltage[new_joltage_to_find] = findMinimumPresses(new_joltage_to_find)

                presses_required_for_joltage[joltage] = 2 * presses_required_for_joltage[new_joltage_to_find]
                return presses_required_for_joltage[joltage]

            # not seen and can't half

            possible_presses = [1e6]

            combos_to_turn_off_lights = turnOffLights(joltage)

            for new_joltage_to_find, presses in combos_to_turn_off_lights:
                if new_joltage_to_find not in presses_required_for_joltage:
                    presses_required_for_joltage[new_joltage_to_find] = findMinimumPresses(new_joltage_to_find)

                possible_presses.append(presses_required_for_joltage[new_joltage_to_find] + presses)

            presses_required_for_joltage[joltage] = min(possible_presses)

            return presses_required_for_joltage[joltage]

        # return findMinimumPresses(joltage_target)

        findMinimumPresses(joltage_target)
        print(presses_required_for_joltage)
        return presses_required_for_joltage[joltage_target]

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
# a.runPart1()
# a.testSolution2()
a.runPart2()