class Solution:
    '''
        Attempt at Day 16
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '16'
        self.prod           = self.read('input.txt')
        self.test0          = self.read('input_test0.txt')
        self.test1          = self.read('input_test1.txt')
        self.part1TestAns0  = 7036
        self.part1TestAns1  = 11048
        self.part2TestAns0  = 45
        self.part2TestAns1  = 64


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    def prettyPrint(self, warehouse: dict):

        real_vals = list({pos.real for pos in warehouse.keys()})
        real_vals.sort()

        imag_vals = list({pos.imag for pos in warehouse.keys()})
        imag_vals.sort()

        for r in real_vals:
            print(''.join([
                warehouse[r + i * 1j] 
                    for i 
                    in imag_vals
            ]))

        print('\n')
    
    
    def solve1(self, maze: dict) -> int:

        dir = 1j

        directionMap = {
            dir**i : i
                for i in range(4)
        }

        validPositions = {
            pos
                for pos, char in maze.items()
                if char != '#'
        }

        for pos, char in maze.items():
            if char == 'S':
                startPos = pos
                break

        pastVectors = {}

        lowestScore = 1e9

        # with a list of current positions move the position with the lowest 
        # score forward, left and right, to be able to sort the list of current 
        # positions (queue), i need to do something with the complex numbers
        # current positions therefore need position, direction, score so far

        currentPositions = [(0, startPos.real, startPos.imag, directionMap[1j])]

        while currentPositions:
            
            currentPositions.sort()
            # print(pastVectors)

            score, realPos, imagPos, dirKey = currentPositions.pop(0)
            direction = dir ** dirKey
            position = realPos + imagPos * 1j

            if score > pastVectors.get((direction, position), 1e9):
                continue
                
            pastVectors[(direction, position)] = score

            if maze[position] == 'E':
                lowestScore = min(lowestScore, score)
                continue

            # try move 
            for addScore, changeDirection in [(1,1), (1001, -1j), (1001, 1j)]:
                if (newPosition := position + (newDirection := direction * changeDirection)) in validPositions:
                    currentPositions += [(score + addScore, newPosition.real, newPosition.imag, directionMap[newDirection])]

            # if currentPositions[0][0] > 7036:
            #     break

        return lowestScore

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
    
    def part1(self, realAttempt = False, test = 0) -> int:

        if realAttempt:
            input = self.prod
        else:
            if test == 0:
                input = self.test0
            else:
                input = self.test1

        maze = {
            i + j * 1j : char
                for i, row in enumerate(input)
                for j, char in enumerate(row)
        }

        attempt = self.solve1(maze)

        return attempt
        
    def runPart1(self):

        try:
            part1TestAttempt = self.part1(False, 0)
            assert part1TestAttempt == self.part1TestAns0
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns0}')
            raise e

        try:
            part1TestAttempt = self.part1(False, 1)
            assert part1TestAttempt == self.part1TestAns1
        except AssertionError as e:
            e.add_note(f'part 1 test ans {part1TestAttempt} is not {self.part1TestAns1}')
            raise e
        
        realAttempt = True
        print(self.part1(realAttempt))




    def solve2(self, maze: dict) -> int:

        dir = 1j

        directionMap = {
            dir**i : i
                for i in range(4)
        }

        validPositions = {
            pos
                for pos, char in maze.items()
                if char != '#'
        }

        for pos, char in maze.items():
            if char == 'S':
                startPos = pos
                break

        pastVectors = {}

        lowestScore = 1e9
        bestPath = set()

        # with a list of current positions move the position with the lowest 
        # score forward, left and right, to be able to sort the list of current 
        # positions (queue), i need to do something with the complex numbers
        # current positions therefore need position, direction, score so far

        currentPositions = [(0, startPos.real, startPos.imag, directionMap[1j], [(startPos.real, startPos.imag)])]

        while currentPositions:
            
            currentPositions.sort()
            # print(pastVectors)

            score, realPos, imagPos, dirKey, path = currentPositions.pop(0)
            direction = dir ** dirKey
            position = realPos + imagPos * 1j

            if score > pastVectors.get((direction, position), 1e9):
                continue
                
            pastVectors[(direction, position)] = score

            if maze[position] == 'E' and score <= lowestScore:
                lowestScore = min(lowestScore, score)
                bestPath.update(path)
                continue

            # try move 
            for addScore, changeDirection in [(1,1), (1001, -1j), (1001, 1j)]:
                if (newPosition := position + (newDirection := direction * changeDirection)) in validPositions:
                    currentPositions += [(
                        score + addScore, 
                        newPosition.real, 
                        newPosition.imag, 
                        directionMap[newDirection],
                        path + [(newPosition.real, newPosition.imag)]
                    )]

            # if currentPositions[0][0] > 7036:
            #     break

        return len(bestPath)

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
    
    def part2(self, realAttempt = False, test = 0) -> int:

        if realAttempt:
            input = self.prod
        else:
            if test == 0:
                input = self.test0
            else:
                input = self.test1

        maze = {
            i + j * 1j : char
                for i, row in enumerate(input)
                for j, char in enumerate(row)
        }

        attempt = self.solve2(maze)

        return attempt
        
    def runPart2(self):

        try:
            part2TestAttempt = self.part2(False, 0)
            assert part2TestAttempt == self.part2TestAns0
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns0}')
            raise e

        try:
            part2TestAttempt = self.part2(False, 1)
            assert part2TestAttempt == self.part2TestAns1
        except AssertionError as e:
            e.add_note(f'part 2 test ans {part2TestAttempt} is not {self.part2TestAns1}')
            raise e
        
        realAttempt = True
        print(self.part2(realAttempt))


a = Solution()
a.runPart2()