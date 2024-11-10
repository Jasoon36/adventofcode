class Solution:
    '''
        Attempt at Day 1
    '''
    def __init__(self):
        self.year       = '2023'
        self.day        = '1'
        self.prod       = self.read('input.txt')
        self.test       = self.read('input_test.txt')
        self.test2      = self.read('input_test2.txt')
        self.test_ans   = [12,38,15,77]
        self.test2_ans  = [29, 83, 13, 24, 42, 14, 76]
        
        self.digits3 = {
            'one'   : '1', 
            'two'   : '2', 
            'six'   : '6', 
        }
        
        self.digits4 = { 
            'four'  : '4', 
            'five'  : '5', 
            'nine'  : '9', 
        }
        
        self.digits5 = {
            'three' : '3', 
            'seven' : '7', 
            'eight' : '8', 
        }

    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [l.strip('\n') for l in f]

        return input
    
    def solve(self, input: str) -> int:

        for char in input:
            if char.isdigit():
                firstNum = char
                break
        
        for char in input[::-1]:
            if char.isdigit():
                secondNum = char
                break
        
        ans = int(firstNum + secondNum)
        
        return ans

    def test_solution(self) -> bool:

        for i, a in zip(self.test, self.test_ans):
            try:
                try_ans = self.solve(i)
                assert try_ans == a
            except AssertionError as e:
                e.add_note(f'{try_ans} is not {a} for input\n{i}')
                raise e
            
        return True
    
    def part1(self):
        try:
            part1_test = sum([self.solve(i) for i in self.test])
            assert part1_test == 142

            print(sum([self.solve(i) for i in self.prod]))

        except AssertionError as e:
            e.add_note(f'part1 test ans {part1_test} is not 142')
            raise e
        
    def solve2(self, input) -> int:
        
        for i, char in enumerate(input, start = 1):
            if char.isdigit():
                firstNum = char
                break
            elif input[i-3:i] in self.digits3.keys():
                firstNum = self.digits3[input[i-3:i]]
                break
            elif input[i-4:i] in self.digits4.keys():
                firstNum = self.digits4[input[i-4:i]]
                break
            elif input[i-5:i] in self.digits5.keys():
                firstNum = self.digits5[input[i-5:i]]
                break
        

        inputReversed = input[::-1]
        for i, char in enumerate(inputReversed, start = 1):
            if char.isdigit():
                secondNum = char
                break
            elif inputReversed[i-3:i][::-1] in self.digits3.keys():
                secondNum = self.digits3[inputReversed[i-3:i][::-1]]
                break
            elif inputReversed[i-4:i][::-1] in self.digits4.keys():
                secondNum = self.digits4[inputReversed[i-4:i][::-1]]
                break
            elif inputReversed[i-5:i][::-1] in self.digits5.keys():
                secondNum = self.digits5[inputReversed[i-5:i][::-1]]
                break

        
        ans = int(firstNum + secondNum)
        
        return ans

        
    def test_solution2(self) -> bool:

        for i, a in zip(self.test2, self.test2_ans):
            try:
                try_ans = self.solve2(i)
                assert try_ans == a
            except AssertionError as e:
                e.add_note(f'{try_ans} is not {a} for input\n{i}')
                raise e
            
        return True

        
    def part2(self):
        try:
            part2_test = sum([self.solve2(i) for i in self.test2])
            assert part2_test == 281

            print(sum([self.solve2(i) for i in self.prod]))

        except AssertionError as e:
            e.add_note(f'part2 test ans {part2_test} is not 281')
            raise e




a = Solution()
a.part2()