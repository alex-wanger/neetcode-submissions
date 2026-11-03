class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for num in hashset:
            if (num - 1 not in hashset):
                length = 1
                while (num + 1 in hashset):
                    length += 1
                    num += 1
                if (length > longest):
                    longest = length
        return longest 