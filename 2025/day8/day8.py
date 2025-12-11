class Solution:
    '''
        Attempt at Day 8
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '8'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 40
        self.part2TestAns   = 25272


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input
    
    def euclideanDistance(self, coordinate_1, coordinate_2) -> float:
        
        return sum(
            (x - y) ** 2
                for x, y
                in zip(coordinate_1, coordinate_2)
        ) ** 0.5
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
            connections = 1000
        else:
            input = self.test
            connections = 10

        coordinates = [
            tuple(map(int, line.split(',')))
                for line
                in input
        ]

        coordinates_by_distances = {
            self.euclideanDistance(coordinates[idx], second_coordinate) : (coordinates[idx], second_coordinate)
                for idx in range(len(coordinates)-1)
                for second_coordinate in coordinates[idx+1:]
        }

        circuits = []

        for distance in sorted(coordinates_by_distances.keys())[:connections]:

            coordinate_1, coordinate_2 = coordinates_by_distances[distance]

            match len((circuits_already_in := [
                idx
                    for idx, circuit
                    in enumerate(circuits)
                    if coordinate_1 in circuit or coordinate_2 in circuit
            ])):
                case 0:
                    circuits.append(set((coordinate_1, coordinate_2)))
                case 1:
                    circuits[circuits_already_in[0]] |= set((coordinate_1, coordinate_2))
                case 2:
                    circuits[circuits_already_in[0]] |= set((coordinate_1, coordinate_2)) | circuits.pop(circuits_already_in[1])
        
        attempt = 1

        for size in sorted([
            len(circuit)
                for circuit
                in circuits
        ])[::-1][:3]:
            attempt *= size

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



    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        coordinates = [
            tuple(map(int, line.split(',')))
                for line
                in input
        ]

        coordinates_by_distances = {
            self.euclideanDistance(coordinates[idx], second_coordinate) : (coordinates[idx], second_coordinate)
                for idx in range(len(coordinates)-1)
                for second_coordinate in coordinates[idx+1:]
        }

        circuits = []
        coordinates_added = set()

        for distance in sorted(coordinates_by_distances.keys()):

            coordinate_1, coordinate_2 = coordinates_by_distances[distance]

            match len((circuits_already_in := [
                idx
                    for idx, circuit
                    in enumerate(circuits)
                    if coordinate_1 in circuit or coordinate_2 in circuit
            ])):
                case 0:
                    circuits.append(set((coordinate_1, coordinate_2)))
                    coordinates_added |= set((coordinate_1, coordinate_2))
                case 1:
                    circuits[circuits_already_in[0]] |= set((coordinate_1, coordinate_2))
                    coordinates_added |= set((coordinate_1, coordinate_2))
                case 2:
                    circuits[circuits_already_in[0]] |= set((coordinate_1, coordinate_2)) | circuits.pop(circuits_already_in[1])
        
            if coordinates_added == set(coordinates):
                if len(circuits) == 1:
                    return coordinate_1[0] * coordinate_2[0]

        attempt = 1

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