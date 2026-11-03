class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for number in nums:
            if (not number in hashset):
                hashset.add(number)
            else:
                return True
        return False