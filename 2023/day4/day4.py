class Solution:
    '''
        Attempt at Day 
    '''
    def __init__(self):
        self.year           = '2023'
        self.day            = '4'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.test1Ans       = [8,2,2,1,0,0]
        self.test2Ans       = []
        self.part1TestAns   = 13
        self.part2TestAns   = 30


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [l.strip('\n') for l in f]

        return input
    
    
    def solve1(self, line: str) -> int:
        
        two_list_of_numbers = line.split(': ')[1]
        winning_numbers, numbers_you_have = two_list_of_numbers.split(' | ')
        winning_numbers_lis = winning_numbers.split(' ')
        numbers_you_have_lis = numbers_you_have.split(' ')

        winning_numbers_you_have = 0
        for number in numbers_you_have_lis:
            if number == '':
                continue
            
            if number in winning_numbers_lis: 
                winning_numbers_you_have += 1 

        print(numbers_you_have_lis)
        print(winning_numbers_lis)
        print(winning_numbers_you_have)

        if winning_numbers_you_have == 0:
            lineAns = 0
        else:
            lineAns = 2**(winning_numbers_you_have-1)

        return lineAns

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

        attempt = sum([self.solve1(line) for line in input])

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



    def solve2(self, line: str) -> tuple:
        
        card, two_list_of_numbers = line.split(': ')

        card_int = int(card.split(' ')[1]) 

        winning_numbers, numbers_you_have = two_list_of_numbers.split(' | ')
        winning_numbers_lis = winning_numbers.split(' ')
        numbers_you_have_lis = numbers_you_have.split(' ')

        winning_numbers_you_have = [
            number
                for index, number in enumerate(numbers_you_have_lis)
                if (number in winning_numbers_lis) and (number != '')
        ]

        copies_you_win = [
            card_int + ind + 1
                for ind in range(len(winning_numbers_you_have))
        ]

        return card_int, copies_you_win

    def testSolution2(self) -> bool:

        for line, ans in zip(self.test, self.test1Ans):
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

        copies = {
            (kv := self.solve2(line))[0]: kv[1]
                for line in input
        }

        number_of_cards = sum([
            1 
                for win in copies.values() 
                if win
        ])

        all_copies = []
        for card_num in reversed(sorted(copies.keys())):

            copies_gained = copies[card_num]

            for copy_num in copies_gained:
                all_copies.extend(copies[copy_num])

            copies[card_num].extend(all_copies)

        print(number_of_cards)

        number_of_cards += sum([
            len(winnings)
                for winnings in copies.values()
        ])

        print(copies)

        return number_of_cards
        
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
a.runPart2()