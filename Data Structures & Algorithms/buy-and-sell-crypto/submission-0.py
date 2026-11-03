class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_value = prices[0]
        maximum_price = 0
        for index, current_price in enumerate(prices[1:], 1):
            if (current_price < lowest_value):
                lowest_value = current_price
            if (current_price - lowest_value > maximum_price):
                maximum_price = current_price - lowest_value
        return maximum_price