class Solution:
    '''
        Attempt at Day 1
    '''
    def __init__(self):
        self.year       = '2023'
        self.day        = '2'
        self.prod       = self.read('input.txt')
        self.test       = self.read('input_test.txt')
        self.test_ans   = [True, True, False, False, True]
        # self.test2      = self.read('input_test2.txt')
        # self.test2_ans  = [29, 83, 13, 24, 42, 14, 76]

        self.valid = {
            'red'     : 12 , 
            'green'   : 13 ,
            'blue'    : 14 ,
        }

    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [l.strip('\n') for l in f]

        return input
    
    def solve(self, input: str) -> tuple[int, bool]:

        game = input.split(': ')

        gameId = int(game[0].split(' ')[1])

        grabs = game[1].split('; ')

        valid = True
        for handful in grabs:
            for cubeSet in handful.split(', '):
                countAndColour = cubeSet.split(' ')

                if int(countAndColour[0]) > self.valid[countAndColour[1]]:
                    valid = False
                    return gameId, valid

        
        return gameId, valid

    def test_solution(self) -> bool:

        for input, ans in zip(self.test, self.test_ans):
            try:
                gameId, valid = self.solve(input)
                assert valid == ans
            except AssertionError as e:
                e.add_note(f'In game {gameId} {valid} is not {ans} for input\n{input}')
                raise e
        
        print('keep going')
        return True
    
    def part1(self):
        try:
            TestGames = [self.solve(input) for input in self.test]
            part1TestAns = sum([gameId for gameId, valid in TestGames if valid])
            testAns = 8
            assert part1TestAns == testAns

            Games = [self.solve(input) for input in self.prod]
            part1Ans = sum([gameId for gameId, valid in Games if valid])
            print(part1Ans)

        except AssertionError as e:
            e.add_note(f'part1 test ans {part1TestAns} is not {testAns}')
            raise e
        
    def solve2(self, input) -> int:

        game = input.split(': ')

        grabs = game[1].split('; ')

        highestCubesSeen = {
            'red'   : 0,
            'green' : 0,
            'blue'  : 0,
        }

        for handful in grabs:
            for cubeSet in handful.split(', '):
                countAndColour = cubeSet.split(' ')

                count = int(countAndColour[0])
                colour = countAndColour[1]

                highestCubesSeen.update({colour : max(highestCubesSeen[colour],count)})

        # f, no product function
        power = 1
        for highestCount in highestCubesSeen.values():
            power *= highestCount

        return power

        
    def part2(self):
        try:
            part2testAns = sum([self.solve2(i) for i in self.test])
            testAns = 2286
            assert part2testAns == testAns

            print(sum([self.solve2(i) for i in self.prod]))

        except AssertionError as e:
            e.add_note(f'part2 test ans {part2testAns} is not {testAns}')
            raise e




a = Solution()
a.part2()