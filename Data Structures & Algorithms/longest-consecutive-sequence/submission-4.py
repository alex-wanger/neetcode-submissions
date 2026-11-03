class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maximum = 0
        for number in hashset:
            counter = 1
            if (number - 1 in hashset):
                continue
            cursor = number + 1
            while (cursor in hashset):
                counter += 1
                cursor += 1
            if counter > maximum:
                maximum = counter
        return maximum