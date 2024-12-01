class Solution:
    '''
        Attempt at Day 
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '1'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 11
        self.part2TestAns   = 31


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n').split() for line in f]

        return input
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test


        left_list, right_list = list(map(sorted, zip(*input)))


        abs_differences = [
            abs(int(left) - int(right))
                for left, right
                in zip(left_list, right_list)
        ]


        attempt = sum(abs_differences)

        return attempt
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))


    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test


        left_list, right_list = list(map(list, zip(*input)))

        similarity_scores = [
            int(left_key) * left_list.count(left_key) * right_list.count(left_key)
                for left_key
                in set(left_list)
        ]


        attempt = sum(similarity_scores)

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