class Solution:
    '''
        Attempt at Day 9
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '9'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 50
        self.part2TestAns   = 24


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input


    def area(self, coordinate_1, coordinate_2) -> int:

        return (abs(coordinate_1[0] - coordinate_2[0]) + 1) * (abs(coordinate_1[1] - coordinate_2[1]) + 1)
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        coordinates = [
            tuple(map(int, line.split(',')))
                for line
                in input
        ]

        attempt = max(
            self.area(coordinates[idx], second_coordinate)
                for idx in range(len(coordinates)-1)
                for second_coordinate in coordinates[idx+1:]
        )

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


    def showMeGreenTiles(self, red_1, red_2) -> list:

        if red_1[0] == red_2[0]:
            return [
                (red_1[0], y)
                    for y
                    in range(min(red_1[1],red_2[1]) + 1, max(red_1[1],red_2[1]))
            ]
        else:
            return [
                (x, red_1[1])
                    for x
                    in range(min(red_1[0],red_2[0]) + 1, max(red_1[0],red_2[0]))
            ]

    def getStartingPoint(self, three_red_tiles):

        coordinates = [
            coor[0] + coor[1] * 1j
                for coor
                in three_red_tiles
        ]

        middle_to_before = coordinates[0] - coordinates[1]
        middle_to_next = coordinates[2] - coordinates[1]

        return coordinates[1] + middle_to_before / abs(middle_to_before) + middle_to_next / abs(middle_to_next)

    def rectangleValid(self, coordinate_1, coordinate_2, allowed_tiles) -> int:

        tiles_created = set((
            x + y * 1j
                for x in range(min(coordinate_1[0], coordinate_2[0]), max(coordinate_1[0], coordinate_2[0]) + 1)
                for y in range(min(coordinate_1[1], coordinate_2[1]), max(coordinate_1[1], coordinate_2[1]) + 1)
        ))

        if tiles_created <= allowed_tiles:
            # print(coordinate_1, coordinate_2)
            return len(tiles_created)

        # print(coordinate_1, coordinate_2, tiles_created)
        
        return 0

    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        red_tiles = [
            tuple(map(int, line.split(',')))
                for line
                in input
        ]

        green_tiles = []

        for red_1, red_2 in zip(red_tiles[:-1], red_tiles[1:]):
            green_tiles.extend(self.showMeGreenTiles(red_1, red_2))

        green_tiles.extend(self.showMeGreenTiles(red_tiles[-1], red_tiles[0]))

        x_min = min(coor[0] for coor in red_tiles)
        x_max = max(coor[0] for coor in red_tiles)
        y_min = min(coor[1] for coor in red_tiles)
        y_max = max(coor[1] for coor in red_tiles)

        movie_theatre = {
            x + y * 1j : False
                for x in range(x_min, x_max)
                for y in range(y_min, y_max)
        }

        for coor in red_tiles:
            movie_theatre[coor[0] + coor[1] * 1j] = True

        for coor in green_tiles:
            movie_theatre[coor[0] + coor[1] * 1j] = True

        starting_points = set([self.getStartingPoint(red_tiles[:3])])
        
        print('i am here')

        while starting_points:

            current_point = starting_points.pop()

            if not movie_theatre[current_point]:
                movie_theatre[current_point] = True

                starting_points |= set((
                    new_point
                        for jitter
                        in (1, -1, 1j, -1j)
                        if not movie_theatre[(new_point := current_point + jitter)]
                ))

            print(len(starting_points))

        print('i actually got here')

        all_tiles = set((
            point
                for point, tile
                in movie_theatre.items()
                if tile
        ))

        print(len(all_tiles))
        
        print('dw im ere')

        attempt = max(
            self.rectangleValid(red_tiles[idx], second_coordinate, all_tiles)
                for idx in range(len(red_tiles)-2)
                for second_coordinate in red_tiles[idx+2:]
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