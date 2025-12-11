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


    def rectangleValid(self, coordinate_1, coordinate_2, line_segment_endpoints) -> bool:

        min_x = min(coordinate_1[0], coordinate_2[0])
        max_x = max(coordinate_1[0], coordinate_2[0])
        min_y = min(coordinate_1[1], coordinate_2[1])
        max_y = max(coordinate_1[1], coordinate_2[1])

        for endpoints in line_segment_endpoints:

            if coordinate_1 in endpoints or coordinate_2 in endpoints:
                # skip if an endpoint matches one of the opposite corners
                continue

            # for x, y in endpoints:
            #     # line ends inside rectangle
            #     if min_x - x <= 0 and max_x - x >= 0 and min_y - y <= 0 and max_y - y >= 0:
            #         # print(coordinate_1, coordinate_2, endpoints)
            #         return False

            end_x_1, end_y_1 = endpoints[0]
            end_x_2, end_y_2 = endpoints[1]

            if end_x_1 == end_x_2 and min_x < end_x_1 < max_x:
                # vertical line

                min_end_y = min(end_y_1, end_y_2)
                max_end_y = max(end_y_1, end_y_2)

                if min_end_y <= min_y and max_end_y >= max_y:
                    # line cuts fully through rectangle
                    return False

                if max_y > min_end_y > min_y and max_end_y >= max_y:
                    # line only cuts into the rectangle
                    return False

                if min_end_y <= min_y and min_y < max_end_y < max_y:
                    # line only cuts into the rectangle
                    return False

            if end_y_1 == end_y_2 and min_y < end_y_1 < max_y:
                # horizontal line

                min_end_x = min(end_x_1, end_x_2)
                max_end_x = max(end_x_1, end_x_2)

                if min_end_x <= min_x and max_end_x >= max_x:
                    # line cuts fully through rectangle
                    return False

                if max_x > min_end_x > min_x and max_end_x >= max_x:
                    # line only cuts into the rectangle
                    return False

                if min_end_x <= min_x and min_x < max_end_x < max_x:
                    # line only cuts into the rectangle
                    return False

        return True


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

        line_segment_endpoints = [
            ((red_1[0], red_1[1]), (red_2[0], red_2[1]))
                for red_1, red_2 in zip(red_tiles[:-1], red_tiles[1:])
        ]

        line_segment_endpoints.append(((red_tiles[0][0], red_tiles[0][1]), (red_tiles[-1][0], red_tiles[-1][1])))

        all_potential_rectangles = {
            (red_tiles[idx], second_coordinate) : self.area(red_tiles[idx], second_coordinate)
                for idx in range(len(red_tiles)-2) # can skip the thin rectangles (or known as lines) so -2 not -1
                for second_coordinate in red_tiles[idx+2:]
        }

        for coordinates, area in dict(sorted(all_potential_rectangles.items(), key=lambda item: item[1], reverse=True)).items():
            if self.rectangleValid(coordinates[0], coordinates[1], line_segment_endpoints):
                print(coordinates)
                return area
        
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