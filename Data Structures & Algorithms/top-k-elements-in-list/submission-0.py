class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_to_freq = dict()
        for index, number in enumerate(nums):
            if number not in number_to_freq:
                number_to_freq[number] = 1
            else:
                number_to_freq[number] += 1
        
        counter = 0
        ans = []
        while (counter < k):
            current_max = -math.inf
            current_max_key = -1
            for key in number_to_freq:
                if (number_to_freq[key] > current_max):
                    current_max = number_to_freq[key]
                    current_max_key = key
            ans.append(current_max_key)
            number_to_freq.pop(current_max_key)
            counter += 1
        return ans