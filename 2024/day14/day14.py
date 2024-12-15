class Solution:
    '''
        Attempt at Day 14
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '14'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 12
        self.part2TestAns   = 0


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    
    def solve1(self, robots: dict, wide: int, tall: int) -> int:

        quadrants = {
            (-1,1)      : [],
            (-1,-1)     : [],
            (1,1)       : [],
            (1,-1)      : [],
        }

        for i, robot in robots.items():
            pos, vel = robot

            new_h = (pos[0] + 100 * vel[0]) % wide
            new_v = (pos[1] + 100 * vel[1]) % tall

            if new_h < wide // 2:

                if new_v < tall // 2:
                    quadrants[(-1,-1)].append((new_h,new_v))
                    
                elif new_v > tall // 2:
                    quadrants[(-1,1)].append((new_h,new_v))

            elif new_h > wide // 2:

                if new_v < tall // 2:
                    quadrants[(1,-1)].append((new_h,new_v))

                elif new_v > tall // 2:
                    quadrants[(1,1)].append((new_h,new_v))
        
        safety_factor = 1

        for robots in quadrants.values():
            safety_factor *= len(robots)
        
        return safety_factor
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
            wide = 101
            tall = 103
        else:
            input = self.test
            wide = 11
            tall = 7

        robots = {}

        for ind, line in enumerate(input):
            p, v = line.split(' ')
            pos = tuple(map(int, p.split('=')[1].split(',')))
            vel = tuple(map(int, v.split('=')[1].split(',')))

            robots[ind] = [pos,vel]

        attempt = self.solve1(robots, wide, tall)

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



    def solve2(self, robots: dict, wide: int, tall: int) -> int:

        seconds = 0
        
        with open(f'./{self.year}/day{self.day}/watch_robots.txt', 'w') as f:

            while seconds < 10000:
                robot_pos = {}

                for i, robot in robots.items():
                    pos, vel = robot

                    new_h = (pos[0] + seconds * vel[0]) % wide
                    new_v = (pos[1] + seconds * vel[1]) % tall

                    robot_pos[(new_h, new_v)] = robot_pos.get((new_h, new_v), 0) + 1


                if (seconds % wide == 14) | (seconds % tall == 64):

                    f.write('\n\n\n\n' + str(seconds) + '\n')
                    f.writelines(
                        '\n'.join([
                            ''.join([
                                str(robot_pos.get((i,j),' '))
                                    for i in range(wide)

                            ])
                                for j in range(tall)
                        ])
                    )
                

                
                seconds += 1
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
            wide = 101
            tall = 103
        else:
            input = self.test
            wide = 11
            tall = 7

        robots = {}

        for ind, line in enumerate(input):
            p, v = line.split(' ')
            pos = tuple(map(int, p.split('=')[1].split(',')))
            vel = tuple(map(int, v.split('=')[1].split(',')))

            robots[ind] = [pos,vel]

        attempt = self.solve2(robots, wide, tall)

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