'''
    Attempt at Day 1
'''
import os
class Solution:
    def __init__(self):
        self.year   = '2023'
        self.day    = '1'
        self.prod   = self.read('input.txt')
        self.test   = self.read('input_test.txt')

    def read(self, filename) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = f.readlines()
            f.close()

        return input
    
    def show_test(self):
        for i in self.test:
            print(i)

Solution()


with open(f'./2023/day1/input_test.txt') as f:
    print(f.readlines())
    f.close()

# def tests(self) -> bool:
#     assert self.solve('1abc2') == 12
#     assert self.solve('pqr3stu8vwx') == 38
#     assert self.solve('a1b2c3d4e5f') == 15
#     assert self.solve('treb7uchet') == 77

#     return True

# def solve(self, input) -> int:

#     numbers = 

#     char_list = input.str.split('')

#     nums = [ for i in char_list]

#     return ans