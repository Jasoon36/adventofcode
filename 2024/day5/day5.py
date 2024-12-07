class Solution:
    '''
        Attempt at Day 5
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '5'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [
            True,
            True,
            True,
            False,
            False,
            False,
        ]
        self.part1TestAns   = 143
        self.test2Ans       = []
        self.part2TestAns   = 123


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, page_numbers: str, rules: dict) -> bool:

        # need to check for each number is not after a number it should be before

        for ind, page_num in enumerate(page_numbers):

            numbers_it_should_be_before = set(rules.get(page_num,[]))

            numbers_it_is_after = set((page_numbers[:ind]))

            numbers_it_should_be_before_it_is_after = numbers_it_should_be_before & numbers_it_is_after

            if len(numbers_it_should_be_before_it_is_after) > 0:
                return False

        return True

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

        split = input.index('')

        page_ordering_rules = input[:split]
        pages_to_produce = [line.split(',') for line in input[split+1:]]

        
        page_order_dict = {}

        for rule in page_ordering_rules:
            before, after = rule.split('|', maxsplit = 1)
            page_order_dict[before] = page_order_dict.get(before, []) + [after]


        middle_pages = 0
        for page_numbers in pages_to_produce:
            if self.solve1(page_numbers, page_order_dict):
                # get middle page

                middle_pages += int(page_numbers[len(page_numbers)//2])

        return middle_pages
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1()
            assert part1TestAttempt == self.part1TestAns
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))



    def solve2(self, page_numbers: str, rules: dict) -> list:
        '''
        it reads like insertion sort and sorts the list in place
        i = 1 (0th number is a freebie)
        for the ith element
            check from the 0th to i-1th element if it should be before it
                (in order so it finds the earliest number to be before)
                if yes pop the ith element out and insert before the number it should be before (and you can stop checking now)
            i + 1
        '''

        if self.solve1(page_numbers, rules):
            return []
        
        pos = 1

        n = len(page_numbers)

        while pos < n:

            numbers_to_be_before = rules.get(page_numbers[pos], [])

            if numbers_to_be_before:
                for ind, pagenum in enumerate(page_numbers[:pos]):
                    if pagenum in numbers_to_be_before:
                        page_numbers = page_numbers[:ind] + [page_numbers[pos]] + page_numbers[ind:pos] + page_numbers[pos+1:]
                        break

                pos += 1
            else:
                pos += 1

        return page_numbers
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        split = input.index('')

        page_ordering_rules = input[:split]
        pages_to_produce = [line.split(',') for line in input[split+1:]]

        
        page_order_dict = {}

        for rule in page_ordering_rules:
            before, after = rule.split('|', maxsplit = 1)
            page_order_dict[before] = page_order_dict.get(before, []) + [after]


        middle_pages = 0
        for page_numbers in pages_to_produce:
            
            sorted_list = self.solve2(page_numbers, page_order_dict)

            if sorted_list:
                # get middle page

                middle_pages += int(sorted_list[len(sorted_list)//2])

        return middle_pages
        
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