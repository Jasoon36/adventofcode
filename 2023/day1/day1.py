class Solution:
    '''
        Attempt at Day 1
    '''
    def __init__(self):
        self.year       = '2023'
        self.day        = '1'
        self.prod       = self.read('input.txt')
        self.test       = self.read('input_test.txt')
        self.test_ans   = [12,38,15,77]

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
    
    def solved(self):
        print(self.test_solution())


a = Solution()
a.solved()