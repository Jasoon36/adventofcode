class Solution:
    '''
        Attempt at Day 2
    '''
    def __init__(self):
        self.year           = '2025'
        self.day            = '2'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        # self.test1Ans       = []
        # self.test2Ans       = []
        self.part1TestAns   = 1227775554
        self.part2TestAns   = 4174379265
        self.prime_numbers  = {}


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = [line.strip('\n') for line in f]

        return input

    
    def find_invalid_ids(self, start: int, end: int) -> list:

        return [
            id
                for id
                in range(start, end + 1)
                if self.invalid(id)
        ]

    def invalid(self, id: int) -> bool:

        power_of_ten = 0

        id_to_divide = id

        while (id_to_divide // 10 > 0):
            id_to_divide = id_to_divide // 10
            power_of_ten += 1

        if power_of_ten % 2:
            # length is even

            to_split_in_half = 10 ** (power_of_ten - power_of_ten // 2)

            first_half = id // to_split_in_half
            second_half = id % (first_half * to_split_in_half)

            if first_half == second_half:
                return True

        return False
    
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        ranges = input[0].split(',')

        attempt = sum(
            sum(self.find_invalid_ids(int(id_range.split('-')[0]), int(id_range.split('-')[1])))
                for id_range
                in ranges
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

    
    def find_invalid_ids2(self, start: int, end: int) -> list:

        return [
            id
                for id
                in range(start, end + 1)
                if self.invalid2(id)
        ]

    def invalid2(self, id: int) -> bool:

        power_of_ten = 0

        id_to_divide = id

        while (id_to_divide // 10 > 0):
            id_to_divide = id_to_divide // 10
            power_of_ten += 1

        prime_numbers_to_check = self.prime_numbers.setdefault(power_of_ten, self.get_primes(power_of_ten))

        for prime_to_try in prime_numbers_to_check:

            if (power_of_ten % prime_to_try + 1) == prime_to_try:
                # length is divisible by prime

                to_split = 10 ** prime_to_try

                number_parts = []

                id_to_divide = id

                for _ in range((power_of_ten + 1) // prime_to_try):

                    number_parts.append(id_to_divide % to_split)

                    id_to_divide = id_to_divide // to_split

                if sum(
                    abs(number_part - number_parts[0])
                        for number_part
                        in number_parts
                ) == 0:
                    return True

        return False

    def get_primes(self, n: int) -> list:

        prime_numbers = []

        for i in range(1, n + 1 // 2 + 1):
            if n % i + 1:
                prime_numbers.append(i)

        return prime_numbers
            
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        ranges = input[0].split(',')

        attempt = sum(
            sum(self.find_invalid_ids2(int(id_range.split('-')[0]), int(id_range.split('-')[1])))
                for id_range
                in ranges
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