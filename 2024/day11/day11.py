class Solution:
    '''
        Attempt at Day 11

        Got back from chimaek 1 shot of soju for each error or incorrect answer and a commit
        And one shot to start

        Shot tracker = 5
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '11'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 55312


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = f.read().strip('\n')

        return input
    
    
    def solve1(self, stones: list, blinks = 25) -> int:

        for _ in range(blinks):
            new_stones = []

            for stone in stones:
                if stone == 0:
                    new_stones.append(1)
                elif (n := len(str(int(stone)))) % 2 == 0:
                    half_length = n / 2

                    new_stones.extend(divmod(stone, 10 ** half_length))
                else:
                    new_stones.append(stone * 2024)

            stones = new_stones.copy()

        number_of_stones = len(stones)

        return number_of_stones
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        stones = [int(number) for number in input.split()]

        attempt = self.solve1(stones)

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


    def getNewStone(self, stone: int) -> int:

        if stone == 0:
            return [1]
        elif (n := len(str(int(stone)))) % 2 == 0:
            half_length = n / 2

            return divmod(stone, 10 ** half_length)
        else:
            return [stone * 2024]
        
    def solve2(self, stones: list, blinks = 75) -> int:

        stone_map = {
            stone : 1
                for stone
                in stones
        }

        for _ in range(blinks):
            new_stones_map = {}

            for stone, number_of_stones in stone_map.items():
                if stone == 0:
                    new_stones_map[1] = new_stones_map.get(1, 0) + number_of_stones
                elif (n := len(str(stone))) % 2 == 0:
                    half_length = n / 2

                    first_num, second_num = tuple(map(int, divmod(stone, 10 ** half_length)))
                    new_stones_map[first_num] = new_stones_map.get(first_num, 0) + number_of_stones
                    new_stones_map[second_num] = new_stones_map.get(second_num, 0) + number_of_stones
                else:
                    new_stones_map[stone * 2024] = new_stones_map.get(stone * 2024, 0) + number_of_stones


            stone_map = new_stones_map.copy()

        total_number_of_stones = sum(stone_map.values())

        return total_number_of_stones
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        stones = [int(number) for number in input.split()]

        attempt = self.solve2(stones, 75)

        return attempt
        
    def runPart2(self):

        # try:
        #     part2TestAttempt = self.part2()
        #     assert part2TestAttempt == self.part2TestAns
        # except AssertionError as e:
        #     e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns}')
        #     raise e
        
        realAttempt = True
        print(self.part2(realAttempt))


a = Solution()
a.runPart1()
a.runPart2()