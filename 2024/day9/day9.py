class Solution:
    '''
        Attempt at Day 9
    '''
    def __init__(self):
        self.year           = '2024'
        self.day            = '9'
        self.prod           = self.read('input.txt')
        self.test           = self.read('input_test.txt')
        self.part1TestAns   = 1928
        self.part2TestAns   = 2858


    def read(self, filename: str) -> list:
        with open(f'./{self.year}/day{self.day}/{filename}') as f:
            input = f.read().strip('\n')

        return input
    
    
    def solve1(self, disk_map: str) -> int:

        file_blocks = []

        file_id = 0

        file = True

        for i, char in enumerate(disk_map):

            length = int(char)
            
            if file:
                while length > 0:
                    file_blocks.append(file_id)
                    length -= 1
                file_id += 1
            else:
                while length > 0:
                    file_blocks.append('.')
                    length -= 1

            file = not file

        
        first_free_space_ind = file_blocks.index('.')
        file_blocks_to_move = len(file_blocks[first_free_space_ind+1:]) - file_blocks[first_free_space_ind+1:].count('.')
        last_file_block_to_move_ind = len(file_blocks) - 1
        last_file_block = file_blocks[last_file_block_to_move_ind]

        while file_blocks_to_move > 0:

            while last_file_block == '.':
                last_file_block_to_move_ind -= 1
                last_file_block = file_blocks[last_file_block_to_move_ind]

            # move
            file_blocks[first_free_space_ind] = last_file_block
            file_blocks[last_file_block_to_move_ind] = '.'
            last_file_block = file_blocks[last_file_block_to_move_ind]

            first_free_space_ind = file_blocks.index('.')
            file_blocks_to_move = len(file_blocks[first_free_space_ind+1:]) - file_blocks[first_free_space_ind+1:].count('.')
        
        checksum = sum([i * val for i, val in enumerate(file_blocks[:first_free_space_ind])])

        return checksum
    
    def part1(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = self.solve1(input)

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



    def solve2(self, disk_map: str) -> int:

        file_blocks = []

        file_id = 0

        file = True

        for i, char in enumerate(disk_map):

            length = int(char)
            
            if file:
                while length > 0:
                    file_blocks.append(file_id)
                    length -= 1
                file_id += 1
            else:
                while length > 0:
                    file_blocks.append('.')
                    length -= 1

            file = not file

        
        # okay so we sweep from both ends
        # from the left for the first free space
        # from the right by file id
        # once it crosses over - stop


        # set file_id already to the highest file id 
        file_id -= 1

        # get sweepers
        first_free_space_ind = file_blocks.index('.')
        file_id_to_move_ind = file_blocks.index(file_id)


        already_moved_ind = len(file_blocks) # already "tried" to move
        length_of_file_id = file_blocks[file_id_to_move_ind:already_moved_ind].count(file_id)

        while first_free_space_ind < file_id_to_move_ind:

            # try to move this file id

            space_to_find = ['.' for _ in range(length_of_file_id)]

            for i, char in enumerate(file_blocks[first_free_space_ind:file_id_to_move_ind]):

                if char != '.':
                    continue

                if file_blocks[first_free_space_ind+i:first_free_space_ind+i+length_of_file_id] == space_to_find:

                    # then move it
                    for j in range(length_of_file_id):
                        file_blocks[first_free_space_ind+i+j] = file_id
                        file_blocks[file_id_to_move_ind+j] = '.'
                    break # out of searching for a file space as you've moved it now

            # get new indices whether you could or couldn't move it
            file_id -= 1
            first_free_space_ind = file_blocks.index('.')
            already_moved_ind = file_id_to_move_ind
            file_id_to_move_ind = file_blocks[:already_moved_ind].index(file_id)
            length_of_file_id = file_blocks[file_id_to_move_ind:already_moved_ind].count(file_id)
        
        checksum = sum([i * val for i, val in enumerate(file_blocks) if val != '.'])

        return checksum
    
    def part2(self, realAttempt = False) -> int:

        if realAttempt:
            input = self.prod
        else:
            input = self.test

        attempt = self.solve2(input)

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