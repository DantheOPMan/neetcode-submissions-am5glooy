class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minValue = prices[0]
        for price in prices:
            maxProfit = max(maxProfit, price - minValue )
            minValue = min(minValue,price)
        return maxProfit