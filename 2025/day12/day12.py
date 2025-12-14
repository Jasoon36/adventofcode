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
        self.part1TestAns   = 2
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [chunk.strip('\n').split('\n') for chunk in f.read().split('\n\n')]

        return input
    
    
    def solve1(self, line: str, presents) -> int:

        region_size, gifts = line.split(': ')

        
        gifts_to_place = []

        for present_id, quantity in enumerate(gifts.split(' ')):
            for _ in range(int(quantity)):
                gifts_to_place.append(present_id)

        x, y = map(int, region_size.split('x'))

        current_areas_under_tree = [{
            i + j * 1j
                for i in range(x)
                for j in range(y)
        }]

        # print(current_areas_under_tree)
        print(len(current_areas_under_tree), len(gifts_to_place))

        while current_areas_under_tree and gifts_to_place:
            
            place_a_present = []

            present_to_try_to_place = presents[gifts_to_place.pop()]


            for current_area in current_areas_under_tree:
                for i in range(1,x-1):
                    for j in range(1,y-1):
                        for present in present_to_try_to_place:
                            if len(current_area & (place_it_here := {coor + i + j * 1j for coor in present})) == len(present):
                                place_a_present.append(current_area - place_it_here)
                            # print(current_area)
                            # print(place_it_here)
                            # print(current_area & place_it_here)
                            # print(len(current_area & place_it_here), len(present))

                            # return False


            current_areas_under_tree = place_a_present

            print(len(current_areas_under_tree), len(gifts_to_place))

        print('done one tree')
        if current_areas_under_tree and not gifts_to_place:
            return True
        else:
            return False
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        presents = {}
        offset_to_origin = -1 - 1 * 1j
        rotations = (1j, -1, -1j)

        for present_input in input[:-1]:
            
            present_id = int(present_input[0].split(':')[0])

            raw_and_reflected_input = set()

            raw_and_reflected_input.add(tuple(
                i + j * 1j + offset_to_origin
                    for i, line in enumerate(present_input[1:])
                    for j, char in enumerate(line)
                    if char == '#'
            ))

            raw_and_reflected_input.add(tuple(
                i + j * 1j + offset_to_origin
                    for i, line in enumerate(present_input[1::][::-1])
                    for j, char in enumerate(line)
                    if char == '#'
            ))

            # add 90, 180, and 270 rotations of both the original and reflected input
            # using a set will eliminate symmettries
            
            raw_and_reflected_input |= {
                tuple(
                    point * rotate
                        for point
                        in present
                )
                    for present in raw_and_reflected_input
                    for rotate in rotations
            }

            presents[present_id] = raw_and_reflected_input

        attempt = sum(
            1 
            for line 
            in input[-1]
            if self.solve1(line, presents)
        )

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