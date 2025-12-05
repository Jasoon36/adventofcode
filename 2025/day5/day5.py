class Solution:
    '''
        Attempt at Day 5
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '5'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 3
        self.part2TestAns   = 14


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        split = input.index('')

        fresh_ranges = [
            tuple(map(int, id_range.split('-')))
                for id_range
                in input[:split]
        ]

        fresh_count = 0

        for ingredient in map(int,input[split+1:]):
            for fresh_range in fresh_ranges:
                if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
                    fresh_count += 1
                    break

        return fresh_count
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))


    def reduce_ranges(self, list_of_ranges, range_to_insert):

        reduce_again = True

        while reduce_again:

            reduce_again = False

            for i, id_range in enumerate(list_of_ranges):

                if range_to_insert[0] <= id_range[1] and range_to_insert[1] >= id_range[0]:
                    
                    reduce_again = True

                    range_to_insert = (
                        min(range_to_insert[0], id_range[0]),
                        max(range_to_insert[1], id_range[1])
                    )
                    
                    list_of_ranges.pop(i)
                    
                    break

        list_of_ranges.append(range_to_insert)

        return list_of_ranges

    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        split = input.index('')

        flattened_ranges = []

        for insert_range in input[:split]:

            insert_min, insert_max = map(int, insert_range.split('-'))

            flattened_ranges = self.reduce_ranges(flattened_ranges, (insert_min, insert_max))

        attempt = sum(
            min_max[1] - min_max[0] + 1
                for min_max
                in flattened_ranges
        )

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