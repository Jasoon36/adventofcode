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
        # then we can iterate through pressing each button twice until the joltage is the same

        # yeah super easy right?


        
        machine = line.split()

        joltage_target = tuple(
            joltage
                for joltage 
                in map(int, machine[-1][1:-1].split(','))
        )

        light_end_state = sum(
            (joltage % 2) * 2 ** power
                for power, joltage 
                in enumerate(joltage_target)
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

        all_button_combinations = {}

        for button, light_change in buttons.items():

            all_button_combinations |= {
                (*button_combo, button) : light ^ light_change
                    for button_combo, light 
                    in all_button_combinations.items()
            }

            all_button_combinations[tuple((button,))] = light_change
        
        all_valid_combinations = [
            button_combo
                for button_combo, light
                in all_button_combinations.items()
                if light == light_end_state
        ]

        get_the_lights_correct = {}
        # joltage_subtract : button_presses

        for button_combo in all_valid_combinations:
            
            # get joltage count

            joltage_count = [0 for _ in range(total_counters)]

            for button in button_combo:
                for counter in button:
                    joltage_count[counter] += 1

            # button press count
            button_press = len(button_combo)

            joltage_key = tuple(j for j in joltage_count)

            if button_press < get_the_lights_correct.get(joltage_key, 1e3):
                get_the_lights_correct[joltage_key] = button_press

        
        # we now have starting joltages
        # so we need to press each button twice and continue doing so until we reach target joltage

        double_press = [
            tuple(
                2 if idx in button else 0
                    for idx
                    in range(total_counters)
                    
            )
                for button
                in buttons.keys()
        ]


        # print(joltage_target)

        # print(get_the_lights_correct)

        # print(double_press)
        min_button_presses = 1e7

        while get_the_lights_correct:

            one_step = {}

            for joltage_to_double_press, current_presses in get_the_lights_correct.items():
                
                new_press = current_presses + 2

                if new_press >= min_button_presses:
                    # skip if already greater than or equal to current minimum
                    continue

                for joltage_to_add in double_press:

                    new_joltage = tuple(
                        a + b
                            for a, b
                            in zip(joltage_to_double_press, joltage_to_add)
                    )

                    if new_joltage == joltage_target:
                        min_button_presses = min(new_press, min_button_presses)

                    if new_joltage <= joltage_target:
                        if new_press < one_step.get(new_joltage, min_button_presses):
                            one_step[new_joltage] = new_press

            get_the_lights_correct = one_step

            # print(get_the_lights_correct)

            # break

            # if min_button_presses < 1e7:
                # break

            print(min_button_presses)

        # this is slow likely becauseI return to the same joltages over and over again and don't do any elimination
        # or maybe its just rubbish - pretty likely

        return min_button_presses

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